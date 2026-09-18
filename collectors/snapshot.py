"""Write a dated snapshot of every venue's market list to snapshots/."""
import json, os, sys, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import venues

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SNAPDIR = os.path.join(ROOT, "snapshots")


def run():
    os.makedirs(SNAPDIR, exist_ok=True)
    data = venues.collect_all()
    day = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
    path = os.path.join(SNAPDIR, f"{day}.json")
    with open(path, "w") as f:
        json.dump(data, f, indent=1, sort_keys=True)
    for v, rows in data["venues"].items():
        print(f"{v:14s} {len(rows)} markets")
    for v, err in data.get("errors", {}).items():
        print(f"{v:14s} ERROR {err}")
    print(f"wrote {path}")
    return path


if __name__ == "__main__":
    run()
