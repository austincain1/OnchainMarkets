# 2026-11-21

## Market list changes
```
2026-11-20.json -> 2026-11-21.json

hl:abcd: no change (1 markets)
hl:cash: no change (17 markets)
hl:flx: no change (16 markets)
hl:hyna: no change (25 markets)
hl:io: no change (25 markets)
hl:km: no change (23 markets)
hl:mkts: no change (24 markets)
hl:para: no change (40 markets)
hl:vntl: no change (15 markets)
hl:xyz: no change (147 markets)
hyperliquid: no change (235 markets)
lighter: no change (235 markets)
variational: no change (595 markets)
```

## Funding dispersion
```
206 symbols quoted on 2+ venues. Top 25 by dispersion.

sym             lighter  hyperliqu    binance      bybit     spread      ann  flag
----------------------------------------------------------------------------------
UNITREE        -0.0632%          -   -0.0308%   -0.3429%    0.3121%      342%/yr
DRV             0.0096%          -          -   -0.1927%    0.2023%      222%/yr  SIGN SPLIT
SOXS                  -          -   -0.1691%   -0.0186%    0.1505%      165%/yr
SOXL            0.0032%          -    0.1446%    0.0000%    0.1446%      158%/yr
MET             0.0096%   -0.1235%   -0.0100%   -0.0039%    0.1331%      146%/yr  SIGN SPLIT
MSTR            0.0032%    0.0050%    0.1275%    0.0000%    0.1275%      140%/yr
GRAM           -0.0344%   -0.0468%   -0.0145%   -0.1373%    0.1228%      135%/yr
XIAOMI          0.0032%          -          -   -0.1177%    0.1209%      132%/yr  SIGN SPLIT
COIN            0.0032%    0.0050%    0.0975%    0.0000%    0.0975%      107%/yr
CRO             0.0096%          -          -   -0.0835%    0.0931%      102%/yr  SIGN SPLIT
CASHCAT         0.0096%    0.0100%          -   -0.0797%    0.0897%       98%/yr  SIGN SPLIT
IREN            0.0032%          -    0.0510%    0.0921%    0.0889%       97%/yr
BB              0.0032%          -    0.0100%   -0.0756%    0.0856%       94%/yr  SIGN SPLIT
EIGEN           0.0096%   -0.0733%   -0.0219%    0.0000%    0.0829%       91%/yr  SIGN SPLIT
ANTHROPIC       0.0800%          -    0.0000%          -    0.0800%       88%/yr
GMX            -0.0352%    0.0100%    0.0003%   -0.0693%    0.0793%       87%/yr  SIGN SPLIT
BMNR            0.0032%          -    0.0792%    0.0000%    0.0792%       87%/yr
PRL             0.0856%          -    0.0100%    0.0100%    0.0756%       83%/yr
CRCL           -0.0032%   -0.0148%    0.0607%   -0.0006%    0.0755%       83%/yr  SIGN SPLIT
UNI            -0.0576%    0.0034%   -0.0015%   -0.0026%    0.0610%       67%/yr  SIGN SPLIT
KORU            0.0032%          -    0.0637%    0.0045%    0.0605%       66%/yr
AVGO            0.0032%          -    0.0525%    0.0000%    0.0525%       58%/yr
INTC            0.0032%    0.0050%    0.0515%    0.0000%    0.0515%       56%/yr
NATGAS          0.0312%    0.0514%    0.0000%          -    0.0514%       56%/yr
1000BONK        0.0032%   -0.0210%   -0.0220%   -0.0481%    0.0513%       56%/yr  SIGN SPLIT

73 symbols where one venue pays longs while another pays shorts:
  DRV, MET, XIAOMI, CRO, CASHCAT, BB, EIGEN, GMX, CRCL, UNI, 1000BONK, MORPHO, PYTH, BIRB, MSFT, LIT, DUSK, CC, TAO, SKR, S, 1000FLOKI, TIA, POPCAT, PONS, PUMP, LINEA, HBAR, SKY, LINK, POL, 1000SHIB, APT, VIRTUAL, ARB, 2Z, BERA, PAXG, FIL, ONDO
```

## Builder-deployed markets
```
hl:xyz        147 mkts  OI $ 4,238,130,232  24h $ 2,965,126,671
             XYZ100, TSLA, NVDA, GOLD, HOOD, INTC, PLTR, COIN, META, AAPL, MSFT, ORCL, GOOGL, AMZN, AMD, MU, SNDK, MSTR
hl:io          25 mkts  OI $   115,270,389  24h $    71,646,303
             OAI, ANTH, SNDK, IONQ, NBIS, EWY, GPRO, SBE, TCNT, DRAM, PRL, XIAOMI, H100, MOONSHOT, NVDA, SKHX, AAPL, CRCL
hl:para        40 mkts  OI $    12,966,221  24h $     8,996,470
             TOTAL2, OTHERS, BTCD, H100, AVGO, COHR, GLW, CRDO, LRCX, NET, STX, IREN, VST, TER, AAOI, 10Y, CIEN, NAVER
hl:mkts        24 mkts  OI $       186,205  24h $       581,037
             US500, BABA, EUR, USBOND, SMALL2000, USTECH, USENERGY, USOIL, TSLA, SILVER, GOLD, AAPL, GOOGL, SEMI, GLDMINE, NVDA, TENCENT, JPN225
hl:flx         16 mkts  OI $             0  24h $             0
             TSLA, NVDA, CRCL, COIN, XMR, GOLD, SILVER, OIL, GAS, BTC, COPPER, PALLADIUM, PLATINUM, USDE, USA500, USA100
hl:vntl        15 mkts  OI $             0  24h $             0  [SUNSET]
             SPACEX, OPENAI, ANTHROPIC, MAG7, SEMIS, ROBOT, INFOTECH, NUCLEAR, DEFENSE, ENERGY, BIOTECH, GOLDJM, SILVERJM, WHEAT, SOY
hl:hyna        25 mkts  OI $             0  24h $             0
             BTC, ETH, HYPE, SOL, LIT, ZEC, XRP, LIGHTER, BNB, DOGE, SUI, PUMP, FARTCOIN, ENA, XMR, LTC, LINK, XPL
hl:km          23 mkts  OI $             0  24h $             0
             US500, BABA, EUR, USBOND, SMALL2000, USTECH, USENERGY, USOIL, TSLA, SILVER, GOLD, AAPL, GOOGL, SEMI, GLDMINE, NVDA, TENCENT, JPN225
hl:abcd         1 mkts  OI $             0  24h $             0
             USA500
hl:cash        17 mkts  OI $             0  24h $             0
             USA500, TSLA, NVDA, HOOD, GOOGL, INTC, AMZN, MSFT, META, GOLD, SILVER, EWY, WTI, BTC, KWEB, ETH, CAR

total 333 builder markets across 10 dexs
```

## Offchain reference rates (FRED)
```
OFFCHAIN REFERENCE RATES (FRED)

  SOFR      3.91%  2026-11-19     +1bp   Secured Overnight Financing Rate (what a desk funds at)
  DFF       3.88%  2026-11-19     +0bp   Effective fed funds
  IORB      3.90%  2026-11-23     +0bp   Interest on reserve balances
  DGS3MO    4.34%  2026-11-19     +0bp   3-month Treasury
  DGS10     5.04%  2026-11-19     -3bp   10-year Treasury
```

## Carry: funding vs borrow
```
PERP FUNDING (annualized from 8h feed) vs ONCHAIN BORROW

asset        lighter  hyperliq   binance     bybit  aave brw  aave sup
----------------------------------------------------------------------
BTC            10.5%      1.1%     -0.2%     -6.0%     0.00%     0.00%
ETH             0.9%     -1.2%      3.4%     -0.7%     0.00%     0.00%
SOL           -19.3%    -14.7%    -12.5%    -12.8%         -         -
ENA            10.5%     10.9%      4.8%     10.9%         -         -
HYPE           10.5%     10.9%      3.4%      3.3%         -         -
LINK          -21.9%      6.5%      1.2%      4.0%     0.00%     0.00%
AVAX            5.3%    -16.4%     -9.0%    -12.0%         -         -
DOGE           10.5%      9.8%      7.2%     10.9%         -         -

STABLE BORROW COST (the cost of carrying a hedged position)
  aave   USDe     borrow  0.00%  supply  0.00%
  aave   USDC     borrow  3.64%  supply  2.39%
  aave   RLUSD    borrow  3.76%  supply  2.21%
  aave   USDC     borrow  3.78%  supply  2.57%
  aave   GHO      borrow  3.80%  supply  2.86%
  aave   GHO      borrow  4.06%  supply  3.26%
  aave   GHO      borrow  4.36%  supply  3.33%
  aave   RLUSD    borrow  4.41%  supply  3.71%
  morpho    cbBTC/USDC    borrow  3.97%  lltv 0.86  $271,917,714
  morpho     kBTC/RLUSD   borrow  3.31%  lltv 0.86  $161,905,133
  morpho     WBTC/USDC    borrow  3.97%  lltv 0.86  $156,530,618
  morpho PT-reUSD-10DEC2026/USDC    borrow  9.12%  lltv 0.92  $130,418,520
  morpho    PRIME/PYUSD   borrow  6.21%  lltv 0.86  $128,537,142
  morpho   wstETH/USDT    borrow  3.54%  lltv 0.86  $120,046,048

OFFCHAIN BENCHMARK: SOFR 3.91% (2026-11-19)
  BTC perp funding 10.51% vs SOFR 3.91%: spread +6.60pp over the offchain cost of money

BUILDER-DEPLOYED PERPS: 333 markets, 175 with volume today
  xyz:NVDA         OI $  501,730,952  funding      5.5%/yr
  xyz:SP500        OI $  485,212,729  funding      5.5%/yr
  xyz:XYZ100       OI $  359,991,130  funding      5.5%/yr
  xyz:BRENTOIL     OI $  304,808,734  funding      5.5%/yr
  xyz:GOLD         OI $  257,096,675  funding      5.5%/yr
  xyz:SKHX         OI $  253,521,101  funding      7.5%/yr
  xyz:ANT          OI $  237,421,700  funding    111.4%/yr
  xyz:SILVER       OI $  174,251,471  funding     25.3%/yr
  xyz:MU           OI $  145,883,532  funding      5.5%/yr
  xyz:CL           OI $  134,981,669  funding      5.5%/yr
```
