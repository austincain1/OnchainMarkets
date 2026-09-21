# 2026-09-21

## Market list changes
```
2026-09-20.json -> 2026-09-21.json

hyperliquid: no change (234 markets)
lighter: no change (235 markets)
variational: no change (552 markets)
```

## Funding dispersion
```
207 symbols quoted on 2+ venues. Top 25 by dispersion.

sym             lighter  hyperliqu    binance      bybit     spread      ann  flag
----------------------------------------------------------------------------------
AI              0.8472%    0.0000%    0.0000%          -    0.8472%      928%/yr
PROVE          -0.3544%   -0.7688%   -0.6741%   -0.9973%    0.6429%      704%/yr
STONK           0.6032%          -          -    0.2154%    0.3878%      425%/yr
BIRB                  -          -    0.0100%    0.3948%    0.3848%      421%/yr
TAO             0.1544%    0.2171%    0.0100%    0.0100%    0.2071%      227%/yr
MINIMAX         0.0032%          -    0.2078%    0.0848%    0.2046%      224%/yr
AERO            0.1968%    0.0532%    0.0100%    0.0100%    0.1868%      205%/yr
NEAR            0.1952%    0.1196%    0.0100%    0.0097%    0.1855%      203%/yr
GRASS           0.1840%    0.0100%    0.0137%    0.0100%    0.1740%      191%/yr
WLD             0.1728%    0.0659%    0.0100%    0.0100%    0.1628%      178%/yr
XMR             0.0144%    0.1597%    0.0331%    0.0100%    0.1497%      164%/yr
MEGA            0.1528%    0.0858%    0.0100%    0.0100%    0.1428%      156%/yr
APEX            0.1392%    0.1523%          -    0.0100%    0.1423%      156%/yr
CC              0.1480%    0.0841%    0.0100%    0.0100%    0.1380%      151%/yr
CASHCAT         0.1448%    0.0100%          -    0.0246%    0.1348%      148%/yr
USELESS         0.0096%    0.1369%    0.0535%    0.1222%    0.1273%      139%/yr
RIVER           0.0096%          -    0.0721%    0.1367%    0.1271%      139%/yr
KAITO           0.1336%    0.0763%    0.0100%    0.0100%    0.1236%      135%/yr
1000BONK        0.0096%    0.1296%    0.0100%    0.0100%    0.1200%      131%/yr
SKHYNIX               -    0.1282%    0.0143%    0.0376%    0.1139%      125%/yr
UNI             0.1112%    0.0907%    0.0100%    0.0054%    0.1058%      116%/yr
ARC             0.0096%          -    0.0297%    0.1151%    0.1055%      116%/yr
FARTCOIN        0.0584%    0.1194%    0.0201%    0.0312%    0.0993%      109%/yr
UNITREE         0.0984%          -    0.0127%    0.0000%    0.0984%      108%/yr
BB              0.1064%          -    0.0100%    0.0100%    0.0964%      106%/yr

18 symbols where one venue pays longs while another pays shorts:
  1000PEPE, XPL, MORPHO, LIT, BOT, FF, PENGU, CAP, SKY, ARB, ZEC, BRENTOIL, PYTH, BCH, MON, TRX, PENDLE, XPD
```

## Builder-deployed markets
```
hl:xyz        123 mkts  OI $ 3,923,833,632  24h $ 2,647,919,032
             XYZ100, TSLA, NVDA, GOLD, HOOD, INTC, PLTR, COIN, META, AAPL, MSFT, ORCL, GOOGL, AMZN, AMD, MU, SNDK, MSTR
hl:io          10 mkts  OI $    58,077,375  24h $    65,006,853
             OAI, ANTH, SNDK, IONQ, NBIS, EWY, GPRO, SBE, TCNT, DRAM
hl:para        36 mkts  OI $    18,280,945  24h $     6,858,874
             TOTAL2, OTHERS, BTCD, H100, AVGO, COHR, GLW, CRDO, LRCX, NET, STX, IREN, VST, TER, AAOI, 10Y, CIEN, NAVER
hl:mkts        24 mkts  OI $     6,657,672  24h $    13,013,724
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

total 290 builder markets across 10 dexs
```

## Offchain reference rates (FRED)
```
OFFCHAIN REFERENCE RATES (FRED)

  SOFR      3.85%  2026-09-18     +0bp   Secured Overnight Financing Rate (what a desk funds at)
  DFF       3.88%  2026-09-18     +0bp   Effective fed funds
  IORB      3.90%  2026-09-22     +0bp   Interest on reserve balances
  DGS3MO    4.14%  2026-09-18     +2bp   3-month Treasury
  DGS10     5.01%  2026-09-18     +7bp   10-year Treasury
```

## Carry: funding vs borrow
```
PERP FUNDING (annualized from 8h feed) vs ONCHAIN BORROW

asset        lighter  hyperliq   binance     bybit  aave brw  aave sup
----------------------------------------------------------------------
BTC            10.5%     10.9%      7.8%     10.9%     0.00%     0.00%
ETH            10.5%     10.9%      7.3%     10.0%     0.00%     0.00%
SOL            10.5%     10.9%     10.9%     10.9%         -         -
ENA            70.1%     92.3%     10.9%     10.9%         -         -
HYPE           10.5%     75.4%      8.6%      2.4%         -         -
LINK           10.5%     31.4%     10.9%     10.9%     0.00%     0.00%
AVAX           10.5%     91.4%     10.9%     10.9%         -         -
DOGE           10.5%     99.1%     10.9%     10.9%         -         -

STABLE BORROW COST (the cost of carrying a hedged position)
  aave   RLUSD    borrow  1.70%  supply  0.47%
  aave   USDT     borrow  2.21%  supply  1.01%
  aave   USDC     borrow  3.15%  supply  2.05%
  aave   GHO      borrow  3.49%  supply  2.20%
  aave   USDC     borrow  3.71%  supply  2.40%
  aave   GHO      borrow  3.78%  supply  2.90%
  aave   GHO      borrow  3.99%  supply  3.22%
  aave   USDT     borrow  3.99%  supply  3.31%
  morpho    cbBTC/USDC    borrow  4.61%  lltv 0.86  $346,317,388
  morpho     kBTC/RLUSD   borrow  3.49%  lltv 0.86  $219,992,313
  morpho    PRIME/PYUSD   borrow  4.72%  lltv 0.86  $182,520,197
  morpho     kBTC/PYUSD   borrow  4.13%  lltv 0.86  $159,910,214
  morpho     WBTC/USDC    borrow  5.94%  lltv 0.86  $125,837,183
  morpho   wstETH/USDT    borrow  9.46%  lltv 0.86  $122,459,996

OFFCHAIN BENCHMARK: SOFR 3.85% (2026-09-18)
  BTC perp funding 10.51% vs SOFR 3.85%: spread +6.66pp over the offchain cost of money

BUILDER-DEPLOYED PERPS: 290 markets, 148 with volume today
  xyz:SP500        OI $  436,190,524  funding      5.5%/yr
  xyz:SKHX         OI $  348,291,852  funding    138.5%/yr
  xyz:GOLD         OI $  293,800,290  funding      5.5%/yr
  xyz:XYZ100       OI $  213,402,347  funding      5.5%/yr
  xyz:CL           OI $  185,601,053  funding    -12.1%/yr
  xyz:MU           OI $  176,706,617  funding     34.5%/yr
  xyz:SILVER       OI $  165,491,323  funding      7.6%/yr
  xyz:SKHY         OI $  165,123,724  funding      3.1%/yr
  xyz:BRENTOIL     OI $  147,655,282  funding    -17.4%/yr
  xyz:NVDA         OI $  147,306,800  funding      5.5%/yr
```
