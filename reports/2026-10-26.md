# 2026-10-26

## Market list changes
```
2026-10-25.json -> 2026-10-26.json

hl:abcd: no change (1 markets)
hl:cash: no change (17 markets)
hl:flx: no change (16 markets)
hl:hyna: no change (25 markets)
hl:io: no change (16 markets)
hl:km: no change (23 markets)
hl:mkts: no change (24 markets)
hl:para: no change (39 markets)
hl:vntl: no change (15 markets)
hl:xyz: 138 -> 139
  NEW     (1): xyz:ANT

hyperliquid: no change (234 markets)
lighter: 235 -> 235
  NEW     (1): XTEN
  REMOVED (1): FOGO

variational: no change (582 markets)
```

## Funding dispersion
```
204 symbols quoted on 2+ venues. Top 25 by dispersion.

sym             lighter  hyperliqu    binance      bybit     spread      ann  flag
----------------------------------------------------------------------------------
CASHCAT         0.6128%    0.0100%          -    0.0100%    0.6028%      660%/yr
BIRB                  -          -   -0.2342%    0.0100%    0.2442%      267%/yr  SIGN SPLIT
SAMSUNG               -    0.2611%    0.1118%    0.1344%    0.1493%      163%/yr
SKHYNIX               -    0.2285%    0.0852%    0.1273%    0.1433%      157%/yr
HYUNDAI               -    0.1225%    0.0000%    0.0000%    0.1225%      134%/yr
PRL            -0.0936%          -    0.0100%    0.0100%    0.1036%      113%/yr  SIGN SPLIT
CHIP            0.0944%    0.0100%   -0.0085%    0.0100%    0.1029%      113%/yr  SIGN SPLIT
CAP             0.0096%          -    0.0938%    0.1100%    0.1004%      110%/yr
FOLKS           0.0096%          -    0.0100%    0.1070%    0.0974%      107%/yr
VVV             0.0816%    0.0100%    0.0100%    0.0100%    0.0716%       78%/yr
BERA            0.0096%   -0.0592%    0.0041%    0.0100%    0.0692%       76%/yr  SIGN SPLIT
BYD             0.0032%          -    0.0000%    0.0638%    0.0638%       70%/yr
MINIMAX         0.1240%          -    0.0727%    0.1353%    0.0626%       69%/yr
BMNR            0.0032%          -    0.0032%    0.0657%    0.0625%       68%/yr
CC              0.0096%    0.0100%   -0.0504%    0.0100%    0.0604%       66%/yr  SIGN SPLIT
JTO            -0.0120%    0.0100%    0.0064%   -0.0450%    0.0550%       60%/yr  SIGN SPLIT
EDGE            0.0096%          -    0.0100%   -0.0429%    0.0529%       58%/yr  SIGN SPLIT
UNITREE         0.0472%          -    0.0000%    0.0000%    0.0472%       52%/yr
SHEIN           0.0032%          -          -    0.0461%    0.0429%       47%/yr
CXMT            0.1024%          -    0.1012%    0.0614%    0.0410%       45%/yr
ADA            -0.0328%   -0.0268%    0.0048%    0.0054%    0.0382%       42%/yr  SIGN SPLIT
NBIS            0.0376%          -    0.0000%    0.0000%    0.0376%       41%/yr
JUP             0.0032%   -0.0262%    0.0090%    0.0100%    0.0362%       40%/yr  SIGN SPLIT
XPD             0.0304%    0.0050%    0.0395%          -    0.0345%       38%/yr
STRC           -0.0448%          -   -0.0107%          -    0.0341%       37%/yr

42 symbols where one venue pays longs while another pays shorts:
  BIRB, PRL, CHIP, BERA, CC, JTO, EDGE, ADA, JUP, DRV, LIT, BRENTOIL, SKY, TRUMP, MET, QNT, MNT, MON, TIA, PAXG, SEI, WLD, TSLA, LDO, FIL, DOGE, PENDLE, 1000FLOKI, S, POL, NEAR, HYPE, AERO, MEGA, DASH, GRAM, DOT, PYTH, APT, MSFT
```

## Builder-deployed markets
```
hl:xyz        139 mkts  OI $ 3,916,411,609  24h $ 3,045,031,782
             XYZ100, TSLA, NVDA, GOLD, HOOD, INTC, PLTR, COIN, META, AAPL, MSFT, ORCL, GOOGL, AMZN, AMD, MU, SNDK, MSTR
hl:io          16 mkts  OI $    77,911,759  24h $    51,169,050
             OAI, ANTH, SNDK, IONQ, NBIS, EWY, GPRO, SBE, TCNT, DRAM, PRL, XIAOMI, H100, MOONSHOT, NVDA, SKHX
hl:para        39 mkts  OI $    17,105,482  24h $     9,411,885
             TOTAL2, OTHERS, BTCD, H100, AVGO, COHR, GLW, CRDO, LRCX, NET, STX, IREN, VST, TER, AAOI, 10Y, CIEN, NAVER
hl:mkts        24 mkts  OI $     9,033,741  24h $     2,995,564
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

  SOFR      3.92%  2026-10-23     +2bp   Secured Overnight Financing Rate (what a desk funds at)
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
BTC            10.5%     10.9%     10.9%     10.9%     0.00%     0.00%
ETH            10.5%      6.5%      8.9%      6.5%     0.00%     0.00%
SOL            10.5%     10.9%     10.9%     10.9%         -         -
ENA            10.5%     10.9%     10.9%     10.9%         -         -
HYPE           10.5%     10.9%     -2.9%     10.9%         -         -
LINK           10.5%     10.2%     10.9%     10.9%     0.00%     0.00%
AVAX           10.5%      9.6%      9.0%      5.6%         -         -
DOGE           10.5%     10.9%      6.9%     -8.7%         -         -

STABLE BORROW COST (the cost of carrying a hedged position)
  aave   USDe     borrow  0.00%  supply  0.00%
  aave   RLUSD    borrow  0.63%  supply  0.02%
  aave   RLUSD    borrow  2.73%  supply  1.17%
  aave   USDC     borrow  4.16%  supply  3.11%
  aave   USDC     borrow  4.33%  supply  3.02%
  aave   GHO      borrow  4.44%  supply  3.59%
  aave   GHO      borrow  4.53%  supply  3.60%
  aave   USDC     borrow  4.67%  supply  3.53%
  morpho    cbBTC/USDC    borrow  5.00%  lltv 0.86  $342,229,875
  morpho     kBTC/RLUSD   borrow  6.15%  lltv 0.86  $260,173,776
  morpho    PRIME/PYUSD   borrow  5.15%  lltv 0.86  $207,717,920
  morpho   wstETH/USDT    borrow  9.70%  lltv 0.86  $142,351,835
  morpho PT-reUSD-10DEC2026/USDC    borrow 10.16%  lltv 0.92  $137,912,992
  morpho     WBTC/USDC    borrow  5.70%  lltv 0.86  $127,612,208

OFFCHAIN BENCHMARK: SOFR 3.92% (2026-10-23)
  BTC perp funding 10.51% vs SOFR 3.92%: spread +6.59pp over the offchain cost of money

BUILDER-DEPLOYED PERPS: 315 markets, 165 with volume today
  xyz:SP500        OI $  389,911,828  funding     -1.6%/yr
  xyz:GOLD         OI $  330,455,795  funding     18.2%/yr
  xyz:SKHX         OI $  319,889,103  funding    250.6%/yr
  xyz:XYZ100       OI $  294,221,260  funding      5.8%/yr
  xyz:CL           OI $  221,153,689  funding     -6.4%/yr
  xyz:BRENTOIL     OI $  211,873,261  funding     -6.6%/yr
  xyz:SILVER       OI $  169,381,367  funding      5.5%/yr
  xyz:SPCX         OI $  157,954,415  funding      5.5%/yr
  xyz:MU           OI $  148,919,825  funding      5.5%/yr
  xyz:SKHY         OI $  144,056,677  funding     -1.8%/yr
```
