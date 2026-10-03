"""Shared helpers for the resampling tool tests (verifier-owned).

Tools are exercised through fastmcp.Client(resampling_mcp); expected values come from the executors' saved upstream
outputs (notebooks/<id>/...) and from direct calls of diffres.resampling made here, never from wrapper output.
"""
import hashlib
import sys
from pathlib import Path

import jax
import jax.numpy as jnp
import numpy as np
import pytest
from fastmcp import Client
from fastmcp.exceptions import ToolError

ROOT = Path(__file__).resolve().parents[3]
NB = ROOT / "notebooks"
DATA = ROOT / "tests" / "data" / "resampling"
RESULTS = ROOT / "tests" / "results" / "resampling"

sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from resampling_fixtures import build  # noqa: E402
from tools.resampling import resampling_mcp  # noqa: E402

jax.config.update("jax_enable_x64", True)

GM_KEY = [700162660, 1620510799]      # notebooks/gaussian_mixture_demo/data/resampling_arguments.json
GMS_KEY = [1100985983, 1476939598]    # resampling key of MC id 0 in every experiments/gms script


@pytest.fixture(scope="session", autouse=True)
def fixtures_built():
    build()
    RESULTS.mkdir(parents=True, exist_ok=True)
    yield


@pytest.fixture
def out_base(tmp_path):
    return str(tmp_path / "out")


async def call(tool: str, arguments: dict) -> dict:
    async with Client(resampling_mcp) as client:
        result = await client.call_tool(tool, arguments)
    return result.data


async def call_error(tool: str, arguments: dict) -> str:
    async with Client(resampling_mcp) as client:
        with pytest.raises(ToolError) as exc:
            await client.call_tool(tool, arguments)
    return str(exc.value)


def load_out(res: dict):
    path = Path(res["artifacts"][0]["path"])
    assert path.is_absolute() and path.is_file()
    with np.load(path) as d:
        assert sorted(d.files) == ["log_weights", "samples"]
        return d["samples"], d["log_weights"]


def load_in(name: str):
    with np.load(DATA / name) as d:
        lw = d["log_weights"] if "log_weights" in d.files else np.log(d["weights"])
        return d["samples"], lw


def normalise(lw):
    """The upstream callers' own step (experiments/gms/*.py, demos/gaussian_mixture.ipynb cell 4)."""
    lw = jnp.asarray(lw)
    return lw - jax.scipy.special.logsumexp(lw)


def ess(lw_normalised):
    """ESS as diffres.feynman_kac.compute_ess, recomputed here with numpy for an independent check."""
    lw = np.asarray(lw_normalised, dtype=np.float64)
    m = np.max(2 * lw)
    return float(np.exp(-(m + np.log(np.sum(np.exp(2 * lw - m))))))


def key(raw):
    return jnp.array(raw, dtype=jnp.uint32)


def sha(path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()
