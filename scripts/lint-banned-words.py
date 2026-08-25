#!/usr/bin/env python3
"""Lint copy and CMS-ish files for Tamia4Life banned presentation terms.

See CLAUDE.md §5 and compliance/banned-words.json.
The constitution and this tooling are allowlisted — they must name the terms.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LIST = ROOT / "compliance" / "banned-words.json"

SCAN_SUFFIXES = {
    ".md",
    ".html",
    ".htm",
    ".json",
    ".txt",
    ".csv",
    ".yml",
    ".yaml",
    ".js",
    ".jsx",
    ".ts",
    ".tsx",
    ".vue",
    ".svg",
    ".xml",
    ".po",
    ".xliff",
}

SKIP_DIR_NAMES = {".git", "node_modules", ".venv", "venv", "dist", "build", ".next"}


def load_config(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def is_allowlisted(rel: str, prefixes: list[str]) -> bool:
    rel_posix = rel.replace("\\", "/")
    for prefix in prefixes:
        if rel_posix == prefix or rel_posix.startswith(prefix):
            return True
    return False


def compile_rules(config: dict) -> list[tuple[str, re.Pattern[str]]]:
    rules: list[tuple[str, re.Pattern[str]]] = []
    for lang, phrases in (config.get("phrases") or {}).items():
        for phrase in phrases:
            p = phrase.strip()
            if not p:
                continue
            rules.append((f"phrase:{lang}:{p}", re.compile(re.escape(p), re.IGNORECASE)))
    token_groups = [config.get("tokens") or {}, config.get("contextual_tokens") or {}]
    for group in token_groups:
        if not isinstance(group, dict):
            continue
        for lang, tokens in group.items():
            if lang == "comment" or not isinstance(tokens, list):
                continue
            for token in tokens:
                t = token.strip()
                if not t:
                    continue
                rules.append(
                    (
                        f"token:{lang}:{t}",
                        re.compile(rf"(?<!\w){re.escape(t)}(?!\w)", re.IGNORECASE),
                    )
                )
    return rules


def iter_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_DIR_NAMES for part in path.parts):
            continue
        if path.suffix.lower() not in SCAN_SUFFIXES:
            continue
        files.append(path)
    return files


def lint(root: Path, config: dict) -> list[str]:
    prefixes = config.get("allowlist_path_prefixes") or []
    rules = compile_rules(config)
    hits: list[str] = []
    for path in iter_files(root):
        rel = str(path.relative_to(root))
        if is_allowlisted(rel, prefixes):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for i, line in enumerate(text.splitlines(), start=1):
            for label, pattern in rules:
                if pattern.search(line):
                    hits.append(f"{rel}:{i}: {label}: {line.strip()[:160]}")
    return hits


def self_test(config: dict) -> int:
    """Tiny matcher tests — does not scan the repo."""
    rules = compile_rules(config)
    by_label = {label: pat for label, pat in rules}
    must_match = [
        ("phrase:it:sostegno psicologico", "Offriamo sostegno psicologico in 24 ore."),
        ("phrase:it:benessere psicologico", "Un programma di benessere psicologico."),
        ("token:it:psicologico", "Servizio psicologico per dipendenti."),
        ("token:it:stress", "Trattiamo lo stress dei lavoratori."),
        ("phrase:en:psychological support", "We offer psychological support."),
    ]
    must_not = [
        ("phrase:en:psychological support", "We sell formation and mediation only."),
        ("phrase:it:sostegno psicologico", "Formazione di gruppo e mediazione culturale."),
    ]
    failed = 0
    for label, sample in must_match:
        if label not in by_label:
            print(f"SELF-TEST missing rule {label}", file=sys.stderr)
            failed += 1
            continue
        if not by_label[label].search(sample):
            print(f"SELF-TEST expected match {label!r} in {sample!r}", file=sys.stderr)
            failed += 1
    for label, sample in must_not:
        if label in by_label and by_label[label].search(sample):
            print(f"SELF-TEST unexpected match {label!r} in {sample!r}", file=sys.stderr)
            failed += 1
    if failed:
        return 1
    print("banned-words self-test: ok")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--list", type=Path, default=DEFAULT_LIST)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args(argv)

    config = load_config(args.list)
    if args.self_test:
        return self_test(config)

    hits = lint(args.root, config)
    if hits:
        print("Banned presentation terms (CLAUDE.md §5 / Cass. 16562/2016):", file=sys.stderr)
        for hit in hits:
            print(hit, file=sys.stderr)
        print(
            f"\n{len(hits)} hit(s). Rewrite the copy or get a human to amend "
            "compliance/banned-words.json (CLAUDE.md §5.1).",
            file=sys.stderr,
        )
        return 1
    print("banned-words lint: clean")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
