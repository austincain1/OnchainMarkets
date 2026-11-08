# 2026-11-08

## Market list changes
```
2026-11-07.json -> 2026-11-08.json

hl:abcd: no change (1 markets)
hl:cash: no change (17 markets)
hl:flx: no change (16 markets)
hl:hyna: no change (25 markets)
hl:io: 20 -> 21
  NEW     (1): io:META

hl:km: no change (23 markets)
hl:mkts: no change (24 markets)
hl:para: no change (40 markets)
hl:vntl: no change (15 markets)
hl:xyz: no change (143 markets)
hyperliquid: no change (235 markets)
lighter: no change (235 markets)
variational: no change (588 markets)
```

## Funding dispersion
```
205 symbols quoted on 2+ venues. Top 25 by dispersion.

sym             lighter  hyperliqu    binance      bybit     spread      ann  flag
----------------------------------------------------------------------------------
DRV             0.0096%          -          -   -0.4122%    0.4218%      462%/yr  SIGN SPLIT
STONK          -0.0904%          -          -    0.2105%    0.3009%      330%/yr  SIGN SPLIT
FOLKS           0.0104%          -    0.2483%    0.2728%    0.2624%      287%/yr
MSTR           -0.0848%   -0.1334%    0.0000%   -0.1501%    0.1501%      164%/yr
XMR             0.0096%    0.1183%    0.0100%    0.0101%    0.1087%      119%/yr
KORU            0.1040%          -    0.0000%    0.0691%    0.1040%      114%/yr
ENA             0.0096%    0.0100%   -0.0167%   -0.0936%    0.1036%      113%/yr  SIGN SPLIT
USDJPY          0.0000%    0.0000%          -   -0.1034%    0.1034%      113%/yr
RIVER           0.0504%          -    0.1472%    0.0692%    0.0968%      106%/yr
MEGA           -0.0736%    0.0100%    0.0100%   -0.0189%    0.0836%       92%/yr  SIGN SPLIT
SOXS            0.0032%          -    0.0821%    0.0000%    0.0821%       90%/yr
SOXL            0.0008%          -   -0.0799%   -0.0329%    0.0807%       88%/yr  SIGN SPLIT
AERO            0.0104%    0.0100%   -0.0691%    0.0100%    0.0795%       87%/yr  SIGN SPLIT
IREN            0.0032%          -    0.0000%    0.0724%    0.0724%       79%/yr
S              -0.0200%   -0.0919%   -0.0209%   -0.0374%    0.0719%       79%/yr
ARC             0.0096%          -    0.0100%    0.0778%    0.0682%       75%/yr
AZTEC          -0.0576%    0.0100%   -0.0155%   -0.0245%    0.0676%       74%/yr  SIGN SPLIT
SKHYNIX               -    0.0665%    0.0000%    0.0153%    0.0665%       73%/yr
INTC            0.0480%    0.0661%    0.0000%    0.0000%    0.0661%       72%/yr
XPL             0.0096%   -0.0557%    0.0100%   -0.0184%    0.0657%       72%/yr  SIGN SPLIT
CRCL           -0.0400%   -0.0651%    0.0000%   -0.0297%    0.0651%       71%/yr
COIN           -0.0360%   -0.0646%    0.0000%   -0.0121%    0.0646%       71%/yr
SKHY            0.0632%          -    0.0000%    0.0459%    0.0632%       69%/yr
XIAOMI          0.0032%          -          -   -0.0537%    0.0569%       62%/yr  SIGN SPLIT
PRL            -0.0448%          -    0.0100%    0.0100%    0.0548%       60%/yr  SIGN SPLIT

76 symbols where one venue pays longs while another pays shorts:
  DRV, STONK, ENA, MEGA, SOXL, AERO, AZTEC, XPL, XIAOMI, PRL, CRO, PENDLE, VIRTUAL, BB, SPCX, STRK, TAO, CHIP, MON, GMX, 1000BONK, WLD, MORPHO, DYDX, CC, 2Z, ARB, ADA, WLFI, BMNR, ETHFI, CRV, OP, GRAM, PUMP, EIGEN, LIT, TRX, ZEC, POL
```

## Builder-deployed markets
```
hl:xyz        143 mkts  OI $ 4,287,645,528  24h $   304,755,755
             XYZ100, TSLA, NVDA, GOLD, HOOD, INTC, PLTR, COIN, META, AAPL, MSFT, ORCL, GOOGL, AMZN, AMD, MU, SNDK, MSTR
hl:io          21 mkts  OI $   168,364,152  24h $    25,697,735
             OAI, ANTH, SNDK, IONQ, NBIS, EWY, GPRO, SBE, TCNT, DRAM, PRL, XIAOMI, H100, MOONSHOT, NVDA, SKHX, AAPL, CRCL
hl:para        40 mkts  OI $    15,930,833  24h $     1,051,400
             TOTAL2, OTHERS, BTCD, H100, AVGO, COHR, GLW, CRDO, LRCX, NET, STX, IREN, VST, TER, AAOI, 10Y, CIEN, NAVER
hl:mkts        24 mkts  OI $       172,989  24h $        74,564
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

total 325 builder markets across 10 dexs
```

## Offchain reference rates (FRED)
```
OFFCHAIN REFERENCE RATES (FRED)

  SOFR      3.92%  2026-11-05     -2bp   Secured Overnight Financing Rate (what a desk funds at)
  DFF       3.88%  2026-11-05     +0bp   Effective fed funds
  IORB      3.90%  2026-11-09     +0bp   Interest on reserve balances
  DGS3MO    4.17%  2026-11-05     -4bp   3-month Treasury
  DGS10     4.84%  2026-11-05     -6bp   10-year Treasury
```

## Carry: funding vs borrow
```
PERP FUNDING (annualized from 8h feed) vs ONCHAIN BORROW

asset        lighter  hyperliq   binance     bybit  aave brw  aave sup
----------------------------------------------------------------------
BTC            10.5%     10.9%      3.3%      7.2%     0.00%     0.00%
ETH             8.8%     10.9%      6.1%      0.1%     0.00%     0.00%
SOL            10.5%     -4.3%      8.1%     10.9%         -         -
ENA            10.5%     10.9%    -18.3%   -102.5%         -         -
HYPE           10.5%     -3.0%     10.9%     -7.7%         -         -
LINK            1.8%     10.9%      1.6%     -5.5%     0.00%     0.00%
AVAX            2.6%     -4.3%      7.0%     -9.3%         -         -
DOGE           10.5%     10.5%     10.5%      7.2%         -         -

STABLE BORROW COST (the cost of carrying a hedged position)
  aave   USDe     borrow  0.00%  supply  0.00%
  aave   RLUSD    borrow  3.61%  supply  2.03%
  aave   RLUSD    borrow  3.80%  supply  2.66%
  aave   USDC     borrow  3.81%  supply  2.61%
  aave   USDC     borrow  4.35%  supply  3.07%
  aave   GHO      borrow  4.53%  supply  3.60%
  aave   GHO      borrow  4.90%  supply  3.97%
  aave   USDC     borrow  5.52%  supply  4.57%
  morpho    cbBTC/USDC    borrow  6.19%  lltv 0.86  $336,101,336
  morpho     kBTC/RLUSD   borrow  3.67%  lltv 0.86  $255,102,022
  morpho    PRIME/PYUSD   borrow  8.45%  lltv 0.86  $184,466,864
  morpho PT-reUSD-10DEC2026/USDC    borrow  9.38%  lltv 0.92  $150,060,829
  morpho     WBTC/USDC    borrow  6.19%  lltv 0.86  $135,481,701
  morpho    sUSDe/PYUSD   borrow  4.25%  lltv 0.92  $115,006,449

OFFCHAIN BENCHMARK: SOFR 3.92% (2026-11-05)
  BTC perp funding 10.51% vs SOFR 3.92%: spread +6.59pp over the offchain cost of money

BUILDER-DEPLOYED PERPS: 325 markets, 168 with volume today
  xyz:BRENTOIL     OI $  392,932,771  funding     14.6%/yr
  xyz:SP500        OI $  388,710,629  funding      5.5%/yr
  xyz:SKHX         OI $  352,241,060  funding     80.8%/yr
  xyz:GOLD         OI $  301,114,903  funding     -9.9%/yr
  xyz:XYZ100       OI $  271,264,302  funding      5.5%/yr
  xyz:SILVER       OI $  205,416,585  funding    -38.6%/yr
  xyz:GOOGL        OI $  196,909,567  funding    -15.3%/yr
  xyz:MU           OI $  181,393,137  funding     42.8%/yr
  xyz:CL           OI $  180,489,317  funding     25.1%/yr
  xyz:SPCX         OI $  161,295,258  funding    -12.5%/yr
```
