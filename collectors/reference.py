"""Reference prices and protocol-level data: Coinbase, Pyth, DefiLlama."""
import urllib.request, json, ssl

CTX = ssl.create_default_context()
H = {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json"}


def _get(url, timeout=40):
    return json.loads(urllib.request.urlopen(
        urllib.request.Request(url, headers=H), timeout=timeout, context=CTX).read())


def coinbase_products():
    """Full Coinbase Exchange product list. The regulated spot reference."""
    return [{"id": p["id"], "base": p["base_currency"], "quote": p["quote_currency"],
             "status": p.get("status"), "trading_disabled": p.get("trading_disabled")}
            for p in _get("https://api.exchange.coinbase.com/products")]


def coinbase_ticker(product="BTC-USD"):
    return _get(f"https://api.exchange.coinbase.com/products/{product}/ticker")


def pyth_feeds(query):
    """Pyth price feed search. Covers equities, FX, commodities and crypto,
    and reports whether the underlying market is currently open."""
    return _get(f"https://hermes.pyth.network/v2/price_feeds?query={query}")


def llama_protocol(slug):
    """DefiLlama protocol detail. Free endpoint. The derivatives overview
    endpoint is paid, this one is not."""
    return _get(f"https://api.llama.fi/protocol/{slug}")


def llama_tvl_summary(slugs):
    out = {}
    for s in slugs:
        try:
            d = llama_protocol(s)
            out[s] = {"name": d.get("name"), "category": d.get("category"),
                      "chains": d.get("chains"), "tvl": _latest_tvl(d)}
        except Exception as e:
            out[s] = {"error": f"{type(e).__name__}: {e}"}
    return out


def _latest_tvl(d):
    t = d.get("tvl")
    if isinstance(t, list) and t:
        return t[-1].get("totalLiquidityUSD")
    return None


if __name__ == "__main__":
    p = coinbase_products()
    print(f"COINBASE: {len(p)} products, {sum(1 for x in p if not x['trading_disabled'])} tradable")
    print("  BTC-USD:", coinbase_ticker()["price"])
    for q in ["SPY", "WHEAT", "USDJPY"]:
        f = pyth_feeds(q)
        opens = sum(1 for x in f if (x.get("market_hours") or {}).get("is_open"))
        print(f"PYTH {q}: {len(f)} feeds, {opens} open now")
    print("\nDEFILLAMA:")
    for s, v in llama_tvl_summary(["lighter", "hyperliquid", "morpho", "aave"]).items():
        tvl = v.get("tvl")
        print(f"  {s:12s} {v.get('name')} tvl=" + (f"${tvl:,.0f}" if tvl else str(v.get('error', 'n/a'))[:60]))
