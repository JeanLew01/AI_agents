"""Parse the logs and compare the native outputs of the runs of execution_id = mbd_planner_hopper.

NumPy only (no JAX import, so this is not a heavy job). It reads what upstream wrote; it computes nothing of the
method. Usage:  $PROJECT_PYTHON compare.py  ->  writes comparison.json next to this file and prints it.

Three executions of the identical command `mbd_planner.py --env_name hopper --seed 0` are read:
  run1               this executor's complete reference run (exit status 0), from the private source copy
  coordinator-probe  the coordinator's earlier complete run (exit status 0) from the pinned checkout; READ ONLY
  run2-interrupted   this executor's replay; the machine froze after upstream had printed its last line and
                     written both files, so no exit status was recorded
"""
import hashlib
import json
import re
from datetime import datetime
from pathlib import Path

import numpy as np

EVID = Path(__file__).resolve().parent
PROJECT_ROOT = EVID.parents[1]
LOGS, OUTS = EVID / "logs", EVID / "outputs"
COORD = PROJECT_ROOT / "tmp" / "env-probe" / "coord"

SOURCES = {
    "run1": {"log": LOGS / "run1.log", "launcher": LOGS / "run1.launcher.log", "out": OUTS / "run1"},
    "coordinator-probe": {"log": COORD / "hopper-default.log", "launcher": COORD / "hopper-default.time",
                          "out": COORD / "hopper-default-out"},
    "run2-interrupted": {"log": LOGS / "run2.log", "launcher": LOGS / "run2.launcher.log",
                         "out": OUTS / "run2-interrupted"},
}


def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def parse_log(path: Path) -> dict:
    text = path.read_text(errors="replace")
    lines = [seg for seg in re.split(r"[\r\n]+", text) if seg.strip()]
    out = {"log": str(path), "log_sha256": sha256(path), "log_bytes": path.stat().st_size}
    m = re.search(r"^override temp_sample to (\S+)\s*$", text, re.M)
    out["override_temp_sample_printed"] = m.group(1) if m else None
    m = re.search(r"^init sigma = (\S+)\s*$", text, re.M)
    out["init_sigma_printed"] = m.group(1) if m else None
    m = re.search(r"final reward = (\S+)\s*$", text, re.M)
    out["final_reward_printed"] = m.group(1) if m else None
    out["final_reward"] = float(m.group(1)) if m else None
    out["traceback_in_log"] = "Traceback (most recent call last)" in text
    out["last_line"] = lines[-1] if lines else None
    m = re.search(r"heavy\.sh: scope memory\.peak=(\d+)MB oom_kills=(\d*)", text)
    out["scope_memory_peak_mb"] = int(m.group(1)) if m else None
    out["oom_kills"] = (int(m.group(2)) if m.group(2) else 0) if m else None
    # tqdm progress: "Diffusing:  12%|#| 12/99 [00:14<01:32,  1.06s/it, rew=1.23e+00]".
    # mbd_planner.py calls pbar.set_postfix after iteration j while the counter still shows j-1, so the LAST display
    # with counter j-1 carries the mean sample reward of diffusion iteration j (j = 1 .. Ndiffuse-1).
    last_by_n, total, last_progress = {}, None, None
    for seg in lines:
        m = re.search(r"Diffusing:.*?\|\s*(\d+)/(\d+) \[([^\]]*)\]", seg)
        if not m:
            continue
        last_progress = seg.strip()
        n, total = int(m.group(1)), int(m.group(2))
        r = re.search(r"rew=([-+0-9.eE]+|nan|inf|-inf)", m.group(3))
        if r:
            last_by_n[n] = r.group(1)
    out["tqdm_total"] = total
    out["last_progress_line"] = last_progress
    seq = [last_by_n.get(j - 1) for j in range(1, (total or 0) + 1)]
    out["sample_mean_reward_per_iteration_printed"] = seq
    out["sample_mean_reward_per_iteration_complete"] = bool(seq) and all(v is not None for v in seq)
    m = None
    for m in re.finditer(r"Diffusing: 100%.*?\[(\d+):(\d+)<", text):
        pass
    out["tqdm_diffusion_elapsed_s"] = int(m.group(1)) * 60 + int(m.group(2)) if m else None
    return out


def parse_launcher(path: Path) -> dict:
    text = path.read_text()
    s = re.search(r"heavy\.sh: start (\S+) MemAvailable=(\d+)MB MemoryMax=(\d+)MB timeout=(\d+)s gpu_used_before=(\d+)MiB", text)
    e = re.search(r"heavy\.sh: end (\S+) exit=(\d+) gpu_used_after=(\d+)MiB", text)
    res = {"launcher_log": str(path), "launcher_start_line": s.group(0) if s else None,
           "launcher_end_line": e.group(0) if e else None,
           "exit_status": int(e.group(2)) if e else None, "wall_time_s_from_launcher": None}
    if s:
        res.update(launcher_start_utc=s.group(1), mem_available_at_start_mb=int(s.group(2)),
                   memory_max_mb=int(s.group(3)), timeout_s=int(s.group(4)), gpu_used_before_mib=int(s.group(5)))
    if s and e:
        f = "%Y-%m-%dT%H:%M:%SZ"
        res.update(launcher_end_utc=e.group(1), gpu_used_after_mib=int(e.group(3)),
                   wall_time_s_from_launcher=(datetime.strptime(e.group(1), f) - datetime.strptime(s.group(1), f)).total_seconds())
    return res


def describe_outputs(d: Path) -> dict:
    files = {}
    for name in ("mu_0ts.npy", "rollout.html"):
        p = d / name
        st = p.stat()
        files[name] = {"path": str(p), "bytes": st.st_size, "sha256": sha256(p),
                       "mtime_utc": datetime.utcfromtimestamp(st.st_mtime).strftime("%Y-%m-%dT%H:%M:%SZ")}
    arr = np.load(d / "mu_0ts.npy")
    files["mu_0ts.npy"].update(
        shape=list(arr.shape), dtype=str(arr.dtype), all_finite=bool(np.isfinite(arr).all()),
        min=float(arr.min()), max=float(arr.max()), mean=float(arr.mean()), abs_max=float(np.abs(arr).max()),
        nonzero_elements=int(np.count_nonzero(arr)), elements=int(arr.size),
        final_iterate_abs_max=float(np.abs(arr[-1]).max()),
        final_iterate_first_action=[float(v) for v in arr[-1, 0]],
        final_iterate_last_action=[float(v) for v in arr[-1, -1]],
    )
    html = (d / "rollout.html").read_text(errors="replace")
    files["rollout.html"].update(
        starts_with_doctype_html=html.lstrip().lower().startswith("<!doctype html>"),
        ends_with_closing_html_tag=html.rstrip().endswith("</html>"),
        embeds_compressed_system_variable='var system = "' in html,
    )
    return files


def compare(a: str, b: str) -> dict:
    da, db = SOURCES[a]["out"], SOURCES[b]["out"]
    A, B = np.load(da / "mu_0ts.npy"), np.load(db / "mu_0ts.npy")
    res = {"runs": [a, b], "shape": [list(A.shape), list(B.shape)], "shape_equal": A.shape == B.shape,
           "dtype_equal": A.dtype == B.dtype}
    if A.shape != B.shape:
        return res
    diff = np.abs(A.astype(np.float64) - B.astype(np.float64))
    per_iter = diff.reshape(diff.shape[0], -1).max(axis=1)
    nz = np.flatnonzero(per_iter > 0)
    res.update(
        mu_0ts_array_equal=bool(np.array_equal(A, B)),
        mu_0ts_max_abs_diff=float(diff.max()),
        mu_0ts_final_iterate_max_abs_diff=float(diff[-1].max()),
        mu_0ts_first_differing_iteration_index=int(nz[0]) if nz.size else None,
        mu_0ts_number_of_differing_elements=int((diff > 0).sum()),
        mu_0ts_number_of_elements=int(diff.size),
        mu_0ts_file_sha256_equal=sha256(da / "mu_0ts.npy") == sha256(db / "mu_0ts.npy"),
        rollout_html_sha256_equal=sha256(da / "rollout.html") == sha256(db / "rollout.html"),
        rollout_html_bytes=[(da / "rollout.html").stat().st_size, (db / "rollout.html").stat().st_size],
    )
    la, lb = parse_log(SOURCES[a]["log"]), parse_log(SOURCES[b]["log"])
    res.update(
        final_reward_printed=[la["final_reward_printed"], lb["final_reward_printed"]],
        final_reward_printed_equal=la["final_reward_printed"] == lb["final_reward_printed"],
        final_reward_printed_abs_diff=abs(la["final_reward"] - lb["final_reward"]),
        init_sigma_printed=[la["init_sigma_printed"], lb["init_sigma_printed"]],
        init_sigma_printed_equal=la["init_sigma_printed"] == lb["init_sigma_printed"],
    )
    sa, sb = la["sample_mean_reward_per_iteration_printed"], lb["sample_mean_reward_per_iteration_printed"]
    if la["sample_mean_reward_per_iteration_complete"] and lb["sample_mean_reward_per_iteration_complete"]:
        d = [abs(float(x) - float(y)) for x, y in zip(sa, sb)]
        res.update(
            sample_mean_reward_per_iteration_printed_equal=sa == sb,
            sample_mean_reward_per_iteration_printed_max_abs_diff=max(d),
            sample_mean_reward_per_iteration_count=len(sa),
        )
    return res


if __name__ == "__main__":
    result = {"numpy_version": np.__version__, "runs": {}, "comparisons": {}}
    for label, src in SOURCES.items():
        result["runs"][label] = {"execution": parse_launcher(src["launcher"]), "log": parse_log(src["log"]),
                                 "files": describe_outputs(src["out"])}
    result["comparisons"]["run1_vs_coordinator-probe"] = compare("run1", "coordinator-probe")
    result["comparisons"]["run1_vs_run2-interrupted"] = compare("run1", "run2-interrupted")
    (EVID / "comparison.json").write_text(json.dumps(result, indent=1) + "\n")
    print(json.dumps(result, indent=1))
