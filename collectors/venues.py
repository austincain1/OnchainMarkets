"""Pull normalized market data from onchain perp venues. No API keys required."""
import urllib.request, json, ssl, time

CTX = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json"}


def _get(url, payload=None, timeout=30):
    data = json.dumps(payload).encode() if payload else None
    req = urllib.request.Request(url, data=data, headers=UA)
    return json.loads(urllib.request.urlopen(req, timeout=timeout, context=CTX).read())


def lighter():
    """Lighter zk-rollup CLOB. Returns per-market dicts."""
    books = _get("https://mainnet.zklighter.elliot.ai/api/v1/orderBooks")["order_books"]
    out = []
    for b in books:
        if b.get("market_type") != "perp":
            continue
        out.append({
            "venue": "lighter",
            "symbol": b["symbol"],
            "market_id": b.get("market_id"),
            "status": b.get("status"),
            "taker_fee": b.get("taker_fee"),
            "maker_fee": b.get("maker_fee"),
            "created_at": b.get("created_at"),
        })
    return out


def lighter_funding(market_id, limit=24):
    """Hourly settled funding history for one Lighter market."""
    url = (f"https://mainnet.zklighter.elliot.ai/api/v1/fundings"
           f"?market_id={market_id}&resolution=1h&count_back={limit}")
    return _get(url)


def hyperliquid():
    meta, ctxs = _get("https://api.hyperliquid.xyz/info", {"type": "metaAndAssetCtxs"})
    out = []
    for asset, c in zip(meta["universe"], ctxs):
        out.append({
            "venue": "hyperliquid",
            "symbol": asset["name"],
            "max_leverage": asset.get("maxLeverage"),
            "funding": _f(c.get("funding")),          # per-hour decimal
            "open_interest": _f(c.get("openInterest")),
            "mark_px": _f(c.get("markPx")),
            "oracle_px": _f(c.get("oraclePx")),
            "premium": _f(c.get("premium")),
            "day_ntl_vlm": _f(c.get("dayNtlVlm")),
        })
    return out


def variational():
    s = _get("https://omni-client-api.prod.ap-northeast-1.variational.io/metadata/stats")
    out = []
    for l in s.get("listings", []):
        oi = l.get("open_interest", {}) or {}
        q = l.get("quotes", {}) or {}
        out.append({
            "venue": "variational",
            "symbol": l["ticker"],
            "name": l.get("name"),
            "mark_px": _f(l.get("mark_price")),
            "funding": _f(l.get("funding_rate")),
            "funding_interval_s": l.get("funding_interval_s"),
            "volume_24h": _f(l.get("volume_24h")),
            "oi_long": _f(oi.get("long_open_interest")),
            "oi_short": _f(oi.get("short_open_interest")),
            "spread_bps": _f(l.get("base_spread_bps")),
            "quote_1k": q.get("size_1k"),
            "quote_100k": q.get("size_100k"),
            "quote_1m": q.get("size_1m"),
        })
    platform = {
        "venue": "variational",
        "num_markets": s.get("num_markets"),
        "volume_24h": _f(s.get("total_volume_24h")),
        "open_interest": _f(s.get("open_interest")),
        "tvl": _f(s.get("tvl")),
    }
    return out, platform


def _f(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def collect_all():
    """Every venue, with per-venue failure isolation."""
    res = {"ts": int(time.time()), "venues": {}, "errors": {}}
    try:
        res["venues"]["lighter"] = lighter()
    except Exception as e:
        res["errors"]["lighter"] = f"{type(e).__name__}: {e}"
    try:
        res["venues"]["hyperliquid"] = hyperliquid()
    except Exception as e:
        res["errors"]["hyperliquid"] = f"{type(e).__name__}: {e}"
    try:
        mkts, plat = variational()
        res["venues"]["variational"] = mkts
        res["platform_variational"] = plat
    except Exception as e:
        res["errors"]["variational"] = f"{type(e).__name__}: {e}"
    # HIP-3 builder markets, one venue key per deployer (hl:xyz, hl:io, ...).
    # This is where listings churn fastest; without it the diff is blind to
    # new trade.xyz and Entropy markets.
    try:
        import builders
        rows, errs = builders.collect_all()
        for r in rows:
            res["venues"].setdefault(r["venue"], []).append(r)
        for d, e in errs.items():
            res["errors"][f"hl:{d}"] = e
    except Exception as e:
        res["errors"]["builders"] = f"{type(e).__name__}: {e}"
    return res
