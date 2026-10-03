# Parse the captured logs of run_mbd.py --mode seed (standard library only, no JAX import).
#
#   python parse_logs.py <label> [<label> ...]      -> writes outputs/<label>/parsed.json, prints a summary
#
# What is parsed is only what upstream printed:
#   * `rew: <mean> \pm <std>`  (run_mbd.py line 38, two decimals)
#   * `time: <mean> \pm <std>` (run_mbd.py line 39, wall-clock seconds, not a reference value)
#   * `override temp_sample to ...` and `init sigma = ...` (mbd_planner.py lines 69 and 93), once per seed
#   * the last state of each tqdm progress bar (mbd_planner.py lines 141-147). Its `rew=` postfix is the mean
#     reward over the Nsample sampled trajectories at the last reverse-diffusion step (i = 1), printed with
#     format .2e. It is NOT the final reward that enters the `rew:` summary (that one is never printed per seed).
import hashlib
import json
import re
import sys
from pathlib import Path

EVID = Path(__file__).resolve().parent

REW = re.compile(r"^rew: (\S+) \\pm (\S+)$")
TIME = re.compile(r"^time: (\S+) \\pm (\S+)$")
TEMP = re.compile(r"^override temp_sample to (\S+)$")
SIGMA = re.compile(r"^init sigma = (\S+)$")
BAR = re.compile(r"^Diffusing:\s+(\d+)%\|.*\|\s*(\d+)/(\d+) \[.*?(?:, rew=(\S+?))?\]\s*$")
PEAK = re.compile(r"^heavy\.sh: scope memory\.peak=(\d+)MB oom_kills=(\d*)$")


def parse(label: str) -> dict:
    out = EVID / "outputs" / label
    log = out / "stdout_stderr.log"
    raw = log.read_bytes()
    text = raw.decode("utf-8", errors="replace")
    rew = tim = None
    temps, sigmas, bars, peak = [], [], [], None
    # a physical line holds the whole history of one progress bar, separated by carriage returns
    for line in text.split("\n"):
        segs = [s for s in line.split("\r") if s.strip()]
        if not segs:
            continue
        last = segs[-1].rstrip()
        m = BAR.match(last)
        if m:
            bars.append(
                {
                    "percent": int(m.group(1)),
                    "steps_done": int(m.group(2)),
                    "steps_total": int(m.group(3)),
                    "last_step_sample_mean_reward_text": m.group(4),
                }
            )
            continue
        for s in segs:
            s = s.rstrip()
            if (m := REW.match(s)) and rew is None:
                rew = {"line": s, "mean_text": m.group(1), "std_text": m.group(2),
                       "mean": float(m.group(1)), "std": float(m.group(2))}
            elif (m := TIME.match(s)) and tim is None:
                tim = {"line": s, "mean_s": float(m.group(1)), "std_s": float(m.group(2))}
            elif m := TEMP.match(s):
                temps.append(m.group(1))
            elif m := SIGMA.match(s):
                sigmas.append(m.group(1))
            elif m := PEAK.match(s):
                peak = {"scope_memory_peak_mb": int(m.group(1)), "oom_kills": m.group(2)}
    # one bar per seed; tqdm may repeat the 100 % state of a bar on its own line, keep completed bars in order
    completed = [b for b in bars if b["steps_done"] == b["steps_total"]]
    meta = {}
    mp = out / "run_meta.txt"
    if mp.exists():
        for ln in mp.read_text().splitlines():
            k, _, v = ln.partition(": ")
            meta[k] = v
    launcher = (out / "launcher_stderr.txt").read_text().splitlines() if (out / "launcher_stderr.txt").exists() else []
    res = {
        "label": label,
        "log": str(log),
        "log_sha256": hashlib.sha256(raw).hexdigest(),
        "log_bytes": len(raw),
        "exit_status": int(meta["exit_status"]) if "exit_status" in meta else None,
        "rew": rew,
        "time": tim,
        "override_temp_sample_lines": temps,
        "init_sigma_lines": sigmas,
        "progress_bar_lines_at_100_percent": len(completed),
        "progress_bar_final_states": completed,
        "launcher_stderr": launcher,
        "scope": peak,
        "run_meta": meta,
        "files_written_by_upstream": (out / "files_written_by_upstream.txt").read_text().split()
        if (out / "files_written_by_upstream.txt").exists() else None,
    }
    (out / "parsed.json").write_text(json.dumps(res, indent=1) + "\n")
    return res


if __name__ == "__main__":
    for lab in sys.argv[1:]:
        r = parse(lab)
        print(lab, "exit", r["exit_status"], "|", r["rew"] and r["rew"]["line"], "|", r["time"] and r["time"]["line"])
        print("  temp lines:", r["override_temp_sample_lines"])
        print("  sigma lines:", r["init_sigma_lines"])
        print("  bar finals:", [(b["steps_done"], b["last_step_sample_mean_reward_text"]) for b in r["progress_bar_final_states"]])
        print("  scope:", r["scope"], "| new files:", r["files_written_by_upstream"])
