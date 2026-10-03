# Runtime identity probe (no simulation): where `mbd` resolves, package versions, device.
import sys, platform, importlib.metadata as md
import mbd, jax, numpy
print("python", sys.version.replace("\n", " "))
print("executable", sys.executable)
print("platform", platform.platform())
print("mbd.__file__", mbd.__file__)
print("mbd.planners.mbd_planner.__file__", mbd.planners.mbd_planner.__file__)
print("mbd.envs.car2d.__file__", sys.modules["mbd.envs.car2d"].__file__)
for p in ["jax", "jaxlib", "jax-cuda12-plugin", "jax-cuda12-pjrt", "brax", "mujoco", "mujoco-mjx", "numpy", "scipy", "flax", "tyro", "tqdm", "matplotlib", "mbd"]:
    try:
        print("version", p, md.version(p))
    except Exception as e:
        print("version", p, "NOT FOUND", repr(e))
print("jax.devices", jax.devices())
print("default_backend", jax.default_backend())
print("x64", jax.config.jax_enable_x64)
import jax.numpy as jnp
print("array device", jnp.zeros(1).devices())
