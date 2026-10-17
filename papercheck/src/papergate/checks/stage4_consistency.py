"""Stage 4: internal consistency (references, acronyms, numbers, notation, restatements)."""

from __future__ import annotations

import difflib
import re
from itertools import combinations

from ..models import Severity
from ..registry import Check, SkipCheck, register
from ..tex.source import find_commands, latex_to_text, prose_mask
from ..tex.tables import table_cells


@register
class UnreferencedFloats(Check):
    id = "consistency.unreferenced_floats"
    stage = 4
    severity = Severity.WARN
    why = "Every figure and table should be referenced (and discussed) in the text."

    def run(self, ctx):
        proj = ctx.project
        refd = proj.referenced_keys
        out = []
        for e in proj.envs_named("figure", "figure*", "table", "table*", "wrapfigure", "wraptable"):
            kind = "figure" if "fig" in e.name else "table"
            labels = [l for l in proj.labels if e.start <= l.start < e.end and l.kind in ("figure", "table")]
            has_caption = re.search(r"\\caption\b", proj.flat[e.start:e.end])
            if not labels:
                if has_caption:
                    out.append(self.at(ctx, e.start, f"{kind} has no \\label, so it cannot be referenced"))
                continue
            if not any(l.key in refd for l in labels):
                l0 = labels[0]
                out.append(self.at(ctx, l0.start, f"{kind} '{l0.key}' is never referenced in the text",
                                   instructions=f"Reference it (e.g. {kind.capitalize()}~\\ref{{{l0.key}}}) where it is discussed."))
        return out


@register
class UnreferencedLabels(Check):
    id = "consistency.unreferenced_labels"
    stage = 4
    severity = Severity.INFO
    why = "Unused labels are harmless but often point to orphaned content."

    def run(self, ctx):
        proj = ctx.project
        refd = proj.referenced_keys
        skip = {"figure", "table"} | (set() if self.opt(ctx, "include_sections", False) else {"section"})
        return [self.at(ctx, l.start, f"label '{l.key}' ({l.kind}) is never referenced")
                for l in proj.labels if l.kind not in skip and l.key not in refd]


ACRONYM_WHITELIST = {
    "GPU", "GPUs", "CPU", "CPUs", "RAM", "RGB", "RGBD", "RGB-D", "LiDAR", "LIDAR", "IMU", "GPS", "URL", "PDF", "API",
    "ID", "IDs", "USA", "UK", "EU", "IEEE", "ACM", "AI", "II", "III", "IV", "VI", "VII", "VIII", "IX", "XI", "XII",
    "OK", "PhD", "MSc", "BSc", "TV", "PC", "CoRL", "ICRA", "IROS", "RSS", "NeurIPS", "ICML", "ICLR", "CVPR", "CDC",
    "ACC", "AAAI", "IJCAI", "ROS", "ROS2", "CUDA", "JAX", "SI", "MuJoCo", "PyTorch", "OpenAI", "DOF", "DoF", "FPS",
    "HTTP", "HTML", "JSON", "CSV", "ASCII", "UTC", "AM", "PM", "MIT", "CMU", "ETH", "NASA", "DARPA", "NSF", "ONR",
}
ACR_TOKEN = re.compile(r"(?<![\w-])([A-Z][A-Za-z0-9]*[A-Z][A-Za-z0-9]*(?:-[A-Z0-9]+)?)(s?)(?![\w-])")
ACR_DEF = re.compile(r"\(\s*([A-Z][A-Za-z0-9-]*[A-Z][A-Za-z0-9-]*?)(s?)\s*\)")


def _initials_match(acr: str, words: list[str]) -> bool:
    letters = [c for c in acr if c.isalpha() and c.isupper()] or [c for c in acr if c.isalpha()]
    target = "".join(letters).lower()
    for k in range(1, min(10, len(words)) + 1):
        tail = words[-k:]
        plain = "".join(w[0] for w in tail if w).lower()
        split = "".join(p[0] for w in tail for p in re.split(r"-", w) if p).lower()
        if target in (plain, split):
            return True
        # subsequence of word-initial letters (e.g. "model predictive control" -> MPC with joiners)
        initials = [p[0].lower() for w in tail for p in re.split(r"-", w) if p]
        if initials and initials[0] == target[0]:
            it = iter(initials)
            if all(ch in it for ch in target) and len(tail) <= len(target) + 2:
                return True
    return False


@register
class Acronyms(Check):
    id = "text.acronyms"
    stage = 4
    severity = Severity.WARN
    why = "Acronyms should be defined once, at first use."

    def run(self, ctx):
        proj = ctx.project
        if re.search(r"\\usepackage\s*(?:\[[^\]]*\])?\s*\{[^}]*\b(acro|glossaries|glossaries-extra|acronym)\b", proj.preamble):
            raise SkipCheck("acronyms are managed by an acronym package")
        flat = proj.flat
        masked = prose_mask(flat[: proj.body_end])
        abstract = proj.abstract_range or (0, 0)
        app = proj.appendix_start or proj.body_end
        white = ACRONYM_WHITELIST | set(self.opt(ctx, "whitelist", []))
        defs: dict[str, list[int]] = {}
        for m in ACR_DEF.finditer(masked, proj.body_start):
            acr = m.group(1)
            before = masked[max(0, m.start() - 150):m.start()]
            before = re.split(r"[.;:!?]\s", before)[-1]
            words = re.findall(r"[A-Za-z][A-Za-z-]*", before)
            if _initials_match(acr, words):
                defs.setdefault(acr, []).append(m.start())
        out = []
        for acr, offs in defs.items():
            if acr in white:
                continue
            body_defs = [o for o in offs if not (abstract[0] <= o < abstract[1]) and o < app]
            if len(body_defs) > 1:
                for o in body_defs[1:]:
                    out.append(self.at(ctx, o, f"acronym {acr} is defined again (first defined at "
                                               f"{proj.locate(body_defs[0]).file}:{proj.locate(body_defs[0]).line})"))
            first_def = body_defs[0] if body_defs else None
            if first_def is None:
                continue
            for m in re.finditer(r"(?<![\w-])" + re.escape(acr) + r"s?(?![\w-])", masked):
                o = m.start()
                if o < proj.body_start or abstract[0] <= o < abstract[1]:
                    continue
                if o < first_def and not (first_def - 3 <= o <= first_def + len(acr) + 3):
                    out.append(self.at(ctx, o, f"acronym {acr} is used before its definition at "
                                               f"{proj.locate(first_def).file}:{proj.locate(first_def).line}",
                                       instructions="Spell it out at first use: 'long form (ACR)'."))
                break
        # used but never defined
        counts: dict[str, list[int]] = {}
        for m in ACR_TOKEN.finditer(masked, proj.body_start):
            if abstract[0] <= m.start() < abstract[1]:
                continue
            counts.setdefault(m.group(1), []).append(m.start())
        for acr, offs in counts.items():
            if acr in defs or acr in white or len(offs) < 2 or not re.search(r"[A-Z].*[A-Z]", acr):
                continue
            if sum(c.isupper() for c in acr) < 2 or len(acr) > 8:
                continue
            out.append(self.at(ctx, offs[0], f"acronym {acr} is used {len(offs)} times but never defined",
                               severity=Severity.INFO))
        return out


NUM_RX = re.compile(r"(?<![\w.])(\d{1,3}(?:,\d{3})+|\d+)(?:\.(\d+))?(\s*(?:\\%|%|\$?\\times\$?|×|x\b|-fold\b|times\b))?")


def _region_ranges(proj) -> list[tuple[str, int, int]]:
    out = []
    if proj.abstract_range:
        out.append(("abstract", *proj.abstract_range))
    secs = [s for s in proj.sections if s.level <= 1 and not proj.in_appendix(s.start)]
    if secs:
        intro = next((s for s in secs if re.search(r"intro", s.title, re.I)), secs[0])
        out.append(("introduction", *proj.section_range(intro)))
        concl = next((s for s in reversed(secs) if re.search(r"conclu|summary|discussion", s.title, re.I)), None)
        if concl:
            out.append(("conclusion", *proj.section_range(concl)))
    return out


def _blank_refs(s: str) -> str:
    return re.sub(r"\\(?:label|ref|cref|Cref|eqref|autoref|cite[a-zA-Z]*|url|includegraphics|vspace|hspace)\*?(?:\[[^\]]*\])?\{[^{}]*\}",
                  lambda m: " " * len(m.group(0)), s)


def _rounds_to(value: float, claim: float, decimals: int) -> bool:
    return abs(round(value, decimals) - claim) < 0.5 * 10 ** (-decimals) + 1e-9


@register
class Numbers(Check):
    id = "consistency.numbers"
    stage = 4
    severity = Severity.WARN
    why = "Numbers in the abstract/introduction/conclusion must agree with the results tables."

    def run(self, ctx):
        proj = ctx.project
        cells = table_cells(proj)
        if not cells:
            raise SkipCheck("no numeric table cells")
        flat = proj.flat
        body_text = _blank_refs(flat[proj.body_start:proj.body_end])
        out = []
        regions = _region_ranges(proj)
        claimed_ranges = [(a, b) for _n, a, b in regions]
        for region, a, b in regions:
            seg = _blank_refs(flat[a:b])
            for m in NUM_RX.finditer(seg):
                intpart, dec, suffix = m.group(1), m.group(2), (m.group(3) or "").strip()
                pct = "%" in suffix
                mult = bool(suffix) and not pct
                if not (dec or pct or mult):
                    continue
                raw = intpart.replace(",", "") + ("." + dec if dec else "")
                v = float(raw)
                d = len(dec) if dec else 0
                if not dec and not pct and not mult:
                    continue
                if 1900 <= v <= 2100 and not dec:
                    continue
                off = a + m.start()
                status, near = self._match(v, d, pct, mult, cells)
                if status == "ok":
                    continue
                # stated elsewhere in the body (e.g. results text)?
                elsewhere = [x for x in re.finditer(r"(?<![\w.])" + re.escape(raw) + r"(?![\d])", body_text)
                             if not any(ca <= proj.body_start + x.start() < cb for ca, cb in claimed_ranges)]
                if near:
                    c = near
                    cl = proj.locate(c.offset)
                    tab = f"Table '{c.table_label}'" if c.table_label else f"table #{c.table_index + 1}"
                    out.append(self.at(ctx, off, f"{region} states {m.group(0).strip()} but {tab} "
                                                 f"({cl.file}:{cl.line}, row '{c.row_header}', column '{c.col_header}') has {c.raw}",
                                       instructions="Decide which number is correct and make both agree "
                                                    "(papergate does not choose)."))
                elif not elsewhere:
                    out.append(self.at(ctx, off, f"{region} states {m.group(0).strip()}, which is not found in any "
                                                 f"table or elsewhere in the text", severity=Severity.INFO))
        return out

    @staticmethod
    def _match(v, d, pct, mult, cells):
        vals = []
        for c in cells:
            vals.append((c.value, c))
            if pct and 0 < abs(c.value) <= 1 and c.decimals >= 2:
                vals.append((c.value * 100, c))
        for x, _c in vals:
            if _rounds_to(x, v, d):
                return "ok", None
        groups: dict = {}
        for c in cells:
            groups.setdefault(("r", c.table_index, c.row), []).append(c)
            groups.setdefault(("c", c.table_index, c.col), []).append(c)
        for grp in groups.values():
            for c1, c2 in combinations(grp, 2):
                a, b = c1.value, c2.value
                cands = []
                if mult:
                    cands += [a / b if b else None, b / a if a else None]
                else:
                    cands += [abs(a - b)]
                    for num, den in ((a - b, b), (b - a, a), (a - b, a), (b - a, b)):
                        if den:
                            cands.append(abs(num) / abs(den) * 100)
                if any(x is not None and _rounds_to(x, v, d) for x in cands):
                    return "ok", None
        best = None
        for x, c in vals:
            rel = abs(x - v) / max(abs(v), 1e-9)
            same_digits = sorted(c.raw.replace(".", "")) == sorted(f"{v:.{d}f}".replace(".", "")) and c.decimals == d
            if rel <= 0.05 or same_digits:
                if best is None or rel < best[0]:
                    best = (rel, c)
        return "miss", best[1] if best else None


DEF_PATTERNS = [
    r"\blet\s+\$([^$]+)\$\s*(?:,\s*)?(?:be|denote|represent)",
    r"\$([^$]+)\$\s+(?:denotes|represents|is defined as|stands for)",
    r"\bwhere\s+\$([^$]+)\$\s+(?:is|are|denotes)",
    r"\bdenote\s+(?:\w+\s+){0,6}?by\s+\$([^$]+)\$",
    r"\bdefine\s+\$([^$]+)\$",
]


DECORATORS = r"mathcal|mathbb|mathbf|mathrm|mathsf|mathfrak|mathscr|bm|boldsymbol|hat|widehat|tilde|widetilde|bar|overline|underline|vec|dot|ddot|check|breve"


def _symbol_key(math: str) -> str | None:
    s = math.strip()
    m = re.match(r"\\(?:" + DECORATORS + r")\s*(?:\{\s*(\\?[A-Za-z]+)\s*\}|(\\[A-Za-z]+|[A-Za-z]))", s)
    if m:
        name = re.match(r"\\[A-Za-z]+", s).group(0)
        return f"{name}{{{m.group(1) or m.group(2)}}}"
    m = re.match(r"\\([A-Za-z]+)", s)
    if m and m.group(1) not in ("left", "big", "Big", "bigl", "Bigl", "operatorname", "text", "mathrm", "textrm",
                                "displaystyle", "quad", "qquad", "forall", "exists", "lim", "max", "min", "sup", "inf"):
        return "\\" + m.group(1)
    m = re.match(r"([A-Za-z])(?![A-Za-z])", s)
    return m.group(1) if m else None


def _symbol_rx(key: str) -> re.Pattern:
    m = re.fullmatch(r"(\\[A-Za-z]+)\{(\\?[A-Za-z]+)\}", key)
    if m:  # \mathcal{X} also written \mathcal X
        return re.compile(re.escape(m.group(1)) + r"\s*(?:\{\s*" + re.escape(m.group(2)) + r"\s*\}|" + re.escape(m.group(2))
                          + r"(?![A-Za-z]))")
    return re.compile(r"(?<![A-Za-z\\])" + re.escape(key) + r"(?![A-Za-z])")


@register
class Notation(Check):
    id = "math.notation"
    stage = 4
    severity = Severity.WARN
    why = "Symbols must be defined before use and keep one meaning throughout."

    def run(self, ctx):
        proj = ctx.project
        flat = proj.flat
        out = []
        # duplicate macro definitions
        defs: dict[str, list[int]] = {}
        for m in re.finditer(r"\\(?:newcommand|renewcommand|providecommand|DeclareMathOperator)\*?\s*\{?\s*(\\[A-Za-z@]+)|\\def\s*(\\[A-Za-z@]+)", flat):
            defs.setdefault(m.group(1) or m.group(2), []).append(m.start())
        for name, offs in defs.items():
            if len(offs) > 1:
                for o in offs[1:]:
                    out.append(self.at(ctx, o, f"macro {name} is defined more than once"))
        # symbol definitions in prose
        symdefs: dict[str, list[tuple[int, str]]] = {}
        body = flat[: proj.body_end]
        for pat in DEF_PATTERNS:
            for m in re.finditer(pat, body, re.I):
                if m.start() < proj.body_start or proj.in_appendix(m.start()):
                    continue
                key = _symbol_key(m.group(1))
                if key:
                    sent_end = body.find(".", m.end())
                    symdefs.setdefault(key, []).append((m.start(), latex_to_text(body[m.start():sent_end if sent_end > 0 else m.end() + 80])))
        table = []
        intro = next((s for s in proj.sections if s.level <= 1), None)
        intro_end = proj.section_range(intro)[1] if intro and re.search(r"intro", intro.title, re.I) else proj.body_start
        math_rx = re.compile(r"\$([^$]+)\$|\\\[(.+?)\\\]|\\begin\{(equation|align|gather|multline)\*?\}(.+?)\\end\{\3\*?\}", re.S)
        for key, items in symdefs.items():
            items.sort()
            first_off, first_desc = items[0]
            loc = proj.locate(first_off)
            table.append({"symbol": key, "defined_at": f"{loc.file}:{loc.line}", "definition": first_desc[:120]})
            descs = {re.sub(r"\W+", " ", d.lower()).strip() for _o, d in items}
            single = len(key) == 1
            if len(items) > 1 and len(descs) > 1:
                o2 = items[1][0]
                out.append(self.at(ctx, o2, f"symbol {key} appears to be defined again (first at {loc.file}:{loc.line})",
                                   severity=Severity.INFO))
            sym_rx = _symbol_rx(key)
            para_start = max(flat.rfind("\n\n", 0, first_off), flat.rfind("\\par", 0, first_off))
            for mm in math_rx.finditer(flat, intro_end, max(intro_end, para_start)):
                content = next(g for g in mm.groups() if g and not g.startswith(("equation", "align", "gather", "multline")))
                if sym_rx.search(content):
                    sec = proj.section_at(mm.start())
                    out.append(self.at(ctx, mm.start(), f"symbol {key} is used before its definition at {loc.file}:{loc.line}"
                                       + (f" (used in '{sec.title}')" if sec else ""),
                                       severity=Severity.INFO if single else Severity.WARN))
                    break
        ctx.metrics["notation"] = table
        return out


def _norm_stmt(s: str) -> str:
    s = re.sub(r"\\label\{[^{}]*\}", "", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s.rstrip(".")


@register
class Restatements(Check):
    id = "math.restatements"
    stage = 4
    severity = Severity.WARN
    why = "A restated theorem must say exactly what the main-text statement says."

    def run(self, ctx):
        proj = ctx.project
        if proj.appendix_start is None:
            return []
        thm_names = {n for n in proj.theorem_envs if n not in ("definition", "remark", "example", "assumption")}
        envs = [e for e in proj.envs if e.name in thm_names or e.name.rstrip("*") in thm_names]
        main = [e for e in envs if not proj.in_appendix(e.start)]
        app = [e for e in envs if proj.in_appendix(e.start)]
        out = []
        for e in app:
            body = proj.flat[e.body_start:e.body_end]
            target = None
            refs = re.findall(r"\\(?:ref|cref|Cref|autoref)\{([^{}]+)\}", e.opt or "")
            for key in refs:
                lab = next((l for l in proj.labels if l.key == key and l.env is not None), None)
                if lab and not proj.in_appendix(lab.start):
                    target = lab.env
            if target is None:
                best = max(main, key=lambda m: difflib.SequenceMatcher(None, _norm_stmt(proj.flat[m.body_start:m.body_end]),
                                                                       _norm_stmt(body)).ratio(), default=None)
                if best and difflib.SequenceMatcher(None, _norm_stmt(proj.flat[best.body_start:best.body_end]),
                                                    _norm_stmt(body)).ratio() >= 0.75 and best.name.rstrip("*") == e.name.rstrip("*"):
                    target = best
            if target is None:
                continue
            a = _norm_stmt(proj.flat[target.body_start:target.body_end])
            b = _norm_stmt(body)
            if a == b:
                continue
            aw, bw = a.split(" "), b.split(" ")
            sm = difflib.SequenceMatcher(None, aw, bw)
            diffs = [f"'{' '.join(aw[i1:i2])}' -> '{' '.join(bw[j1:j2])}'" for op, i1, i2, j1, j2 in sm.get_opcodes() if op != "equal"]
            tl = proj.locate(target.start)
            out.append(self.at(ctx, e.start, f"restated {e.name} differs from the statement at {tl.file}:{tl.line}: "
                                             + "; ".join(diffs[:4]),
                               instructions="Make the restatement identical (or use thmtools' restatable)."))
        return out
