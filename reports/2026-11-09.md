# 2026-11-09

## Market list changes
```
2026-11-08.json -> 2026-11-09.json

hl:abcd: no change (1 markets)
hl:cash: no change (17 markets)
hl:flx: no change (16 markets)
hl:hyna: no change (25 markets)
hl:io: no change (21 markets)
hl:km: no change (23 markets)
hl:mkts: no change (24 markets)
hl:para: no change (40 markets)
hl:vntl: no change (15 markets)
hl:xyz: 143 -> 144
  NEW     (1): xyz:PANW

hyperliquid: no change (235 markets)
lighter: no change (235 markets)
variational: no change (588 markets)
```

## Funding dispersion
```
205 symbols quoted on 2+ venues. Top 25 by dispersion.

sym             lighter  hyperliqu    binance      bybit     spread      ann  flag
----------------------------------------------------------------------------------
PRL             0.6096%          -    0.0100%    0.0100%    0.5996%      657%/yr
NATGAS          1.4032%    1.4213%    1.0000%          -    0.4213%      461%/yr
BOT            -0.2968%          -   -0.0572%   -0.0787%    0.2396%      262%/yr
RIVER           0.0096%          -    0.1423%    0.0100%    0.1327%      145%/yr
IBM            -0.0784%          -    0.0000%   -0.1232%    0.1232%      135%/yr
BRENTOIL       -0.2280%   -0.2581%   -0.3506%          -    0.1226%      134%/yr
CXMT           -0.1128%          -    0.0000%    0.0000%    0.1128%      124%/yr
ENA             0.0096%    0.0100%   -0.0003%   -0.0890%    0.0990%      108%/yr  SIGN SPLIT
XMR             0.0872%    0.0355%    0.0210%    0.0100%    0.0772%       85%/yr
WTI            -0.1608%   -0.1493%   -0.2206%   -0.1883%    0.0713%       78%/yr
SAMSUNG               -   -0.0516%    0.0184%    0.0071%    0.0700%       77%/yr  SIGN SPLIT
XCU             0.1536%    0.1608%    0.2185%          -    0.0649%       71%/yr
GRAM            0.0064%    0.0100%    0.0000%   -0.0526%    0.0626%       69%/yr  SIGN SPLIT
2Z              0.0096%    0.0100%    0.0100%   -0.0486%    0.0586%       64%/yr  SIGN SPLIT
MORPHO          0.0096%   -0.0230%   -0.0057%   -0.0472%    0.0568%       62%/yr  SIGN SPLIT
TRUMP          -0.0488%   -0.0224%   -0.0507%   -0.0786%    0.0562%       62%/yr
NOW             0.0536%          -    0.0000%    0.0000%    0.0536%       59%/yr
MET            -0.0432%    0.0100%   -0.0033%   -0.0055%    0.0532%       58%/yr  SIGN SPLIT
AVAX           -0.0432%   -0.0341%    0.0078%    0.0100%    0.0532%       58%/yr  SIGN SPLIT
DIA                   -          -   -0.0422%    0.0100%    0.0522%       57%/yr  SIGN SPLIT
BERA            0.0096%   -0.0387%   -0.0038%    0.0100%    0.0487%       53%/yr  SIGN SPLIT
WEN            -0.0472%          -    0.0000%          -    0.0472%       52%/yr
HANMI                 -          -    0.0467%    0.0000%    0.0467%       51%/yr
WLFI           -0.0088%    0.0100%    0.0100%   -0.0357%    0.0457%       50%/yr  SIGN SPLIT
CC              0.0096%   -0.0017%    0.0100%   -0.0356%    0.0456%       50%/yr  SIGN SPLIT

52 symbols where one venue pays longs while another pays shorts:
  ENA, SAMSUNG, GRAM, 2Z, MORPHO, MET, AVAX, DIA, BERA, WLFI, CC, MNT, PENGU, SPX, AERO, DYDX, CASHCAT, XRP, JUP, MEGA, FIL, AAPL, OP, ARB, DOGE, LTC, VIRTUAL, PONS, SKY, CHIP, HYPE, SOL, LIT, AZTEC, XLM, S, ICP, ETHFI, QNT, SEI
```

## Builder-deployed markets
```
hl:xyz        144 mkts  OI $ 4,337,810,489  24h $ 6,370,028,346
             XYZ100, TSLA, NVDA, GOLD, HOOD, INTC, PLTR, COIN, META, AAPL, MSFT, ORCL, GOOGL, AMZN, AMD, MU, SNDK, MSTR
hl:io          21 mkts  OI $   185,463,566  24h $    86,866,372
             OAI, ANTH, SNDK, IONQ, NBIS, EWY, GPRO, SBE, TCNT, DRAM, PRL, XIAOMI, H100, MOONSHOT, NVDA, SKHX, AAPL, CRCL
hl:para        40 mkts  OI $    15,506,220  24h $     8,573,188
             TOTAL2, OTHERS, BTCD, H100, AVGO, COHR, GLW, CRDO, LRCX, NET, STX, IREN, VST, TER, AAOI, 10Y, CIEN, NAVER
hl:mkts        24 mkts  OI $       185,258  24h $        91,844
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

total 326 builder markets across 10 dexs
```

## Offchain reference rates (FRED)
```
OFFCHAIN REFERENCE RATES (FRED)

  SOFR      3.89%  2026-11-06     -3bp   Secured Overnight Financing Rate (what a desk funds at)
  DFF       3.88%  2026-11-06     +0bp   Effective fed funds
  IORB      3.90%  2026-11-09     +0bp   Interest on reserve balances
  DGS3MO    4.19%  2026-11-06     +2bp   3-month Treasury
  DGS10     4.86%  2026-11-06     +2bp   10-year Treasury
```

## Carry: funding vs borrow
```
PERP FUNDING (annualized from 8h feed) vs ONCHAIN BORROW

asset        lighter  hyperliq   binance     bybit  aave brw  aave sup
----------------------------------------------------------------------
BTC            10.5%     10.9%     10.9%      9.7%     0.00%     0.00%
ETH            10.5%      2.1%     10.9%     10.9%     0.00%     0.00%
SOL             7.0%    -10.1%     10.9%      4.8%         -         -
ENA            10.5%     10.9%     -0.3%    -97.4%         -         -
HYPE           10.5%    -13.1%      4.4%      3.2%         -         -
LINK            0.9%      2.6%     10.9%     10.9%     0.00%     0.00%
AVAX          -47.3%    -37.3%      8.5%     10.9%         -         -
DOGE            4.4%    -17.9%     10.9%      1.5%         -         -

STABLE BORROW COST (the cost of carrying a hedged position)
  aave   USDe     borrow  0.00%  supply  0.00%
  aave   RLUSD    borrow  3.61%  supply  2.03%
  aave   USDC     borrow  3.79%  supply  2.58%
  aave   RLUSD    borrow  3.81%  supply  2.69%
  aave   GHO      borrow  4.06%  supply  3.27%
  aave   USDC     borrow  4.49%  supply  3.27%
  aave   GHO      borrow  4.53%  supply  3.60%
  aave   USDC     borrow  4.57%  supply  3.75%
  morpho    cbBTC/USDC    borrow  5.25%  lltv 0.86  $347,301,272
  morpho     kBTC/RLUSD   borrow  3.66%  lltv 0.86  $255,139,861
  morpho    PRIME/PYUSD   borrow  5.33%  lltv 0.86  $185,885,347
  morpho PT-reUSD-10DEC2026/USDC    borrow  9.39%  lltv 0.92  $150,187,812
  morpho     WBTC/USDC    borrow  5.26%  lltv 0.86  $140,964,071
  morpho   wstETH/USDT    borrow  3.70%  lltv 0.86  $130,958,378

OFFCHAIN BENCHMARK: SOFR 3.89% (2026-11-06)
  BTC perp funding 10.51% vs SOFR 3.89%: spread +6.62pp over the offchain cost of money

BUILDER-DEPLOYED PERPS: 326 markets, 170 with volume today
  xyz:SP500        OI $  406,428,225  funding      5.5%/yr
  xyz:BRENTOIL     OI $  344,501,412  funding   -282.8%/yr
  xyz:SKHX         OI $  334,585,899  funding    107.0%/yr
  xyz:GOLD         OI $  309,895,698  funding      5.5%/yr
  xyz:NVDA         OI $  245,519,216  funding     30.4%/yr
  xyz:XYZ100       OI $  219,721,302  funding      5.5%/yr
  xyz:SILVER       OI $  199,218,354  funding      5.5%/yr
  xyz:GOOGL        OI $  187,172,389  funding      5.5%/yr
  xyz:MU           OI $  171,649,496  funding     11.1%/yr
  io:ANTH          OI $  155,839,362  funding    -24.9%/yr
```
