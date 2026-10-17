"""Stage 7: figures (captions, text size relative to the body text, colour distinguishability)."""

from __future__ import annotations

import re
import statistics
from itertools import combinations

import numpy as np
import pymupdf

from ..models import Severity
from ..registry import Check, SkipCheck, register
from ..tex.source import latex_to_text, read_group
from .stage2_pdf import _strip_subset

FLOATS = ("figure", "figure*", "table", "table*", "wrapfigure", "wraptable")


@register
class Captions(Check):
    id = "figures.captions"
    stage = 7
    severity = Severity.WARN
    why = "Every figure and table needs a caption that says what it shows."

    def run(self, ctx):
        proj = ctx.project
        out = []
        for e in proj.envs_named(*FLOATS):
            body = proj.flat[e.start:e.end]
            kind = "figure" if "fig" in e.name else "table"
            caps = list(re.finditer(r"\\caption(?:of\{[^}]*\})?\*?\s*(?:\[[^\]]*\])?", body))
            if not caps:
                if re.search(r"\\includegraphics|\\begin\{tabular|\\input", body):
                    out.append(self.at(ctx, e.start, f"{kind} has no caption"))
                continue
            for c in caps:
                g = read_group(body, c.end())
                if g is not None and not latex_to_text(g[0]).strip():
                    out.append(self.at(ctx, e.start + c.start(), f"{kind} caption is empty"))
        return out


def _figure_spans(path) -> tuple[float, list[tuple[str, float]]]:
    """(page width in bp, [(text, native size in bp)]) of the first page of a vector PDF figure."""
    doc = pymupdf.open(str(path))
    page = doc[0]
    width = page.rect.width
    spans = []
    for b in page.get_text("dict").get("blocks", []):
        for ln in b.get("lines", []):
            for sp in ln.get("spans", []):
                t = sp.get("text", "").strip()
                if t:
                    spans.append((t, sp["size"]))
    doc.close()
    return width, spans


UNIT_PT = {"pt": 1.0, "bp": 72.27 / 72, "in": 72.27, "cm": 28.4528, "mm": 2.84528, "pc": 12.0, "em": 10.0, "ex": 4.3}


def parse_length(expr: str, base: float, layout: dict) -> float | None:
    """A TeX width expression in pt; \\linewidth and friends resolve to `base`."""
    e = expr.strip().replace(" ", "")
    m = re.fullmatch(r"([\d.]*)\\(linewidth|columnwidth|textwidth|hsize|paperwidth)", e)
    if m:
        f = float(m.group(1)) if m.group(1) not in ("", ".") else 1.0
        ref = {"textwidth": layout.get("textwidth", base), "paperwidth": layout.get("paperwidth", base)}.get(m.group(2), base)
        return f * ref
    m = re.fullmatch(r"([\d.]+)(pt|bp|in|cm|mm|pc|em|ex)", e)
    if m:
        return float(m.group(1)) * UNIT_PT[m.group(2)]
    return None


def placed_scale(ctx, off: int, native_width_bp: float) -> float | None:
    """Scale at which the \\includegraphics at flat offset `off` places its figure."""
    proj = ctx.project
    lay = (ctx.build.layout if ctx.build else {}) or ctx.config.template.layout or {}
    if not lay.get("columnwidth") and not lay.get("textwidth"):
        return None
    envs = proj.enclosing_envs(off)
    star = any(e.name.endswith("*") and e.name.startswith(("figure", "table")) for e in envs)
    width = lay.get("textwidth") if star else lay.get("columnwidth", lay.get("textwidth"))
    for e in envs:
        if e.name in ("minipage", "subfigure"):
            m = re.match(r"\\begin\{" + re.escape(e.name) + r"\}\s*(?:\[[^\]]*\])*\s*\{([^{}]*)\}", proj.flat[e.start:e.start + 200])
            if m:
                w = parse_length(m.group(1), width, lay)
                if w:
                    width = w
    m = re.match(r"\\includegraphics\s*\[([^\]]*)\]", proj.flat[off:off + 300])
    native_pt = native_width_bp * 72.27 / 72
    if not m:
        return 1.0
    opts = dict(kv.split("=", 1) for kv in (x.strip() for x in m.group(1).split(",")) if "=" in kv)
    opts = {k.strip(): v.strip() for k, v in opts.items()}
    if "scale" in opts:
        try:
            return float(opts["scale"])
        except ValueError:
            return None
    if "width" in opts:
        w = parse_length(opts["width"], width, lay)
        return w / native_pt if w else None
    if any(k in opts for k in ("height", "totalheight")):
        return None
    return 1.0


@register
class FigureTextSize(Check):
    id = "figures.text_size"
    stage = 7
    requires = frozenset({"pdf"})
    severity = Severity.WARN
    why = "Figure text much smaller than the body text is unreadable in print."

    def run(self, ctx):
        body = ctx.pdf.body_font_size
        ratio = float(self.opt(ctx, "min_ratio", 0.6))
        min_pt = float(self.opt(ctx, "min_pt", 5.0))
        out, measured, skipped = [], [], []
        for off, _name, rel in ctx.project.graphics:
            if not rel:
                continue
            if not rel.lower().endswith(".pdf"):
                skipped.append(f"{rel} (raster)")
                continue
            try:
                width, spans = _figure_spans(ctx.paper_dir / rel)
            except Exception:
                continue
            sizes = [sz for t, sz in spans if len(t) >= 1]
            if not sizes:
                continue  # no extractable text (outlined fonts or no text)
            scale = placed_scale(ctx, off, width)
            if scale is None:
                skipped.append(f"{rel} (placement size not parsed)")
                continue
            eff = [sz * scale for sz in sizes]
            med = statistics.median(eff)
            measured.append({"figure": rel, "scale": round(scale, 2), "median_pt": round(med, 1), "min_pt": round(min(eff), 1)})
            limit = max(min_pt, ratio * body)
            if med < limit:
                out.append(self.at(ctx, off, f"text in {rel} is about {med:.1f}pt in the PDF (smallest {min(eff):.1f}pt); "
                                             f"body text is {body:.1f}pt (minimum {limit:.1f}pt)",
                                   instructions="Enlarge the fonts in the plotting script or include the figure "
                                                "at a larger width (papergate does not regenerate figures)."))
        ctx.metrics["figure_text"] = {"body_pt": body, "measured": measured, "not_measured": skipped}
        return out


def _srgb_to_lin(c):
    return np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)


def _lin_to_lab(lin):
    m = np.array([[0.4124, 0.3576, 0.1805], [0.2126, 0.7152, 0.0722], [0.0193, 0.1192, 0.9505]])
    xyz = lin @ m.T / np.array([0.95047, 1.0, 1.08883])
    f = np.where(xyz > 0.008856, np.cbrt(xyz), 7.787 * xyz + 16 / 116)
    return np.stack([116 * f[..., 1] - 16, 500 * (f[..., 0] - f[..., 1]), 200 * (f[..., 1] - f[..., 2])], -1)


CVD = {  # Machado, Oliveira & Fernandes (2009), severity 1.0, linear RGB
    "protanopia": np.array([[0.152286, 1.052583, -0.204868], [0.114503, 0.786281, 0.099216], [-0.003882, -0.048116, 1.051998]]),
    "deuteranopia": np.array([[0.367322, 0.860646, -0.227968], [0.280085, 0.672501, 0.047413], [-0.011820, 0.042940, 0.968881]]),
}


def palette(rgb: np.ndarray, min_frac: float = 0.03) -> list[np.ndarray]:
    """Dominant saturated colours (sRGB in [0,1]) of an image."""
    px = rgb.reshape(-1, 3).astype(float) / 255.0
    mx, mn = px.max(1), px.min(1)
    colored = px[((mx - mn) / (mx + 1e-6) > 0.35) & (mx > 0.2)]
    if len(colored) < 200:
        return []
    q = np.clip((colored * 16).astype(int), 0, 15)
    keys = q[:, 0] * 256 + q[:, 1] * 16 + q[:, 2]
    counts = np.bincount(keys, minlength=4096)
    out: list[np.ndarray] = []
    for k in np.argsort(counts)[::-1][:40]:
        if counts[k] < min_frac * len(colored):
            break
        mean = colored[keys == k].mean(0)
        lab = _lin_to_lab(_srgb_to_lin(mean))
        if all(np.linalg.norm(lab - _lin_to_lab(_srgb_to_lin(c))) > 12 for c in out):
            out.append(mean)
    return out


def collapses(colors: list[np.ndarray], d_normal: float = 20.0, d_cvd: float = 10.0, d_gray: float = 8.0):
    """Pairs distinct in normal vision but not under CVD / in grayscale."""
    res = {"protanopia": [], "deuteranopia": [], "grayscale": []}
    for a, b in combinations(colors, 2):
        la, lb = _srgb_to_lin(a), _srgb_to_lin(b)
        if np.linalg.norm(_lin_to_lab(la) - _lin_to_lab(lb)) < d_normal:
            continue
        for name, m in CVD.items():
            if np.linalg.norm(_lin_to_lab(np.clip(m @ la, 0, 1)) - _lin_to_lab(np.clip(m @ lb, 0, 1))) < d_cvd:
                res[name].append((a, b))
        ya, yb = la @ [0.2126, 0.7152, 0.0722], lb @ [0.2126, 0.7152, 0.0722]
        if abs(_lin_to_lab(np.array([ya, ya, ya]))[0] - _lin_to_lab(np.array([yb, yb, yb]))[0]) < d_gray:
            res["grayscale"].append((a, b))
    return res


def _hex(c: np.ndarray) -> str:
    return "#" + "".join(f"{int(round(x * 255)):02x}" for x in c)


def _load_rgb(path) -> np.ndarray | None:
    p = str(path)
    if p.lower().endswith(".pdf"):
        doc = pymupdf.open(p)
        pix = doc[0].get_pixmap(dpi=100, colorspace=pymupdf.csRGB, alpha=False)
        arr = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, 3).copy()
        doc.close()
        return arr
    try:
        from PIL import Image

        with Image.open(p) as im:
            im.thumbnail((1200, 1200))
            return np.asarray(im.convert("RGB"))
    except Exception:
        return None


@register
class FigureColors(Check):
    id = "figures.colors"
    stage = 7
    severity = Severity.WARN
    why = "About 8% of men have red-green colour vision deficiency, and many readers print in grayscale."

    def run(self, ctx):
        out = []
        seen = set()
        n = 0
        for off, _name, rel in ctx.project.graphics:
            if not rel or rel in seen or not re.search(r"\.(pdf|png|jpe?g)$", rel, re.I):
                continue
            seen.add(rel)
            img = _load_rgb(ctx.paper_dir / rel)
            if img is None:
                continue
            n += 1
            cols = palette(img)
            if len(cols) < 2:
                continue
            res = collapses(cols)
            for kind in ("deuteranopia", "protanopia"):
                if res[kind]:
                    pairs = ", ".join(f"{_hex(a)}/{_hex(b)}" for a, b in res[kind][:3])
                    out.append(self.at(ctx, off, f"{rel}: colours {pairs} are hard to tell apart with {kind}",
                                       instructions="Use a colour-blind-safe palette (e.g. Okabe-Ito, viridis) "
                                                    "and/or vary markers and line styles."))
                    break
            if res["grayscale"]:
                pairs = ", ".join(f"{_hex(a)}/{_hex(b)}" for a, b in res["grayscale"][:3])
                out.append(self.at(ctx, off, f"{rel}: colours {pairs} have nearly the same lightness in grayscale",
                                   severity=Severity.INFO,
                                   instructions="Vary lightness, markers or line styles so the figure survives b/w print."))
        if n == 0:
            raise SkipCheck("no PDF/PNG/JPEG figures")
        return out
