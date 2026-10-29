# 2026-10-29

## Market list changes
```
2026-10-28.json -> 2026-10-29.json

hl:abcd: no change (1 markets)
hl:cash: no change (17 markets)
hl:flx: no change (16 markets)
hl:hyna: no change (25 markets)
hl:io: no change (16 markets)
hl:km: no change (23 markets)
hl:mkts: no change (24 markets)
hl:para: no change (39 markets)
hl:vntl: no change (15 markets)
hl:xyz: 140 -> 141
  NEW     (1): xyz:ICE

hyperliquid: no change (235 markets)
lighter: no change (235 markets)
variational: no change (583 markets)
```

## Funding dispersion
```
205 symbols quoted on 2+ venues. Top 25 by dispersion.

sym             lighter  hyperliqu    binance      bybit     spread      ann  flag
----------------------------------------------------------------------------------
PRL            -0.9160%          -    0.0100%    0.0100%    0.9260%     1014%/yr  SIGN SPLIT
BIRB                  -          -   -0.0227%   -0.2147%    0.1920%      210%/yr
FOLKS           0.1464%          -    0.0100%    0.0100%    0.1364%      149%/yr
CXMT           -0.0840%          -   -0.0416%   -0.1670%    0.1253%      137%/yr
SKHYNIX               -   -0.1512%   -0.0316%   -0.1525%    0.1209%      132%/yr
UNITREE         0.0032%          -    0.0962%    0.0000%    0.0962%      105%/yr
PROVE                 -    0.0100%   -0.0288%   -0.0756%    0.0856%       94%/yr  SIGN SPLIT
XMR             0.0096%    0.0917%    0.0131%    0.0423%    0.0821%       90%/yr
SAMSUNG               -   -0.0815%    0.0000%   -0.0384%    0.0815%       89%/yr
STRC           -0.0752%          -    0.0000%          -    0.0752%       82%/yr
MEGA            0.0096%    0.0100%    0.0100%   -0.0584%    0.0684%       75%/yr  SIGN SPLIT
ZHIPU          -0.0376%          -    0.0000%   -0.0637%    0.0637%       70%/yr
HYUNDAI               -   -0.0564%    0.0000%    0.0000%    0.0564%       62%/yr
LIT             0.0616%    0.0342%    0.0100%    0.0100%    0.0516%       57%/yr
TTWO            0.0536%          -    0.0093%    0.0475%    0.0443%       49%/yr
PYTH            0.0096%    0.0100%    0.0018%   -0.0328%    0.0428%       47%/yr  SIGN SPLIT
WTI            -0.0048%    0.0050%   -0.0160%   -0.0338%    0.0388%       43%/yr  SIGN SPLIT
ICP            -0.0288%   -0.0044%    0.0100%    0.0100%    0.0388%       42%/yr  SIGN SPLIT
NMR             0.0096%          -   -0.0083%   -0.0267%    0.0363%       40%/yr  SIGN SPLIT
USELESS         0.0456%    0.0100%    0.0100%    0.0100%    0.0356%       39%/yr
GOOGL           0.0480%    0.0250%    0.0538%    0.0604%    0.0355%       39%/yr
NOW             0.0792%          -    0.0443%    0.0549%    0.0349%       38%/yr
BERA            0.0096%    0.0100%   -0.0248%    0.0059%    0.0348%       38%/yr  SIGN SPLIT
HANMI                 -          -    0.0000%   -0.0292%    0.0292%       32%/yr
OP             -0.0184%    0.0100%    0.0082%    0.0057%    0.0284%       31%/yr  SIGN SPLIT

26 symbols where one venue pays longs while another pays shorts:
  PRL, PROVE, MEGA, PYTH, WTI, ICP, NMR, BERA, OP, S, CAP, GRASS, AXS, DYDX, MORPHO, HYPE, QNT, UNI, AERO, POL, ZK, TRX, BCH, ANTHROPIC, MRNA, BRENTOIL
```

## Builder-deployed markets
```
hl:xyz        141 mkts  OI $ 3,989,509,555  24h $ 4,940,128,926
             XYZ100, TSLA, NVDA, GOLD, HOOD, INTC, PLTR, COIN, META, AAPL, MSFT, ORCL, GOOGL, AMZN, AMD, MU, SNDK, MSTR
hl:io          16 mkts  OI $    86,578,566  24h $    50,254,778
             OAI, ANTH, SNDK, IONQ, NBIS, EWY, GPRO, SBE, TCNT, DRAM, PRL, XIAOMI, H100, MOONSHOT, NVDA, SKHX
hl:para        39 mkts  OI $    15,407,183  24h $     6,379,647
             TOTAL2, OTHERS, BTCD, H100, AVGO, COHR, GLW, CRDO, LRCX, NET, STX, IREN, VST, TER, AAOI, 10Y, CIEN, NAVER
hl:mkts        24 mkts  OI $       108,840  24h $     2,227,403
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

total 317 builder markets across 10 dexs
```

## Offchain reference rates (FRED)
```
OFFCHAIN REFERENCE RATES (FRED)

  SOFR      3.94%  2026-10-28     -1bp   Secured Overnight Financing Rate (what a desk funds at)
  DFF       3.88%  2026-10-27     +0bp   Effective fed funds
  IORB      3.90%  2026-10-29     +0bp   Interest on reserve balances
  DGS3MO    4.22%  2026-10-27     +0bp   3-month Treasury
  DGS10     4.99%  2026-10-27     -1bp   10-year Treasury
```

## Carry: funding vs borrow
```
PERP FUNDING (annualized from 8h feed) vs ONCHAIN BORROW

asset        lighter  hyperliq   binance     bybit  aave brw  aave sup
----------------------------------------------------------------------
BTC            10.5%     10.9%     10.9%     10.9%     0.00%     0.00%
ETH            10.5%     10.9%     10.9%     10.9%     0.00%     0.00%
SOL            10.5%     10.9%     10.9%     10.9%         -         -
ENA            10.5%     10.9%     10.9%     10.9%         -         -
HYPE           10.5%     10.9%     10.9%     -7.7%         -         -
LINK           10.5%     10.9%     10.9%      9.8%     0.00%     0.00%
AVAX           10.5%     10.9%     10.9%     10.9%         -         -
DOGE           10.5%     10.9%     10.9%     10.9%         -         -

STABLE BORROW COST (the cost of carrying a hedged position)
  aave   USDe     borrow  0.00%  supply  0.00%
  aave   RLUSD    borrow  0.63%  supply  0.02%
  aave   GHO      borrow  3.93%  supply  3.05%
  aave   USDC     borrow  4.07%  supply  2.98%
  aave   GHO      borrow  4.08%  supply  3.30%
  aave   GHO      borrow  4.53%  supply  3.60%
  aave   USDC     borrow  4.68%  supply  3.55%
  aave   USDC     borrow  4.74%  supply  3.61%
  morpho    cbBTC/USDC    borrow  5.01%  lltv 0.86  $343,935,079
  morpho     kBTC/RLUSD   borrow  3.91%  lltv 0.86  $261,101,226
  morpho    PRIME/PYUSD   borrow  5.16%  lltv 0.86  $206,214,155
  morpho PT-reUSD-10DEC2026/USDC    borrow  9.90%  lltv 0.92  $142,644,013
  morpho     WBTC/USDC    borrow  5.05%  lltv 0.86  $128,731,603
  morpho     kBTC/PYUSD   borrow  4.20%  lltv 0.86  $126,444,517

OFFCHAIN BENCHMARK: SOFR 3.94% (2026-10-28)
  BTC perp funding 10.51% vs SOFR 3.94%: spread +6.57pp over the offchain cost of money

BUILDER-DEPLOYED PERPS: 317 markets, 170 with volume today
  xyz:SP500        OI $  396,757,021  funding      5.5%/yr
  xyz:GOLD         OI $  315,814,830  funding      5.5%/yr
  xyz:GOOGL        OI $  306,382,723  funding     27.2%/yr
  xyz:XYZ100       OI $  278,538,670  funding      5.5%/yr
  xyz:SKHX         OI $  271,544,199  funding   -164.8%/yr
  xyz:CL           OI $  239,442,783  funding      5.5%/yr
  xyz:BRENTOIL     OI $  207,995,098  funding      5.4%/yr
  xyz:SILVER       OI $  174,722,023  funding      5.5%/yr
  xyz:SPCX         OI $  165,197,681  funding      5.5%/yr
  xyz:SKHY         OI $  129,261,796  funding      3.7%/yr
```
