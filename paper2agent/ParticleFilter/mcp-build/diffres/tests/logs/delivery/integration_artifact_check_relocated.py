"""ADAPTED COPY for delivery validation: only the two path roots changed (acceptance output root -> extracted package; notebooks/ -> absolute workspace references). Criteria unchanged."""
"""Compare acceptance-run artifacts (tmp/outputs/acceptance) with the executors' saved upstream outputs."""
import glob, sys
import numpy as np
L = lambda p, k: np.asarray(np.load(p)[k])
refs = {
    'gms diffusion euler SDE T1 K8': L('/home/jixia/AI_agents/paper2agent/ParticleFilter/mcp-build/diffres/notebooks/gms_diffusion_experiment/data/native_B_euler_sde_T1_K8.npz', 'approx_post_samples'),
    'gms soft 0.9': L('/home/jixia/AI_agents/paper2agent/ParticleFilter/mcp-build/diffres/notebooks/gms_soft_experiment/data/soft_gms_outputs.npz', 'approx_post_samples'),
    'gms gumbel 0.1': L('/home/jixia/AI_agents/paper2agent/ParticleFilter/mcp-build/diffres/notebooks/gms_gumbel_experiment/data/gumbel_inputs_outputs.npz', 'approx_post_samples'),
    'gm notebook diffusion': L('/home/jixia/AI_agents/paper2agent/ParticleFilter/mcp-build/diffres/notebooks/gaussian_mixture_demo/data/outputs_capture.npz', 'approx_post_samples'),
}
d = np.load('/home/jixia/AI_agents/paper2agent/ParticleFilter/mcp-build/diffres/notebooks/gms_baselines_experiment/data/replay_ot_eps0.3.npz')
refs['gms OT 0.3'] = np.asarray(d[[k for k in d if 'samples' in k and 'prior' not in k and k != 'post_samples'][0]])
found = {}
for f in sorted(glob.glob('/tmp/claude-1000/-home-jixia-AI-agents/ef6b2c1c-3bd8-4cd2-9bf4-2412bb4b0690/scratchpad/delivery test/diffres-mcp/tmp/outputs/acceptance/*/resampled.npz')):
    s = np.load(f)['samples']
    for name, r in refs.items():
        if r.shape == s.shape and np.max(np.abs(r - s)) < 1e-12:
            found[name] = float(np.max(np.abs(r - s)))
gd = np.load('/home/jixia/AI_agents/paper2agent/ParticleFilter/mcp-build/diffres/notebooks/lgssm_gradient_demo/data/reference_nsteps16_np8.npz')
sim = [f for f in glob.glob('/tmp/claude-1000/-home-jixia-AI-agents/ef6b2c1c-3bd8-4cd2-9bf4-2412bb4b0690/scratchpad/delivery test/diffres-mcp/tmp/outputs/acceptance/*/data.npz')
       if np.load(f)['xs'].size == gd['xs'].size and np.array_equal(np.load(f)['xs'].reshape(-1), gd['xs'].reshape(-1))
       and np.array_equal(np.load(f)['ys'].reshape(-1), gd['ys'].reshape(-1))]
kal = sorted(float(np.load(f)['nll']) for f in glob.glob('/tmp/claude-1000/-home-jixia-AI-agents/ef6b2c1c-3bd8-4cd2-9bf4-2412bb4b0690/scratchpad/delivery test/diffres-mcp/tmp/outputs/acceptance/*/kalman_results.npz'))
fc = np.load('/home/jixia/AI_agents/paper2agent/ParticleFilter/mcp-build/diffres/notebooks/filters_tests/outputs/capture_outputs.npz')
pf = [float(np.load(f)['nll']) for f in glob.glob('/tmp/claude-1000/-home-jixia-AI-agents/ef6b2c1c-3bd8-4cd2-9bf4-2412bb4b0690/scratchpad/delivery test/diffres-mcp/tmp/outputs/acceptance/*/particle_filter.npz')]
checks = {
    'resampling outputs matching references': found,
    'simulate == demo xs/ys (bitwise)': len(sim) >= 1,
    'kalman nll demo theta 34.829210096507474': 34.829210096507474 in kal,
    'kalman nll OU 141.42165070795778': float(fc['kf/nll']) in kal,
    'pf nll diffusion tweedie == filters_tests': float(fc['pf/diffusion_tweedie/nll']) in pf,
}
print(checks)
ok = len(found) == 5 and all(v for k, v in checks.items() if k != 'resampling outputs matching references')
print('ALL OK' if ok else 'MISMATCH'); sys.exit(0 if ok else 1)
