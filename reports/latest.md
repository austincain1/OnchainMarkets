# 2026-11-17

## Market list changes
```
2026-11-16.json -> 2026-11-17.json

hl:abcd: no change (1 markets)
hl:cash: no change (17 markets)
hl:flx: no change (16 markets)
hl:hyna: no change (25 markets)
hl:io: no change (24 markets)
hl:km: no change (23 markets)
hl:mkts: no change (24 markets)
hl:para: no change (40 markets)
hl:vntl: no change (15 markets)
hl:xyz: no change (145 markets)
hyperliquid: no change (235 markets)
lighter: 235 -> 235
  NEW     (1): ANT
  REMOVED (1): BOTZ

variational: 590 -> 590
  NEW     (1): ANT
  REMOVED (1): ANTHROPIC

```

## Funding dispersion
```
205 symbols quoted on 2+ venues. Top 25 by dispersion.

sym             lighter  hyperliqu    binance      bybit     spread      ann  flag
----------------------------------------------------------------------------------
PRL             0.4720%          -    0.0100%    0.0100%    0.4620%      506%/yr
FOLKS           0.1448%          -    0.0100%    0.0100%    0.1348%      148%/yr
SKY             0.0096%   -0.0674%    0.0051%   -0.0338%    0.0770%       84%/yr  SIGN SPLIT
BABA            0.0760%          -    0.0000%    0.0000%    0.0760%       83%/yr
CASHCAT         0.0096%    0.0100%          -   -0.0654%    0.0754%       83%/yr  SIGN SPLIT
BB              0.0032%          -    0.0015%   -0.0715%    0.0747%       82%/yr  SIGN SPLIT
LIT            -0.0464%   -0.0602%   -0.0158%    0.0085%    0.0687%       75%/yr  SIGN SPLIT
AVNT           -0.0360%   -0.0561%   -0.0007%    0.0100%    0.0661%       72%/yr  SIGN SPLIT
ICP            -0.0008%   -0.0590%   -0.0132%   -0.0204%    0.0582%       64%/yr
OP              0.0096%   -0.0482%   -0.0332%   -0.0020%    0.0578%       63%/yr  SIGN SPLIT
ZORA           -0.0576%   -0.0476%   -0.0005%   -0.0102%    0.0571%       63%/yr
1000BONK        0.0096%   -0.0441%   -0.0050%   -0.0041%    0.0537%       59%/yr  SIGN SPLIT
SKHYNIX               -    0.1383%    0.0873%    0.1099%    0.0510%       56%/yr
MNT             0.0096%   -0.0402%          -    0.0100%    0.0502%       55%/yr  SIGN SPLIT
MON            -0.0168%    0.0068%   -0.0106%   -0.0407%    0.0475%       52%/yr  SIGN SPLIT
BERA           -0.0600%   -0.0557%   -0.0977%   -0.0514%    0.0463%       51%/yr
XPT             0.0528%    0.0334%    0.0787%          -    0.0453%       50%/yr
SOXS                  -          -   -0.0436%    0.0000%    0.0436%       48%/yr
FIL             0.0072%   -0.0316%   -0.0055%    0.0097%    0.0412%       45%/yr  SIGN SPLIT
CXMT           -0.0224%          -    0.0074%    0.0186%    0.0410%       45%/yr  SIGN SPLIT
TTWO            0.0032%          -    0.0249%    0.0441%    0.0409%       45%/yr
ETHFI          -0.0160%    0.0100%   -0.0042%   -0.0304%    0.0404%       44%/yr  SIGN SPLIT
1000SHIB        0.0096%   -0.0005%   -0.0305%   -0.0011%    0.0401%       44%/yr  SIGN SPLIT
WLD            -0.0032%    0.0100%   -0.0290%   -0.0232%    0.0390%       43%/yr  SIGN SPLIT
GMX             0.0096%    0.0100%    0.0016%   -0.0278%    0.0378%       41%/yr  SIGN SPLIT

62 symbols where one venue pays longs while another pays shorts:
  SKY, CASHCAT, BB, LIT, AVNT, OP, 1000BONK, MNT, MON, FIL, CXMT, ETHFI, 1000SHIB, WLD, GMX, POPCAT, JUP, STABLE, APT, VIRTUAL, MEGA, CC, MET, WIF, GRASS, POL, ZRO, SEI, KAITO, EDGE, SUI, ADA, LDO, PYTH, TRUMP, CRV, WLFI, STRK, NEAR, 1000PEPE
```

## Builder-deployed markets
```
hl:xyz        145 mkts  OI $ 4,148,815,965  24h $ 4,235,371,879
             XYZ100, TSLA, NVDA, GOLD, HOOD, INTC, PLTR, COIN, META, AAPL, MSFT, ORCL, GOOGL, AMZN, AMD, MU, SNDK, MSTR
hl:io          24 mkts  OI $   229,263,669  24h $    86,284,369
             OAI, ANTH, SNDK, IONQ, NBIS, EWY, GPRO, SBE, TCNT, DRAM, PRL, XIAOMI, H100, MOONSHOT, NVDA, SKHX, AAPL, CRCL
hl:para        40 mkts  OI $    14,185,065  24h $     4,667,358
             TOTAL2, OTHERS, BTCD, H100, AVGO, COHR, GLW, CRDO, LRCX, NET, STX, IREN, VST, TER, AAOI, 10Y, CIEN, NAVER
hl:mkts        24 mkts  OI $       314,543  24h $       279,612
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

total 330 builder markets across 10 dexs
```

## Offchain reference rates (FRED)
```
OFFCHAIN REFERENCE RATES (FRED)

  SOFR      3.93%  2026-11-16     +3bp   Secured Overnight Financing Rate (what a desk funds at)
  DFF       3.88%  2026-11-13     +0bp   Effective fed funds
  IORB      3.90%  2026-11-17     +0bp   Interest on reserve balances
  DGS3MO    4.32%  2026-11-13     +0bp   3-month Treasury
  DGS10     5.15%  2026-11-13     +5bp   10-year Treasury
```

## Carry: funding vs borrow
```
PERP FUNDING (annualized from 8h feed) vs ONCHAIN BORROW

asset        lighter  hyperliq   binance     bybit  aave brw  aave sup
----------------------------------------------------------------------
BTC            10.5%      9.2%      2.8%      2.2%     0.00%     0.00%
ETH             7.9%     -7.9%      0.9%     -2.8%     0.00%     0.00%
SOL            -0.9%    -12.5%     -7.5%    -22.5%         -         -
ENA            10.5%     10.9%      6.8%     10.2%         -         -
HYPE           10.5%     10.9%     10.9%     -5.2%         -         -
LINK            5.3%     10.9%      6.4%      2.9%     0.00%     0.00%
AVAX           10.5%     -0.1%      1.4%     -5.4%         -         -
DOGE           10.5%      3.4%     -6.9%     -0.8%         -         -

STABLE BORROW COST (the cost of carrying a hedged position)
  aave   USDe     borrow  0.00%  supply  0.00%
  aave   USDC     borrow  3.78%  supply  2.57%
  aave   GHO      borrow  3.84%  supply  2.92%
  aave   RLUSD    borrow  3.92%  supply  2.79%
  aave   GHO      borrow  3.92%  supply  3.04%
  aave   GHO      borrow  4.35%  supply  3.32%
  aave   USDC     borrow  4.55%  supply  3.35%
  aave   USDC     borrow  4.73%  supply  3.27%
  morpho    cbBTC/USDC    borrow  5.10%  lltv 0.86  $334,342,657
  morpho    PRIME/PYUSD   borrow  5.90%  lltv 0.86  $180,630,510
  morpho     kBTC/RLUSD   borrow  3.30%  lltv 0.86  $167,434,711
  morpho PT-reUSD-10DEC2026/USDC    borrow  9.48%  lltv 0.92  $141,838,747
  morpho     WBTC/USDC    borrow  5.11%  lltv 0.86  $123,194,063
  morpho   wstETH/USDT    borrow  3.60%  lltv 0.86  $120,459,303

OFFCHAIN BENCHMARK: SOFR 3.93% (2026-11-16)
  BTC perp funding 10.51% vs SOFR 3.93%: spread +6.58pp over the offchain cost of money

BUILDER-DEPLOYED PERPS: 330 markets, 172 with volume today
  xyz:NVDA         OI $  459,472,088  funding     13.4%/yr
  xyz:SP500        OI $  450,854,121  funding      5.5%/yr
  xyz:BRENTOIL     OI $  331,774,479  funding     10.5%/yr
  xyz:SKHX         OI $  283,564,948  funding    145.3%/yr
  xyz:GOLD         OI $  262,198,118  funding     13.8%/yr
  xyz:XYZ100       OI $  260,217,531  funding      5.5%/yr
  io:ANTH          OI $  197,686,960  funding     -5.6%/yr
  xyz:MU           OI $  141,633,410  funding      5.5%/yr
  xyz:ANT          OI $  139,972,582  funding     -0.4%/yr
  xyz:GOOGL        OI $  136,976,139  funding      5.5%/yr
```
