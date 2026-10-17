"""Regenerate the figure files used by the test fixtures (committed; only needed if they change).
Usage: python tests/fixtures/_tools/make_figures.py"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

OUT = Path(__file__).resolve().parents[1] / "_common"


def plot(path: Path, fonttype: int, colors=("tab:blue", "tab:orange"), fontsize=9.0, width=3.5):
    plt.rcParams.update({"pdf.fonttype": fonttype, "ps.fonttype": fonttype, "font.size": fontsize})
    fig, ax = plt.subplots(figsize=(width, 2.2))
    noise = [0.0, 0.1, 0.2, 0.3]
    ax.plot(noise, [0.92, 0.89, 0.87, 0.857], marker="o", color=colors[0], label="GDP (ours)")
    ax.plot(noise, [0.80, 0.76, 0.73, 0.712], marker="s", color=colors[1], label="Baseline")
    ax.set_xlabel("noise level")
    ax.set_ylabel("success rate")
    ax.legend()
    fig.tight_layout()
    fig.savefig(path, metadata={"Creator": "papergate fixtures", "Author": None, "Title": None})
    plt.close(fig)


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    plot(OUT / "plot.pdf", 42)
    plot(OUT / "plot_type3.pdf", 3)
    plot(OUT / "plot_redgreen.png", 42, colors=("#d62728", "#2ca02c"))
    plot(OUT / "plot_tiny.pdf", 42, fontsize=5.0, width=6.0)
    print("written to", OUT)
