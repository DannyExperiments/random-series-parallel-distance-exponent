#!/usr/bin/env python3
"""Regenerate the root per-file SHA-256 ledger."""

from __future__ import annotations

import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "SHA256SUMS.txt"


def digest(path: Path) -> str:
    result = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            result.update(block)
    return result.hexdigest()


def main() -> None:
    symlinks = [path for path in ROOT.rglob("*") if path.is_symlink()]
    if symlinks:
        names = ", ".join(
            sorted(path.relative_to(ROOT).as_posix() for path in symlinks)
        )
        raise SystemExit(f"refusing to hash symlinks: {names}")

    files: list[Path] = []
    for path in ROOT.rglob("*"):
        relative = path.relative_to(ROOT)
        if not path.is_file() or ".git" in relative.parts or path == OUTPUT:
            continue
        if "__pycache__" in relative.parts or path.suffix in {".pyc", ".pyo"}:
            raise SystemExit(
                f"refusing to hash generated Python cache: {relative.as_posix()}"
            )
        files.append(path)

    OUTPUT.write_text(
        "".join(
            f"{digest(path)}  {path.relative_to(ROOT).as_posix()}\n"
            for path in sorted(files)
        ),
        encoding="utf-8",
    )
    print(f"HASHED {len(files)} FILES")


if __name__ == "__main__":
    main()
