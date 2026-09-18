"""Carry comparison: perp funding versus onchain borrow cost.

This is the "margin that earns" thesis with numbers. If a perp costs less in
funding than the same exposure costs to borrow against, or the collateral
earns more than the funding bleeds, the trade is in the gap.

UNITS, VERIFIED 2026-09-18: Lighter's /funding-rates feed normalizes every
venue to an 8-HOUR rate. Checked against Hyperliquid's native hourly funding
field, the ratio is exactly 8.0 across BTC, ETH, SOL, ENA and DOGE. So
annualize the feed as rate * 3 * 365, and Hyperliquid's own metaAndAssetCtxs
"funding" field as rate * 24 * 365. Do not mix the two.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dispersion, lending, builders

PER_8H = 3 * 365      # Lighter cross-venue feed convention
PER_HOUR = 24 * 365   # Hyperliquid native metaAndAssetCtxs convention


def funding_annualized():
    """Annualized from the Lighter cross-venue feed, which is 8h-normalized."""
    out = {}
    for r in dispersion.fetch():
        out.setdefault(r["symbol"], {})[r["exchange"]] = r["rate"] * PER_8H
    return out


def report(top=15):
    fund = funding_annualized()
    aave = {r["symbol"]: r for r in lending.aave()}
    morpho = lending.morpho()

    print("PERP FUNDING (annualized from 8h feed) vs ONCHAIN BORROW\n")
    print(f"{'asset':<10}{'lighter':>10}{'hyperliq':>10}{'binance':>10}{'bybit':>10}"
          f"{'aave brw':>10}{'aave sup':>10}")
    print("-" * 70)
    for sym in ["BTC", "ETH", "SOL", "ENA", "HYPE", "LINK", "AVAX", "DOGE"]:
        f = fund.get(sym, {})
        a = aave.get("W" + sym) or aave.get(sym) or {}
        line = f"{sym:<10}"
        for v in ["lighter", "hyperliquid", "binance", "bybit"]:
            x = f.get(v)
            line += f"{(f'{x*100:.1f}%' if x is not None else '-'):>10}"
        for k in ["borrow_apy", "supply_apy"]:
            x = a.get(k)
            line += f"{(f'{x*100:.2f}%' if x is not None else '-'):>10}"
        print(line)

    print("\nSTABLE BORROW COST (the cost of carrying a hedged position)")
    for r in sorted([x for x in lending.aave() if x["symbol"] in
                     ("USDC", "USDT", "GHO", "RLUSD", "USDe")],
                    key=lambda r: r["borrow_apy"] or 0)[:8]:
        print(f"  aave   {r['symbol']:<8} borrow {r['borrow_apy']*100:5.2f}%  supply {r['supply_apy']*100:5.2f}%")
    for r in sorted(morpho, key=lambda r: -(r["supply_usd"] or 0))[:6]:
        print(f"  morpho {str(r['collateral']):>8}/{str(r['loan']):<7} borrow {r['borrow_apy']*100:5.2f}%"
              f"  lltv {r['lltv']:.2f}  ${r['supply_usd']:,.0f}")

    rows, _ = builders.collect_all()
    live = [r for r in rows if (r["day_ntl_vlm"] or 0) > 0]
    print(f"\nBUILDER-DEPLOYED PERPS: {len(rows)} markets, {len(live)} with volume today")
    for r in sorted(live, key=lambda r: -(r["oi_usd"] or 0))[:10]:
        f = (r["funding"] or 0) * PER_HOUR * 100
        print(f"  {r['symbol']:<16} OI ${r['oi_usd']:>13,.0f}  funding {f:>8.1f}%/yr")


if __name__ == "__main__":
    report()
