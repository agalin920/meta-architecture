#!/usr/bin/env python3
"""
The meta layer's scoreboard, computed from the core systems' own data.

  python3 scoreboard/score.py              # summary, now
  python3 scoreboard/score.py --json       # machine-readable
  python3 scoreboard/score.py --baseline   # writes scoreboard/baseline-2026-10-28.json

Exposes compute(since, until) and merged_prs(since, until) for verdicts.py.
For this layer a "unit" is a review run. This file is locked.
"""

import argparse
import datetime as dt
import importlib.util
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEV = os.path.dirname(ROOT)
CORE = {
    "zesty-eng-team": os.path.join(DEV, "zestyio/zesty-eng-team"),
    "mpulse-engage-team": os.path.join(DEV, "mpulsemobile/mpulse-engage-team"),
    "mpulse-dpi-team": os.path.join(DEV, "mpulsemobile/mpulse-dpi-team"),
}
MEASURES = ["S1", "S2", "S3", "S4", "G1"]
UP_IS_GOOD = {"G1"}
EVENT = re.compile(r"^- (\d{4}-\d{2}-\d{2})[^|]*\|\s*(\w[\w-]*)\s*\|")
STATUS = re.compile(r"\*\*Status:\*\*\s*`?(founding|candidate|proven|retired)`?", re.I)


def events(repo, kind, since, until):
    n, logdir = 0, os.path.join(repo, "log")
    if not os.path.isdir(logdir):
        return 0
    for name in os.listdir(logdir):
        if not name.startswith("events-"):
            continue
        with open(os.path.join(logdir, name), encoding="utf-8", errors="replace") as f:
            for line in f:
                m = EVENT.match(line)
                if m and m.group(2) == kind and since <= dt.date.fromisoformat(m.group(1)) < until:
                    n += 1
    return n


def child_scores(name, repo, since, until):
    path = os.path.join(repo, "scoreboard", "score.py")
    if not os.path.exists(path):
        return None, "no scoreboard"
    cwd = os.getcwd()
    try:
        os.chdir(repo)
        spec = importlib.util.spec_from_file_location(f"score_{name.replace('-', '_')}", path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod.compute(since, until), None
    except Exception as e:  # a child's failure is reported, not hidden
        return None, f"error: {e}"
    finally:
        os.chdir(cwd)


def m1(since, until):
    out = {}
    for name, repo in CORE.items():
        base_path = os.path.join(repo, "scoreboard", "baseline-2026-10-28.json")
        try:
            base = json.load(open(base_path))
            base = base.get("scores") or base.get("measures") or base   # systems store them under "scores"
        except Exception:
            out[name] = {"error": "no baseline"}
            continue
        now, err = child_scores(name, repo, since, until)
        if err:
            out[name] = {"error": err}
            continue
        # S1 only counts PRs merged 30+ days ago, so read it from the window 30 days earlier.
        lag = dt.timedelta(days=30)
        s1, err1 = child_scores(name, repo, since - lag, until - lag)
        if not err1 and s1:
            now = {**now, "S1": s1.get("S1", {})}
        row = {}
        for k in MEASURES:
            b, a = (base.get(k) or {}).get("value"), (now.get(k) or {}).get("value")
            if a is None or b is None:
                row[k] = "no data"
            elif a == b:
                row[k] = "flat"
            else:
                row[k] = "better" if ((a > b) if k in UP_IS_GOOD else (a < b)) else "worse"
        out[name] = row
    return out


def m3():
    counts = {"founding": 0, "candidate": 0, "proven": 0, "retired": 0}
    d = os.path.join(ROOT, "lessons")
    for name in os.listdir(d) if os.path.isdir(d) else []:
        if name.endswith(".md") and name not in ("README.md", "observations.md"):
            m = STATUS.search(open(os.path.join(d, name), encoding="utf-8").read())
            if m:
                counts[m.group(1).lower()] += 1
    trials = open(os.path.join(ROOT, "trials.md"), encoding="utf-8").read() \
        if os.path.exists(os.path.join(ROOT, "trials.md")) else ""
    counts["open_trials"] = len(re.findall(r"^- \*\*Status:\*\*\s*open", trials, re.M))
    return counts


def m4():
    judged = reverted = 0
    for repo in CORE.values():
        p = os.path.join(repo, "CHANGELOG.md")
        if not os.path.exists(p):
            continue
        for v in re.findall(r"\*\*Verdict:\*\*\s*(.+)", open(p, encoding="utf-8").read()):
            v = v.strip().lower()
            if v.startswith(("helped", "reverted")):
                judged += 1
                reverted += v.startswith("reverted")
    return {"judged": judged, "reverted": reverted,
            "value": round(reverted / judged, 2) if judged else None}


def compute(since, until):
    weeks = max((until - since).days / 7, 1)
    m1v = m1(since, until)
    better = sum(1 for r in m1v.values() for v in r.values() if v == "better")
    worse = sum(1 for r in m1v.values() for v in r.values() if v == "worse")
    esc = {n: round(events(r, "escalation", since, until) / weeks, 2) for n, r in CORE.items()}
    return {
        "M1": {"value": better - worse, "n": better + worse, "note": "measures better minus worse", "detail": m1v},
        "M2": {"value": round(sum(esc.values()) / len(esc), 2), "n": len(esc), "note": "per system per week", "detail": esc},
        "M3": {"value": m3().get("proven", 0) + m3().get("candidate", 0), "note": "candidate+proven", "detail": m3()},
        "M4": {**m4(), "note": "share reverted of judged"},
    }


def merged_prs(since, until):
    return events(ROOT, "review", since, until)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--baseline", action="store_true")
    a = ap.parse_args()
    today = dt.date.today()
    if a.baseline:
        res = {"date": "2026-10-28", "M1": "baseline by definition",
               "M2": "no pre-migration instrument", "M3": m3(), "M4": "n/a: no self-change judged"}
        json.dump(res, open(os.path.join(ROOT, "scoreboard", "baseline-2026-10-28.json"), "w"), indent=2)
        print(json.dumps(res, indent=2))
        return
    res = compute(today - dt.timedelta(days=30), today + dt.timedelta(days=1))
    if a.json:
        print(json.dumps(res, indent=2, default=str))
        return
    print(f"Meta scoreboard, last 30 days to {today}")
    for name, row in res["M1"]["detail"].items():
        print(f"  M1 {name}: " + (row.get("error") or ", ".join(f"{k} {v}" for k, v in row.items())))
    print(f"  M2 escalations/system/week: {res['M2']['value']}  {res['M2']['detail']}")
    print(f"  M3 playbook: {res['M3']['detail']}")
    print(f"  M4 reverted/judged: {res['M4']['reverted']}/{res['M4']['judged']}")


if __name__ == "__main__":
    main()
