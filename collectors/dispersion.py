"""Cross-venue funding dispersion.

Lighter publishes funding for lighter, binance, bybit and hyperliquid in one
public endpoint, which also routes around the geo-blocks on the CEX APIs.

The spread between venues on the same exposure is the trade and the post.

CAVEAT: rates are compared as published. Funding intervals differ by venue
(Hyperliquid settles hourly, Binance and Bybit typically 8h). Verify interval
normalization before quoting annualized figures publicly.
"""
import urllib.request, json, ssl, collections, sys

CTX = ssl.create_default_context()
URL = "https://mainnet.zklighter.elliot.ai/api/v1/funding-rates"


def fetch():
    req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0"})
    return json.loads(urllib.request.urlopen(req, timeout=30, context=CTX).read())["funding_rates"]


def table(min_venues=2):
    by_sym = collections.defaultdict(dict)
    for r in fetch():
        by_sym[r["symbol"]][r["exchange"]] = r["rate"]
    rows = []
    for sym, v in by_sym.items():
        if len(v) < min_venues:
            continue
        rates = list(v.values())
        rows.append({
            "symbol": sym,
            "rates": v,
            "spread": max(rates) - min(rates),
            "max_venue": max(v, key=v.get),
            "min_venue": min(v, key=v.get),
            "sign_split": (max(rates) > 0 > min(rates)),
        })
    return sorted(rows, key=lambda r: -r["spread"])


def report(top=20):
    rows = table()
    venues = ["lighter", "hyperliquid", "binance", "bybit"]
    print(f"{len(rows)} symbols quoted on 2+ venues. Top {top} by dispersion.\n")
    hdr = f"{'sym':<12}" + "".join(f"{v[:9]:>11}" for v in venues) + f"{'spread':>11}  flag"
    print(hdr); print("-" * len(hdr))
    for r in rows[:top]:
        line = f"{r['symbol']:<12}"
        for v in venues:
            x = r["rates"].get(v)
            line += f"{(f'{x*100:.4f}%' if x is not None else '-'):>11}"
        line += f"{r['spread']*100:>10.4f}%"
        line += "  SIGN SPLIT" if r["sign_split"] else ""
        print(line)
    splits = [r for r in rows if r["sign_split"]]
    print(f"\n{len(splits)} symbols where one venue pays longs while another pays shorts:")
    print("  " + ", ".join(r["symbol"] for r in splits[:40]))


if __name__ == "__main__":
    report(int(sys.argv[1]) if len(sys.argv) > 1 else 20)
