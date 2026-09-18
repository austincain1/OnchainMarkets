"""Venue share and category size from DefiLlama's free endpoints.

The /overview/derivatives endpoint is paid (402). These are not. The
defillama.com PAGES route documented in live-sources.md stays the fallback
for the row of record; this is the machine-readable approximation.
"""
import urllib.request, json, ssl

CTX = ssl.create_default_context()
H = {"User-Agent": "Mozilla/5.0"}

PERP_VENUES = ["lighter", "hyperliquid", "hyperliquid-perps", "lighter-robinhood-perps",
               "variational", "derive", "aster", "edgex", "paradex", "drift",
               "vertex-protocol", "gmx", "dydx", "apex-protocol", "ostium"]

LENDING = ["aave", "morpho", "aave-v3", "morpho-blue", "euler", "fluid-lending"]


def _get(url, timeout=45):
    return json.loads(urllib.request.urlopen(
        urllib.request.Request(url, headers=H), timeout=timeout, context=CTX).read())


def protocol(slug):
    d = _get(f"https://api.llama.fi/protocol/{slug}")
    tvl = d.get("tvl")
    return {
        "slug": slug, "name": d.get("name"), "category": d.get("category"),
        "chains": d.get("chains"), "symbol": d.get("symbol"),
        "tvl": tvl[-1].get("totalLiquidityUSD") if isinstance(tvl, list) and tvl else None,
        "mcap": d.get("mcap"),
    }


def table(slugs):
    out, errs = [], {}
    for s in slugs:
        try:
            out.append(protocol(s))
        except Exception as e:
            errs[s] = f"{type(e).__name__}"
    return out, errs


def dex_overview():
    """Spot DEX volume by protocol. Free endpoint."""
    d = _get("https://api.llama.fi/overview/dexs"
             "?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true")
    return {"total_24h": d.get("total24h"), "total_30d": d.get("total30d"),
            "change_1d": d.get("change_1d"),
            "protocols": [{"name": p.get("name"), "vol_24h": p.get("total24h"),
                           "vol_30d": p.get("total30d"), "change_1d": p.get("change_1d")}
                          for p in (d.get("protocols") or [])[:25]]}


if __name__ == "__main__":
    rows, errs = table(PERP_VENUES + LENDING)
    print(f"{'slug':<28}{'category':<16}{'tvl':>16}")
    for r in sorted(rows, key=lambda r: -(r["tvl"] or 0)):
        t = f"${r['tvl']:,.0f}" if r["tvl"] else "-"
        print(f"{r['slug']:<28}{str(r['category'])[:15]:<16}{t:>16}")
    if errs:
        print("not found:", ", ".join(errs))
    d = dex_overview()
    print(f"\nSPOT DEX 24h ${d['total_24h']:,.0f}  30d ${d['total_30d']:,.0f}")
