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

Lighter's `/api/v1/funding-rates` also republishes Binance, Bybit and
Hyperliquid funding, which routes around the geo-blocks on those APIs.

## Scripts

```
python3 collectors/snapshot.py     # write today's market list to snapshots/
python3 collectors/diff.py         # compare the two most recent snapshots
python3 collectors/dispersion.py   # cross-venue funding spread table
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
- Funding intervals differ by venue. Verify normalization before publishing
  annualized numbers.
