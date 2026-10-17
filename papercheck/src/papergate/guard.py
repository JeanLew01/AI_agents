"""Read-only guarantee: hash the whole paper directory before and after a run."""

from __future__ import annotations

import hashlib
import os
from pathlib import Path

Entry = tuple[str, str]  # (kind, digest): kind is "f" file, "d" directory, "l" symlink


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def snapshot(root: Path) -> dict[str, Entry]:
    """Every path under root (hidden files and .git included), without following symlinks."""
    root = Path(root)
    snap: dict[str, Entry] = {}
    for dirpath, dirnames, filenames in os.walk(root, followlinks=False):
        d = Path(dirpath)
        for name in dirnames + filenames:
            p = d / name
            rel = p.relative_to(root).as_posix()
            if p.is_symlink():
                snap[rel] = ("l", os.readlink(p))
            elif p.is_dir():
                snap[rel] = ("d", "")
            elif p.is_file():
                snap[rel] = ("f", _sha256(p))
            else:  # sockets, fifos: record existence only
                snap[rel] = ("o", "")
    return snap


def compare(before: dict[str, Entry], after: dict[str, Entry]) -> list[str]:
    changes = []
    for rel in sorted(before.keys() - after.keys()):
        changes.append(f"removed: {rel}")
    for rel in sorted(after.keys() - before.keys()):
        changes.append(f"added: {rel}")
    for rel in sorted(before.keys() & after.keys()):
        if before[rel] != after[rel]:
            changes.append(f"modified: {rel}")
    return changes


def tree_hash(snap: dict[str, Entry]) -> str:
    """Hash of the source tree (contents and layout), excluding .git."""
    h = hashlib.sha256()
    for rel in sorted(snap):
        if rel == ".git" or rel.startswith(".git/"):
            continue
        kind, digest = snap[rel]
        h.update(f"{rel}\x1f{kind}\x1f{digest}\n".encode())
    return h.hexdigest()[:16]


class ReadOnlyGuard:
    """Usage: g = ReadOnlyGuard(dir); g.start(); ...; changes = g.finish()."""

    def __init__(self, root: Path):
        self.root = Path(root)
        self.before: dict[str, Entry] = {}
        self.after: dict[str, Entry] = {}

    def start(self) -> None:
        self.before = snapshot(self.root)

    def finish(self) -> list[str]:
        self.after = snapshot(self.root)
        return compare(self.before, self.after)

    @property
    def files_hashed(self) -> int:
        return sum(1 for k, _ in self.before.values() if k == "f")
