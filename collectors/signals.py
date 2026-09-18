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


# Question shapes that have produced usable analysis. Deliberately mechanical:
# the point is to remove the blank page, not to pre-load an argument. Austin
# picks one, sends it cold, and the analysis comes back unprimed.
QBANK = {
    "funding": [
        "Who is on the other side of this and what are they being paid to do?",
        "What would it cost to carry this for 30 days, all-in, including the leg I am forgetting?",
        "What breaks if enough people put this trade on?",
        "Is this a real dislocation or a thin book printing a number? How would I tell?",
    ],
    "carry": [
        "How would a desk actually construct this, and what is the minimum size where it is worth the operational effort?",
        "What does this cost offchain, and what specifically stops it from existing there?",
        "What has to be true for this gap to close, and what would keep it open?",
        "Where does the money come from? Name the party who is worse off.",
    ],
    "listing": [
        "Who wanted this market badly enough to list it, and what were they doing before it existed?",
        "What can a trader do the day this lists that they could not do the day before?",
        "What would make this market fail, and how fast would that show up in the data?",
    ],
    "structure": [
        "What is the tradeoff being made here, and who eats it?",
        "How would this look to someone who runs a book on a traditional venue?",
        "What does this number actually measure, and what does it miss?",
        "Is this a design choice or an accident of how the thing was built?",
    ],
}


def sig(rank, text, theme, qkey="structure"):
    return {"rank": rank, "text": text, "theme": theme,
            "questions": QBANK.get(qkey, QBANK["structure"])}


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
                           "price-discovery-markets-on-everything", "listing"))
        if removed:
            out.append(sig(90, f"{v} removed {len(removed)} market(s): {', '.join(removed)}. "
                           f"A delisting is a market that failed to find two sides.",
                           "market-sizing-reauction", "listing"))
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
                      "funding-as-yield-delta-neutral", "funding"))
    wide = [r for r in rows if r["spread"] * PER_8H > 0.25][:5]
    if wide:
        out.append(sig(70, "Widest funding dispersion: " + "; ".join(
            f"{r['symbol']} {r['spread']*PER_8H*100:.0f}pp between {r['max_venue']} and {r['min_venue']}"
            for r in wide) + ". Venues do not share a balance sheet, so the spread persists.",
            "execution-costs-venue-selection", "funding"))
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
