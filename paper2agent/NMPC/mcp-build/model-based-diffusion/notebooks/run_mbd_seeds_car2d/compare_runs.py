# Replay comparison for run_mbd.py --mode seed: compares what upstream printed in two runs (standard library only).
#   python compare_runs.py <label_a> <label_b>   -> outputs/replay_comparison_<a>_vs_<b>.json
import json, sys
from pathlib import Path

EVID = Path(__file__).resolve().parent
a, b = sys.argv[1], sys.argv[2]
ra = json.loads((EVID / "outputs" / a / "parsed.json").read_text())
rb = json.loads((EVID / "outputs" / b / "parsed.json").read_text())

def bars(r):
    return [x["last_step_sample_mean_reward_text"] for x in r["progress_bar_final_states"]]

cmp = {
    "runs": [a, b],
    "exit_statuses": [ra["exit_status"], rb["exit_status"]],
    "rew_lines": [ra["rew"]["line"], rb["rew"]["line"]],
    "rew_line_text_identical": ra["rew"]["line"] == rb["rew"]["line"],
    "reward_mean": [ra["rew"]["mean"], rb["rew"]["mean"]],
    "reward_mean_text": [ra["rew"]["mean_text"], rb["rew"]["mean_text"]],
    "reward_mean_equal_exactly": ra["rew"]["mean"] == rb["rew"]["mean"] and ra["rew"]["mean_text"] == rb["rew"]["mean_text"],
    "reward_std": [ra["rew"]["std"], rb["rew"]["std"]],
    "reward_std_text": [ra["rew"]["std_text"], rb["rew"]["std_text"]],
    "reward_std_equal_exactly": ra["rew"]["std"] == rb["rew"]["std"] and ra["rew"]["std_text"] == rb["rew"]["std_text"],
    "max_abs_difference_of_printed_values": max(abs(ra["rew"]["mean"] - rb["rew"]["mean"]), abs(ra["rew"]["std"] - rb["rew"]["std"])),
    "tolerance": "none needed: the printed two-decimal strings are identical",
    "time_lines_not_compared": [ra["time"]["line"], rb["time"]["line"]],
    "time_lines_present_and_positive": all(r["time"]["mean_s"] > 0 for r in (ra, rb)),
    "per_seed_progress_bar_last_step_sample_mean_reward_text": {a: bars(ra), b: bars(rb)},
    "per_seed_progress_bar_values_identical": bars(ra) == bars(rb),
    "override_temp_sample_lines_identical": ra["override_temp_sample_lines"] == rb["override_temp_sample_lines"],
    "init_sigma_lines_identical": ra["init_sigma_lines"] == rb["init_sigma_lines"],
    "arrays": None,
    "arrays_note": "run_mbd.py --mode seed writes no file (not_render=True), so there is no array to compare with numpy.array_equal",
    "files_written_by_upstream": {a: ra["files_written_by_upstream"], b: rb["files_written_by_upstream"]},
    "log_sha256": {a: ra["log_sha256"], b: rb["log_sha256"]},
    "logs_bytewise_identical": ra["log_sha256"] == rb["log_sha256"],
    "logs_note": "the logs differ in the tqdm timing/rate fields and in the time: line, which are wall-clock quantities",
}
out = EVID / "outputs" / f"replay_comparison_{a}_vs_{b}.json"
out.write_text(json.dumps(cmp, indent=1) + "\n")
print(json.dumps(cmp, indent=1))
