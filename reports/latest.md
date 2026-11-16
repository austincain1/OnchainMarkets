# 2026-11-16

## Market list changes
```
2026-11-15.json -> 2026-11-16.json

hl:abcd: no change (1 markets)
hl:cash: no change (17 markets)
hl:flx: no change (16 markets)
hl:hyna: no change (25 markets)
hl:io: no change (24 markets)
hl:km: no change (23 markets)
hl:mkts: no change (24 markets)
hl:para: no change (40 markets)
hl:vntl: no change (15 markets)
hl:xyz: 144 -> 145
  NEW     (1): xyz:TENCENT

hyperliquid: no change (235 markets)
lighter: no change (235 markets)
variational: 589 -> 590
  NEW     (1): EWZS

```

## Funding dispersion
```
204 symbols quoted on 2+ venues. Top 25 by dispersion.

sym             lighter  hyperliqu    binance      bybit     spread      ann  flag
----------------------------------------------------------------------------------
LINEA          -0.2408%    0.0100%   -0.0018%   -0.0316%    0.2508%      275%/yr  SIGN SPLIT
SKHYNIX               -   -0.2480%   -0.0958%   -0.0567%    0.1913%      209%/yr
LIT             0.0096%    0.0100%   -0.1278%   -0.1506%    0.1606%      176%/yr  SIGN SPLIT
BOT             0.1456%          -    0.0000%    0.0000%    0.1456%      159%/yr
WLFI           -0.0384%   -0.0115%    0.0100%   -0.1037%    0.1137%      124%/yr  SIGN SPLIT
SKR            -0.4928%   -0.4639%   -0.5454%   -0.5661%    0.1022%      112%/yr
BYD                   -          -    0.0000%    0.1015%    0.1015%      111%/yr
PRL             0.1072%          -    0.0100%    0.0100%    0.0972%      106%/yr
CASHCAT        -0.0064%   -0.0977%          -   -0.0775%    0.0913%      100%/yr
CC             -0.0504%   -0.1060%   -0.0454%   -0.0195%    0.0865%       95%/yr
NMR            -0.0120%          -   -0.0093%   -0.0913%    0.0820%       90%/yr
HYUNDAI               -   -0.0806%    0.0000%    0.0000%    0.0806%       88%/yr
AZTEC          -0.0608%    0.0100%    0.0100%    0.0100%    0.0708%       78%/yr  SIGN SPLIT
CTR             0.0096%          -    0.0793%    0.0100%    0.0697%       76%/yr
ZHIPU          -0.0192%          -   -0.0870%   -0.0342%    0.0678%       74%/yr
SPX            -0.0568%    0.0009%    0.0060%    0.0100%    0.0668%       73%/yr  SIGN SPLIT
EDGE                  -          -    0.0100%   -0.0558%    0.0658%       72%/yr  SIGN SPLIT
1000BONK        0.0096%   -0.0548%   -0.0344%    0.0100%    0.0648%       71%/yr  SIGN SPLIT
POPCAT         -0.0072%   -0.0528%    0.0100%    0.0100%    0.0628%       69%/yr  SIGN SPLIT
KAITO          -0.0528%   -0.0401%    0.0100%    0.0100%    0.0628%       69%/yr  SIGN SPLIT
WEN            -0.0624%          -    0.0000%          -    0.0624%       68%/yr
GRAM           -0.0232%   -0.0462%   -0.0163%    0.0100%    0.0562%       62%/yr  SIGN SPLIT
NOW            -0.0560%          -    0.0000%    0.0000%    0.0560%       61%/yr
GMX            -0.0072%    0.0100%   -0.0029%   -0.0448%    0.0548%       60%/yr  SIGN SPLIT
1000SHIB        0.0096%   -0.0445%   -0.0227%    0.0005%    0.0541%       59%/yr  SIGN SPLIT

67 symbols where one venue pays longs while another pays shorts:
  LINEA, LIT, WLFI, AZTEC, SPX, EDGE, 1000BONK, POPCAT, KAITO, GRAM, GMX, 1000SHIB, ROBO, MORPHO, JUP, TAO, 1000FLOKI, MET, WIF, MON, MNT, ZK, ETHFI, TIA, BB, OP, CRV, CRO, PYTH, SKY, EIGEN, CHIP, ZORA, STRK, ICP, ONDO, PUMP, APT, UNI, MINIMAX
```

## Builder-deployed markets
```
hl:xyz        145 mkts  OI $ 4,039,069,609  24h $ 4,270,494,175
             XYZ100, TSLA, NVDA, GOLD, HOOD, INTC, PLTR, COIN, META, AAPL, MSFT, ORCL, GOOGL, AMZN, AMD, MU, SNDK, MSTR
hl:io          24 mkts  OI $   224,520,303  24h $    71,599,236
             OAI, ANTH, SNDK, IONQ, NBIS, EWY, GPRO, SBE, TCNT, DRAM, PRL, XIAOMI, H100, MOONSHOT, NVDA, SKHX, AAPL, CRCL
hl:para        40 mkts  OI $    14,570,357  24h $     7,494,202
             TOTAL2, OTHERS, BTCD, H100, AVGO, COHR, GLW, CRDO, LRCX, NET, STX, IREN, VST, TER, AAOI, 10Y, CIEN, NAVER
hl:mkts        24 mkts  OI $       186,631  24h $       187,027
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

  SOFR      3.90%  2026-11-13     +0bp   Secured Overnight Financing Rate (what a desk funds at)
  DFF       3.88%  2026-11-12     +0bp   Effective fed funds
  IORB      3.90%  2026-11-16     +0bp   Interest on reserve balances
  DGS3MO    4.32%  2026-11-12     +2bp   3-month Treasury
  DGS10     5.10%  2026-11-12    +12bp   10-year Treasury
```

## Carry: funding vs borrow
```
PERP FUNDING (annualized from 8h feed) vs ONCHAIN BORROW

asset        lighter  hyperliq   binance     bybit  aave brw  aave sup
----------------------------------------------------------------------
BTC            10.5%      7.2%      6.3%      9.7%     0.00%     0.00%
ETH             1.8%      9.5%     -1.2%     -0.4%     0.00%     0.00%
SOL             1.8%      1.3%      0.6%     -4.7%         -         -
ENA            10.5%     10.9%     10.9%     -8.0%         -         -
HYPE           10.5%     10.9%     10.9%     10.9%         -         -
LINK           -3.5%     10.9%      6.8%      5.7%     0.00%     0.00%
AVAX           -2.6%     -1.3%      5.3%    -14.5%         -         -
DOGE            1.8%     -3.7%     -8.0%     -2.1%         -         -

STABLE BORROW COST (the cost of carrying a hedged position)
  aave   USDe     borrow  0.00%  supply  0.00%
  aave   GHO      borrow  3.86%  supply  2.95%
  aave   USDC     borrow  3.89%  supply  2.72%
  aave   RLUSD    borrow  3.94%  supply  2.82%
  aave   GHO      borrow  4.04%  supply  3.24%
  aave   GHO      borrow  4.35%  supply  3.32%
  aave   USDC     borrow  4.51%  supply  3.30%
  aave   USDC     borrow  5.25%  supply  4.35%
  morpho    cbBTC/USDC    borrow  5.11%  lltv 0.86  $333,317,638
  morpho    PRIME/PYUSD   borrow  6.17%  lltv 0.86  $173,135,587
  morpho     kBTC/RLUSD   borrow  3.30%  lltv 0.86  $169,692,190
  morpho PT-reUSD-10DEC2026/USDC    borrow  9.67%  lltv 0.92  $140,313,796
  morpho     WBTC/USDC    borrow  5.12%  lltv 0.86  $122,537,004
  morpho   wstETH/USDT    borrow  3.62%  lltv 0.86  $115,477,976

OFFCHAIN BENCHMARK: SOFR 3.90% (2026-11-13)
  BTC perp funding 10.51% vs SOFR 3.90%: spread +6.61pp over the offchain cost of money

BUILDER-DEPLOYED PERPS: 330 markets, 171 with volume today
  xyz:SP500        OI $  444,443,638  funding      5.5%/yr
  xyz:NVDA         OI $  412,038,313  funding     27.6%/yr
  xyz:BRENTOIL     OI $  324,950,235  funding     23.5%/yr
  xyz:SKHX         OI $  287,674,712  funding   -274.1%/yr
  xyz:XYZ100       OI $  272,428,026  funding      5.5%/yr
  xyz:GOLD         OI $  248,163,831  funding      9.0%/yr
  io:ANTH          OI $  191,071,741  funding     -6.8%/yr
  xyz:MU           OI $  146,335,759  funding      7.2%/yr
  xyz:GOOGL        OI $  139,390,106  funding      5.5%/yr
  xyz:SILVER       OI $  136,440,268  funding     21.4%/yr
```
