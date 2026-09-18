"""Candidate content inputs, ranked.

Applies rules to the day's data and emits plain-language observations with the
numbers attached. These are RAW INPUTS, not drafts. Austin edits, keeps the
ones he has a view on, and feeds them back for a content pass.

Every signal names the theme it feeds (content/themes/<theme>.md) so the
observation lands on an existing shelf instead of floating.
"""
import sys, os, glob, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dispersion, lending, builders, derive

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PER_8H, PER_HOUR = 3 * 365, 24 * 365


def sig(rank, text, theme):
    return {"rank": rank, "text": text, "theme": theme}


def new_listings():
    out = []
    files = sorted(glob.glob(os.path.join(ROOT, "snapshots", "*.json")))
    if len(files) < 2:
        return [sig(0, "No listing diff yet: needs two snapshots.", "-")]
    old, new = json.load(open(files[-2])), json.load(open(files[-1]))
    for v in new["venues"]:
        so = {r["symbol"] for r in old["venues"].get(v, [])}
        sn = {r["symbol"] for r in new["venues"][v]}
        added, removed = sorted(sn - so), sorted(so - sn)
        if added:
            out.append(sig(100, f"{v} listed {len(added)} new market(s) overnight: "
                           f"{', '.join(added)}. Each one had no funding rate yesterday.",
                           "price-discovery-markets-on-everything"))
        if removed:
            out.append(sig(90, f"{v} removed {len(removed)} market(s): {', '.join(removed)}. "
                           f"A delisting is a market that failed to find two sides.",
                           "market-sizing-reauction"))
    return out


def funding_signals():
    out, rows = [], dispersion.table()
    splits = [r for r in rows if r["sign_split"]]
    if splits:
        top = splits[0]
        out.append(sig(85, f"{len(splits)} symbols have one venue paying longs while another pays "
                      f"shorts right now. Widest is {top['symbol']}: "
                      f"{top['max_venue']} at {top['rates'][top['max_venue']]*PER_8H*100:.1f}%/yr "
                      f"versus {top['min_venue']} at {top['rates'][top['min_venue']]*PER_8H*100:.1f}%/yr. "
                      f"Same exposure, opposite sign, simultaneously.",
                      "funding-as-yield-delta-neutral"))
    wide = [r for r in rows if r["spread"] * PER_8H > 0.25][:5]
    if wide:
        out.append(sig(70, "Widest funding dispersion: " + "; ".join(
            f"{r['symbol']} {r['spread']*PER_8H*100:.0f}pp between {r['max_venue']} and {r['min_venue']}"
            for r in wide) + ". Venues do not share a balance sheet, so the spread persists.",
            "execution-costs-venue-selection"))
    return out


def carry_signals():
    out = []
    try:
        aave = {r["symbol"]: r for r in lending.aave()}
        stables = [aave[s] for s in ("USDC", "USDT", "GHO") if s in aave and aave[s].get("borrow_apy")]
        fund = {}
        for r in dispersion.fetch():
            fund.setdefault(r["symbol"], {})[r["exchange"]] = r["rate"] * PER_8H
        btc = fund.get("BTC", {}).get("lighter")
        if stables and btc is not None:
            cheapest = min(stables, key=lambda r: r["borrow_apy"])
            out.append(sig(80, f"BTC perp funding annualizes at {btc*100:.1f}% on Lighter. "
                          f"Borrowing {cheapest['symbol']} against collateral on Aave costs "
                          f"{cheapest['borrow_apy']*100:.2f}%. The gap is {(btc-cheapest['borrow_apy'])*100:.1f}pp "
                          f"and it is the whole argument for collateral that earns while it margins.",
                          "yield-bearing-collateral"))
    except Exception as e:
        out.append(sig(0, f"carry signal unavailable: {type(e).__name__}", "-"))
    return out


def margin_signals():
    out = []
    try:
        d = {r["currency"]: r for r in derive.currencies() if r.get("im_perp")}
        near_cap = [r for r in d.values() if r.get("oi_cap") and
                    (r["oi_current"] or 0) / r["oi_cap"] > 0.5]
        if near_cap:
            out.append(sig(60, "Derive open interest near its cap: " + "; ".join(
                f"{r['currency']} at {(r['oi_current']/r['oi_cap'])*100:.0f}% of a "
                f"{r['oi_cap']:,.0f} cap" for r in near_cap) +
                ". An OI cap is a venue deciding how much of a risk it will hold.",
                "risk-parameters-transparency"))
        if "BTC" in d:
            b = d["BTC"]
            out.append(sig(55, f"Derive requires {b['im_perp']*100:.1f}% initial margin on BTC perp "
                          f"({b['max_leverage']:.1f}x max). Reg-T on US equities is 50%. "
                          f"Same trader, same collateral, two different worlds.",
                          "capital-efficiency-reg-t"))
    except Exception as e:
        out.append(sig(0, f"margin signal unavailable: {type(e).__name__}", "-"))
    return out


def zombie_signals():
    out = []
    try:
        rows, _ = builders.collect_all()
        by = {}
        for r in rows:
            b = by.setdefault(r["venue"], {"n": 0, "oi": 0.0, "vol": 0.0})
            b["n"] += 1
            b["oi"] += r["oi_usd"] or 0
            b["vol"] += r["day_ntl_vlm"] or 0
        dead = [(v, b) for v, b in by.items() if b["vol"] == 0 and b["n"] > 2]
        if dead:
            n_mkts = sum(b["n"] for _, b in dead)
            names = ", ".join(v.split(":")[1] for v, _ in dead)
            out.append(sig(65, f"{len(dead)} of {len(by)} HIP-3 builders are dark: {names}, "
                          f"{n_mkts} markets between them carrying live-looking marks with zero "
                          f"open interest and zero volume. A market list is not a market, and "
                          f"counting listings without checking open interest overstates the "
                          f"category badly.", "price-discovery-markets-on-everything"))
        live = sorted([(v, b) for v, b in by.items() if b["vol"] > 0],
                      key=lambda kv: -kv[1]["oi"])
        if live:
            v, b = live[0]
            out.append(sig(75, f"{v} carries ${b['oi']:,.0f} of open interest across {b['n']} "
                          f"builder-deployed markets on ${b['vol']:,.0f} of daily volume. "
                          f"These are equities and commodities settling on a crypto venue.",
                          "spot-collateral-collapsing-basis"))
    except Exception as e:
        out.append(sig(0, f"zombie signal unavailable: {type(e).__name__}", "-"))
    return out


def run():
    sigs = []
    for fn in (new_listings, funding_signals, carry_signals, margin_signals, zombie_signals):
        try:
            sigs.extend(fn())
        except Exception as e:
            sigs.append(sig(0, f"{fn.__name__} failed: {type(e).__name__}: {e}", "-"))
    sigs.sort(key=lambda s: -s["rank"])
    print("CANDIDATE INPUTS (raw, ranked. Edit, keep what you have a view on, discard the rest.)\n")
    for i, s in enumerate(sigs, 1):
        print(f"{i}. {s['text']}")
        print(f"   -> theme: {s['theme']}\n")


if __name__ == "__main__":
    run()
