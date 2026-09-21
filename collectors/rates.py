"""Offchain reference rates from FRED. The leg that turns funding into a curve.

Perp funding and onchain borrow only mean something against the offchain cost
of money. SOFR is the benchmark a desk actually funds at; the rest bracket it.

The API key is read from the FRED_API_KEY environment variable and is NEVER
written into this repo, which is public. In GitHub Actions it comes from an
encrypted repository secret. Locally or in a session, export it first.
"""
import urllib.request, json, ssl, os

CTX = ssl.create_default_context()
BASE = "https://api.stlouisfed.org/fred/series/observations"

SERIES = {
    "SOFR":   "Secured Overnight Financing Rate (what a desk funds at)",
    "DFF":    "Effective fed funds",
    "IORB":   "Interest on reserve balances",
    "DGS3MO": "3-month Treasury",
    "DGS10":  "10-year Treasury",
}


def key():
    k = os.environ.get("FRED_API_KEY")
    if not k:
        raise RuntimeError("FRED_API_KEY not set")
    return k


def latest(series_id, n=5):
    """Most recent non-missing observation, plus the prior one for a change."""
    url = (f"{BASE}?series_id={series_id}&api_key={key()}"
           f"&file_type=json&sort_order=desc&limit={n}")
    d = json.loads(urllib.request.urlopen(
        urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}),
        timeout=30, context=CTX).read())
    obs = [o for o in d.get("observations", []) if o.get("value") not in (".", None)]
    if not obs:
        return None
    cur = obs[0]
    prev = obs[1] if len(obs) > 1 else None
    return {"series": series_id, "date": cur["date"], "value": float(cur["value"]),
            "prev_date": prev["date"] if prev else None,
            "prev": float(prev["value"]) if prev else None}


def all_rates():
    out, errs = {}, {}
    for s in SERIES:
        try:
            out[s] = latest(s)
        except Exception as e:
            errs[s] = f"{type(e).__name__}: {e}"
    return out, errs


if __name__ == "__main__":
    rates, errs = all_rates()
    print("OFFCHAIN REFERENCE RATES (FRED)\n")
    for s, r in rates.items():
        if not r:
            continue
        chg = f"{(r['value']-r['prev'])*100:+.0f}bp" if r["prev"] is not None else ""
        print(f"  {s:<7} {r['value']:>6.2f}%  {r['date']}  {chg:>7}   {SERIES[s]}")
    for s, e in errs.items():
        print(f"  {s:<7} unavailable: {e}")
