"""Supplementary diagnostic for execution_id run_mbd_temp_car2d (NOT the reference run).

Question: is the value -1.1920929e-07 printed eight times by the temperature sweep simply the lowest reward
the car2d environment can return (car never within 0.2 of the goal)?

Only upstream functions are called (mbd.envs.get_env, env.reset, env.step, env.get_reward, mbd.utils.rollout_us),
evaluated exactly the way mbd_planner.run_diffusion evaluates its final reward (mbd_planner.py:74-80, 179-180):
    rewss_final, _ = rollout_us(state_init, Y); rew_final = rewss_final.mean()
Here Y is (a) all zeros, i.e. a car that never moves, and (b) a few constant action sequences.
Nothing of the planner is re-implemented.
"""
import functools
import json
import sys

import jax
from jax import numpy as jnp
import numpy as np

import mbd

env = mbd.envs.get_env("car2d")
step_env_jit = jax.jit(env.step)
reset_env_jit = jax.jit(env.reset)
rollout_us = jax.jit(functools.partial(mbd.utils.rollout_us, step_env_jit))

rng = jax.random.PRNGKey(seed=0)
rng, rng_reset = jax.random.split(rng)
state_init = reset_env_jit(rng_reset)

out = {
    "mbd_file": mbd.__file__,
    "device": str(jax.devices()[0]),
    "x64": bool(jax.config.jax_enable_x64),
    "x0": np.asarray(env.x0).tolist(),
    "xg": np.asarray(env.xg).tolist(),
    "distance_x0_to_goal": float(jnp.linalg.norm(env.x0[:2] - env.xg[:2])),
    "get_reward_at_x0": repr(np.asarray(env.get_reward(env.x0))[()]),
    "get_reward_at_goal": repr(np.asarray(env.get_reward(env.xg))[()]),
    "get_reward_far_away": repr(np.asarray(env.get_reward(jnp.array([5.0, 5.0, 0.0])))[()]),
    "float32_eps": repr(np.finfo(np.float32).eps),
    "rollouts": {},
}

Hsample, Nu = 50, env.action_size
cases = {
    "zeros (car does not move)": jnp.zeros([Hsample, Nu]),
    "constant [0, 1]": jnp.tile(jnp.array([0.0, 1.0]), (Hsample, 1)),
    "constant [0, -1]": jnp.tile(jnp.array([0.0, -1.0]), (Hsample, 1)),
    "constant [1, 1]": jnp.tile(jnp.array([1.0, 1.0]), (Hsample, 1)),
}
for name, Y in cases.items():
    rewss, qs = rollout_us(state_init, Y)
    rewss = np.asarray(rewss)
    qs = np.asarray(qs)
    dist = np.linalg.norm(qs[:, :2] - np.asarray(env.xg)[:2], axis=1)
    out["rollouts"][name] = {
        "mean_reward_repr": repr(rewss.mean(dtype=np.float32)),
        "mean_reward_jax_repr": repr(np.asarray(jnp.asarray(rewss).mean())[()]),
        "unique_step_rewards": [repr(v) for v in np.unique(rewss)],
        "min_distance_to_goal": float(dist.min()),
        "final_xy": qs[-1, :2].tolist(),
    }

json.dump(out, sys.stdout, indent=1)
print()
