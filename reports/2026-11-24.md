# 2026-11-24

## Market list changes
```
2026-11-23.json -> 2026-11-24.json

hl:abcd: no change (1 markets)
hl:cash: no change (17 markets)
hl:flx: no change (16 markets)
hl:hyna: no change (25 markets)
hl:io: no change (26 markets)
hl:km: no change (23 markets)
hl:mkts: no change (24 markets)
hl:para: no change (40 markets)
hl:vntl: no change (15 markets)
hl:xyz: 148 -> 149
  NEW     (1): xyz:TQQQ

hyperliquid: no change (235 markets)
lighter: no change (235 markets)
variational: 594 -> 595
  NEW     (1): POPMART

```

## Funding dispersion
```
206 symbols quoted on 2+ venues. Top 25 by dispersion.

sym             lighter  hyperliqu    binance      bybit     spread      ann  flag
----------------------------------------------------------------------------------
MINIMAX         0.2640%          -    0.0585%    0.0499%    0.2141%      234%/yr
AVNT           -0.1256%   -0.0573%   -0.0189%    0.0040%    0.1296%      142%/yr  SIGN SPLIT
0G             -0.1080%   -0.0106%   -0.0297%    0.0100%    0.1180%      129%/yr  SIGN SPLIT
ZHIPU           0.1240%          -    0.0228%    0.0771%    0.1012%      111%/yr
JUP            -0.0800%   -0.0614%   -0.0247%    0.0100%    0.0900%       99%/yr  SIGN SPLIT
FOLKS           0.0984%          -    0.0100%    0.0100%    0.0884%       97%/yr
DRV             0.0096%          -          -   -0.0781%    0.0877%       96%/yr  SIGN SPLIT
BB              0.0032%          -   -0.0724%    0.0100%    0.0824%       90%/yr  SIGN SPLIT
MNT             0.0000%   -0.0725%          -    0.0094%    0.0819%       90%/yr  SIGN SPLIT
IBM             0.0792%          -    0.0000%    0.0000%    0.0792%       87%/yr
CC             -0.1152%   -0.0375%   -0.0754%   -0.1106%    0.0777%       85%/yr
CXMT           -0.0368%          -    0.0000%    0.0363%    0.0731%       80%/yr  SIGN SPLIT
MON            -0.0576%   -0.0306%    0.0100%   -0.0114%    0.0676%       74%/yr  SIGN SPLIT
GEV             0.0032%          -    0.0000%    0.0653%    0.0653%       71%/yr
AERO            0.0096%   -0.0529%    0.0100%    0.0100%    0.0629%       69%/yr  SIGN SPLIT
WLFI           -0.0520%   -0.0025%    0.0100%   -0.0077%    0.0620%       68%/yr  SIGN SPLIT
PRL             0.0096%          -    0.0100%   -0.0492%    0.0592%       65%/yr  SIGN SPLIT
JTO             0.0024%    0.0020%    0.0004%   -0.0554%    0.0578%       63%/yr  SIGN SPLIT
1000FLOKI      -0.0408%    0.0100%   -0.0079%    0.0100%    0.0508%       56%/yr  SIGN SPLIT
1000SHIB        0.0096%   -0.0370%   -0.0086%   -0.0035%    0.0466%       51%/yr  SIGN SPLIT
1000PEPE        0.0056%   -0.0363%   -0.0365%    0.0100%    0.0465%       51%/yr  SIGN SPLIT
ZORA           -0.0328%    0.0100%   -0.0298%    0.0085%    0.0428%       47%/yr  SIGN SPLIT
XIAOMI          0.0032%          -          -    0.0451%    0.0419%       46%/yr
MET            -0.0720%   -0.0778%   -0.0428%   -0.0361%    0.0417%       46%/yr
BERA            0.0008%   -0.0310%    0.0039%    0.0100%    0.0410%       45%/yr  SIGN SPLIT

69 symbols where one venue pays longs while another pays shorts:
  AVNT, 0G, JUP, DRV, BB, MNT, CXMT, MON, AERO, WLFI, PRL, JTO, 1000FLOKI, 1000SHIB, 1000PEPE, ZORA, BERA, AAPL, ZEC, ROBO, DOT, PAXG, BCH, 2Z, SUI, GMX, POL, SOL, VIRTUAL, DASH, DOGE, HOOD, DIA, DYDX, ETHFI, SKR, CHIP, PENGU, TIA, AXS
```

## Builder-deployed markets
```
hl:xyz        149 mkts  OI $ 3,754,420,391  24h $ 4,936,525,136
             XYZ100, TSLA, NVDA, GOLD, HOOD, INTC, PLTR, COIN, META, AAPL, MSFT, ORCL, GOOGL, AMZN, AMD, MU, SNDK, MSTR
hl:io          26 mkts  OI $    96,991,930  24h $    70,684,329
             OAI, ANTH, SNDK, IONQ, NBIS, EWY, GPRO, SBE, TCNT, DRAM, PRL, XIAOMI, H100, MOONSHOT, NVDA, SKHX, AAPL, CRCL
hl:para        40 mkts  OI $    11,508,244  24h $     9,427,104
             TOTAL2, OTHERS, BTCD, H100, AVGO, COHR, GLW, CRDO, LRCX, NET, STX, IREN, VST, TER, AAOI, 10Y, CIEN, NAVER
hl:mkts        24 mkts  OI $       219,361  24h $       185,155
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

total 336 builder markets across 10 dexs
```

## Offchain reference rates (FRED)
```
OFFCHAIN REFERENCE RATES (FRED)

  SOFR      3.92%  2026-11-23     +0bp   Secured Overnight Financing Rate (what a desk funds at)
  DFF       3.88%  2026-11-20     +0bp   Effective fed funds
  IORB      3.90%  2026-11-24     +0bp   Interest on reserve balances
  DGS3MO    4.32%  2026-11-20     -2bp   3-month Treasury
  DGS10     4.92%  2026-11-20    -12bp   10-year Treasury
```

## Carry: funding vs borrow
```
PERP FUNDING (annualized from 8h feed) vs ONCHAIN BORROW

asset        lighter  hyperliq   binance     bybit  aave brw  aave sup
----------------------------------------------------------------------
BTC             7.0%     -9.3%      8.8%      4.6%     0.00%     0.00%
ETH            10.5%     10.8%      9.3%      8.4%     0.00%     0.00%
SOL           -20.1%     -3.7%      3.0%      7.6%         -         -
ENA            10.5%      1.0%      2.8%     10.9%         -         -
HYPE           -4.4%     10.9%     10.9%     10.1%         -         -
LINK           -7.9%     10.9%      4.7%      3.3%     0.00%     0.00%
AVAX            0.0%      0.6%      0.5%     -3.1%         -         -
DOGE          -23.7%     -5.8%      0.4%      2.6%         -         -

STABLE BORROW COST (the cost of carrying a hedged position)
  aave   USDe     borrow  0.00%  supply  0.00%
  aave   RLUSD    borrow  3.78%  supply  2.23%
  aave   USDC     borrow  3.78%  supply  2.57%
  aave   GHO      borrow  4.02%  supply  3.21%
  aave   GHO      borrow  4.07%  supply  3.28%
  aave   RLUSD    borrow  4.07%  supply  3.47%
  aave   USDC     borrow  4.32%  supply  3.35%
  aave   GHO      borrow  4.35%  supply  3.32%
  morpho    cbBTC/USDC    borrow  3.67%  lltv 0.86  $259,683,453
  morpho     kBTC/RLUSD   borrow  3.30%  lltv 0.86  $162,531,525
  morpho     WBTC/USDC    borrow  3.68%  lltv 0.86  $150,005,571
  morpho PT-reUSD-10DEC2026/USDC    borrow  8.66%  lltv 0.92  $137,925,700
  morpho    PRIME/PYUSD   borrow  6.20%  lltv 0.86  $129,184,384
  morpho   wstETH/USDT    borrow  3.49%  lltv 0.86  $119,447,090

OFFCHAIN BENCHMARK: SOFR 3.92% (2026-11-23)
  BTC perp funding 7.01% vs SOFR 3.92%: spread +3.09pp over the offchain cost of money

BUILDER-DEPLOYED PERPS: 336 markets, 178 with volume today
  xyz:SP500        OI $  402,203,754  funding      5.5%/yr
  xyz:SKHX         OI $  345,668,906  funding    -34.1%/yr
  xyz:NVDA         OI $  310,351,379  funding      5.5%/yr
  xyz:XYZ100       OI $  280,941,006  funding      6.5%/yr
  xyz:ANT          OI $  251,943,703  funding    -32.3%/yr
  xyz:GOLD         OI $  236,862,328  funding      7.5%/yr
  xyz:BRENTOIL     OI $  158,248,265  funding      3.7%/yr
  xyz:SILVER       OI $  142,606,781  funding     11.6%/yr
  xyz:CL           OI $  139,018,705  funding      5.5%/yr
  xyz:MU           OI $  135,711,451  funding      5.5%/yr
```
