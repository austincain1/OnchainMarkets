# 2026-10-11

## Market list changes
```
2026-10-10.json -> 2026-10-11.json

hl:abcd: no change (1 markets)
hl:cash: no change (17 markets)
hl:flx: no change (16 markets)
hl:hyna: no change (25 markets)
hl:io: no change (12 markets)
hl:km: no change (23 markets)
hl:mkts: no change (24 markets)
hl:para: no change (38 markets)
hl:vntl: no change (15 markets)
hl:xyz: 133 -> 134
  NEW     (1): xyz:RELIANCE

hyperliquid: no change (234 markets)
lighter: no change (235 markets)
variational: no change (568 markets)
```

## Funding dispersion
```
205 symbols quoted on 2+ venues. Top 25 by dispersion.

sym             lighter  hyperliqu    binance      bybit     spread      ann  flag
----------------------------------------------------------------------------------
AI              1.0520%    0.0000%    0.0000%          -    1.0520%     1152%/yr
BMNR            0.0288%          -    0.0812%    0.5969%    0.5681%      622%/yr
BOT             0.4504%          -    0.0000%    0.0000%    0.4504%      493%/yr
MINIMAX         0.0032%          -    0.0867%    0.3308%    0.3276%      359%/yr
MSTR            0.1800%    0.2099%    0.0594%    0.3335%    0.2740%      300%/yr
PRL             0.2624%          -    0.0365%    0.0100%    0.2524%      276%/yr
SOXS            0.0032%          -   -0.0584%   -0.1695%    0.1727%      189%/yr  SIGN SPLIT
SOXL            0.1592%          -    0.0662%    0.2282%    0.1621%      177%/yr
CRCL            0.1280%    0.1396%    0.0084%    0.1625%    0.1541%      169%/yr
AXTI            0.0032%          -    0.0000%    0.1324%    0.1324%      145%/yr
S              -0.0024%   -0.0026%   -0.0366%   -0.1313%    0.1289%      141%/yr
COIN            0.1024%    0.1155%    0.0206%    0.1494%    0.1288%      141%/yr
CASHCAT         0.1368%    0.0140%          -    0.0100%    0.1268%      139%/yr
MU              0.0992%          -    0.0066%    0.1256%    0.1191%      130%/yr
HOOD            0.0808%    0.0962%    0.0000%    0.1063%    0.1063%      116%/yr
PIPPIN                -          -    0.1030%    0.0100%    0.0930%      102%/yr
RKLB            0.0032%          -    0.0000%    0.0925%    0.0925%      101%/yr
CRWV            0.0032%          -    0.0000%    0.0914%    0.0914%      100%/yr
DRAM            0.0744%          -    0.0036%    0.0931%    0.0894%       98%/yr
CC              0.0968%    0.0100%    0.0100%    0.0100%    0.0868%       95%/yr
AMD             0.0696%    0.0843%    0.0000%          -    0.0843%       92%/yr
BE              0.0032%          -    0.0000%    0.0811%    0.0811%       89%/yr
SKHYNIX               -    0.1013%    0.0210%    0.0794%    0.0803%       88%/yr
KORU            0.0032%          -    0.0212%    0.0802%    0.0770%       84%/yr
SKHY            0.0752%          -    0.0183%    0.0930%    0.0747%       82%/yr

33 symbols where one venue pays longs while another pays shorts:
  SOXS, STRK, MRNA, XMR, MET, XLM, CHIP, TRX, XRP, LIT, AERO, DOGE, SKY, VIRTUAL, WLFI, PYTH, ARB, JUP, 2Z, 1000PEPE, 1000SHIB, HYPE, FIL, BTC, BCH, SUI, AAVE, BRENTOIL, OP, ADA, ASTER, DYDX, ETH
```

## Builder-deployed markets
```
hl:xyz        134 mkts  OI $ 3,603,577,836  24h $   211,540,664
             XYZ100, TSLA, NVDA, GOLD, HOOD, INTC, PLTR, COIN, META, AAPL, MSFT, ORCL, GOOGL, AMZN, AMD, MU, SNDK, MSTR
hl:io          12 mkts  OI $    65,242,675  24h $    31,389,090
             OAI, ANTH, SNDK, IONQ, NBIS, EWY, GPRO, SBE, TCNT, DRAM, PRL, XIAOMI
hl:para        38 mkts  OI $    17,879,676  24h $     1,133,693
             TOTAL2, OTHERS, BTCD, H100, AVGO, COHR, GLW, CRDO, LRCX, NET, STX, IREN, VST, TER, AAOI, 10Y, CIEN, NAVER
hl:mkts        24 mkts  OI $    11,320,043  24h $     1,000,418
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

total 305 builder markets across 10 dexs
```

## Offchain reference rates (FRED)
```
OFFCHAIN REFERENCE RATES (FRED)

  SOFR      3.87%  2026-10-08     -1bp   Secured Overnight Financing Rate (what a desk funds at)
  DFF       3.88%  2026-10-08     +0bp   Effective fed funds
  IORB      3.90%  2026-10-13     +0bp   Interest on reserve balances
  DGS3MO    4.23%  2026-10-08     +1bp   3-month Treasury
  DGS10     5.22%  2026-10-08     -6bp   10-year Treasury
```

## Carry: funding vs borrow
```
PERP FUNDING (annualized from 8h feed) vs ONCHAIN BORROW

asset        lighter  hyperliq   binance     bybit  aave brw  aave sup
----------------------------------------------------------------------
BTC           -10.5%      5.8%      1.6%     -5.1%     0.00%     0.00%
ETH             2.6%     -2.2%      1.9%      6.2%     0.00%     0.00%
SOL            10.5%     10.9%      9.3%      5.7%         -         -
ENA            10.5%     21.8%     10.9%     10.9%         -         -
HYPE           10.5%     10.9%      1.9%     -5.5%         -         -
LINK           10.5%     10.9%      5.1%      2.8%     0.00%     0.00%
AVAX           10.5%     10.9%     10.9%     10.9%         -         -
DOGE          -15.8%     10.9%      5.8%      5.0%         -         -

STABLE BORROW COST (the cost of carrying a hedged position)
  aave   USDT     borrow  0.11%  supply  0.00%
  aave   GHO      borrow  3.11%  supply  1.70%
  aave   USDC     borrow  3.90%  supply  2.74%
  aave   RLUSD    borrow  3.91%  supply  2.38%
  aave   GHO      borrow  3.99%  supply  3.15%
  aave   GHO      borrow  4.06%  supply  3.26%
  aave   USDC     borrow  4.36%  supply  3.15%
  aave   USDT     borrow  4.41%  supply  3.48%
  morpho    cbBTC/USDC    borrow  5.00%  lltv 0.86  $337,293,335
  morpho     kBTC/RLUSD   borrow  4.12%  lltv 0.86  $235,197,340
  morpho    PRIME/PYUSD   borrow  5.33%  lltv 0.86  $209,660,327
  morpho     kBTC/PYUSD   borrow  4.20%  lltv 0.86  $160,730,064
  morpho   wstETH/USDT    borrow  3.08%  lltv 0.86  $149,858,412
  morpho     WBTC/USDC    borrow  5.08%  lltv 0.86  $128,807,476

OFFCHAIN BENCHMARK: SOFR 3.87% (2026-10-08)
  BTC perp funding -10.51% vs SOFR 3.87%: spread -14.38pp over the offchain cost of money

BUILDER-DEPLOYED PERPS: 305 markets, 155 with volume today
  xyz:SP500        OI $  375,948,559  funding      5.5%/yr
  xyz:GOLD         OI $  301,288,198  funding      5.5%/yr
  xyz:SKHX         OI $  275,053,479  funding    110.6%/yr
  xyz:XYZ100       OI $  240,785,410  funding     17.0%/yr
  xyz:BRENTOIL     OI $  197,547,347  funding    -10.6%/yr
  xyz:SILVER       OI $  158,853,475  funding     19.7%/yr
  xyz:CL           OI $  144,388,215  funding      5.5%/yr
  xyz:SKHY         OI $  141,970,749  funding    100.3%/yr
  xyz:CRCL         OI $  131,405,673  funding    152.3%/yr
  xyz:SPCX         OI $  125,249,675  funding      5.5%/yr
```
