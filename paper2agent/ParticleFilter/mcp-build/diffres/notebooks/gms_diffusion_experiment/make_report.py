"""Assemble reports/executed_notebook_gms_diffusion_experiment.json from the saved evidence (stdlib + numpy only;
no JAX). Values are read from the evidence files; run facts (timestamps, peak memory) are parsed from heavy.sh logs."""
import hashlib
import json
import os
import re

import numpy as np

ROOT = '/home/jixia/AI_agents/paper2agent/ParticleFilter/mcp-build/diffres'
NS = 'notebooks/gms_diffusion_experiment'
N = f'{ROOT}/{NS}'
HEAVY = '/home/jixia/AI_agents/paper2agent/ParticleFilter/mcp-build/heavy.sh'
PY = f'{ROOT}/diffres-env/bin/python'
SCRIPT = f'{ROOT}/repo/diffres/experiments/gms/diffusion.py'


def sha(p):
    with open(p if p.startswith('/') else f'{ROOT}/{p}', 'rb') as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def heavy_log(name):
    txt = open(f'{N}/logs/{name}').read()
    launcher = '\n'.join(l for l in open(f'{N}/logs/heavy_launcher_stderr.txt') if l.startswith(name + ' '))
    start = re.search(r'start (\S+)', launcher).group(1)
    end = re.search(r'end (\S+) exit=(\d+)', launcher)
    peak = int(re.search(r'memory.peak=(\d+)MB', txt).group(1))
    oom = re.search(r'oom_kills=(\S*)', txt).group(1)
    from datetime import datetime
    dur = (datetime.fromisoformat(end.group(1).replace('Z', '+00:00')) - datetime.fromisoformat(start.replace('Z', '+00:00'))).total_seconds()
    return dict(log=f'{NS}/logs/{name}', launcher_lines=f'{NS}/logs/heavy_launcher_stderr.txt', heavy_start_utc=start,
                heavy_end_utc=end.group(1), runtime_seconds_excluding_lock_wait=dur,
                exit_status=int(end.group(2)), peak_memory_mb=peak, oom_kills=oom)


def rel(p):
    return os.path.relpath(p, ROOT)


cmp = json.load(open(f'{N}/data/replay_comparison.json'))
files = sorted(os.listdir(f'{N}/data'))
hashes = {f'{NS}/data/{f}': sha(f'{N}/data/{f}') for f in files}
for f in ['capture_driver.py', 'replay_driver.py', 'make_report.py']:
    hashes[f'{NS}/{f}'] = sha(f'{N}/{f}')

cfgs = {
    'A_jk_ode_T3_K128': dict(argv='--id_l=0 --id_u=0 --nsamples=1000 --a=-1. --T=3. --nsteps=128 --integrator=jentzen_and_kloeden',
                             log='native_A_jk_ode_T3_K128.log',
                             upstream_out='diffres--1.0-3.0-128-jentzen_and_kloeden-ode-0.npz',
                             paper=dict(table='tbl:app-gm-swd-1 (and Table tbl:gm-compare, best SWD)',
                                        swd_mean_std_scaled_1e_minus1='0.80 +- 0.21', resampling_variance_scaled_1e_minus2='3.74 +- 2.99 (Table tbl:gm-compare)',
                                        settings='n=10000, 100 MC runs')),
    'B_euler_sde_T1_K8': dict(argv='--id_l=0 --id_u=0 --nsamples=1000 --a=-1. --T=1. --nsteps=8 --integrator=euler --sde',
                              log='native_B_euler_sde_T1_K8.log',
                              upstream_out='diffres--1.0-1.0-8-euler-sde-0.npz',
                              paper=dict(table='tbl:app-gm-swd-1', swd_mean_std_scaled_1e_minus1='2.39 +- 0.57',
                                         resampling_variance_scaled_1e_minus2=None, settings='n=10000, 100 MC runs')),
}

runs = {}
for name, c in cfgs.items():
    nat = np.load(f'{N}/data/native_{name}.npz')
    cc = cmp['configs'][name]
    runs[name] = dict(
        command=f'cd {NS}/work_native && {HEAVY} --limit-mb 1200 --timeout 1800 --log {NS}/logs/{c["log"]} -- '
                f'env PYTHONDONTWRITEBYTECODE=1 {PY} {SCRIPT} {c["argv"]}',
        cwd=f'{NS}/work_native', **heavy_log(c['log']),
        upstream_output_file=f'{NS}/work_native/gms/results/{c["upstream_out"]}',
        reference_output_copy=f'{NS}/data/native_{name}.npz',
        printed_line=open(f'{N}/logs/{c["log"]}').read().splitlines()[0],
        metrics=dict(swd_err=float(nat['err']), swd_err_repr=repr(float(nat['err'])),
                     residual=nat['residual'].tolist(), sum_sq_residual=float(np.sum(nat['residual'] ** 2)),
                     output_log_weights_unique=np.unique(nat['approx_post_log_ws']).tolist()),
        diffusion_resampling_call=json.load(open(f'{N}/data/args_{name}.json'))['diffusion_resampling_call'],
        captured_inputs=f'{NS}/data/inputs_{name}.npz',
        captured_args=f'{NS}/data/args_{name}.json',
        input_checks=cc['input_checks'],
        output_summary=cc['summary'],
        paper_reference=c['paper'],
    )

report = {
    'gms_diffusion_experiment': dict(
        execution_id='gms_diffusion_experiment',
        status='success',
        module='resampling',
        supports_tools=['diffres_resample_particles_diffusion'],
        source_path='repo/diffres/experiments/gms/diffusion.py',
        source_sha256=sha('repo/diffres/experiments/gms/diffusion.py'),
        source_sha256_matches_scanner=sha('repo/diffres/experiments/gms/diffusion.py') == '886496bab31d254ac8030286ea350e48db817bd680cccc8cdda50c58a94ba774',
        source_revision='767effe3e755067eb8a04422597fbf37eb8ab754',
        source_url='https://github.com/zgbkdlm/diffres/blob/767effe3e755067eb8a04422597fbf37eb8ab754/experiments/gms/diffusion.py',
        upstream_function='diffres.resampling.diffusion_resampling (diffres/resampling.py lines 195-308)',
        execution_mode='native_script (unmodified upstream script run directly; plus runpy capture driver and replay driver)',
        execution_path='repo/diffres/experiments/gms/diffusion.py',
        drivers=dict(capture=f'{NS}/capture_driver.py', replay=f'{NS}/replay_driver.py', report_builder=f'{NS}/make_report.py'),
        runtime=dict(python=f'{PY} (CPython 3.11.17)', jax=cmp['jax_version'], backend=cmp['backend'], jax_enable_x64=True,
                     launcher=f'{HEAVY} --limit-mb 1200 --timeout 1800 (JAX_PLATFORMS=cpu, no GPU; gpu_used 0 MiB before/after)',
                     env='PYTHONDONTWRITEBYTECODE=1 so nothing was written under repo/'),
        changed_arguments_vs_upstream=dict(
            reference='experiments/run_gms.sh (nsamples=10000, --id_l=0 --id_u=99, a=-1., T in {1,2,3}, nsteps in {8,32,128}, 7 integrator/flow combos)',
            changes=['--id_u=99 -> --id_u=0 (single Monte Carlo id 0)', '--nsamples=10000 -> --nsamples=1000 (memory: (n,n,d) float64 arrays per step)'],
            unchanged=['--a=-1. (as run_gms.sh; script default -0.5 overridden as upstream does)', 'dx=8, dy=1, c=5, offset=0 (script defaults, as run_gms.sh)',
                       'config A: --T=3. --nsteps=128 --integrator=jentzen_and_kloeden, ODE (paper best SWD in Table tbl:gm-compare / tbl:app-gm-swd-1)',
                       'config B: --T=1. --nsteps=8 --integrator=euler --sde (Euler-Maruyama SDE path, in run_gms.sh grid)']),
        data_provenance=dict(
            rnd_keys='repo/diffres/experiments/rnd_keys.npy copied into work_native/ and work_capture/ (generated upstream by experiments/generate_keys.py: PRNGKey(666) split 10000)',
            rnd_keys_sha256=sha('repo/diffres/experiments/rnd_keys.npy'),
            mc_key_row0=json.load(open(f'{N}/data/args_A_jk_ode_T3_K128.json'))['key_mc'],
            data_generation='script-internal: GM prior (c=5, d=8, means U[-5,5], covs = g g^T + I), prior samples via diffres.tools.sampling_gm, log-likelihood weights normalised with logsumexp, exact posterior via diffres.tools.gm_lin_posterior',
            diffusion_resampling_key_A=json.load(open(f'{N}/data/args_A_jk_ode_T3_K128.json'))['key'],
            diffusion_resampling_key_B=json.load(open(f'{N}/data/args_B_euler_sde_T1_K8.json'))['key'],
            note='Both configs use the same MC key, hence identical prior samples/log-weights/posterior samples and the same resampling key; only a/ts/integrator/ode differ.'),
        runs=runs,
        capture_run=dict(
            command=f'cd {NS}/work_capture && {HEAVY} --limit-mb 1200 --timeout 1800 --log {NS}/logs/capture_A_B.log -- env PYTHONDONTWRITEBYTECODE=1 {PY} {NS}/capture_driver.py {NS}/data',
            **heavy_log('capture_A_B.log'),
            method='runpy of the unmodified script for both configs; jax.jit wrapper records concrete args/outputs of the script\'s jitted `resampling` and `swd` (same XLA program), diffusion_resampling wrapper records static args at trace time, gm_lin_posterior wrapper records inputs/outputs',
            non_invasive_check={k: v['capture_vs_native'] for k, v in cmp['configs'].items()}),
        replay=dict(
            command=f'cd {NS} && {HEAVY} --limit-mb 1200 --timeout 1800 --log {NS}/logs/replay.log -- env PYTHONDONTWRITEBYTECODE=1 {PY} {NS}/replay_driver.py',
            **heavy_log('replay.log'),
            method='fresh process, x64, load data/inputs_<cfg>.npz, call diffres.resampling.diffusion_resampling inside jax.jit exactly as the script; recompute SWD with ott sliced_wasserstein(PNormP(p=1), n_proj=1000) and the mean residual as the script does; extra eager (no outer jit) call',
            comparison_file=f'{NS}/data/replay_comparison.json',
            results={k: dict(jit=v['replay_jit_vs_native'], eager=v['replay_eager_vs_native']) for k, v in cmp['configs'].items()},
            tolerance_policy='jit replay: bitwise required and observed (same key/inputs/x64/CPU). Eager call: not bitwise because XLA compiles the computation differently without the outer jit; observed max |diff| 4.9e-13 (A) and 8.7e-14 (B), within the ~1e-12 expectation stated in the brief.'),
        figures=dict(applicable=False, reason='experiments/gms/diffusion.py produces no plots; only an .npz and a printed line.'),
        outputs_and_hashes=hashes,
        key_reference_numbers=dict(
            A_jk_ode_T3_K128=dict(swd=runs['A_jk_ode_T3_K128']['metrics']['swd_err'], sum_sq_residual=runs['A_jk_ode_T3_K128']['metrics']['sum_sq_residual']),
            B_euler_sde_T1_K8=dict(swd=runs['B_euler_sde_T1_K8']['metrics']['swd_err'], sum_sq_residual=runs['B_euler_sde_T1_K8']['metrics']['sum_sq_residual']),
            input_ess=cmp['configs']['A_jk_ode_T3_K128']['input_checks']['ess']),
        limitations=[
            'Single MC id (0) and n=1000 instead of 100 MC ids and n=10000: the SWD values (0.224, 0.269) are not comparable to the paper averages (0.080 +- 0.021 and 0.239 +- 0.057 at n=10000). SWD at n=1000 is dominated by finite-sample error (ESS of the input weights is about 130), so these numbers are reference values for replaying the exact same call, not reproductions of the paper table.',
            'Only two of the seven integrator/flow combinations in run_gms.sh were executed (jentzen_and_kloeden ODE and euler SDE); lord_and_rougemont, tweedie, and the remaining ODE/SDE combos were not run here (test_filters.py covered them at stage 1).',
            'The upstream script saves only post_samples, approx_post_log_ws, approx_post_samples, err, residual; the inputs to diffusion_resampling (key, log_ws, prior samples, ts) were captured by the runpy capture driver, which was shown to produce bitwise-identical script outputs to the native run.',
            'The work_native/ and work_capture/ scratch folders each contain a copy of rnd_keys.npy (sha256 above) and the script\'s ./gms/results output.'],
        attempts=[
            dict(n=1, what='native config A', exit=0), dict(n=2, what='native config B', exit=0),
            dict(n=3, what='capture driver (A and B)', exit=0), dict(n=4, what='replay driver', exit=0)],
        repo_unmodified='git status --short --ignored in repo/diffres is empty after all runs; HEAD 767effe3e755067eb8a04422597fbf37eb8ab754',
    )
}
with open(f'{ROOT}/reports/executed_notebook_gms_diffusion_experiment.json', 'w') as fh:
    json.dump(report, fh, indent=1)
print('written')
