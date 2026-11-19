# 2026-11-19

## Market list changes
```
2026-11-18.json -> 2026-11-19.json

hl:abcd: no change (1 markets)
hl:cash: no change (17 markets)
hl:flx: no change (16 markets)
hl:hyna: no change (25 markets)
hl:io: no change (24 markets)
hl:km: no change (23 markets)
hl:mkts: no change (24 markets)
hl:para: no change (40 markets)
hl:vntl: no change (15 markets)
hl:xyz: 146 -> 147
  NEW     (1): xyz:SMCI

hyperliquid: no change (235 markets)
lighter: no change (235 markets)
variational: 592 -> 594
  NEW     (2): PFE, VKTX

```

## Funding dispersion
```
206 symbols quoted on 2+ venues. Top 25 by dispersion.

sym             lighter  hyperliqu    binance      bybit     spread      ann  flag
----------------------------------------------------------------------------------
ZHIPU          -0.0800%          -   -0.4472%   -0.4020%    0.3672%      402%/yr
MINIMAX        -0.1144%          -   -0.4533%   -0.3132%    0.3389%      371%/yr
CXMT           -0.0552%          -   -0.2360%   -0.1444%    0.1808%      198%/yr
SKY             0.0096%   -0.1086%   -0.0350%   -0.0481%    0.1182%      129%/yr  SIGN SPLIT
HYUNDAI               -   -0.0992%    0.0000%    0.0000%    0.0992%      109%/yr
WEN            -0.0760%          -    0.0000%          -    0.0760%       83%/yr
IREN            0.0736%          -    0.0347%    0.1061%    0.0714%       78%/yr
ARC             0.0248%          -    0.0100%    0.0703%    0.0603%       66%/yr
BB              0.0032%          -   -0.0502%    0.0100%    0.0602%       66%/yr  SIGN SPLIT
UNITREE        -0.1072%          -   -0.1392%   -0.1662%    0.0590%       65%/yr
WLFI           -0.0096%    0.0033%    0.0100%   -0.0456%    0.0556%       61%/yr  SIGN SPLIT
BMNR            0.0032%          -    0.0133%    0.0584%    0.0552%       60%/yr
AAVE           -0.0496%   -0.0006%    0.0034%    0.0031%    0.0530%       58%/yr  SIGN SPLIT
POL            -0.0424%    0.0100%    0.0010%   -0.0170%    0.0524%       57%/yr  SIGN SPLIT
AVNT           -0.0232%   -0.0156%    0.0048%   -0.0464%    0.0512%       56%/yr  SIGN SPLIT
VVV             0.0576%    0.0100%    0.0100%    0.0100%    0.0476%       52%/yr
SMIC           -0.0464%          -          -   -0.0004%    0.0460%       50%/yr
DRV             0.0096%          -          -   -0.0357%    0.0453%       50%/yr  SIGN SPLIT
WLD            -0.0272%   -0.0022%   -0.0209%   -0.0462%    0.0440%       48%/yr
XPT             0.0144%    0.0195%    0.0582%          -    0.0438%       48%/yr
CRV            -0.0312%    0.0100%   -0.0061%    0.0037%    0.0412%       45%/yr  SIGN SPLIT
BERA           -0.0040%   -0.0385%    0.0003%   -0.0109%    0.0388%       42%/yr  SIGN SPLIT
1000PEPE        0.0096%    0.0100%   -0.0094%   -0.0268%    0.0368%       40%/yr  SIGN SPLIT
KORU            0.0072%          -    0.0423%    0.0062%    0.0361%       40%/yr
ROBO           -0.0256%          -   -0.0071%    0.0100%    0.0356%       39%/yr  SIGN SPLIT

64 symbols where one venue pays longs while another pays shorts:
  SKY, BB, WLFI, AAVE, POL, AVNT, DRV, CRV, BERA, 1000PEPE, ROBO, VIRTUAL, 2Z, TRUMP, SEI, MON, TIA, HYPE, CC, FIL, LTC, BCH, CASHCAT, PYTH, OP, 0G, 1000BONK, STRK, ASTER, PENGU, 1000FLOKI, S, ARB, TRX, PRL, ZK, DOGE, PENDLE, MNT, LINK
```

## Builder-deployed markets
```
hl:xyz        147 mkts  OI $ 4,112,964,050  24h $ 5,816,500,013
             XYZ100, TSLA, NVDA, GOLD, HOOD, INTC, PLTR, COIN, META, AAPL, MSFT, ORCL, GOOGL, AMZN, AMD, MU, SNDK, MSTR
hl:io          24 mkts  OI $   189,417,449  24h $   219,601,776
             OAI, ANTH, SNDK, IONQ, NBIS, EWY, GPRO, SBE, TCNT, DRAM, PRL, XIAOMI, H100, MOONSHOT, NVDA, SKHX, AAPL, CRCL
hl:para        40 mkts  OI $    13,731,905  24h $     5,473,523
             TOTAL2, OTHERS, BTCD, H100, AVGO, COHR, GLW, CRDO, LRCX, NET, STX, IREN, VST, TER, AAOI, 10Y, CIEN, NAVER
hl:mkts        24 mkts  OI $       315,351  24h $       249,152
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

total 332 builder markets across 10 dexs
```

## Offchain reference rates (FRED)
```
OFFCHAIN REFERENCE RATES (FRED)

  SOFR      3.90%  2026-11-18     -2bp   Secured Overnight Financing Rate (what a desk funds at)
  DFF       3.88%  2026-11-17     +0bp   Effective fed funds
  IORB      3.90%  2026-11-19     +0bp   Interest on reserve balances
  DGS3MO    4.33%  2026-11-17     -1bp   3-month Treasury
  DGS10     5.10%  2026-11-17     -2bp   10-year Treasury
```

## Carry: funding vs borrow
```
PERP FUNDING (annualized from 8h feed) vs ONCHAIN BORROW

asset        lighter  hyperliq   binance     bybit  aave brw  aave sup
----------------------------------------------------------------------
BTC            10.5%     10.9%     10.9%      5.0%     0.00%     0.00%
ETH            10.5%      7.1%      3.2%      7.5%     0.00%     0.00%
SOL            10.5%     -0.1%      6.6%     -5.7%         -         -
ENA            10.5%     10.9%      1.8%     10.9%         -         -
HYPE          -20.1%     10.9%      7.9%     -1.4%         -         -
LINK           10.5%     10.9%      4.1%     -9.1%     0.00%     0.00%
AVAX          -13.1%    -10.1%     -8.3%    -27.3%         -         -
DOGE           10.5%      2.3%     -5.9%    -11.2%         -         -

STABLE BORROW COST (the cost of carrying a hedged position)
  aave   USDe     borrow  0.00%  supply  0.00%
  aave   RLUSD    borrow  3.76%  supply  2.21%
  aave   USDC     borrow  3.78%  supply  2.57%
  aave   RLUSD    borrow  3.80%  supply  2.62%
  aave   GHO      borrow  3.94%  supply  3.07%
  aave   GHO      borrow  3.99%  supply  3.16%
  aave   USDC     borrow  4.13%  supply  3.06%
  aave   GHO      borrow  4.36%  supply  3.33%
  morpho    cbBTC/USDC    borrow  5.24%  lltv 0.86  $328,263,203
  morpho    PRIME/PYUSD   borrow  8.06%  lltv 0.86  $163,833,337
  morpho     kBTC/RLUSD   borrow  3.45%  lltv 0.86  $161,868,311
  morpho PT-reUSD-10DEC2026/USDC    borrow 19.61%  lltv 0.92  $131,548,036
  morpho     WBTC/USDC    borrow  5.31%  lltv 0.86  $121,054,085
  morpho   wstETH/USDT    borrow  3.56%  lltv 0.86  $118,645,324

OFFCHAIN BENCHMARK: SOFR 3.90% (2026-11-18)
  BTC perp funding 10.51% vs SOFR 3.90%: spread +6.61pp over the offchain cost of money

BUILDER-DEPLOYED PERPS: 332 markets, 174 with volume today
  xyz:SP500        OI $  447,568,821  funding     15.9%/yr
  xyz:NVDA         OI $  371,278,459  funding     14.7%/yr
  xyz:BRENTOIL     OI $  299,103,054  funding      7.6%/yr
  xyz:ANT          OI $  293,571,932  funding     -6.1%/yr
  xyz:XYZ100       OI $  263,137,502  funding      5.5%/yr
  xyz:SKHX         OI $  249,812,831  funding   -185.7%/yr
  xyz:GOLD         OI $  247,567,411  funding     14.7%/yr
  io:ANTH          OI $  156,428,298  funding      5.5%/yr
  xyz:MU           OI $  146,693,839  funding     12.3%/yr
  xyz:SILVER       OI $  145,407,921  funding     22.5%/yr
```
