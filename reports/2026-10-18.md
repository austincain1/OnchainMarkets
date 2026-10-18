# 2026-10-18

## Market list changes
```
2026-10-17.json -> 2026-10-18.json

hl:abcd: no change (1 markets)
hl:cash: no change (17 markets)
hl:flx: no change (16 markets)
hl:hyna: no change (25 markets)
hl:io: no change (13 markets)
hl:km: no change (23 markets)
hl:mkts: no change (24 markets)
hl:para: 38 -> 39
  NEW     (1): para:PAPER

hl:vntl: no change (15 markets)
hl:xyz: no change (136 markets)
hyperliquid: no change (234 markets)
lighter: no change (235 markets)
variational: no change (575 markets)
```

## Funding dispersion
```
206 symbols quoted on 2+ venues. Top 25 by dispersion.

sym             lighter  hyperliqu    binance      bybit     spread      ann  flag
----------------------------------------------------------------------------------
PRL             0.5840%          -    0.0100%    0.0100%    0.5740%      629%/yr
CASHCAT        -0.2320%    0.0100%          -    0.0100%    0.2420%      265%/yr  SIGN SPLIT
KORU            0.0032%          -   -0.1647%   -0.1698%    0.1730%      189%/yr  SIGN SPLIT
MSTR           -0.1752%   -0.2051%   -0.0381%   -0.0605%    0.1671%      183%/yr
COIN           -0.1296%   -0.1617%   -0.0215%   -0.0085%    0.1532%      168%/yr
CRCL           -0.1520%   -0.1735%   -0.0349%   -0.0599%    0.1386%      152%/yr
SOXS            0.0032%          -    0.1340%    0.1340%    0.1308%      143%/yr
HOOD           -0.0952%   -0.1140%    0.0000%   -0.0109%    0.1140%      125%/yr
TSLA           -0.0792%   -0.1001%    0.0000%    0.0000%    0.1001%      110%/yr
SAMSUNG               -   -0.1464%   -0.0757%   -0.0463%    0.1001%      110%/yr
INTC           -0.1480%   -0.1780%   -0.0817%   -0.1065%    0.0963%      105%/yr
BERA            0.0016%   -0.0928%   -0.0537%   -0.0719%    0.0944%      103%/yr  SIGN SPLIT
AMD            -0.1288%   -0.1516%   -0.0587%          -    0.0929%      102%/yr
SMIC           -0.0920%          -          -    0.0000%    0.0920%      101%/yr
BE              0.0032%          -   -0.0206%   -0.0800%    0.0832%       91%/yr  SIGN SPLIT
SNDK           -0.1144%   -0.1360%   -0.0529%   -0.0772%    0.0831%       91%/yr
SOXL           -0.1944%          -   -0.1163%   -0.1152%    0.0792%       87%/yr
WDC             0.0032%          -   -0.0238%   -0.0746%    0.0778%       85%/yr  SIGN SPLIT
NVDA           -0.0624%   -0.0774%   -0.0023%    0.0000%    0.0774%       85%/yr
CBRS           -0.0760%          -   -0.0031%   -0.0002%    0.0758%       83%/yr
MRVL           -0.0936%          -   -0.0197%   -0.0514%    0.0739%       81%/yr
ARM             0.0032%          -   -0.0141%   -0.0692%    0.0724%       79%/yr  SIGN SPLIT
HYUNDAI               -   -0.0702%    0.0000%    0.0000%    0.0702%       77%/yr
BMNR           -0.1088%          -   -0.0993%   -0.1694%    0.0701%       77%/yr
SKHYNIX               -   -0.1135%   -0.0896%   -0.0454%    0.0681%       75%/yr

85 symbols where one venue pays longs while another pays shorts:
  CASHCAT, KORU, BERA, BE, WDC, ARM, CXMT, PROVE, 2Z, WLD, MON, MORPHO, AVAX, TSM, LIT, AXTI, PONS, UNI, TRUMP, SPX, DOT, ZRO, SPCX, ADA, GRAM, MET, APT, JUP, AAVE, ZORA, PAXG, OP, ETHFI, WLFI, VIRTUAL, XLM, XCU, CC, JTO, TIA
```

## Builder-deployed markets
```
hl:xyz        136 mkts  OI $ 3,743,271,964  24h $   866,894,183
             XYZ100, TSLA, NVDA, GOLD, HOOD, INTC, PLTR, COIN, META, AAPL, MSFT, ORCL, GOOGL, AMZN, AMD, MU, SNDK, MSTR
hl:io          13 mkts  OI $    68,273,100  24h $    46,541,343
             OAI, ANTH, SNDK, IONQ, NBIS, EWY, GPRO, SBE, TCNT, DRAM, PRL, XIAOMI, H100
hl:para        39 mkts  OI $    19,223,120  24h $     7,868,315
             TOTAL2, OTHERS, BTCD, H100, AVGO, COHR, GLW, CRDO, LRCX, NET, STX, IREN, VST, TER, AAOI, 10Y, CIEN, NAVER
hl:mkts        24 mkts  OI $    10,299,145  24h $     1,245,805
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

total 309 builder markets across 10 dexs
```

## Offchain reference rates (FRED)
```
OFFCHAIN REFERENCE RATES (FRED)

  SOFR      3.89%  2026-10-15     +1bp   Secured Overnight Financing Rate (what a desk funds at)
  DFF       3.88%  2026-10-15     +0bp   Effective fed funds
  IORB      3.90%  2026-10-19     +0bp   Interest on reserve balances
  DGS3MO    4.28%  2026-10-15     +0bp   3-month Treasury
  DGS10     5.10%  2026-10-15     -9bp   10-year Treasury
```

## Carry: funding vs borrow
```
PERP FUNDING (annualized from 8h feed) vs ONCHAIN BORROW

asset        lighter  hyperliq   binance     bybit  aave brw  aave sup
----------------------------------------------------------------------
BTC            10.5%      2.3%     10.6%      3.0%     0.00%     0.00%
ETH            -1.8%      4.2%      6.1%      5.2%     0.00%     0.00%
SOL           -14.9%    -18.2%     -2.2%     -7.9%         -         -
ENA           -20.1%    -23.2%     -2.7%    -14.4%         -         -
HYPE            3.5%     10.9%      2.1%     -1.9%         -         -
LINK           -0.9%     10.9%      1.7%      2.4%     0.00%     0.00%
AVAX           -9.6%    -44.0%     -2.4%      3.4%         -         -
DOGE           10.5%     -2.2%     -4.4%     -8.4%         -         -

STABLE BORROW COST (the cost of carrying a hedged position)
  aave   GHO      borrow  3.11%  supply  1.70%
  aave   RLUSD    borrow  3.85%  supply  2.31%
  aave   GHO      borrow  4.05%  supply  3.24%
  aave   USDT     borrow  4.05%  supply  2.94%
  aave   GHO      borrow  4.08%  supply  3.30%
  aave   USDT     borrow  4.31%  supply  3.33%
  aave   USDC     borrow  4.32%  supply  3.34%
  aave   USDC     borrow  4.51%  supply  3.37%
  morpho    cbBTC/USDC    borrow  5.01%  lltv 0.86  $343,205,940
  morpho     kBTC/RLUSD   borrow  3.50%  lltv 0.86  $243,181,052
  morpho    PRIME/PYUSD   borrow  5.40%  lltv 0.86  $206,335,943
  morpho   wstETH/USDT    borrow  2.96%  lltv 0.86  $144,280,760
  morpho     kBTC/PYUSD   borrow  4.00%  lltv 0.86  $141,949,793
  morpho PT-reUSD-10DEC2026/USDC    borrow  8.21%  lltv 0.92  $135,707,408

OFFCHAIN BENCHMARK: SOFR 3.89% (2026-10-15)
  BTC perp funding 10.51% vs SOFR 3.89%: spread +6.62pp over the offchain cost of money

BUILDER-DEPLOYED PERPS: 309 markets, 163 with volume today
  xyz:SKHX         OI $  371,389,033  funding   -126.1%/yr
  xyz:SP500        OI $  351,784,878  funding     -6.3%/yr
  xyz:XYZ100       OI $  314,768,378  funding    -39.5%/yr
  xyz:GOLD         OI $  281,915,365  funding     -6.3%/yr
  xyz:SKHY         OI $  187,864,460  funding   -107.3%/yr
  xyz:BRENTOIL     OI $  184,872,627  funding     18.4%/yr
  xyz:MU           OI $  162,595,958  funding    -94.0%/yr
  xyz:SILVER       OI $  159,201,556  funding    -56.7%/yr
  xyz:CL           OI $  150,869,219  funding      8.6%/yr
  xyz:SNDK         OI $  125,734,951  funding   -149.2%/yr
```
