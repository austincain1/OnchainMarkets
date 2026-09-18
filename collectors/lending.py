"""Lending markets: Morpho and Aave. The collateral side of the thesis.

Borrow cost here versus funding cost on a perp venue is the comparison that
makes "margin that earns" concrete.
"""
import urllib.request, json, ssl

CTX = ssl.create_default_context()
H = {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json"}


def _gql(url, query, variables=None):
    payload = {"query": query}
    if variables:
        payload["variables"] = variables
    req = urllib.request.Request(url, data=json.dumps(payload).encode(), headers=H)
    d = json.loads(urllib.request.urlopen(req, timeout=40, context=CTX).read())
    if d.get("errors"):
        raise RuntimeError(d["errors"][0].get("message"))
    return d["data"]


MORPHO_Q = """
{ markets(first: %d, orderBy: SupplyAssetsUsd, orderDirection: Desc,
          where: {chainId_in: [1]}) {
    items { marketId lltv
      loanAsset { symbol } collateralAsset { symbol }
      state { supplyApy borrowApy utilization supplyAssetsUsd borrowAssetsUsd } } } }
"""


def morpho(first=100, max_apy=2.0, min_usd=1_000_000):
    """Morpho Blue markets on Ethereum.

    max_apy filters out broken/manipulated markets. Several markets report
    APYs in the thousands of percent at 100%% utilization; they are noise.
    """
    items = _gql("https://api.morpho.org/graphql", MORPHO_Q % first)["markets"]["items"]
    out = []
    for m in items:
        st = m.get("state") or {}
        apy = st.get("borrowApy")
        usd = st.get("supplyAssetsUsd") or 0
        if apy is None or apy > max_apy or usd < min_usd:
            continue
        out.append({
            "protocol": "morpho",
            "market_id": m.get("marketId"),
            "loan": (m.get("loanAsset") or {}).get("symbol"),
            "collateral": (m.get("collateralAsset") or {}).get("symbol"),
            "lltv": int(m["lltv"]) / 1e18 if m.get("lltv") else None,
            "supply_apy": st.get("supplyApy"),
            "borrow_apy": apy,
            "utilization": st.get("utilization"),
            "supply_usd": usd,
            "borrow_usd": st.get("borrowAssetsUsd"),
        })
    return out


AAVE_Q = """
{ reserves(request: {query: {chainIds: [1]}, filter: ALL,
                     orderBy: {borrowApy: DESC}}) {
    id asset { underlying { info { symbol name } } }
    summary { supplyApy { value } borrowApy { value } } } }
"""


def aave():
    """Aave v4 reserves on Ethereum. APY values are decimal fractions."""
    rows = _gql("https://api.v4.aave.com/graphql", AAVE_Q)["reserves"]
    out, seen = [], set()
    for r in rows:
        info = (((r.get("asset") or {}).get("underlying") or {}).get("info") or {})
        sym = info.get("symbol")
        s = r.get("summary") or {}
        key = (sym, (s.get("borrowApy") or {}).get("value"))
        if not sym or key in seen:
            continue
        seen.add(key)
        out.append({
            "protocol": "aave",
            "symbol": sym,
            "name": info.get("name"),
            "supply_apy": _f((s.get("supplyApy") or {}).get("value")),
            "borrow_apy": _f((s.get("borrowApy") or {}).get("value")),
        })
    return out


def _f(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


if __name__ == "__main__":
    m = morpho()
    print(f"MORPHO: {len(m)} markets (filtered)")
    for r in sorted(m, key=lambda r: -(r["supply_usd"] or 0))[:12]:
        print(f"  {str(r['collateral']):>10} / {str(r['loan']):<8} "
              f"borrow {r['borrow_apy']*100:6.2f}%  supply {r['supply_apy']*100:6.2f}%  "
              f"${r['supply_usd']:>14,.0f}  util {r['utilization']:.2f}")
    a = aave()
    print(f"\nAAVE: {len(a)} reserves")
    for r in a[:12]:
        print(f"  {r['symbol']:<10} borrow {r['borrow_apy']*100:6.2f}%  supply {r['supply_apy']*100:6.2f}%")
