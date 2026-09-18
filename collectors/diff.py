"""Compare the two most recent snapshots and report market list changes.

This is the content engine. Every new listing is a market that did not have a
funding rate yesterday and has one today.
"""
import json, os, sys, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SNAPDIR = os.path.join(ROOT, "snapshots")


def _symbols(snap):
    return {v: {r["symbol"] for r in rows} for v, rows in snap["venues"].items()}


def run(a=None, b=None):
    files = sorted(glob.glob(os.path.join(SNAPDIR, "*.json")))
    if len(files) < 2:
        print(f"need 2 snapshots, have {len(files)}")
        return
    a = a or files[-2]
    b = b or files[-1]
    old, new = json.load(open(a)), json.load(open(b))
    so, sn = _symbols(old), _symbols(new)
    print(f"{os.path.basename(a)} -> {os.path.basename(b)}\n")
    for v in sorted(set(so) | set(sn)):
        added = sorted(sn.get(v, set()) - so.get(v, set()))
        removed = sorted(so.get(v, set()) - sn.get(v, set()))
        if not added and not removed:
            print(f"{v}: no change ({len(sn.get(v, []))} markets)")
            continue
        print(f"{v}: {len(so.get(v,[]))} -> {len(sn.get(v,[]))}")
        if added:
            print(f"  NEW     ({len(added)}): {', '.join(added)}")
        if removed:
            print(f"  REMOVED ({len(removed)}): {', '.join(removed)}")
        print()


if __name__ == "__main__":
    run(*(sys.argv[1:3] or [None, None]))
