#!/usr/bin/env python3
"""
Conservation check for compaction: did any fact silently disappear?

Compaction may drop prose. It may never drop a lesson, a result, a decision or
a number. This script does the mechanical half of that check: it pulls every
hard token out of the lines a change removes, and confirms each still appears
somewhere in the working tree (the new text, or the verbatim original under
archive/). The change-reviewer judges the rest: lesson-shaped sentences whose
meaning was lost even though their tokens survived.

Usage:
  python3 tools/conservation_check.py                # staged + unstaged changes vs HEAD
  python3 tools/conservation_check.py --rev A..B     # a committed range

Exit 0 when every token is still present, 1 when any is missing (listed).
"""

import argparse
import os
import re
import subprocess
import sys

TOKENS = [
    re.compile(r"\b\d{4}-\d{2}-\d{2}\b"),                       # dates
    re.compile(r"\b(?:[A-Z][A-Z0-9]+-\d+)\b"),                   # D-012, C-003, ticket keys
    re.compile(r"(?<![\w/])#\d{2,}\b"),                          # PR / issue numbers
    re.compile(r"\b[0-9a-f]{7,12}\b"),                           # short commit shas
    re.compile(r"(?<![\w.])\d+(?:[.,]\d+)*(?:%|/\d+)?(?![\w.])"),  # numbers, ratios, percents
]
SKIP_NUMBERS = {str(i) for i in range(0, 11)}   # list markers and small counts are noise


def git(args):
    return subprocess.run(["git"] + args, capture_output=True, text=True, check=False).stdout


def removed_lines(rev):
    diff = git(["diff", "--unified=0", rev] if rev else ["diff", "--unified=0", "HEAD"])
    out, path = [], None
    for line in diff.splitlines():
        if line.startswith("--- "):
            path = line[6:] if line.startswith("--- a/") else None
        elif line.startswith("-") and not line.startswith("---") and path:
            out.append((path, line[1:]))
    return out


def corpus():
    files = git(["ls-files", "-co", "--exclude-standard"]).splitlines()
    parts = []
    for f in files:
        if f.endswith((".png", ".jpg", ".gif", ".pdf", ".zip")):
            continue
        try:
            with open(f, encoding="utf-8", errors="replace") as fh:
                parts.append(fh.read())
        except OSError:
            pass
    return "\n".join(parts)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rev", help="git range, e.g. HEAD~1..HEAD (default: working tree vs HEAD)")
    args = ap.parse_args()
    if args.rev and ".." in args.rev:
        # For a committed range, compare against the tree at the range's end.
        end = args.rev.split("..")[1] or "HEAD"
        if git(["rev-parse", end]).strip() != git(["rev-parse", "HEAD"]).strip():
            sys.exit("Check out the range's end first; the corpus is the working tree.")
    text = corpus()
    missing = {}
    for path, line in removed_lines(args.rev):
        for rx in TOKENS:
            for tok in rx.findall(line):
                if tok in SKIP_NUMBERS or tok in text:
                    continue
                missing.setdefault(tok, (path, line.strip()[:100]))
    if not missing:
        print("conservation: every removed token is still present (new text or archive/).")
        return 0
    print(f"conservation: {len(missing)} token(s) removed and found nowhere else:")
    for tok, (path, line) in sorted(missing.items()):
        print(f"  {tok!r:>14}  {path}: {line}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
