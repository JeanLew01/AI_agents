"""Parse the two captured logs of `run_mbd.py --env_name car2d --algo mbd --mode temp` and compare them.

Reads only outputs/run1/stdout_stderr.log and outputs/run2/stdout_stderr.log (numpy only, no JAX).
Writes replay_comparison.json next to this file.
"""
import hashlib
import json
import re
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
TEMPS = [0.01, 0.03, 0.06, 0.1, 0.2, 0.4, 0.6, 0.8]  # run_mbd.py:43


def parse(log_path: Path) -> dict:
    raw = log_path.read_bytes()
    text = raw.decode("utf-8", errors="replace").replace("\r", "\n")
    m = re.search(r"^rews: \[(.*?)\]", text, flags=re.S | re.M)
    if m is None:
        raise SystemExit(f"no `rews: [...]` in {log_path}")
    rew_tokens = m.group(1).split()
    m2 = re.search(r"^best_temp: (\S+)", text, flags=re.M)
    if m2 is None:
        raise SystemExit(f"no `best_temp:` in {log_path}")
    progress = re.findall(r"rew=([-+0-9.eE]+)", text)
    final_bar = re.findall(r"Diffusing: 100%\|[^|]*\| (\d+)/(\d+) \[[^\]]*rew=([-+0-9.eE]+)\]", text)
    return {
        "log": str(log_path),
        "log_sha256": hashlib.sha256(raw).hexdigest(),
        "rews_printed_block": "rews: [" + m.group(1) + "]",
        "rews_tokens": rew_tokens,
        "rews_float32": np.array(rew_tokens, dtype=np.float32),
        "best_temp_token": m2.group(1),
        "best_temp": float(m2.group(1)),
        "init_sigma_lines": re.findall(r"^init sigma = (\S+)", text, flags=re.M),
        "override_lines": len(re.findall(r"^override temp_sample", text, flags=re.M)),
        "completed_progress_bars": [
            {"steps_done": int(a), "steps_total": int(b), "last_displayed_sample_mean_rew": c} for a, b, c in final_bar
        ],
        "displayed_progress_rew_values": {v: progress.count(v) for v in sorted(set(progress))},
        "traceback_lines": len(re.findall(r"Traceback", text)),
    }


r1 = parse(HERE / "outputs/run1/stdout_stderr.log")
r2 = parse(HERE / "outputs/run2/stdout_stderr.log")
a, b = r1["rews_float32"], r2["rews_float32"]

result = {
    "temperatures_run_mbd_py_line_43": TEMPS,
    "run1": {k: (v.tolist() if isinstance(v, np.ndarray) else v) for k, v in r1.items()},
    "run2": {k: (v.tolist() if isinstance(v, np.ndarray) else v) for k, v in r2.items()},
    "run1_rews_repr": [repr(x) for x in a],
    "run2_rews_repr": [repr(x) for x in b],
    "comparison": {
        "rews_shape_run1": list(a.shape),
        "rews_shape_run2": list(b.shape),
        "rews_dtype_as_parsed": str(a.dtype),
        "rews_tokens_identical": r1["rews_tokens"] == r2["rews_tokens"],
        "rews_numpy_array_equal": bool(np.array_equal(a, b)),
        "rews_max_abs_diff": float(np.max(np.abs(a.astype(np.float64) - b.astype(np.float64)))),
        "best_temp_identical": r1["best_temp_token"] == r2["best_temp_token"],
        "init_sigma_lines_identical": r1["init_sigma_lines"] == r2["init_sigma_lines"],
        "whole_log_bytes_identical": r1["log_sha256"] == r2["log_sha256"],
        "whole_log_note": "The logs contain tqdm timing text (elapsed time, it/s), so byte identity of the whole log is not expected.",
    },
    "degeneracy": {
        "n_unique_rewards_run1": int(np.unique(a).size),
        "n_unique_rewards_run2": int(np.unique(b).size),
        "unique_rewards_run1": [repr(x) for x in np.unique(a)],
        "all_eight_rewards_equal": bool(np.unique(a).size == 1 and np.unique(b).size == 1),
        "argmax_index_run1": int(np.argmax(a)),
        "best_temp_is_first_grid_value_by_argmax_tie_rule": bool(
            np.unique(a).size == 1 and float(r1["best_temp_token"]) == TEMPS[0]
        ),
        "minus_float32_eps": repr(-np.finfo(np.float32).eps),
        "reward_equals_minus_float32_eps": bool(np.all(a == -np.finfo(np.float32).eps)),
    },
}
(HERE / "replay_comparison.json").write_text(json.dumps(result, indent=1) + "\n")
print(json.dumps({k: result[k] for k in ("comparison", "degeneracy")}, indent=1))
print("run1 rews:", result["run1_rews_repr"], "best_temp:", r1["best_temp_token"])
print("run2 rews:", result["run2_rews_repr"], "best_temp:", r2["best_temp_token"])
print("run1 bars:", r1["completed_progress_bars"])
print("run1 displayed rew values:", r1["displayed_progress_rew_values"], "run2:", r2["displayed_progress_rew_values"])
