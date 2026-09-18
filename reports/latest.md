# 2026-09-18

## Market list changes
```
need 2 snapshots, have 1
```

## Funding dispersion
```
207 symbols quoted on 2+ venues. Top 25 by dispersion.

sym             lighter  hyperliqu    binance      bybit     spread      ann  flag
----------------------------------------------------------------------------------
XMR             0.4336%    0.3839%    0.1463%    0.2972%    0.2873%      315%/yr
AZTEC           0.0976%    0.2907%    0.0100%    0.0100%    0.2807%      307%/yr
GRASS           0.1448%    0.1135%    0.0100%    0.0100%    0.1348%      148%/yr
RAY             0.1160%          -    0.0000%          -    0.1160%      127%/yr
GRAM            0.1160%    0.0234%    0.0100%    0.0100%    0.1060%      116%/yr
ZHIPU          -0.0264%          -   -0.1041%    0.0000%    0.1041%      114%/yr
PROVE           0.0096%    0.0100%    0.0100%   -0.0892%    0.0992%      109%/yr  SIGN SPLIT
MYX             0.0760%          -    0.1057%    0.0100%    0.0957%      105%/yr
S              -0.0688%   -0.0004%    0.0100%    0.0100%    0.0788%       86%/yr  SIGN SPLIT
CRWV            0.0032%          -    0.0180%    0.0727%    0.0695%       76%/yr
1000PEPE        0.0096%    0.0738%    0.0100%    0.0100%    0.0642%       70%/yr
XAU             0.0200%    0.0072%    0.0478%    0.0675%    0.0603%       66%/yr
MEGA            0.0096%    0.0638%    0.0100%    0.0100%    0.0542%       59%/yr
CTR             0.0096%          -    0.0622%    0.0100%    0.0526%       58%/yr
EIGEN           0.0592%    0.0100%    0.0100%    0.0100%    0.0492%       54%/yr
LIT             0.0200%    0.0146%    0.0100%   -0.0272%    0.0472%       52%/yr  SIGN SPLIT
ONDO            0.0096%    0.0563%    0.0100%    0.0100%    0.0467%       51%/yr
USELESS         0.0096%    0.0561%    0.0100%    0.0100%    0.0465%       51%/yr
HBAR           -0.0360%    0.0100%    0.0048%    0.0100%    0.0460%       50%/yr  SIGN SPLIT
AERO            0.0544%    0.0209%    0.0100%    0.0100%    0.0444%       49%/yr
CC              0.0520%    0.0220%    0.0100%    0.0100%    0.0420%       46%/yr
NEAR            0.0504%    0.0100%    0.0100%    0.0100%    0.0404%       44%/yr
VVV             0.0376%    0.0488%    0.0100%    0.0100%    0.0388%       43%/yr
MORPHO          0.0464%    0.0100%    0.0100%    0.0100%    0.0364%       40%/yr
CRV             0.0096%    0.0460%    0.0100%    0.0100%    0.0364%       40%/yr

23 symbols where one venue pays longs while another pays shorts:
  PROVE, S, LIT, HBAR, UNI, MINIMAX, BOT, ZEC, PENGU, TRUMP, PUMP, SPY, JTO, 2Z, FF, POL, XPL, DELL, TRX, STABLE, XLM, PLTR, AAPL
```

## Builder-deployed markets
```
hl:xyz        123 mkts  OI $ 3,831,628,966  24h $ 1,871,258,839
             XYZ100, TSLA, NVDA, GOLD, HOOD, INTC, PLTR, COIN, META, AAPL, MSFT, ORCL, GOOGL, AMZN, AMD, MU, SNDK, MSTR
hl:io          10 mkts  OI $    56,105,958  24h $    25,271,929
             OAI, ANTH, SNDK, IONQ, NBIS, EWY, GPRO, SBE, TCNT, DRAM
hl:para        35 mkts  OI $    16,640,969  24h $     6,288,774
             TOTAL2, OTHERS, BTCD, H100, AVGO, COHR, GLW, CRDO, LRCX, NET, STX, IREN, VST, TER, AAOI, 10Y, CIEN, NAVER
hl:mkts        24 mkts  OI $     7,314,688  24h $    12,591,790
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

total 289 builder markets across 10 dexs
```

## Carry: funding vs borrow
```
PERP FUNDING (annualized from 8h feed) vs ONCHAIN BORROW

asset        lighter  hyperliq   binance     bybit  aave brw  aave sup
----------------------------------------------------------------------
BTC            10.5%     10.9%      6.8%     10.9%     0.00%     0.00%
ETH            10.5%     10.9%     10.9%     10.9%     0.00%     0.00%
SOL            10.5%     10.9%     10.9%     10.9%         -         -
ENA            10.5%     10.9%      7.3%     10.9%         -         -
HYPE           10.5%     15.7%     10.9%      7.5%         -         -
LINK           10.5%     10.9%     10.9%     10.9%     0.00%     0.00%
AVAX           10.5%     10.9%     10.9%     10.9%         -         -
DOGE           10.5%     10.9%     10.9%     10.9%         -         -

STABLE BORROW COST (the cost of carrying a hedged position)
  aave   USDT     borrow  2.21%  supply  1.01%
  aave   USDC     borrow  3.15%  supply  2.05%
  aave   GHO      borrow  3.49%  supply  2.19%
  aave   GHO      borrow  3.65%  supply  2.71%
  aave   GHO      borrow  3.75%  supply  2.86%
  aave   USDT     borrow  3.77%  supply  2.94%
  aave   RLUSD    borrow  3.80%  supply  2.32%
  aave   USDT     borrow  3.97%  supply  3.27%
  morpho    cbBTC/USDC    borrow  4.60%  lltv 0.86  $343,514,608
  morpho     kBTC/RLUSD   borrow  3.07%  lltv 0.86  $205,109,327
  morpho    PRIME/PYUSD   borrow  4.75%  lltv 0.86  $183,454,144
  morpho     kBTC/PYUSD   borrow  6.68%  lltv 0.86  $150,041,143
  morpho   wstETH/USDT    borrow  2.96%  lltv 0.86  $133,339,316
  morpho     WBTC/USDC    borrow  4.61%  lltv 0.86  $126,212,485

BUILDER-DEPLOYED PERPS: 289 markets, 147 with volume today
  xyz:SP500        OI $  420,229,229  funding    -11.4%/yr
  xyz:SKHX         OI $  338,935,736  funding     18.7%/yr
  xyz:GOLD         OI $  296,163,266  funding      7.9%/yr
  xyz:XYZ100       OI $  255,723,425  funding      5.5%/yr
  xyz:SKHY         OI $  192,775,778  funding     -9.4%/yr
  xyz:CL           OI $  170,723,827  funding    -10.3%/yr
  xyz:SILVER       OI $  163,720,964  funding      5.8%/yr
  xyz:BRENTOIL     OI $  158,004,347  funding      2.6%/yr
  xyz:SPCX         OI $  156,789,571  funding      5.5%/yr
  xyz:MU           OI $  143,421,367  funding      5.5%/yr
```
