# 2026-10-28

## Market list changes
```
2026-10-27.json -> 2026-10-28.json

hl:abcd: no change (1 markets)
hl:cash: no change (17 markets)
hl:flx: no change (16 markets)
hl:hyna: no change (25 markets)
hl:io: no change (16 markets)
hl:km: no change (23 markets)
hl:mkts: no change (24 markets)
hl:para: no change (39 markets)
hl:vntl: no change (15 markets)
hl:xyz: 139 -> 140
  NEW     (1): xyz:NU

hyperliquid: no change (235 markets)
lighter: no change (235 markets)
variational: 582 -> 583
  NEW     (2): AMC, BAC
  REMOVED (1): VELODROME

```

## Funding dispersion
```
205 symbols quoted on 2+ venues. Top 25 by dispersion.

sym             lighter  hyperliqu    binance      bybit     spread      ann  flag
----------------------------------------------------------------------------------
PRL             0.6016%          -    0.0100%    0.0100%    0.5916%      648%/yr
CASHCAT        -0.3104%    0.0100%          -    0.0100%    0.3204%      351%/yr  SIGN SPLIT
BIRB                  -          -   -0.0186%   -0.2155%    0.1970%      216%/yr
CXMT            0.0688%          -    0.1041%    0.2548%    0.1860%      204%/yr
SKHYNIX               -    0.2658%    0.1125%    0.0866%    0.1792%      196%/yr
EDGE                  -          -    0.0100%   -0.1361%    0.1461%      160%/yr  SIGN SPLIT
HYUNDAI               -    0.1361%    0.0000%    0.0000%    0.1361%      149%/yr
CHIP            0.0096%    0.0100%   -0.0003%   -0.1118%    0.1218%      133%/yr  SIGN SPLIT
SAMSUNG               -    0.1029%    0.0000%    0.0000%    0.1029%      113%/yr
TTWO            0.0520%          -    0.0322%    0.1125%    0.0802%       88%/yr
USDJPY          0.0000%   -0.0118%          -   -0.0752%    0.0752%       82%/yr
UNITREE         0.0032%          -    0.0000%   -0.0716%    0.0748%       82%/yr  SIGN SPLIT
STRC           -0.0816%          -   -0.0102%          -    0.0714%       78%/yr
GEV             0.0032%          -    0.0137%    0.0683%    0.0651%       71%/yr
APEX            0.0096%    0.0724%          -    0.0100%    0.0628%       69%/yr
MON            -0.0320%    0.0100%   -0.0357%   -0.0513%    0.0613%       67%/yr  SIGN SPLIT
SKR             0.0096%    0.0100%    0.0100%   -0.0426%    0.0526%       58%/yr  SIGN SPLIT
WTI            -0.0216%   -0.0140%   -0.0405%   -0.0657%    0.0517%       57%/yr
RIVER           0.0096%          -    0.0356%    0.0595%    0.0499%       55%/yr
FOLKS           0.0096%          -    0.0100%    0.0590%    0.0495%       54%/yr
XPT             0.0488%    0.0263%    0.0000%          -    0.0488%       53%/yr
XLM             0.0096%   -0.0038%   -0.0042%   -0.0392%    0.0488%       53%/yr  SIGN SPLIT
AERO            0.0096%    0.0100%    0.0100%   -0.0359%    0.0459%       50%/yr  SIGN SPLIT
LINEA           0.0096%    0.0100%    0.0100%   -0.0345%    0.0445%       49%/yr  SIGN SPLIT
NMR             0.0096%          -   -0.0349%   -0.0134%    0.0445%       49%/yr  SIGN SPLIT

53 symbols where one venue pays longs while another pays shorts:
  CASHCAT, EDGE, CHIP, UNITREE, MON, SKR, XLM, AERO, LINEA, NMR, PENGU, TRUMP, BERA, MNT, ADA, VIRTUAL, FIL, JTO, PYTH, DIA, VVV, BCH, TRX, ZK, DOT, AVNT, HBAR, MORPHO, AXS, DYDX, SEI, WLD, CC, SUI, AVAX, GRAM, ENA, EIGEN, LTC, JUP
```

## Builder-deployed markets
```
hl:xyz        140 mkts  OI $ 4,054,779,840  24h $ 2,979,948,245
             XYZ100, TSLA, NVDA, GOLD, HOOD, INTC, PLTR, COIN, META, AAPL, MSFT, ORCL, GOOGL, AMZN, AMD, MU, SNDK, MSTR
hl:io          16 mkts  OI $    87,951,299  24h $    45,883,778
             OAI, ANTH, SNDK, IONQ, NBIS, EWY, GPRO, SBE, TCNT, DRAM, PRL, XIAOMI, H100, MOONSHOT, NVDA, SKHX
hl:para        39 mkts  OI $    16,669,154  24h $     5,571,396
             TOTAL2, OTHERS, BTCD, H100, AVGO, COHR, GLW, CRDO, LRCX, NET, STX, IREN, VST, TER, AAOI, 10Y, CIEN, NAVER
hl:mkts        24 mkts  OI $     8,245,917  24h $     1,550,496
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

total 316 builder markets across 10 dexs
```

## Offchain reference rates (FRED)
```
OFFCHAIN REFERENCE RATES (FRED)

  SOFR      3.95%  2026-10-27     +2bp   Secured Overnight Financing Rate (what a desk funds at)
  DFF       3.88%  2026-10-26     +0bp   Effective fed funds
  IORB      3.90%  2026-10-28     +0bp   Interest on reserve balances
  DGS3MO    4.22%  2026-10-26     +0bp   3-month Treasury
  DGS10     5.00%  2026-10-26     +0bp   10-year Treasury
```

## Carry: funding vs borrow
```
PERP FUNDING (annualized from 8h feed) vs ONCHAIN BORROW

asset        lighter  hyperliq   binance     bybit  aave brw  aave sup
----------------------------------------------------------------------
BTC            10.5%     10.9%     10.6%      8.9%     0.00%     0.00%
ETH            10.5%      8.6%      9.6%     10.9%     0.00%     0.00%
SOL            10.5%     10.9%     10.9%      9.9%         -         -
ENA            10.5%      3.1%     -8.5%     10.9%         -         -
HYPE           10.5%      1.9%     10.9%     -0.3%         -         -
LINK           10.5%     10.9%     10.0%     10.9%     0.00%     0.00%
AVAX           10.5%     -0.5%      2.8%     -9.4%         -         -
DOGE           10.5%     10.9%     10.9%      3.3%         -         -

STABLE BORROW COST (the cost of carrying a hedged position)
  aave   USDe     borrow  0.00%  supply  0.00%
  aave   RLUSD    borrow  0.63%  supply  0.02%
  aave   RLUSD    borrow  3.20%  supply  1.60%
  aave   GHO      borrow  3.93%  supply  3.05%
  aave   USDC     borrow  4.07%  supply  2.98%
  aave   GHO      borrow  4.08%  supply  3.30%
  aave   GHO      borrow  4.53%  supply  3.60%
  aave   USDC     borrow  4.65%  supply  3.50%
  morpho    cbBTC/USDC    borrow  5.01%  lltv 0.86  $343,918,173
  morpho     kBTC/RLUSD   borrow  4.69%  lltv 0.86  $259,032,641
  morpho    PRIME/PYUSD   borrow  5.12%  lltv 0.86  $207,056,456
  morpho PT-reUSD-10DEC2026/USDC    borrow 10.97%  lltv 0.92  $137,676,544
  morpho     WBTC/USDC    borrow  5.04%  lltv 0.86  $128,498,377
  morpho     kBTC/PYUSD   borrow  4.22%  lltv 0.86  $126,421,832

OFFCHAIN BENCHMARK: SOFR 3.95% (2026-10-27)
  BTC perp funding 10.51% vs SOFR 3.95%: spread +6.56pp over the offchain cost of money

BUILDER-DEPLOYED PERPS: 316 markets, 169 with volume today
  xyz:SP500        OI $  419,710,319  funding     -0.8%/yr
  xyz:SKHX         OI $  326,293,976  funding    290.3%/yr
  xyz:GOLD         OI $  319,627,436  funding     16.3%/yr
  xyz:XYZ100       OI $  299,260,903  funding      5.5%/yr
  xyz:CL           OI $  260,794,365  funding    -15.1%/yr
  xyz:BRENTOIL     OI $  218,672,430  funding     -8.0%/yr
  xyz:SILVER       OI $  168,234,889  funding      7.5%/yr
  xyz:SPCX         OI $  160,751,128  funding     16.0%/yr
  xyz:GOOGL        OI $  140,072,572  funding      9.2%/yr
  xyz:SKHY         OI $  139,178,730  funding    -12.3%/yr
```
