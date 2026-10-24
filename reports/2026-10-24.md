# 2026-10-24

## Market list changes
```
2026-10-23.json -> 2026-10-24.json

hl:abcd: no change (1 markets)
hl:cash: no change (17 markets)
hl:flx: no change (16 markets)
hl:hyna: no change (25 markets)
hl:io: no change (15 markets)
hl:km: no change (23 markets)
hl:mkts: no change (24 markets)
hl:para: no change (39 markets)
hl:vntl: no change (15 markets)
hl:xyz: no change (138 markets)
hyperliquid: no change (234 markets)
lighter: no change (235 markets)
variational: no change (582 markets)
```

## Funding dispersion
```
205 symbols quoted on 2+ venues. Top 25 by dispersion.

sym             lighter  hyperliqu    binance      bybit     spread      ann  flag
----------------------------------------------------------------------------------
BIRB                  -          -   -2.1672%   -3.8272%    1.6600%     1818%/yr
PRL            -0.8104%          -    0.0100%    0.0100%    0.8204%      898%/yr  SIGN SPLIT
SOXL           -0.2968%          -   -0.0157%    0.0000%    0.2968%      325%/yr
ZORA           -0.0296%   -0.2014%   -0.2574%   -0.1102%    0.2278%      249%/yr
SKHYNIX               -   -0.2003%   -0.0439%   -0.0047%    0.1956%      214%/yr
SNDK           -0.1792%   -0.2007%   -0.0134%   -0.0089%    0.1918%      210%/yr
CRCL           -0.1608%   -0.1719%   -0.0042%    0.0000%    0.1719%      188%/yr
SKHY           -0.1632%          -    0.0000%    0.0000%    0.1632%      179%/yr
SAMSUNG               -   -0.1539%   -0.0209%    0.0000%    0.1539%      169%/yr
NBIS           -0.1496%          -   -0.0092%    0.0000%    0.1496%      164%/yr
DRAM           -0.1496%          -    0.0000%    0.0000%    0.1496%      164%/yr
INTC           -0.1288%   -0.1392%    0.0000%    0.0000%    0.1392%      152%/yr
MSTR           -0.1240%   -0.1356%    0.0000%    0.0000%    0.1356%      148%/yr
CBRS           -0.1320%          -    0.0000%    0.0000%    0.1320%      145%/yr
MRVL           -0.1296%          -    0.0000%    0.0000%    0.1296%      142%/yr
MU             -0.1248%          -    0.0000%    0.0000%    0.1248%      137%/yr
CASHCAT        -0.1080%    0.0100%          -    0.0100%    0.1180%      129%/yr  SIGN SPLIT
BERA            0.0096%   -0.0277%   -0.0364%   -0.1007%    0.1103%      121%/yr  SIGN SPLIT
FARTCOIN        0.0016%   -0.0998%    0.0100%   -0.0272%    0.1098%      120%/yr  SIGN SPLIT
LITE           -0.1096%          -    0.0000%    0.0000%    0.1096%      120%/yr
SHEIN          -0.0064%          -          -    0.0973%    0.1037%      114%/yr  SIGN SPLIT
AMD            -0.0928%   -0.1017%    0.0000%          -    0.1017%      111%/yr
XPD            -0.0032%   -0.0928%    0.0000%          -    0.0928%      102%/yr
ROBO           -0.0800%          -   -0.0040%    0.0100%    0.0900%       99%/yr  SIGN SPLIT
CRWV           -0.0816%          -    0.0000%    0.0000%    0.0816%       89%/yr

79 symbols where one venue pays longs while another pays shorts:
  PRL, CASHCAT, BERA, FARTCOIN, SHEIN, ROBO, CHIP, KAITO, BMNR, WLD, MET, PROVE, WLFI, 2Z, ONDO, KORU, NEAR, SEI, JTO, JUP, SPX, LIT, 1000BONK, DRV, PENDLE, AERO, S, UNI, AXS, DYDX, DOT, XPL, TRX, TRUMP, TIA, XLM, AXTI, LINEA, CRO, ADA
```

## Builder-deployed markets
```
hl:xyz        138 mkts  OI $ 3,848,506,749  24h $ 1,079,567,058
             XYZ100, TSLA, NVDA, GOLD, HOOD, INTC, PLTR, COIN, META, AAPL, MSFT, ORCL, GOOGL, AMZN, AMD, MU, SNDK, MSTR
hl:io          15 mkts  OI $    77,623,320  24h $    35,426,500
             OAI, ANTH, SNDK, IONQ, NBIS, EWY, GPRO, SBE, TCNT, DRAM, PRL, XIAOMI, H100, MOONSHOT, NVDA
hl:para        39 mkts  OI $    16,619,739  24h $     3,255,865
             TOTAL2, OTHERS, BTCD, H100, AVGO, COHR, GLW, CRDO, LRCX, NET, STX, IREN, VST, TER, AAOI, 10Y, CIEN, NAVER
hl:mkts        24 mkts  OI $     9,648,304  24h $     2,277,723
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

total 313 builder markets across 10 dexs
```

## Offchain reference rates (FRED)
```
OFFCHAIN REFERENCE RATES (FRED)

  SOFR      3.90%  2026-10-22     +2bp   Secured Overnight Financing Rate (what a desk funds at)
  DFF       3.88%  2026-10-22     +0bp   Effective fed funds
  IORB      3.90%  2026-10-26     +0bp   Interest on reserve balances
  DGS3MO    4.22%  2026-10-22     -3bp   3-month Treasury
  DGS10     4.96%  2026-10-22    -17bp   10-year Treasury
```

## Carry: funding vs borrow
```
PERP FUNDING (annualized from 8h feed) vs ONCHAIN BORROW

asset        lighter  hyperliq   binance     bybit  aave brw  aave sup
----------------------------------------------------------------------
BTC            10.5%     10.9%      3.7%      5.7%     0.00%     0.00%
ETH             0.0%      8.7%      6.2%      7.6%     0.00%     0.00%
SOL            -6.1%      6.6%      1.5%     -0.2%         -         -
ENA            10.5%      7.6%     10.9%     10.9%         -         -
HYPE           10.5%     -5.9%     -3.6%     -0.3%         -         -
LINK           10.5%      8.9%     -3.8%      8.3%     0.00%     0.00%
AVAX            0.0%     -4.2%     -2.6%     -8.4%         -         -
DOGE            7.9%    -13.5%     -4.7%     -8.4%         -         -

STABLE BORROW COST (the cost of carrying a hedged position)
  aave   USDe     borrow  0.00%  supply  0.00%
  aave   RLUSD    borrow  0.50%  supply  0.00%
  aave   RLUSD    borrow  2.73%  supply  1.17%
  aave   GHO      borrow  4.04%  supply  3.23%
  aave   USDC     borrow  4.16%  supply  3.11%
  aave   GHO      borrow  4.53%  supply  3.60%
  aave   USDC     borrow  4.54%  supply  3.41%
  aave   USDC     borrow  4.78%  supply  3.68%
  morpho    cbBTC/USDC    borrow  5.03%  lltv 0.86  $343,089,549
  morpho     kBTC/RLUSD   borrow  4.39%  lltv 0.86  $265,047,212
  morpho    PRIME/PYUSD   borrow  5.11%  lltv 0.86  $210,099,992
  morpho   wstETH/USDT    borrow  2.96%  lltv 0.86  $162,336,049
  morpho PT-reUSD-10DEC2026/USDC    borrow  8.37%  lltv 0.92  $138,449,303
  morpho     WBTC/USDC    borrow  4.92%  lltv 0.86  $128,582,514

OFFCHAIN BENCHMARK: SOFR 3.90% (2026-10-22)
  BTC perp funding 10.51% vs SOFR 3.90%: spread +6.61pp over the offchain cost of money

BUILDER-DEPLOYED PERPS: 313 markets, 164 with volume today
  xyz:SP500        OI $  390,379,023  funding     -8.3%/yr
  xyz:GOLD         OI $  335,611,013  funding    -19.3%/yr
  xyz:SKHX         OI $  307,698,143  funding   -217.8%/yr
  xyz:XYZ100       OI $  287,949,142  funding    -33.9%/yr
  xyz:BRENTOIL     OI $  236,864,124  funding      5.5%/yr
  xyz:CL           OI $  218,476,784  funding      5.5%/yr
  xyz:SILVER       OI $  163,365,153  funding    -61.0%/yr
  xyz:MU           OI $  154,762,874  funding   -147.2%/yr
  xyz:SPCX         OI $  150,311,379  funding    -95.6%/yr
  xyz:SKHY         OI $  146,987,375  funding   -199.6%/yr
```
