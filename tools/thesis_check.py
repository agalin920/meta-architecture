#!/usr/bin/env python3
"""
Check meta/thesis.md's falsifier against the data, on its dates (2027-01-31, 2027-03-31).

Each criterion is computed where it can be and named as unmeasured where it
cannot, so the answer is never a guess. Read-only: prints a report; the
scheduled run copies it into meta/thesis.md's "Checked on" table.

  python3 tools/thesis_check.py [--since 2026-10-29] [--until today]
"""

import argparse
import datetime as dt
import glob
import importlib.util
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEV = os.path.dirname(ROOT)
CORE = {
    "zesty-eng-team": os.path.join(DEV, "zestyio/zesty-eng-team"),
    "mpulse-engage-team": os.path.join(DEV, "mpulsemobile/mpulse-engage-team"),
    "mpulse-dpi-team": os.path.join(DEV, "mpulsemobile/mpulse-dpi-team"),
}
EVENT = re.compile(r"^- (\d{4}-\d{2}-\d{2})[^|]*\|\s*([\w -]+?)\s*\|")


def load_score(name, repo):
    spec = importlib.util.spec_from_file_location(f"s_{name.replace('-', '_')}", os.path.join(repo, "scoreboard", "score.py"))
    mod = importlib.util.module_from_spec(spec)
    cwd = os.getcwd()
    os.chdir(repo)
    try:
        spec.loader.exec_module(mod)
    finally:
        os.chdir(cwd)
    return mod


def compute(mod, repo, since, until):
    cwd = os.getcwd()
    os.chdir(repo)
    try:
        return mod.compute(since, until)
    finally:
        os.chdir(cwd)


def events(repo, kind, since, until):
    n = 0
    for f in glob.glob(os.path.join(repo, "log", "events-*.md")):
        for line in open(f, encoding="utf-8", errors="replace"):
            m = EVENT.match(line)
            if m and m.group(2).strip() == kind and since <= dt.date.fromisoformat(m.group(1)) <= until:
                n += 1
    return n


def verdicts_helped(repo):
    try:
        text = open(os.path.join(repo, "CHANGELOG.md"), encoding="utf-8").read()
    except OSError:
        return 0
    return len(re.findall(r"\*\*Verdict:\*\*\s*helped", text, re.I))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--since", default="2026-10-29")
    ap.add_argument("--until", default=str(dt.date.today()))
    a = ap.parse_args()
    since, until = dt.date.fromisoformat(a.since), dt.date.fromisoformat(a.until)
    weeks = max((until - since).days / 7, 1)
    lag = dt.timedelta(days=30)
    print(f"Thesis check {since} .. {until}  (meta/thesis.md § What would prove it wrong)\n")

    flat_or_worse, no_data, esc_rates, helped = [], [], {}, 0
    for name, repo in CORE.items():
        base = json.load(open(os.path.join(repo, "scoreboard", "baseline-2026-10-28.json")))
        base = base.get("scores") or base.get("measures") or base
        try:
            mod = load_score(name, repo)
            now = compute(mod, repo, since, until)
            s1 = compute(mod, repo, since - lag, until - lag).get("S1", {})
            now = {**now, "S1": s1}
        except Exception as e:
            print(f"  {name}: scoreboard error: {e}")
            no_data.append(name)
            continue
        better = []
        for k in ("S1", "S2", "S3"):
            b, v = (base.get(k) or {}).get("value"), (now.get(k) or {}).get("value")
            better.append(b is not None and v is not None and v < b)
        g_b, g_v = (base.get("G1") or {}).get("value"), (now.get("G1") or {}).get("value")
        g_up = g_b is not None and g_v is not None and g_v > g_b
        line = ", ".join(f"{k} {(base.get(k) or {}).get('value')}→{(now.get(k) or {}).get('value')}" for k in ("S1", "S2", "S3", "G1"))
        print(f"  {name}: {line}")
        have = [(base.get(k) or {}).get("value") is not None and (now.get(k) or {}).get("value") is not None
                for k in ("S1", "S2", "S3")]
        if not any(have):
            no_data.append(name)
        elif not any(better) and not g_up:
            flat_or_worse.append(name)
        esc_rates[name] = round(events(repo, "escalation", since, until) / weeks, 2)
        helped += verdicts_helped(repo)

    c1 = len(flat_or_worse) >= 2
    if len(no_data) >= 2:
        print("\n1. No improvement: INSUFFICIENT DATA — no comparable scores for "
              f"{', '.join(no_data)}. Re-run when the window has merged PRs.")
    c2 = any(r > 2 for r in esc_rates.values())
    c3 = helped == 0 and (until - since).days >= 44   # a change needs 14 days to be judged, a lesson 44
    if len(no_data) < 2:
      print("\n1. No improvement (2 of 3 systems flat or worse on S1-S3, G1 not up): "
          f"{'TRIPPED' if c1 else 'not tripped'} — flat/worse: {', '.join(flat_or_worse) or 'none'}"
          + (f"; no data: {', '.join(no_data)}" if no_data else ""))
    print(f"2. Andres back in the middle (> 2 escalations per system per week): "
          f"{'TRIPPED' if c2 else 'not tripped'} — {esc_rates}. "
          "Unmeasured half: whether he was asked to start a retro or approve a routine change; ask him.")
    print(f"3. The loop changes nothing that works (no self-change judged 'helped'): "
          f"{'TRIPPED' if c3 else 'not tripped'} — {helped} helped verdict(s) across the core systems"
          + ("" if (until - since).days >= 44 else " (too early to judge: under 44 days)") + ".")
    print("4. A lock broken without the tripwire saying so: unmeasured by script; ask Andres and check "
          "each system's log for LOCK BROKEN reports.")


if __name__ == "__main__":
    main()
