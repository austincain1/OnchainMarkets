# 2026-10-12

## Market list changes
```
2026-10-11.json -> 2026-10-12.json

hl:abcd: no change (1 markets)
hl:cash: no change (17 markets)
hl:flx: no change (16 markets)
hl:hyna: no change (25 markets)
hl:io: no change (12 markets)
hl:km: no change (23 markets)
hl:mkts: no change (24 markets)
hl:para: no change (38 markets)
hl:vntl: no change (15 markets)
hl:xyz: no change (134 markets)
hyperliquid: no change (234 markets)
lighter: no change (235 markets)
variational: no change (568 markets)
```

## Funding dispersion
```
205 symbols quoted on 2+ venues. Top 25 by dispersion.

sym             lighter  hyperliqu    binance      bybit     spread      ann  flag
----------------------------------------------------------------------------------
PRL             0.6608%          -    0.0429%    0.0100%    0.6508%      713%/yr
CASHCAT         0.5712%    0.0100%          -    0.0100%    0.5612%      615%/yr
NATGAS          1.1456%    1.1639%    1.0000%          -    0.1639%      180%/yr
BRENTOIL       -0.3336%   -0.3594%   -0.4679%          -    0.1343%      147%/yr
RIVER          -0.1136%          -    0.0130%    0.0127%    0.1266%      139%/yr  SIGN SPLIT
CTR             0.0096%          -    0.1253%    0.0100%    0.1157%      127%/yr
STRC           -0.1024%          -   -0.0180%          -    0.0844%       92%/yr
PROVE          -0.0664%    0.0100%    0.0100%    0.0100%    0.0764%       84%/yr  SIGN SPLIT
PIPPIN                -          -    0.0776%    0.0100%    0.0676%       74%/yr
WTI            -0.1320%   -0.1156%   -0.1541%   -0.1742%    0.0587%       64%/yr
LITE            0.0520%          -    0.0000%    0.0000%    0.0520%       57%/yr
GRAM            0.0008%   -0.0201%   -0.0173%   -0.0511%    0.0519%       57%/yr  SIGN SPLIT
XPL            -0.0408%    0.0017%    0.0063%    0.0100%    0.0508%       56%/yr  SIGN SPLIT
JUP            -0.0256%    0.0100%   -0.0154%   -0.0387%    0.0487%       53%/yr  SIGN SPLIT
STBL            0.0096%    0.0315%    0.0100%    0.0575%    0.0479%       52%/yr
NBIS            0.0192%          -    0.0000%    0.0470%    0.0470%       51%/yr
MON             0.0096%    0.0100%   -0.0362%   -0.0187%    0.0462%       51%/yr  SIGN SPLIT
AVNT            0.0096%    0.0100%    0.0100%   -0.0355%    0.0455%       50%/yr  SIGN SPLIT
GEV             0.0032%          -   -0.0064%   -0.0409%    0.0441%       48%/yr  SIGN SPLIT
ONDO            0.0096%    0.0100%    0.0041%   -0.0328%    0.0428%       47%/yr  SIGN SPLIT
ENA             0.0096%    0.0100%    0.0014%   -0.0305%    0.0405%       44%/yr  SIGN SPLIT
TRX             0.0000%   -0.0081%   -0.0352%   -0.0393%    0.0393%       43%/yr
BOT             0.0032%          -    0.0418%    0.0323%    0.0386%       42%/yr
HOOD            0.0272%    0.0369%    0.0000%    0.0024%    0.0369%       40%/yr
NEAR            0.0096%    0.0100%   -0.0065%   -0.0266%    0.0366%       40%/yr  SIGN SPLIT

53 symbols where one venue pays longs while another pays shorts:
  RIVER, PROVE, GRAM, XPL, JUP, MON, AVNT, GEV, ONDO, ENA, NEAR, PENGU, OP, PENDLE, S, MET, AERO, JTO, 1000SHIB, CRV, ARB, PLTR, ADA, PONS, POL, APT, LIT, BCH, LDO, ETH, 1000FLOKI, WLD, LTC, WLFI, DYDX, VIRTUAL, FIL, CRO, LINK, SEI
```

## Builder-deployed markets
```
hl:xyz        134 mkts  OI $ 3,780,971,330  24h $ 2,348,865,800
             XYZ100, TSLA, NVDA, GOLD, HOOD, INTC, PLTR, COIN, META, AAPL, MSFT, ORCL, GOOGL, AMZN, AMD, MU, SNDK, MSTR
hl:io          12 mkts  OI $    62,678,792  24h $    80,301,638
             OAI, ANTH, SNDK, IONQ, NBIS, EWY, GPRO, SBE, TCNT, DRAM, PRL, XIAOMI
hl:para        38 mkts  OI $    17,651,331  24h $     2,498,392
             TOTAL2, OTHERS, BTCD, H100, AVGO, COHR, GLW, CRDO, LRCX, NET, STX, IREN, VST, TER, AAOI, 10Y, CIEN, NAVER
hl:mkts        24 mkts  OI $    11,530,339  24h $     3,534,964
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

total 305 builder markets across 10 dexs
```

## Offchain reference rates (FRED)
```
OFFCHAIN REFERENCE RATES (FRED)

  SOFR      3.87%  2026-10-08     -1bp   Secured Overnight Financing Rate (what a desk funds at)
  DFF       3.88%  2026-10-08     +0bp   Effective fed funds
  IORB      3.90%  2026-10-13     +0bp   Interest on reserve balances
  DGS3MO    4.23%  2026-10-08     +1bp   3-month Treasury
  DGS10     5.22%  2026-10-08     -6bp   10-year Treasury
```

## Carry: funding vs borrow
```
PERP FUNDING (annualized from 8h feed) vs ONCHAIN BORROW

asset        lighter  hyperliq   binance     bybit  aave brw  aave sup
----------------------------------------------------------------------
BTC             4.4%     10.9%      4.0%     -1.2%     0.00%     0.00%
ETH            -7.9%     10.9%      2.5%      0.4%     0.00%     0.00%
SOL            10.5%     10.9%      4.5%     -1.1%         -         -
ENA            10.5%     10.9%      1.6%    -33.9%         -         -
HYPE            2.6%      7.1%     -1.8%     -1.7%         -         -
LINK            4.4%     10.9%     -4.4%      2.9%     0.00%     0.00%
AVAX          -34.2%     -5.3%     -2.4%    -17.6%         -         -
DOGE           10.5%     10.9%     -2.7%      8.4%         -         -

STABLE BORROW COST (the cost of carrying a hedged position)
  aave   USDT     borrow  0.11%  supply  0.00%
  aave   GHO      borrow  3.11%  supply  1.70%
  aave   USDC     borrow  3.90%  supply  2.74%
  aave   GHO      borrow  4.06%  supply  3.26%
  aave   USDC     borrow  4.35%  supply  3.13%
  aave   RLUSD    borrow  4.39%  supply  2.79%
  aave   USDT     borrow  4.42%  supply  3.51%
  aave   USDT     borrow  4.56%  supply  3.73%
  morpho    cbBTC/USDC    borrow  5.01%  lltv 0.86  $337,400,203
  morpho     kBTC/RLUSD   borrow  4.17%  lltv 0.86  $235,259,540
  morpho    PRIME/PYUSD   borrow  5.07%  lltv 0.86  $209,682,225
  morpho     kBTC/PYUSD   borrow  4.20%  lltv 0.86  $160,746,574
  morpho   wstETH/USDT    borrow  3.06%  lltv 0.86  $149,066,702
  morpho     WBTC/USDC    borrow  4.87%  lltv 0.86  $129,709,518

OFFCHAIN BENCHMARK: SOFR 3.87% (2026-10-08)
  BTC perp funding 4.38% vs SOFR 3.87%: spread +0.51pp over the offchain cost of money

BUILDER-DEPLOYED PERPS: 305 markets, 159 with volume today
  xyz:SP500        OI $  368,568,271  funding      1.4%/yr
  xyz:GOLD         OI $  316,496,346  funding      8.1%/yr
  xyz:SKHX         OI $  271,290,065  funding      5.5%/yr
  xyz:XYZ100       OI $  244,368,585  funding      6.1%/yr
  xyz:BRENTOIL     OI $  207,508,034  funding   -393.4%/yr
  xyz:GOOGL        OI $  182,623,458  funding     44.2%/yr
  xyz:SILVER       OI $  177,241,490  funding     22.6%/yr
  xyz:SNDK         OI $  154,330,945  funding     27.5%/yr
  xyz:CRCL         OI $  143,725,225  funding      5.5%/yr
  xyz:CL           OI $  131,548,382  funding   -126.6%/yr
```
