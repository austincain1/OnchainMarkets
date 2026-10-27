# 2026-10-27

## Market list changes
```
2026-10-26.json -> 2026-10-27.json

hl:abcd: no change (1 markets)
hl:cash: no change (17 markets)
hl:flx: no change (16 markets)
hl:hyna: no change (25 markets)
hl:io: no change (16 markets)
hl:km: no change (23 markets)
hl:mkts: no change (24 markets)
hl:para: no change (39 markets)
hl:vntl: no change (15 markets)
hl:xyz: no change (139 markets)
hyperliquid: 234 -> 235
  NEW     (1): XTEN

lighter: no change (235 markets)
variational: no change (582 markets)
```

## Funding dispersion
```
205 symbols quoted on 2+ venues. Top 25 by dispersion.

sym             lighter  hyperliqu    binance      bybit     spread      ann  flag
----------------------------------------------------------------------------------
STONK           0.5192%          -          -    0.0100%    0.5092%      558%/yr
CASHCAT         0.2448%    0.0100%          -    0.0100%    0.2348%      257%/yr
CXMT            0.0032%          -    0.1562%    0.0163%    0.1530%      168%/yr
PRL             0.1392%          -    0.0100%    0.0100%    0.1292%      141%/yr
AERO            0.0096%    0.0100%   -0.0092%   -0.1179%    0.1279%      140%/yr  SIGN SPLIT
UNITREE         0.0032%          -    0.1251%    0.0621%    0.1219%      133%/yr
BIRB                  -          -   -0.1070%    0.0100%    0.1170%      128%/yr  SIGN SPLIT
CTR            -0.1008%          -   -0.0465%    0.0100%    0.1108%      121%/yr  SIGN SPLIT
MINIMAX         0.1592%          -    0.1668%    0.2685%    0.1093%      120%/yr
PIPPIN                -          -    0.1173%    0.0100%    0.1073%      118%/yr
ROBO           -0.0040%          -    0.0100%   -0.0886%    0.0986%      108%/yr  SIGN SPLIT
SAMSUNG               -    0.0461%    0.0866%    0.0000%    0.0866%       95%/yr
HYUNDAI               -    0.0845%    0.0000%    0.0000%    0.0845%       93%/yr
ZHIPU           0.2480%          -    0.2262%    0.3072%    0.0810%       89%/yr
NMR             0.0096%          -   -0.0188%   -0.0663%    0.0759%       83%/yr  SIGN SPLIT
TTWO            0.0120%          -    0.0149%    0.0848%    0.0728%       80%/yr
XPD             0.0600%    0.0780%    0.0064%          -    0.0716%       78%/yr
BERA            0.0096%   -0.0560%   -0.0076%    0.0100%    0.0660%       72%/yr  SIGN SPLIT
SKHYNIX               -    0.0839%    0.0280%    0.0194%    0.0645%       71%/yr
ZORA            0.0096%   -0.0448%   -0.0248%   -0.0167%    0.0544%       60%/yr  SIGN SPLIT
DYDX           -0.0352%    0.0100%    0.0100%    0.0100%    0.0452%       49%/yr  SIGN SPLIT
RAY            -0.0432%          -    0.0000%          -    0.0432%       47%/yr
CAP             0.0096%          -    0.0481%    0.0329%    0.0385%       42%/yr
GEV             0.0032%          -    0.0380%    0.0000%    0.0380%       42%/yr
TRX            -0.0376%   -0.0253%   -0.0155%    0.0003%    0.0379%       41%/yr  SIGN SPLIT

37 symbols where one venue pays longs while another pays shorts:
  AERO, BIRB, CTR, ROBO, NMR, BERA, ZORA, DYDX, TRX, CRO, GRAM, POL, FIL, TIA, S, LIT, CC, AAVE, SEI, AVAX, 1000FLOKI, DOT, PAXG, CRV, PYTH, ARB, JUP, OP, HBAR, ONDO, MEGA, MORPHO, ZEC, SPY, TSLA, APT, WTI
```

## Builder-deployed markets
```
hl:xyz        139 mkts  OI $ 3,970,720,641  24h $ 2,713,489,041
             XYZ100, TSLA, NVDA, GOLD, HOOD, INTC, PLTR, COIN, META, AAPL, MSFT, ORCL, GOOGL, AMZN, AMD, MU, SNDK, MSTR
hl:io          16 mkts  OI $    84,428,198  24h $    38,323,608
             OAI, ANTH, SNDK, IONQ, NBIS, EWY, GPRO, SBE, TCNT, DRAM, PRL, XIAOMI, H100, MOONSHOT, NVDA, SKHX
hl:para        39 mkts  OI $    16,917,904  24h $     5,211,680
             TOTAL2, OTHERS, BTCD, H100, AVGO, COHR, GLW, CRDO, LRCX, NET, STX, IREN, VST, TER, AAOI, 10Y, CIEN, NAVER
hl:mkts        24 mkts  OI $     8,684,544  24h $     1,383,297
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

total 315 builder markets across 10 dexs
```

## Offchain reference rates (FRED)
```
OFFCHAIN REFERENCE RATES (FRED)

  SOFR      3.93%  2026-10-26     +1bp   Secured Overnight Financing Rate (what a desk funds at)
  DFF       3.88%  2026-10-23     +0bp   Effective fed funds
  IORB      3.90%  2026-10-27     +0bp   Interest on reserve balances
  DGS3MO    4.22%  2026-10-23     +0bp   3-month Treasury
  DGS10     5.00%  2026-10-23     +4bp   10-year Treasury
```

## Carry: funding vs borrow
```
PERP FUNDING (annualized from 8h feed) vs ONCHAIN BORROW

asset        lighter  hyperliq   binance     bybit  aave brw  aave sup
----------------------------------------------------------------------
BTC            10.5%     10.9%     10.9%     10.9%     0.00%     0.00%
ETH            10.5%     10.9%     10.9%     10.9%     0.00%     0.00%
SOL            10.5%     10.9%      8.7%     10.9%         -         -
ENA            10.5%     10.9%     10.9%     10.9%         -         -
HYPE           10.5%     10.9%     10.9%      5.7%         -         -
LINK           10.5%     10.9%     10.9%     10.9%     0.00%     0.00%
AVAX          -14.0%      2.9%      6.6%      9.6%         -         -
DOGE           10.5%     10.9%      8.3%     10.9%         -         -

STABLE BORROW COST (the cost of carrying a hedged position)
  aave   USDe     borrow  0.00%  supply  0.00%
  aave   RLUSD    borrow  0.63%  supply  0.02%
  aave   RLUSD    borrow  2.73%  supply  1.17%
  aave   USDC     borrow  4.14%  supply  2.77%
  aave   USDC     borrow  4.16%  supply  3.11%
  aave   GHO      borrow  4.45%  supply  3.60%
  aave   GHO      borrow  4.53%  supply  3.60%
  aave   USDC     borrow  4.66%  supply  3.51%
  morpho    cbBTC/USDC    borrow  5.01%  lltv 0.86  $342,835,133
  morpho     kBTC/RLUSD   borrow  3.83%  lltv 0.86  $261,376,644
  morpho    PRIME/PYUSD   borrow  5.15%  lltv 0.86  $206,997,502
  morpho PT-reUSD-10DEC2026/USDC    borrow 11.66%  lltv 0.92  $137,649,885
  morpho     WBTC/USDC    borrow  5.15%  lltv 0.86  $128,008,604
  morpho     kBTC/PYUSD   borrow  4.21%  lltv 0.86  $126,375,265

OFFCHAIN BENCHMARK: SOFR 3.93% (2026-10-26)
  BTC perp funding 10.51% vs SOFR 3.93%: spread +6.58pp over the offchain cost of money

BUILDER-DEPLOYED PERPS: 315 markets, 169 with volume today
  xyz:SP500        OI $  410,993,311  funding     -6.5%/yr
  xyz:GOLD         OI $  329,171,951  funding      5.5%/yr
  xyz:SKHX         OI $  317,549,089  funding     87.8%/yr
  xyz:XYZ100       OI $  288,333,630  funding      5.5%/yr
  xyz:CL           OI $  225,608,059  funding      0.8%/yr
  xyz:BRENTOIL     OI $  204,896,714  funding      5.5%/yr
  xyz:SILVER       OI $  170,754,916  funding      5.5%/yr
  xyz:SPCX         OI $  155,645,773  funding      5.5%/yr
  xyz:MU           OI $  150,601,620  funding      5.5%/yr
  xyz:SKHY         OI $  134,583,115  funding      5.5%/yr
```
