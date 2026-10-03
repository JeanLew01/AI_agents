"""Capture and replay driver for repo/diffres/demos/gaussian_mixture.ipynb (execution_id gaussian_mixture_demo).

This driver does not re-implement any algorithm.

capture: reads the unchanged upstream notebook, checks its sha256, and executes the source of its code cells
         (cells 2, 4, 6, then 7 for the figure) verbatim in one namespace. It saves the notebook's own inputs to the
         resampling step (key, log_ws, prior_samples; float64 / uint32), the resampling arguments, and the three
         resample sets it produced, plus a re-rendering of the cell-7 figure through IPython's print_figure (the
         function the inline backend uses), so it can be compared with the figure in the papermill run.
replay:  in a fresh process, loads only the saved inputs/arguments, calls the upstream functions
         diffres.resampling.diffusion_resampling / ensemble_ot / multinomial directly, compares with the captured
         outputs, re-renders the notebook's cell-7 plotting code with the replayed arrays and compares the pixels
         with the figure extracted from the papermill-executed notebook.

Usage (always through heavy.sh): python gaussian_mixture_driver.py {capture|replay}
"""
import hashlib
import io
import json
import sys
import time
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
PROJECT_ROOT = HERE.parents[1]
NOTEBOOK = PROJECT_ROOT / 'repo/diffres/demos/gaussian_mixture.ipynb'
NOTEBOOK_SHA256 = '52d2c7fc97fe8ddeacb84e4dd4204869dec34d0092b5060653412cf599e3e295'
DATA = HERE / 'data'
PAPERMILL_FIGURE = HERE / 'images/figure_1.png'

INPUTS_NPZ = DATA / 'inputs_resampling.npz'
ARGS_JSON = DATA / 'resampling_arguments.json'
CAPTURE_NPZ = DATA / 'outputs_capture.npz'
REPLAY_NPZ = DATA / 'outputs_replay.npz'
EXTRA_NPZ = DATA / 'notebook_context.npz'


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def code_cells():
    raw = NOTEBOOK.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if digest != NOTEBOOK_SHA256:
        raise RuntimeError(f'notebook sha256 mismatch: {digest}')
    nb = json.loads(raw)
    return {i: ''.join(c['source']) for i, c in enumerate(nb['cells']) if c['cell_type'] == 'code'}


def render_png(fig):
    from IPython.core.pylabtools import print_figure
    return print_figure(fig, 'png')  # same call the matplotlib_inline backend makes (bbox_inches='tight')


def decode_png(data):
    import matplotlib.image as mpimg
    return mpimg.imread(io.BytesIO(data), format='png')


def summary(ns_arrays):
    out = {}
    for k, v in ns_arrays.items():
        v = np.asarray(v)
        out[k] = {'shape': list(v.shape), 'dtype': str(v.dtype),
                  'mean_dims01': v.reshape(v.shape[0], -1).mean(axis=0)[:2].tolist() if v.ndim == 2 else None,
                  'mean_all': float(v.mean()), 'std_all': float(v.std())}
    return out


def capture():
    import matplotlib
    matplotlib.use('Agg')
    cells = code_cells()
    assert sorted(cells) == [2, 4, 6, 7], sorted(cells)
    ns = {}
    timings = {}
    for i in (2, 4):
        t0 = time.time()
        exec(compile(cells[i], f'gaussian_mixture.ipynb[cell {i}]', 'exec'), ns)
        timings[f'cell_{i}'] = time.time() - t0
    import jax
    assert jax.config.jax_enable_x64
    # Key before cell 6: cell 6 splits it once more and uses the result for all three resamplers.
    key_before_cell6 = np.asarray(ns['key'])
    t0 = time.time()
    exec(compile(cells[6], 'gaussian_mixture.ipynb[cell 6]', 'exec'), ns)
    jax.block_until_ready(ns['approx_post_samples'])
    timings['cell_6'] = time.time() - t0
    key_resample = np.asarray(ns['key'])

    DATA.mkdir(parents=True, exist_ok=True)
    np.savez(INPUTS_NPZ,
             key=key_resample.astype(np.uint32),
             log_ws=np.asarray(ns['log_ws'], dtype=np.float64),
             prior_samples=np.asarray(ns['prior_samples'], dtype=np.float64),
             ts=np.asarray(ns['ts'], dtype=np.float64))
    args = {
        'x64': True,
        'key': {'description': 'jax.random.PRNGKey(666) split 4 times as in cells 2/4/6 (raw uint32[2] key)',
                'value': key_resample.tolist(), 'key_before_cell6': key_before_cell6.tolist(),
                'construct': 'jnp.asarray(np.load(inputs)["key"])  # dtype uint32'},
        'diffusion_resampling': {'function': 'diffres.resampling.diffusion_resampling',
                                 'call': 'diffusion_resampling(key, log_ws, prior_samples, a, ts, integrator=integrator, ode=ode)',
                                 'a': ns['a'], 'T': ns['T'], 'nsteps': ns['nsteps'],
                                 'ts': 'jnp.linspace(0., T, nsteps + 1) (saved as inputs ts, float64, 33 points)',
                                 'integrator': ns['integrator'], 'ode': ns['ode'],
                                 'jitter': 0.0, 'einsum': False, 'defaults_used': ['jitter', 'einsum']},
        'ensemble_ot': {'function': 'diffres.resampling.ensemble_ot',
                        'call': 'ensemble_ot(key, log_ws, prior_samples, eps=0.3)',
                        'eps': 0.3, 'implicit_diff': True, 'defaults_used': ['implicit_diff']},
        'multinomial': {'function': 'diffres.resampling.multinomial',
                        'call': 'multinomial(key, log_ws, prior_samples)'},
        'notes': 'log_ws already normalised by logsumexp in cell 4; all three calls share the same key.',
        'notebook_constants': {'nsamples': ns['nsamples'], 'c': ns['c'], 'd': ns['d'], 'dy': ns['dy'],
                               'seed': 666},
    }
    ARGS_JSON.write_text(json.dumps(args, indent=1))

    # Cell 6 discards the returned log weights into `_`; record the particle outputs.
    np.savez(CAPTURE_NPZ,
             approx_post_samples=np.asarray(ns['approx_post_samples'], dtype=np.float64),
             approx_post_samples_ot=np.asarray(ns['approx_post_samples_ot'], dtype=np.float64),
             approx_post_samples_multinomial=np.asarray(ns['approx_post_samples_multinomial'], dtype=np.float64))
    np.savez(EXTRA_NPZ,
             true_post_samples=np.asarray(ns['true_post_samples'], dtype=np.float64),
             ms=np.asarray(ns['ms']), covs=np.asarray(ns['covs']), y=np.asarray(ns['y']),
             post_vs=np.asarray(ns['post_vs']), post_ms=np.asarray(ns['post_ms']),
             post_covs=np.asarray(ns['post_covs']))

    # Figure: cell 7 verbatim
    exec(compile(cells[7], 'gaussian_mixture.ipynb[cell 7]', 'exec'), ns)
    png = render_png(ns['fig'])
    (HERE / 'images_driver').mkdir(exist_ok=True)
    (HERE / 'images_driver/capture_cell7.png').write_bytes(png)

    lw = np.asarray(ns['log_ws'])
    ws = np.exp(lw)
    info = {'timings_s': timings,
            'input_ess': float(1.0 / np.sum(ws ** 2)),
            'sum_ws': float(ws.sum()),
            'weighted_mean_prior_dims01': (ws @ np.asarray(ns['prior_samples']))[:2].tolist(),
            'true_post_mean_dims01': np.asarray(ns['true_post_samples']).mean(axis=0)[:2].tolist(),
            'outputs': summary({k: ns[k] for k in ('approx_post_samples', 'approx_post_samples_ot',
                                                  'approx_post_samples_multinomial')}),
            'files': {p.name: sha256(p) for p in (INPUTS_NPZ, ARGS_JSON, CAPTURE_NPZ, EXTRA_NPZ,
                                                  HERE / 'images_driver/capture_cell7.png')}}
    if PAPERMILL_FIGURE.exists():
        a, b = decode_png(png), decode_png(PAPERMILL_FIGURE.read_bytes())
        info['capture_vs_papermill_figure'] = {'same_shape': a.shape == b.shape,
                                               'png_bytes_equal': png == PAPERMILL_FIGURE.read_bytes(),
                                               'pixels_equal': bool(a.shape == b.shape and np.array_equal(a, b)),
                                               'shape_capture': list(a.shape), 'shape_papermill': list(b.shape)}
    (DATA / 'capture_info.json').write_text(json.dumps(info, indent=1))
    print(json.dumps(info, indent=1))


def replay():
    import matplotlib
    matplotlib.use('Agg')
    import jax
    jax.config.update('jax_enable_x64', True)
    import jax.numpy as jnp
    from diffres.resampling import diffusion_resampling, ensemble_ot, multinomial

    inp = np.load(INPUTS_NPZ)
    args = json.loads(ARGS_JSON.read_text())
    key = jnp.asarray(inp['key'])
    log_ws = jnp.asarray(inp['log_ws'])
    samples = jnp.asarray(inp['prior_samples'])
    da = args['diffusion_resampling']
    ts = jnp.linspace(0., da['T'], da['nsteps'] + 1)
    assert np.array_equal(np.asarray(ts), inp['ts'])

    t = {}
    t0 = time.time()
    lw_d, x_d = diffusion_resampling(key, log_ws, samples, da['a'], ts, integrator=da['integrator'], ode=da['ode'])
    x_d.block_until_ready(); t['diffusion_resampling'] = time.time() - t0
    t0 = time.time()
    lw_o, x_o = ensemble_ot(key, log_ws, samples, eps=args['ensemble_ot']['eps'])
    x_o.block_until_ready(); t['ensemble_ot'] = time.time() - t0
    t0 = time.time()
    lw_m, x_m = multinomial(key, log_ws, samples)
    x_m.block_until_ready(); t['multinomial'] = time.time() - t0

    rep = {'approx_post_samples': np.asarray(x_d), 'approx_post_samples_ot': np.asarray(x_o),
           'approx_post_samples_multinomial': np.asarray(x_m)}
    np.savez(REPLAY_NPZ, **rep, log_ws_diffusion=np.asarray(lw_d), log_ws_ot=np.asarray(lw_o),
             log_ws_multinomial=np.asarray(lw_m))

    cap = np.load(CAPTURE_NPZ)
    cmp = {}
    for k, v in rep.items():
        c = cap[k]
        cmp[k] = {'bitwise_equal': bool(np.array_equal(v, c)), 'max_abs_diff': float(np.max(np.abs(v - c))),
                  'dtype': str(v.dtype), 'shape': list(v.shape)}
    # multinomial: also check that every output row is an exact copy of an input particle
    prior = inp['prior_samples']
    match = (rep['approx_post_samples_multinomial'][:, None, :] == prior[None, :, :]).all(-1)
    cmp['approx_post_samples_multinomial']['all_rows_are_input_particles'] = bool(match.any(1).all())
    cmp['approx_post_samples_multinomial']['n_unique_ancestors'] = int(np.unique(match.argmax(1)).size)
    n = prior.shape[0]
    for name, lw in (('diffusion', lw_d), ('ot', lw_o), ('multinomial', lw_m)):
        cmp[f'log_ws_{name}_uniform'] = bool(np.allclose(np.asarray(lw), -np.log(n), rtol=0, atol=1e-12))

    # Figure: notebook cell 7 verbatim with the replayed arrays
    cells = code_cells()
    ctx = np.load(EXTRA_NPZ)
    ns = {'true_post_samples': jnp.asarray(ctx['true_post_samples']),
          'approx_post_samples': x_d, 'approx_post_samples_ot': x_o, 'approx_post_samples_multinomial': x_m,
          'plt': __import__('matplotlib.pyplot').pyplot}
    exec(compile(cells[7], 'gaussian_mixture.ipynb[cell 7]', 'exec'), ns)
    png = render_png(ns['fig'])
    (HERE / 'images_driver').mkdir(exist_ok=True)
    (HERE / 'images_driver/replay_cell7.png').write_bytes(png)
    fig_cmp = {}
    if PAPERMILL_FIGURE.exists():
        ref = PAPERMILL_FIGURE.read_bytes()
        a, b = decode_png(png), decode_png(ref)
        fig_cmp = {'png_bytes_equal': png == ref, 'same_shape': a.shape == b.shape,
                   'pixels_equal': bool(a.shape == b.shape and np.array_equal(a, b)),
                   'max_abs_pixel_diff': float(np.max(np.abs(a - b))) if a.shape == b.shape else None,
                   'shape_replay': list(a.shape), 'shape_papermill': list(b.shape)}
    result = {'timings_s': t, 'array_comparisons_vs_capture': cmp, 'replay_vs_papermill_figure': fig_cmp,
              'jax_version': jax.__version__, 'devices': [str(dv) for dv in jax.devices()],
              'files': {p.name: sha256(p) for p in (REPLAY_NPZ, HERE / 'images_driver/replay_cell7.png')}}
    (DATA / 'replay_comparison.json').write_text(json.dumps(result, indent=1))
    print(json.dumps(result, indent=1))
    ok = all(v['bitwise_equal'] for k, v in cmp.items() if isinstance(v, dict))
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    {'capture': capture, 'replay': replay}[sys.argv[1]]()
