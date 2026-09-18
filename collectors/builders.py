"""HIP-3 builder-deployed perp markets on Hyperliquid.

trade.xyz has no separate API. It is a HIP-3 builder, so its markets live
inside the Hyperliquid info endpoint under the dex name "xyz". Same for the
other builders, which is where equities, commodities, rates and private
companies are being listed as perps.
"""
import urllib.request, json, ssl

CTX = ssl.create_default_context()
URL = "https://api.hyperliquid.xyz/info"
H = {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json"}

# Builder identities. Ventuals (vntl) is sunset; its pre-IPO markets are dead
# and carry no OI. Entropy (io) is the live pre-IPO deployer, launched
# 2026-08-24, backed by Ribbit, bonded with ~500k HYPE.
KNOWN = {"xyz": "trade[XYZ]", "io": "Entropy", "vntl": "Ventuals (sunset)",
         "para": "para", "mkts": "mkts", "km": "km", "flx": "flx",
         "hyna": "hyna", "cash": "cash", "abcd": "abcd"}

DEAD = {"vntl"}


def _post(payload):
    req = urllib.request.Request(URL, data=json.dumps(payload).encode(), headers=H)
    return json.loads(urllib.request.urlopen(req, timeout=30, context=CTX).read())


def dexs():
    return [d["name"] for d in _post({"type": "perpDexs"}) if d and d.get("name")]


def markets(dex):
    meta, ctxs = _post({"type": "metaAndAssetCtxs", "dex": dex})
    out = []
    for a, c in zip(meta["universe"], ctxs):
        mark = _f(c.get("markPx"))
        oi = _f(c.get("openInterest"))
        out.append({
            "venue": f"hl:{dex}",
            "builder": KNOWN.get(dex, dex),
            "sunset": dex in DEAD,
            "symbol": a["name"],
            "max_leverage": a.get("maxLeverage"),
            "funding": _f(c.get("funding")),
            "mark_px": mark,
            "oracle_px": _f(c.get("oraclePx")),
            "premium": _f(c.get("premium")),
            "oi_base": oi,
            "oi_usd": (oi * mark) if (oi is not None and mark is not None) else None,
            "day_ntl_vlm": _f(c.get("dayNtlVlm")),
        })
    return out


def collect_all(include_sunset=True):
    """Every builder dex. Sunset deployers keep stale marks and zero OI, so
    they are flagged rather than silently dropped."""
    out, errs = [], {}
    for d in dexs():
        if not include_sunset and d in DEAD:
            continue
        try:
            out.extend(markets(d))
        except Exception as e:
            errs[d] = f"{type(e).__name__}: {e}"
    return out, errs


def _f(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


if __name__ == "__main__":
    rows, errs = collect_all()
    by = {}
    for r in rows:
        b = by.setdefault(r["venue"], {"n": 0, "oi": 0.0, "vol": 0.0, "syms": []})
        b["n"] += 1
        b["oi"] += r["oi_usd"] or 0
        b["vol"] += r["day_ntl_vlm"] or 0
        b["syms"].append(r["symbol"].split(":")[-1])
    for v, b in sorted(by.items(), key=lambda kv: -kv[1]["oi"]):
        tag = "  [SUNSET]" if v.split(":")[1] in DEAD else ""
        print(f"{v:12s} {b['n']:4d} mkts  OI ${b['oi']:>14,.0f}  24h ${b['vol']:>14,.0f}{tag}")
        print(f"             {', '.join(b['syms'][:18])}")
    print(f"\ntotal {len(rows)} builder markets across {len(by)} dexs")
    if errs:
        print("errors:", errs)
