# 2026-11-11

## Market list changes
```
2026-11-10.json -> 2026-11-11.json

hl:abcd: no change (1 markets)
hl:cash: no change (17 markets)
hl:flx: no change (16 markets)
hl:hyna: no change (25 markets)
hl:io: 21 -> 22
  NEW     (1): io:INTC

hl:km: no change (23 markets)
hl:mkts: no change (24 markets)
hl:para: no change (40 markets)
hl:vntl: no change (15 markets)
hl:xyz: no change (144 markets)
hyperliquid: no change (235 markets)
lighter: no change (235 markets)
variational: no change (590 markets)
```

## Funding dispersion
```
204 symbols quoted on 2+ venues. Top 25 by dispersion.

sym             lighter  hyperliqu    binance      bybit     spread      ann  flag
----------------------------------------------------------------------------------
CXMT           -0.0360%          -    0.1091%    0.0000%    0.1451%      159%/yr  SIGN SPLIT
AVAX           -0.1304%   -0.0461%    0.0025%   -0.0173%    0.1329%      146%/yr  SIGN SPLIT
SKHYNIX               -   -0.0730%    0.0537%    0.0020%    0.1268%      139%/yr  SIGN SPLIT
PRL             0.1232%          -    0.0100%    0.0100%    0.1132%      124%/yr
NATGAS          1.0600%    1.1118%    1.0000%          -    0.1118%      122%/yr
BRENTOIL       -0.1712%   -0.2173%   -0.2729%          -    0.1017%      111%/yr
SAMSUNG               -   -0.0429%    0.0510%    0.0000%    0.0939%      103%/yr  SIGN SPLIT
FOLKS           0.1016%          -    0.0100%    0.0100%    0.0916%      100%/yr
PONS            0.0096%    0.0100%    0.0100%   -0.0744%    0.0844%       92%/yr  SIGN SPLIT
ETHFI           0.0096%    0.0100%    0.0100%   -0.0715%    0.0815%       89%/yr  SIGN SPLIT
ZORA           -0.0672%    0.0100%    0.0100%    0.0100%    0.0772%       85%/yr  SIGN SPLIT
BERA            0.0040%   -0.0646%   -0.0017%    0.0100%    0.0746%       82%/yr  SIGN SPLIT
MET             0.0096%   -0.0047%   -0.0316%   -0.0634%    0.0730%       80%/yr  SIGN SPLIT
WTI            -0.1208%   -0.1256%   -0.1761%   -0.1903%    0.0695%       76%/yr
UNITREE         0.0032%          -    0.0000%   -0.0658%    0.0690%       76%/yr  SIGN SPLIT
MEGA            0.0096%    0.0100%    0.0100%   -0.0588%    0.0688%       75%/yr  SIGN SPLIT
PYTH            0.0096%    0.0100%   -0.0043%   -0.0547%    0.0647%       71%/yr  SIGN SPLIT
DRV             0.0712%          -          -    0.0100%    0.0612%       67%/yr
XCU             0.0824%    0.1369%    0.1173%          -    0.0545%       60%/yr
SKR             0.0096%    0.0100%    0.0100%   -0.0428%    0.0528%       58%/yr  SIGN SPLIT
JUP            -0.0216%   -0.0743%   -0.0267%   -0.0649%    0.0527%       58%/yr
1000PEPE        0.0096%    0.0100%   -0.0107%   -0.0403%    0.0503%       55%/yr  SIGN SPLIT
CC              0.0096%   -0.0388%    0.0100%    0.0100%    0.0488%       53%/yr  SIGN SPLIT
NMR             0.0096%          -   -0.0364%    0.0100%    0.0464%       51%/yr  SIGN SPLIT
BIRB                  -          -   -0.0358%    0.0100%    0.0458%       50%/yr  SIGN SPLIT

53 symbols where one venue pays longs while another pays shorts:
  CXMT, AVAX, SKHYNIX, SAMSUNG, PONS, ETHFI, ZORA, BERA, MET, UNITREE, MEGA, PYTH, SKR, 1000PEPE, CC, NMR, BIRB, DYDX, ROBO, VVV, GRAM, EIGEN, MORPHO, 0G, POL, AAPL, WLD, PENGU, ZK, APT, ONDO, SUI, ARB, AMD, GMX, HBAR, SPX, ASTER, AAVE, TRX
```

## Builder-deployed markets
```
hl:xyz        144 mkts  OI $ 4,440,234,119  24h $ 3,917,509,027
             XYZ100, TSLA, NVDA, GOLD, HOOD, INTC, PLTR, COIN, META, AAPL, MSFT, ORCL, GOOGL, AMZN, AMD, MU, SNDK, MSTR
hl:io          22 mkts  OI $   236,247,251  24h $   112,176,092
             OAI, ANTH, SNDK, IONQ, NBIS, EWY, GPRO, SBE, TCNT, DRAM, PRL, XIAOMI, H100, MOONSHOT, NVDA, SKHX, AAPL, CRCL
hl:para        40 mkts  OI $    15,906,605  24h $     6,478,081
             TOTAL2, OTHERS, BTCD, H100, AVGO, COHR, GLW, CRDO, LRCX, NET, STX, IREN, VST, TER, AAOI, 10Y, CIEN, NAVER
hl:mkts        24 mkts  OI $       190,918  24h $       110,368
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

total 327 builder markets across 10 dexs
```

## Offchain reference rates (FRED)
```
OFFCHAIN REFERENCE RATES (FRED)

  SOFR      3.88%  2026-11-09     -1bp   Secured Overnight Financing Rate (what a desk funds at)
  DFF       3.88%  2026-11-09     +0bp   Effective fed funds
  IORB      3.90%  2026-11-12     +0bp   Interest on reserve balances
  DGS3MO    4.24%  2026-11-09     +5bp   3-month Treasury
  DGS10     4.88%  2026-11-09     +2bp   10-year Treasury
```

## Carry: funding vs borrow
```
PERP FUNDING (annualized from 8h feed) vs ONCHAIN BORROW

asset        lighter  hyperliq   binance     bybit  aave brw  aave sup
----------------------------------------------------------------------
BTC            10.5%      8.0%      5.1%      6.2%     0.00%     0.00%
ETH             0.0%     10.9%      7.0%     10.9%     0.00%     0.00%
SOL             4.4%      6.5%      4.5%      5.7%         -         -
ENA            10.5%     10.9%     10.9%     10.9%         -         -
HYPE           10.5%     10.9%     10.9%     -0.4%         -         -
LINK           10.5%     10.9%     10.9%      4.0%     0.00%     0.00%
AVAX         -142.8%    -50.5%      2.8%    -18.9%         -         -
DOGE            3.5%     -0.4%      4.0%     -5.7%         -         -

STABLE BORROW COST (the cost of carrying a hedged position)
  aave   USDe     borrow  0.00%  supply  0.00%
  aave   RLUSD    borrow  3.14%  supply  1.76%
  aave   RLUSD    borrow  3.61%  supply  2.03%
  aave   USDC     borrow  3.90%  supply  2.73%
  aave   GHO      borrow  4.06%  supply  3.27%
  aave   USDC     borrow  4.49%  supply  3.27%
  aave   GHO      borrow  4.53%  supply  3.60%
  aave   USDC     borrow  4.55%  supply  3.72%
  morpho    cbBTC/USDC    borrow  5.18%  lltv 0.86  $349,399,989
  morpho     kBTC/RLUSD   borrow  3.72%  lltv 0.86  $255,137,391
  morpho    PRIME/PYUSD   borrow  5.27%  lltv 0.86  $194,241,437
  morpho PT-reUSD-10DEC2026/USDC    borrow  9.21%  lltv 0.92  $153,522,836
  morpho     WBTC/USDC    borrow  5.20%  lltv 0.86  $140,755,162
  morpho   wstETH/USDT    borrow  3.68%  lltv 0.86  $128,118,386

OFFCHAIN BENCHMARK: SOFR 3.88% (2026-11-09)
  BTC perp funding 10.51% vs SOFR 3.88%: spread +6.63pp over the offchain cost of money

BUILDER-DEPLOYED PERPS: 327 markets, 171 with volume today
  xyz:SP500        OI $  463,997,730  funding      1.4%/yr
  xyz:NVDA         OI $  356,474,842  funding      9.6%/yr
  xyz:SKHX         OI $  322,705,969  funding    -79.5%/yr
  xyz:BRENTOIL     OI $  313,840,302  funding   -237.9%/yr
  xyz:GOLD         OI $  297,226,484  funding     18.8%/yr
  xyz:XYZ100       OI $  218,620,949  funding      3.0%/yr
  io:ANTH          OI $  203,062,903  funding      1.4%/yr
  xyz:SILVER       OI $  200,118,149  funding      8.9%/yr
  xyz:GOOGL        OI $  184,983,522  funding      5.5%/yr
  xyz:MU           OI $  171,540,515  funding      5.5%/yr
```
