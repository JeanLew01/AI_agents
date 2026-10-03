# Assemble reports/executed_notebook_run_mbd_seeds_car2d.json from the captured evidence (standard library only).
# Every number in the report is read from a file under notebooks/run_mbd_seeds_car2d/; nothing is typed in by hand
# except descriptions.
#   python build_report.py [--hopper-state pending|done|not_attempted] [--hopper-note TEXT]
import argparse
import hashlib
import json
from pathlib import Path

EVID = Path(__file__).resolve().parent
PROJECT_ROOT = EVID.parents[1]
REPORT = PROJECT_ROOT / "reports" / "executed_notebook_run_mbd_seeds_car2d.json"
COMMIT = "c1eb913783f1713f7a1ebb657b34e0188d52cd8b"
EID = "run_mbd_seeds_car2d"

ap = argparse.ArgumentParser()
ap.add_argument("--hopper-state", default="pending")
ap.add_argument("--hopper-note", default="")
a = ap.parse_args()


def sha(p: Path):
    return hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else None


def rel(p: Path):
    return str(p.relative_to(PROJECT_ROOT))


def load(label):
    p = EVID / "outputs" / label / "parsed.json"
    return json.loads(p.read_text()) if p.exists() else None


def kv(path: Path):
    d = {}
    for ln in path.read_text().splitlines():
        parts = ln.split(" ", 1)
        if parts[0] == "version":
            name, _, ver = parts[1].partition(" ")
            d.setdefault("versions", {})[name] = ver
        elif len(parts) == 2:
            d[parts[0]] = parts[1]
    return d


def run_entry(label, r):
    m = r["run_meta"]
    out = EVID / "outputs" / label
    return {
        "label": label,
        "cwd": m.get("cwd"),
        "command": m.get("command"),
        "invoked_utc": m.get("invoked_utc"),
        "finished_utc": m.get("finished_utc"),
        "exit_status": r["exit_status"],
        "wall_seconds_including_lock_wait": float(m["wall_seconds_including_lock_wait"]) if "wall_seconds_including_lock_wait" in m else None,
        "launcher_stderr": r["launcher_stderr"],
        "scope_memory_peak_mb": r["scope"]["scope_memory_peak_mb"] if r["scope"] else None,
        "oom_kills": r["scope"]["oom_kills"] if r["scope"] else None,
        "log": rel(out / "stdout_stderr.log"),
        "log_sha256": r["log_sha256"],
        "log_bytes": r["log_bytes"],
        "parsed": rel(out / "parsed.json"),
        "files_written_by_upstream": r["files_written_by_upstream"],
    }


def ref_values(r):
    return {
        "rew_line": r["rew"]["line"] if r["rew"] else None,
        "reward_mean": r["rew"]["mean"] if r["rew"] else None,
        "reward_mean_text": r["rew"]["mean_text"] if r["rew"] else None,
        "reward_std": r["rew"]["std"] if r["rew"] else None,
        "reward_std_text": r["rew"]["std_text"] if r["rew"] else None,
        "time_line": r["time"]["line"] if r["time"] else None,
        "time_mean_s": r["time"]["mean_s"] if r["time"] else None,
        "time_std_s": r["time"]["std_s"] if r["time"] else None,
        "override_temp_sample_lines": r["override_temp_sample_lines"],
        "init_sigma_lines": r["init_sigma_lines"],
        "per_seed_progress_bar_last_step_sample_mean_reward_text": [
            b["last_step_sample_mean_reward_text"] for b in r["progress_bar_final_states"]
        ],
        "per_seed_progress_bar_steps": [f'{b["steps_done"]}/{b["steps_total"]}' for b in r["progress_bar_final_states"]],
    }


r1, r2, rh = load("run1"), load("run2"), load("hopper_run1")
cmp = json.loads((EVID / "outputs" / "replay_comparison_run1_vs_run2.json").read_text())
rt = kv(EVID / "logs" / "runtime_probe.log")
gpu = (EVID / "logs" / "gpu.txt").read_text().strip() if (EVID / "logs" / "gpu.txt").exists() else None

replay_ok = (
    r1["exit_status"] == 0 and r2["exit_status"] == 0
    and cmp["reward_mean_equal_exactly"] and cmp["reward_std_equal_exactly"]
)

hopper = {"state": a.hopper_state, "note": a.hopper_note or None}
hop_dir = EVID / "outputs" / "hopper_run1"
if rh is None and hop_dir.exists():
    # the supplementary run was launched but never produced a result: keep exactly what is on disk
    hm = {}
    if (hop_dir / "run_meta.txt").exists():
        for ln in (hop_dir / "run_meta.txt").read_text().splitlines():
            k, _, v = ln.partition(": ")
            hm[k] = v
    ls = hop_dir / "launcher_stderr.txt"
    hopper["partial_evidence"] = {
        "directory": rel(hop_dir),
        "command": hm.get("command"),
        "cwd": hm.get("cwd"),
        "invoked_utc": hm.get("invoked_utc"),
        "finished_utc": hm.get("finished_utc"),
        "exit_status": int(hm["exit_status"]) if "exit_status" in hm else None,
        "exit_status_note": None if "exit_status" in hm else "never recorded: the driver did not return",
        "launcher_stderr_bytes": ls.stat().st_size if ls.exists() else None,
        "launcher_printed_start_line": ("heavy.sh: start" in ls.read_text()) if ls.exists() else None,
        "stdout_stderr_log_exists": (hop_dir / "stdout_stderr.log").exists(),
        "files_present": sorted(p.name for p in hop_dir.iterdir()),
        "values": None,
        "values_note": "no value exists: the Python process was never started, so there is no log to parse",
    }
if rh is not None and rh["exit_status"] is not None:
    hopper.update(
        {
            "role": "supplementary single run (no replay), because the car2d summary is degenerate",
            "run": run_entry("hopper_run1", rh),
            "values": ref_values(rh),
        }
    )

report = {
    EID: {
        "execution_id": EID,
        "title": "Multi-seed evaluation (owner of mbd_evaluate_seeds)",
        "source_path": "mbd/scripts/run_mbd.py",
        "source_commit": COMMIT,
        "source_url": "https://github.com/LeCAR-Lab/model-based-diffusion",
        "source_sha256": {
            "mbd/scripts/run_mbd.py": sha(EVID / "source/mbd/scripts/run_mbd.py"),
            "mbd/planners/mbd_planner.py": sha(EVID / "source/mbd/planners/mbd_planner.py"),
            "mbd/envs/car2d.py": sha(EVID / "source/mbd/envs/car2d.py"),
            "mbd/envs/hopper.py": sha(EVID / "source/mbd/envs/hopper.py"),
            "mbd/utils.py": sha(EVID / "source/mbd/utils.py"),
        },
        "status": "succeeded" if replay_ok else "failed",
        "execution_mode": "native-command",
        "execution_path": rel(EVID / "run.sh"),
        "evidence_namespace": rel(EVID),
        "private_source_copy": {
            "path": rel(EVID / "source"),
            "created_with": f"git -C repo/model-based-diffusion archive {COMMIT} | tar -x -C notebooks/{EID}/source",
            "identity_check": "For each of the 34 files of the commit, `git hash-object --no-filters <file in copy>` was "
            "compared with the blob id from `git ls-tree -r <commit>`; the two sorted lists are identical "
            "(logs/source_commit_blobs.txt and logs/source_copy_blobs.txt have the same SHA-256). All 34 entries have "
            "mode 100644, there is no symbolic link. The SHA-256 of run_mbd.py in the copy equals `sha256_at_scan` of "
            "the scanner entry.",
            "commit_blob_list": rel(EVID / "logs/source_commit_blobs.txt"),
            "commit_blob_list_sha256": sha(EVID / "logs/source_commit_blobs.txt"),
            "copy_blob_list": rel(EVID / "logs/source_copy_blobs.txt"),
            "copy_blob_list_sha256": sha(EVID / "logs/source_copy_blobs.txt"),
            "copy_sha256_manifest": rel(EVID / "logs/source_copy_sha256.txt"),
            "copy_sha256_manifest_sha256": sha(EVID / "logs/source_copy_sha256.txt"),
            "files_after_runs": "unchanged; only __pycache__ directories were added by the interpreter (files_before.txt and "
            "files_after.txt of every run are identical)",
        },
        "import_resolution": {
            "how_run_mbd_imports_the_planner": "run_mbd.py line 6 does `import mbd` and uses `mbd.planners.mbd_planner.Args` / "
            "`run_diffusion` (lines 28-31). It does not touch sys.path. mbd/__init__.py imports utils, envs and planners; "
            "mbd/planners/__init__.py imports mbd_planner and path_integral.",
            "risk": "The project environment has an editable install of mbd pointing at the pinned checkout "
            "(site-packages/__editable__.mbd-0.0.1.pth -> repo/model-based-diffusion). Without PYTHONPATH the checkout "
            "would be imported instead of the copy.",
            "resolution": "PYTHONPATH=<copy> is set inside the launched command; PYTHONPATH entries precede site-packages "
            "and the .pth entry on sys.path.",
            "proof_command": "heavy.sh --timeout 300 --log logs/import_proof.log -- env PYTHONPATH=<copy> $PROJECT_PYTHON -c "
            "\"import mbd; print(mbd.__file__)\"  (cwd <copy>/mbd/scripts)",
            "proof_output": (EVID / "logs/import_proof.log").read_text().splitlines()[0],
            "planner_module_file": rt.get("mbd.planners.mbd_planner.__file__"),
            "env_module_file": rt.get("mbd.envs.car2d.__file__"),
            "proof_logs": [rel(EVID / "logs/import_proof.log"), rel(EVID / "logs/runtime_probe.log")],
        },
        "commands": [run_entry("run1", r1), run_entry("run2", r2)],
        "runtime": {
            "interpreter": rt.get("executable"),
            "python": rt.get("python"),
            "platform": rt.get("platform"),
            "package_versions": rt.get("versions"),
            "device": "cuda:0",
            "jax_devices": rt.get("jax.devices"),
            "jax_default_backend": rt.get("default_backend"),
            "jax_enable_x64": rt.get("x64"),
            "gpu": gpu,
            "environment_set_by_launcher": {"XLA_PYTHON_CLIENT_PREALLOCATE": "false", "MPLBACKEND": "Agg"},
            "environment_set_in_command": {"PYTHONPATH": str(EVID / "source")},
            "launcher": "/home/jixia/AI_agents/paper2agent/NMPC/mcp-build/heavy.sh",
            "launcher_sha256": sha(Path("/home/jixia/AI_agents/paper2agent/NMPC/mcp-build/heavy.sh")),
            "runtime_probe": rel(EVID / "runtime_probe.py"),
            "runtime_probe_log": rel(EVID / "logs/runtime_probe.log"),
        },
        "seed_and_data_provenance": {
            "seeds": "0..7, fixed by `for seed in range(8)` (run_mbd.py line 20); each becomes jax.random.PRNGKey(seed) "
            "(mbd_planner.py line 40). The command has no seed option in this mode.",
            "planner_parameters": "planner defaults (mbd_planner.py lines 29-35): Nsample 2048, Hsample 50, Ndiffuse 100, "
            "beta0 1e-4, betaT 1e-2, enable_demo False; not_render=True. For car2d the recommended-parameter tables have "
            "no entry, so temp_sample stays 0.1 (printed: `override temp_sample to 0.1`).",
            "input_data": "none supplied by the caller. Car2d.__init__ loads mbd/assets/car2d_xref.npy from the copy "
            "(used only for the demonstration terms, which are off here).",
            "input_files": {"mbd/assets/car2d_xref.npy": sha(EVID / "source/mbd/assets/car2d_xref.npy")},
        },
        "outputs": {
            "native_files": [],
            "native_files_note": "The script writes no file in this mode (not_render=True). Verified per run: no new file in "
            "the copy and no results/ directory (outputs/<run>/files_written_by_upstream.txt is empty).",
            "stdout_stderr_logs": {
                rel(EVID / "outputs/run1/stdout_stderr.log"): sha(EVID / "outputs/run1/stdout_stderr.log"),
                rel(EVID / "outputs/run2/stdout_stderr.log"): sha(EVID / "outputs/run2/stdout_stderr.log"),
            },
            "parsed": {
                rel(EVID / "outputs/run1/parsed.json"): sha(EVID / "outputs/run1/parsed.json"),
                rel(EVID / "outputs/run2/parsed.json"): sha(EVID / "outputs/run2/parsed.json"),
            },
            "driver_and_helpers": {
                rel(EVID / "run.sh"): sha(EVID / "run.sh"),
                rel(EVID / "parse_logs.py"): sha(EVID / "parse_logs.py"),
                rel(EVID / "compare_runs.py"): sha(EVID / "compare_runs.py"),
                rel(EVID / "build_report.py"): sha(EVID / "build_report.py"),
            },
        },
        "reference_values": {
            "env_name": "car2d",
            "algo": "mbd",
            "mode": "seed",
            **ref_values(r1),
            "reward_mean_sign_note": "The printed mean is `-0.00`: a negative number that rounds to zero at two decimals. "
            "float('-0.00') is -0.0, which compares equal to 0.0; a test that wants to pin the sign must compare the text.",
            "time_note": "wall-clock seconds per seed including JIT compilation; not a reference value (presence and "
            "positivity only).",
        },
        "per_seed_information_printed_by_the_script": {
            "final_reward_per_seed": None,
            "final_reward_per_seed_note": "run_mbd.py prints only the aggregate; the per-seed final rewards are never printed "
            "and are therefore not available from this command.",
            "what_is_printed_per_seed": "`override temp_sample to 0.1`, `init sigma = 6.30e-01` and one tqdm progress bar "
            "(99 reverse-diffusion steps) whose `rew=` postfix is the mean reward of the 2048 sampled trajectories at the "
            "current step, format .2e (mbd_planner.py lines 135 and 147). That quantity is not the final reward.",
            "progress_bar_last_step_sample_mean_reward_text": {
                "run1": ref_values(r1)["per_seed_progress_bar_last_step_sample_mean_reward_text"],
                "run2": ref_values(r2)["per_seed_progress_bar_last_step_sample_mean_reward_text"],
            },
            "all_progress_updates": "In both logs every captured progress update of every seed shows rew=0.00e+00 "
            "(run1: 849 updates, run2: 853 updates; counted with grep, see README).",
        },
        "degenerate_summary": {
            "is_degenerate": True,
            "explanation": "The printed summary is `rew: -0.00 \\pm 0.00`. A standard deviation below 0.005 over eight "
            "values together with a mean of magnitude below 0.005 bounds every per-seed final reward to within about 0.02 "
            "of zero (largest possible deviation is std * sqrt(8)); the exact per-seed values are not printed, so exact "
            "equality of the eight rewards is not shown by the log. In addition the sample-mean reward shown in the "
            "progress bars was 0.00e+00 at every captured diffusion step of every seed in both runs. The car2d reward "
            "(car2d.py lines 89-93) is 1 - (clip(distance to goal, 0, 0.2) / 0.2)^2, which is zero unless the car is within "
            "0.2 of the goal, so without the demonstration no sampled trajectory came close to the goal. Consequently "
            "this reference cannot distinguish seeds or detect a change of the planner's numerical behaviour; it verifies "
            "exit status, the output format and the eight-run structure only.",
            "all_rewards_zero_at_printed_precision": True,
            "exact_equality_of_the_eight_rewards_shown_by_log": False,
            "supplementary_hopper_run": hopper,
        },
        "replay_comparison": {
            **cmp,
            "result": "identical" if replay_ok else "different",
            "normalized_log_check": "After removing the intermediate progress updates and replacing the wall-clock fields "
            "(tqdm elapsed/remaining/rate, the `time:` line, the launcher's peak-memory figure), the two logs are "
            "identical line by line (27 lines each; command in README).",
            "file": rel(EVID / "outputs/replay_comparison_run1_vs_run2.json"),
        },
        "interruption": {
            "what": "machine freeze on 2026-10-02 at about 15:05Z (reported by the coordinator); heavy jobs were then disabled "
            "workspace-wide",
            "effect_on_this_execution": "Both car2d runs, their parsing and the replay comparison had finished before the "
            "freeze (run2 ended 14:59:39Z, comparison written 15:00:38Z, first report 15:02Z). Only the supplementary "
            "hopper run was lost; it had not started. After the freeze the report was rebuilt from the files on disk and "
            "checked against the raw logs with standard-library code only; no JAX command was run.",
        },
        "figures": None,
        "figures_note": "The command produces no figure (not_render=True).",
        "limitations": [
            "The car2d summary is degenerate (all rewards zero at two decimals); see degenerate_summary.",
            "Per-seed final rewards are not printed by upstream, so they are not part of the reference.",
            "The reward values are printed with two decimals only; equality of the printed text is the strongest check this "
            "command allows.",
            "stdout and stderr are captured in one file by the launcher (`--log`); tqdm writes its bars to stderr with "
            "carriage returns, so each bar is one long physical line.",
            "Lock waiting time is included in wall_seconds_including_lock_wait; the launcher's start/end lines give the "
            "actual run window (run1 34 s, run2 41 s for eight seeds).",
        ],
        "attempts": [
            {"n": 1, "label": "run1", "what": "documented command, car2d", "exit_status": r1["exit_status"], "outcome": "succeeded"},
            {"n": 2, "label": "run2", "what": "replay, identical arguments", "exit_status": r2["exit_status"], "outcome": "succeeded"},
        ],
        "coordinator_decisions": [],
    }
}
if rh is not None and rh["exit_status"] is not None:
    report[EID]["attempts"].append(
        {"n": 3, "label": "hopper_run1", "what": "same command with --env_name hopper (supplementary, single run)",
         "exit_status": rh["exit_status"], "outcome": "succeeded" if rh["exit_status"] == 0 and rh["rew"] else "failed"}
    )
elif "partial_evidence" in hopper:
    report[EID]["attempts"].append(
        {"n": 3, "label": "hopper_run1", "what": "same command with --env_name hopper (supplementary, single run)",
         "exit_status": None, "outcome": a.hopper_state}
    )
    report[EID]["limitations"].append(
        "The supplementary hopper evaluation produced no result (" + a.hopper_state + "), so there is no non-degenerate "
        "reference for this command."
    )
    report[EID]["coordinator_decisions"] = [
        "The car2d reference is degenerate. Decide whether mbd_evaluate_seeds is accepted with a structural reference "
        "only (exit status, eight runs, output format, `rew: -0.00 \\pm 0.00`), or whether a non-degenerate reference "
        "(hopper, eight seeds, about 35 minutes, about 1.2 GB or more) must be produced once heavy jobs are allowed again.",
        "The driver for that run is ready: notebooks/run_mbd_seeds_car2d/run.sh hopper_run1 hopper 3000 (not to be "
        "started while heavy jobs are disabled).",
    ]
REPORT.write_text(json.dumps(report, indent=1, ensure_ascii=False) + "\n")
print("wrote", REPORT, "status", report[EID]["status"], "hopper", hopper["state"])
