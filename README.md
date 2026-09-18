# OnchainMarkets

Market data collection for tracking onchain derivatives venues.
Public endpoints only. No API keys. No secrets in this repo, ever.

## Venues

| Venue | Endpoint | Auth |
|---|---|---|
| Lighter | `mainnet.zklighter.elliot.ai/api/v1` | none |
| Hyperliquid | `api.hyperliquid.xyz/info` | none |
| Variational Omni | `omni-client-api.prod.ap-northeast-1.variational.io` | none |
| Derive | `api.derive.xyz` | none for market data |
| trade[XYZ] + 9 other HIP-3 builders | via `api.hyperliquid.xyz` `dex` param | none |
| Morpho | `api.morpho.org/graphql` | none |
| Aave v4 | `api.v4.aave.com/graphql` | none |
| Coinbase Exchange | `api.exchange.coinbase.com` | none |
| Pyth | `hermes.pyth.network` | none |
| DefiLlama | `api.llama.fi` (free endpoints) | none |

Lighter's `/api/v1/funding-rates` also republishes Binance, Bybit and
Hyperliquid funding, which routes around the geo-blocks on those APIs.

## Scripts

```
python3 collectors/snapshot.py     # write today's market list to snapshots/
python3 collectors/diff.py         # compare the two most recent snapshots
python3 collectors/dispersion.py   # cross-venue funding spread table
python3 collectors/builders.py     # HIP-3 builder markets (equities, commodities, rates)
python3 collectors/lending.py      # Morpho + Aave borrow/supply rates
python3 collectors/reference.py    # Coinbase, Pyth, DefiLlama
python3 collectors/carry.py        # funding vs borrow cost, side by side
```

## Daily routine

1. `snapshot.py` every morning. Commit the snapshot.
2. `diff.py` to see what listed or delisted overnight.
3. `dispersion.py` for funding spreads and sign splits.

New listings and sign splits are the two highest-signal outputs.

## Known gaps

- DefiLlama derivatives overview is behind their paid tier. Free protocol
  endpoints cover most of the same ground.
- Binance, Bybit, DexScreener and GeckoTerminal block the sandbox IP directly.
  Use the Lighter funding-rates feed instead.
- Funding intervals: RESOLVED. Lighter's `/funding-rates` feed is 8h-normalized
  across all four venues (verified against Hyperliquid's native hourly field,
  ratio exactly 8.0). Annualize that feed as `rate * 3 * 365`. Hyperliquid's own
  `metaAndAssetCtxs.funding` is hourly, annualize as `rate * 24 * 365`.
  Do not mix conventions.
- Morpho returns broken markets with 1000%+ APY at 100% utilization. `lending.morpho()`
  filters these by default via `max_apy` and `min_usd`.
- Uniswap `api.uniswap.org` returns 409 on quote endpoints. Not solved.
- trade.xyz has no standalone API. It is HIP-3 builder `xyz` on Hyperliquid.
