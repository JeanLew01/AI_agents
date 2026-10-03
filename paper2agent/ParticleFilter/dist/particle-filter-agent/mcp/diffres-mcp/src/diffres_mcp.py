"""MCP server for diffres (Andersson & Zhao, "Diffusion differentiable resampling", ICML 2026).

Mounts the independently verified tool modules; tool names already carry the `diffres_` prefix, so the
modules are mounted without a namespace. Upstream: https://github.com/zgbkdlm/diffres @ 767effe.
"""
import os
import sys
from pathlib import Path

# The upstream code is evaluated on CPU in float64 (the modules enable x64 on import). Keep JAX off the GPU
# unless the user explicitly chose a platform, and do not let XLA preallocate device memory.
os.environ.setdefault("JAX_PLATFORMS", "cpu")
os.environ.setdefault("XLA_PYTHON_CLIENT_PREALLOCATE", "false")

sys.path.insert(0, str(Path(__file__).resolve().parent))

from fastmcp import FastMCP  # noqa: E402

from tools.feynman_kac import feynman_kac_mcp  # noqa: E402
from tools.gaussian_filters import gaussian_filters_mcp  # noqa: E402
from tools.resampling import resampling_mcp  # noqa: E402

mcp = FastMCP(name="diffres")
mcp.mount(resampling_mcp)
mcp.mount(feynman_kac_mcp)
mcp.mount(gaussian_filters_mcp)

if __name__ == "__main__":
    mcp.run(show_banner=False)
