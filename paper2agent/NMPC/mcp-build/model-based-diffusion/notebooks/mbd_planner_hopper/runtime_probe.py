# Records interpreter, package versions and the JAX default device. No simulation is run.
import sys, json, platform, importlib.metadata as md
import jax, jax.numpy as jnp
import mbd
info = {
    "python": sys.version, "executable": sys.executable, "platform": platform.platform(),
    "mbd_file": mbd.__file__, "mbd_version": mbd.__version__,
    "packages": {},
    "jax_devices": [str(d) for d in jax.devices()],
    "jax_default_backend": jax.default_backend(),
    "array_device": str(jnp.zeros(1).devices()),
    "jax_enable_x64": bool(jax.config.jax_enable_x64),
    "default_float_dtype": str(jnp.zeros(1).dtype),
}
for p in ["jax", "jaxlib", "jax-cuda12-plugin", "jax-cuda12-pjrt", "brax", "mujoco", "mujoco-mjx", "numpy", "scipy",
          "tyro", "tqdm", "matplotlib", "etils", "flax", "nvidia-cudnn-cu12", "nvidia-cuda-runtime-cu12"]:
    try: info["packages"][p] = md.version(p)
    except Exception as e: info["packages"][p] = None
print(json.dumps(info, indent=1))
