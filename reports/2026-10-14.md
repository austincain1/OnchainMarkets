# 2026-10-14

## Market list changes
```
2026-10-13.json -> 2026-10-14.json

hl:abcd: no change (1 markets)
hl:cash: no change (17 markets)
hl:flx: no change (16 markets)
hl:hyna: no change (25 markets)
hl:io: no change (13 markets)
hl:km: no change (23 markets)
hl:mkts: no change (24 markets)
hl:para: no change (38 markets)
hl:vntl: no change (15 markets)
hl:xyz: 134 -> 135
  NEW     (1): xyz:JIO

hyperliquid: no change (234 markets)
lighter: no change (235 markets)
variational: 570 -> 572
  NEW     (2): NOW, US30S

```

## Funding dispersion
```
205 symbols quoted on 2+ venues. Top 25 by dispersion.

sym             lighter  hyperliqu    binance      bybit     spread      ann  flag
----------------------------------------------------------------------------------
SMIC           -0.5232%          -          -    0.0000%    0.5232%      573%/yr
PRL             0.4632%          -    0.0100%    0.0100%    0.4532%      496%/yr
CASHCAT         0.2256%    0.0100%          -    0.0100%    0.2156%      236%/yr
ARC            -0.1784%          -    0.0100%   -0.1934%    0.2034%      223%/yr  SIGN SPLIT
SKHYNIX               -   -0.1836%   -0.0753%   -0.0259%    0.1577%      173%/yr
MET             0.0096%   -0.1175%   -0.0422%   -0.0550%    0.1271%      139%/yr  SIGN SPLIT
SAMSUNG               -   -0.1584%   -0.0577%   -0.0346%    0.1239%      136%/yr
CXMT            0.0032%          -   -0.1120%   -0.0529%    0.1152%      126%/yr  SIGN SPLIT
HYUNDAI               -   -0.1118%   -0.0026%    0.0000%    0.1118%      122%/yr
PROVE           0.0096%    0.0100%    0.0100%   -0.0784%    0.0884%       97%/yr  SIGN SPLIT
AVNT            0.0096%   -0.0701%    0.0100%   -0.0026%    0.0801%       88%/yr  SIGN SPLIT
KAITO           0.0096%    0.0100%    0.0058%   -0.0690%    0.0790%       86%/yr  SIGN SPLIT
BOT             0.0032%          -   -0.0735%   -0.0215%    0.0767%       84%/yr  SIGN SPLIT
USDJPY          0.0000%   -0.0140%          -   -0.0664%    0.0664%       73%/yr
FOGO                  -    0.0100%    0.0100%   -0.0410%    0.0510%       56%/yr  SIGN SPLIT
JUP            -0.0400%   -0.0245%   -0.0075%    0.0100%    0.0500%       55%/yr  SIGN SPLIT
VIRTUAL        -0.0344%    0.0100%   -0.0035%    0.0029%    0.0444%       49%/yr  SIGN SPLIT
TTWO            0.0440%          -    0.0113%    0.0000%    0.0440%       48%/yr
BERA            0.0096%    0.0089%   -0.0274%   -0.0342%    0.0438%       48%/yr  SIGN SPLIT
ONDO           -0.0368%   -0.0293%   -0.0252%    0.0038%    0.0406%       44%/yr  SIGN SPLIT
EIGEN           0.0096%    0.0100%    0.0002%   -0.0262%    0.0362%       40%/yr  SIGN SPLIT
SKY             0.0096%    0.0100%    0.0059%   -0.0248%    0.0348%       38%/yr  SIGN SPLIT
CRCL            0.0224%    0.0408%    0.0280%    0.0061%    0.0347%       38%/yr
SYRUP           0.0096%    0.0100%   -0.0138%   -0.0242%    0.0342%       37%/yr  SIGN SPLIT
CRWV            0.0032%          -    0.0097%    0.0369%    0.0337%       37%/yr

62 symbols where one venue pays longs while another pays shorts:
  ARC, MET, CXMT, PROVE, AVNT, KAITO, BOT, FOGO, JUP, VIRTUAL, BERA, ONDO, EIGEN, SKY, SYRUP, MINIMAX, 1000SHIB, ZORA, JTO, 1000FLOKI, SEI, MON, MNT, XLM, OP, GRAM, S, MORPHO, ARB, DOT, DYDX, QNT, CHIP, WTI, FIL, ZHIPU, XPL, AVAX, PENGU, PLTR
```

## Builder-deployed markets
```
hl:xyz        135 mkts  OI $ 3,940,557,126  24h $ 2,909,451,236
             XYZ100, TSLA, NVDA, GOLD, HOOD, INTC, PLTR, COIN, META, AAPL, MSFT, ORCL, GOOGL, AMZN, AMD, MU, SNDK, MSTR
hl:io          13 mkts  OI $    61,981,059  24h $    93,760,794
             OAI, ANTH, SNDK, IONQ, NBIS, EWY, GPRO, SBE, TCNT, DRAM, PRL, XIAOMI, H100
hl:para        38 mkts  OI $    15,633,932  24h $     7,053,259
             TOTAL2, OTHERS, BTCD, H100, AVGO, COHR, GLW, CRDO, LRCX, NET, STX, IREN, VST, TER, AAOI, 10Y, CIEN, NAVER
hl:mkts        24 mkts  OI $    10,959,039  24h $     2,320,354
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

total 307 builder markets across 10 dexs
```

## Offchain reference rates (FRED)
```
OFFCHAIN REFERENCE RATES (FRED)

  SOFR      3.89%  2026-10-13     +2bp   Secured Overnight Financing Rate (what a desk funds at)
  DFF       3.88%  2026-10-12     +0bp   Effective fed funds
  IORB      3.90%  2026-10-14     +0bp   Interest on reserve balances
  DGS3MO    4.25%  2026-10-09     +2bp   3-month Treasury
  DGS10     5.24%  2026-10-09     +2bp   10-year Treasury
```

## Carry: funding vs borrow
```
PERP FUNDING (annualized from 8h feed) vs ONCHAIN BORROW

asset        lighter  hyperliq   binance     bybit  aave brw  aave sup
----------------------------------------------------------------------
BTC            10.5%     10.9%     -1.8%      1.4%     0.00%     0.00%
ETH            10.5%     10.9%     -1.7%     -3.4%     0.00%     0.00%
SOL             2.6%    -13.5%      0.3%     -5.5%         -         -
ENA            10.5%     10.9%      2.2%      7.5%         -         -
HYPE           10.5%     10.9%      6.7%      5.9%         -         -
LINK           10.5%      4.7%      3.3%      6.1%     0.00%     0.00%
AVAX           -7.0%     10.9%      0.8%      3.1%         -         -
DOGE           10.5%     10.9%      0.5%     -2.2%         -         -

STABLE BORROW COST (the cost of carrying a hedged position)
  aave   USDT     borrow  0.11%  supply  0.00%
  aave   GHO      borrow  3.11%  supply  1.70%
  aave   GHO      borrow  4.06%  supply  3.26%
  aave   USDT     borrow  4.22%  supply  3.19%
  aave   USDC     borrow  4.28%  supply  3.28%
  aave   RLUSD    borrow  4.39%  supply  2.80%
  aave   USDC     borrow  4.54%  supply  3.41%
  aave   USDT     borrow  4.60%  supply  3.50%
  morpho    cbBTC/USDC    borrow  4.76%  lltv 0.86  $344,040,763
  morpho     kBTC/RLUSD   borrow  3.47%  lltv 0.86  $249,171,019
  morpho    PRIME/PYUSD   borrow  5.04%  lltv 0.86  $209,770,022
  morpho     kBTC/PYUSD   borrow  4.16%  lltv 0.86  $178,356,022
  morpho   wstETH/USDT    borrow  3.02%  lltv 0.86  $146,086,658
  morpho     WBTC/USDC    borrow  4.85%  lltv 0.86  $130,415,327

OFFCHAIN BENCHMARK: SOFR 3.89% (2026-10-13)
  BTC perp funding 10.51% vs SOFR 3.89%: spread +6.62pp over the offchain cost of money

BUILDER-DEPLOYED PERPS: 307 markets, 160 with volume today
  xyz:SP500        OI $  384,576,306  funding      5.5%/yr
  xyz:GOLD         OI $  328,704,910  funding     31.6%/yr
  xyz:SKHX         OI $  311,409,724  funding   -201.7%/yr
  xyz:XYZ100       OI $  282,297,161  funding     14.0%/yr
  xyz:SILVER       OI $  220,031,087  funding     28.7%/yr
  xyz:GOOGL        OI $  182,854,853  funding     10.5%/yr
  xyz:BRENTOIL     OI $  176,152,479  funding      5.5%/yr
  xyz:SKHY         OI $  160,276,717  funding     -1.2%/yr
  xyz:CRCL         OI $  154,995,461  funding     44.2%/yr
  xyz:SNDK         OI $  143,898,593  funding     20.3%/yr
```
