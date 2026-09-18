"""Derive v3. JSON-RPC 2.0 over HTTP POST at https://api.derive.xyz/v3.

Derive publishes per-currency margin requirements and open-interest caps,
which is the cross-venue capital-efficiency comparison in machine form.
"""
import urllib.request, json, ssl

CTX = ssl.create_default_context()
BASE = "https://api.derive.xyz/v3"
H = {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json"}


def call(method, params=None):
    req = urllib.request.Request(f"{BASE}/{method}",
                                 data=json.dumps(params or {}).encode(), headers=H)
    d = json.loads(urllib.request.urlopen(req, timeout=30, context=CTX).read())
    if "error" in d:
        raise RuntimeError(d["error"])
    return d["result"]


def currencies():
    """Spot price, 24h-ago price, perp margin requirements and OI caps."""
    out = []
    for c in call("public/get_all_currencies"):
        row = {"venue": "derive", "currency": c.get("currency"),
               "spot": _f(c.get("spot_price")), "spot_24h": _f(c.get("spot_price_24h")),
               "has_perp": bool(c.get("perp")), "has_option": bool(c.get("option"))}
        perp = c.get("perp") or {}
        for u in (perp.get("universes") or []):
            m = u.get("srm_perp_margin_requirements") or {}
            oi = u.get("oi") or {}
            row.update({
                "risk_universe": u.get("risk_universe_name"),
                "im_perp": _f(m.get("im_perp_req")),
                "mm_perp": _f(m.get("mm_perp_req")),
                "max_leverage": _f(m.get("max_leverage")),
                "oi_current": _f(oi.get("current_open_interest")),
                "oi_cap": _f(oi.get("interest_cap")),
            })
            break
        out.append(row)
    return out


def _f(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


if __name__ == "__main__":
    rows = currencies()
    perps = [r for r in rows if r.get("im_perp")]
    print(f"DERIVE: {len(rows)} currencies, {len(perps)} with perp margin published\n")
    print(f"{'ccy':<8}{'spot':>12}{'IM':>8}{'MM':>8}{'maxlev':>9}{'OI':>12}{'OI cap':>12}{'util':>8}")
    for r in sorted(perps, key=lambda r: -(r["oi_current"] or 0)):
        util = (r["oi_current"] / r["oi_cap"] * 100) if r.get("oi_cap") else None
        print(f"{r['currency']:<8}{r['spot']:>12,.2f}{r['im_perp']*100:>7.1f}%"
              f"{r['mm_perp']*100:>7.1f}%{r['max_leverage']:>9.1f}"
              f"{r['oi_current']:>12,.1f}{r['oi_cap']:>12,.0f}"
              + (f"{util:>7.1f}%" if util is not None else f"{'-':>8}"))
