# 2026-11-22

## Market list changes
```
2026-11-21.json -> 2026-11-22.json

hl:abcd: no change (1 markets)
hl:cash: no change (17 markets)
hl:flx: no change (16 markets)
hl:hyna: no change (25 markets)
hl:io: 25 -> 26
  NEW     (1): io:SOXL

hl:km: no change (23 markets)
hl:mkts: no change (24 markets)
hl:para: no change (40 markets)
hl:vntl: no change (15 markets)
hl:xyz: no change (147 markets)
hyperliquid: no change (235 markets)
lighter: no change (235 markets)
variational: no change (595 markets)
```

## Funding dispersion
```
206 symbols quoted on 2+ venues. Top 25 by dispersion.

sym             lighter  hyperliqu    binance      bybit     spread      ann  flag
----------------------------------------------------------------------------------
BB              0.0032%          -    0.0100%   -0.4172%    0.4272%      468%/yr  SIGN SPLIT
IREN            0.0032%          -    0.0068%    0.2935%    0.2903%      318%/yr
SNDK            0.3056%    0.3370%    0.0579%    0.3004%    0.2792%      306%/yr
DRV            -0.0264%          -          -   -0.2716%    0.2452%      269%/yr
SOXS                  -          -   -0.0217%   -0.1968%    0.1751%      192%/yr
PRL             0.1736%          -    0.0100%    0.0100%    0.1636%      179%/yr
NBIS            0.1304%          -    0.0268%    0.1869%    0.1600%      175%/yr
AI             -0.1584%    0.0000%    0.0000%          -    0.1584%      173%/yr
SOXL            0.0712%          -    0.0057%    0.1284%    0.1226%      134%/yr
BERA           -0.0856%   -0.1909%   -0.1006%   -0.0772%    0.1137%      125%/yr
NATGAS         -0.0872%   -0.1214%   -0.0131%          -    0.1083%      119%/yr
MET             0.0096%   -0.0942%   -0.0142%   -0.0071%    0.1038%      114%/yr  SIGN SPLIT
SKHY            0.0736%          -    0.0000%    0.1030%    0.1030%      113%/yr
KORU            0.1192%          -    0.0917%    0.1936%    0.1019%      112%/yr
MSTR           -0.0576%   -0.0987%    0.0000%   -0.1010%    0.1010%      111%/yr
SKHYNIX               -    0.0850%    0.0000%    0.0716%    0.0850%       93%/yr
MU              0.0808%          -    0.0000%    0.0291%    0.0808%       88%/yr
JUP            -0.0656%   -0.0489%   -0.0056%    0.0100%    0.0756%       83%/yr  SIGN SPLIT
AAOI            0.0456%          -    0.0000%    0.0728%    0.0728%       80%/yr
SAMSUNG               -    0.0776%    0.0051%    0.0592%    0.0725%       79%/yr
VVV             0.0576%    0.0100%    0.0100%   -0.0105%    0.0681%       75%/yr  SIGN SPLIT
EWY             0.0256%          -    0.0000%    0.0655%    0.0655%       72%/yr
DRAM            0.0648%          -    0.0000%    0.0530%    0.0648%       71%/yr
STBL            0.0728%    0.0100%    0.0100%    0.0100%    0.0628%       69%/yr
TRUMP           0.0096%   -0.0510%   -0.0088%    0.0100%    0.0610%       67%/yr  SIGN SPLIT

74 symbols where one venue pays longs while another pays shorts:
  BB, MET, JUP, VVV, TRUMP, BCH, MNT, BIRB, POL, OP, GMX, ZRO, 1000BONK, UNITREE, ZK, CHIP, ROBO, MORPHO, ZORA, MEGA, AVAX, CRV, ARB, DYDX, LINK, 1000PEPE, ETHFI, ICP, SKY, BTC, FF, TAO, WLD, TIA, XLM, PENGU, 1000SHIB, NMR, PUMP, LINEA
```

## Builder-deployed markets
```
hl:xyz        147 mkts  OI $ 4,391,493,159  24h $   698,087,716
             XYZ100, TSLA, NVDA, GOLD, HOOD, INTC, PLTR, COIN, META, AAPL, MSFT, ORCL, GOOGL, AMZN, AMD, MU, SNDK, MSTR
hl:io          26 mkts  OI $   113,747,412  24h $    18,786,195
             OAI, ANTH, SNDK, IONQ, NBIS, EWY, GPRO, SBE, TCNT, DRAM, PRL, XIAOMI, H100, MOONSHOT, NVDA, SKHX, AAPL, CRCL
hl:para        40 mkts  OI $    13,274,262  24h $    10,957,552
             TOTAL2, OTHERS, BTCD, H100, AVGO, COHR, GLW, CRDO, LRCX, NET, STX, IREN, VST, TER, AAOI, 10Y, CIEN, NAVER
hl:mkts        24 mkts  OI $       129,699  24h $       245,373
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

total 334 builder markets across 10 dexs
```

## Offchain reference rates (FRED)
```
OFFCHAIN REFERENCE RATES (FRED)

  SOFR      3.91%  2026-11-19     +1bp   Secured Overnight Financing Rate (what a desk funds at)
  DFF       3.88%  2026-11-19     +0bp   Effective fed funds
  IORB      3.90%  2026-11-23     +0bp   Interest on reserve balances
  DGS3MO    4.34%  2026-11-19     +0bp   3-month Treasury
  DGS10     5.04%  2026-11-19     -3bp   10-year Treasury
```

## Carry: funding vs borrow
```
PERP FUNDING (annualized from 8h feed) vs ONCHAIN BORROW

asset        lighter  hyperliq   binance     bybit  aave brw  aave sup
----------------------------------------------------------------------
BTC            10.5%    -19.4%      0.4%      1.5%     0.00%     0.00%
ETH            10.5%     -1.9%      6.1%      0.2%     0.00%     0.00%
SOL            -4.4%      3.5%      1.7%      4.7%         -         -
ENA            10.5%     10.9%     -4.3%     -2.3%         -         -
HYPE            9.6%     10.9%      6.9%     -7.0%         -         -
LINK          -24.5%      6.5%      2.2%     -8.4%     0.00%     0.00%
AVAX            7.0%    -27.1%    -14.8%    -11.7%         -         -
DOGE           10.5%      2.4%      3.0%      0.8%         -         -

STABLE BORROW COST (the cost of carrying a hedged position)
  aave   USDe     borrow  0.00%  supply  0.00%
  aave   RLUSD    borrow  3.78%  supply  2.22%
  aave   USDC     borrow  3.78%  supply  2.57%
  aave   USDC     borrow  3.86%  supply  2.68%
  aave   RLUSD    borrow  4.06%  supply  3.41%
  aave   GHO      borrow  4.07%  supply  3.28%
  aave   GHO      borrow  4.07%  supply  3.29%
  aave   GHO      borrow  4.36%  supply  3.33%
  morpho    cbBTC/USDC    borrow  3.82%  lltv 0.86  $271,652,373
  morpho     kBTC/RLUSD   borrow  3.30%  lltv 0.86  $161,465,867
  morpho     WBTC/USDC    borrow  3.83%  lltv 0.86  $156,251,113
  morpho PT-reUSD-10DEC2026/USDC    borrow  8.88%  lltv 0.92  $131,763,250
  morpho    PRIME/PYUSD   borrow  6.22%  lltv 0.86  $128,888,933
  morpho   wstETH/USDT    borrow  3.52%  lltv 0.86  $119,743,084

OFFCHAIN BENCHMARK: SOFR 3.91% (2026-11-19)
  BTC perp funding 10.51% vs SOFR 3.91%: spread +6.60pp over the offchain cost of money

BUILDER-DEPLOYED PERPS: 334 markets, 175 with volume today
  xyz:NVDA         OI $  514,952,371  funding     -4.3%/yr
  xyz:SP500        OI $  492,487,669  funding      5.5%/yr
  xyz:XYZ100       OI $  398,060,218  funding      5.5%/yr
  xyz:BRENTOIL     OI $  307,474,809  funding      9.5%/yr
  xyz:SKHX         OI $  269,074,911  funding     90.0%/yr
  xyz:GOLD         OI $  261,077,943  funding      5.5%/yr
  xyz:ANT          OI $  247,284,283  funding      9.7%/yr
  xyz:SILVER       OI $  173,162,157  funding      5.5%/yr
  xyz:MU           OI $  148,948,422  funding     97.9%/yr
  xyz:CL           OI $  139,408,783  funding      5.5%/yr
```
