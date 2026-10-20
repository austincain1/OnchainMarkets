# 2026-10-20

## Market list changes
```
2026-10-19.json -> 2026-10-20.json

hl:abcd: no change (1 markets)
hl:cash: no change (17 markets)
hl:flx: no change (16 markets)
hl:hyna: no change (25 markets)
hl:io: no change (14 markets)
hl:km: no change (23 markets)
hl:mkts: no change (24 markets)
hl:para: no change (39 markets)
hl:vntl: no change (15 markets)
hl:xyz: 136 -> 137
  NEW     (1): xyz:TTWO

hyperliquid: no change (234 markets)
lighter: no change (235 markets)
variational: 576 -> 577
  NEW     (1): ASTS

```

## Funding dispersion
```
206 symbols quoted on 2+ venues. Top 25 by dispersion.

sym             lighter  hyperliqu    binance      bybit     spread      ann  flag
----------------------------------------------------------------------------------
PRL             1.0960%          -    0.0100%    0.0100%    1.0860%     1189%/yr
SKHYNIX               -   -0.0872%    0.1265%    0.1559%    0.2431%      266%/yr  SIGN SPLIT
CXMT            0.0032%          -    0.2419%    0.1653%    0.2387%      261%/yr
CASHCAT        -0.2008%    0.0100%          -    0.0100%    0.2108%      231%/yr  SIGN SPLIT
SAMSUNG               -   -0.0075%    0.1916%    0.1414%    0.1991%      218%/yr  SIGN SPLIT
ZHIPU           0.0456%          -    0.1967%    0.0707%    0.1511%      165%/yr
MINIMAX         0.0344%          -    0.1472%    0.1268%    0.1128%      123%/yr
HYUNDAI               -    0.0050%    0.0329%    0.0774%    0.0724%       79%/yr
MET             0.0096%    0.0015%   -0.0183%   -0.0432%    0.0528%       58%/yr  SIGN SPLIT
EDGE            0.0096%          -    0.0591%    0.0100%    0.0495%       54%/yr
QNT            -0.0392%          -    0.0030%    0.0085%    0.0477%       52%/yr  SIGN SPLIT
LIT            -0.0256%    0.0100%    0.0100%    0.0072%    0.0356%       39%/yr  SIGN SPLIT
PYTH           -0.0232%    0.0100%    0.0017%    0.0100%    0.0332%       36%/yr  SIGN SPLIT
TIA             0.0080%    0.0100%   -0.0228%   -0.0154%    0.0328%       36%/yr  SIGN SPLIT
BERA            0.0096%   -0.0220%    0.0100%    0.0100%    0.0320%       35%/yr  SIGN SPLIT
AAVE            0.0072%   -0.0243%    0.0021%    0.0017%    0.0315%       35%/yr  SIGN SPLIT
AAPL            0.0032%    0.0006%    0.0000%   -0.0242%    0.0274%       30%/yr  SIGN SPLIT
WTI             0.0032%    0.0042%    0.0000%   -0.0223%    0.0265%       29%/yr  SIGN SPLIT
S               0.0096%   -0.0164%   -0.0100%    0.0100%    0.0264%       29%/yr  SIGN SPLIT
AAOI            0.0032%          -    0.0000%    0.0258%    0.0258%       28%/yr
GEV             0.0032%          -    0.0000%    0.0258%    0.0258%       28%/yr
LITE            0.0240%          -    0.0000%    0.0000%    0.0240%       26%/yr
AZTEC           0.0096%    0.0100%    0.0325%    0.0100%    0.0229%       25%/yr
POPMART         0.0032%          -    0.0212%    0.0000%    0.0212%       23%/yr
KAITO           0.0096%    0.0100%    0.0100%   -0.0110%    0.0210%       23%/yr  SIGN SPLIT

34 symbols where one venue pays longs while another pays shorts:
  SKHYNIX, CASHCAT, SAMSUNG, MET, QNT, LIT, PYTH, TIA, BERA, AAVE, AAPL, WTI, S, KAITO, ARB, ZK, AXS, PAXG, NEAR, TRX, STONK, SPY, XLM, MEGA, GRAM, 1000BONK, SOXS, STRK, SOL, BCH, DOGE, UNI, PLTR, CRCL
```

## Builder-deployed markets
```
hl:xyz        137 mkts  OI $ 3,881,660,325  24h $ 3,232,538,802
             XYZ100, TSLA, NVDA, GOLD, HOOD, INTC, PLTR, COIN, META, AAPL, MSFT, ORCL, GOOGL, AMZN, AMD, MU, SNDK, MSTR
hl:io          14 mkts  OI $    87,994,198  24h $    94,626,746
             OAI, ANTH, SNDK, IONQ, NBIS, EWY, GPRO, SBE, TCNT, DRAM, PRL, XIAOMI, H100, MOONSHOT
hl:para        39 mkts  OI $    15,868,731  24h $     4,661,930
             TOTAL2, OTHERS, BTCD, H100, AVGO, COHR, GLW, CRDO, LRCX, NET, STX, IREN, VST, TER, AAOI, 10Y, CIEN, NAVER
hl:mkts        24 mkts  OI $    11,169,450  24h $     3,370,126
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

total 311 builder markets across 10 dexs
```

## Offchain reference rates (FRED)
```
OFFCHAIN REFERENCE RATES (FRED)

  SOFR      3.87%  2026-10-19     -1bp   Secured Overnight Financing Rate (what a desk funds at)
  DFF       3.88%  2026-10-16     +0bp   Effective fed funds
  IORB      3.90%  2026-10-20     +0bp   Interest on reserve balances
  DGS3MO    4.26%  2026-10-16     -2bp   3-month Treasury
  DGS10     5.09%  2026-10-16     -1bp   10-year Treasury
```

## Carry: funding vs borrow
```
PERP FUNDING (annualized from 8h feed) vs ONCHAIN BORROW

asset        lighter  hyperliq   binance     bybit  aave brw  aave sup
----------------------------------------------------------------------
BTC            10.5%     10.9%      8.1%      5.1%     0.00%     0.00%
ETH             7.0%     10.9%      7.8%      3.0%     0.00%     0.00%
SOL            -0.9%     10.9%      4.8%     -1.0%         -         -
ENA            10.5%     10.9%     10.9%     10.9%         -         -
HYPE           10.5%      9.0%      6.8%      4.6%         -         -
LINK           10.5%     10.9%     10.9%      9.3%     0.00%     0.00%
AVAX           10.5%     10.9%      4.7%     10.9%         -         -
DOGE           10.5%     10.9%     10.8%     -0.1%         -         -

STABLE BORROW COST (the cost of carrying a hedged position)
  aave   RLUSD    borrow  2.97%  supply  1.38%
  aave   GHO      borrow  4.08%  supply  3.30%
  aave   USDC     borrow  4.18%  supply  3.14%
  aave   GHO      borrow  4.53%  supply  3.60%
  aave   USDC     borrow  4.53%  supply  3.40%
  aave   USDC     borrow  4.63%  supply  3.45%
  aave   GHO      borrow  5.38%  supply  4.36%
  aave   USDe     borrow  6.82%  supply  0.00%
  morpho    cbBTC/USDC    borrow  4.84%  lltv 0.86  $345,399,647
  morpho     kBTC/RLUSD   borrow  3.49%  lltv 0.86  $242,211,634
  morpho    PRIME/PYUSD   borrow  5.19%  lltv 0.86  $205,721,580
  morpho   wstETH/USDT    borrow  5.92%  lltv 0.86  $141,178,346
  morpho PT-reUSD-10DEC2026/USDC    borrow 10.88%  lltv 0.92  $132,391,263
  morpho     WBTC/USDC    borrow  4.87%  lltv 0.86  $131,598,305

OFFCHAIN BENCHMARK: SOFR 3.87% (2026-10-19)
  BTC perp funding 10.51% vs SOFR 3.87%: spread +6.64pp over the offchain cost of money

BUILDER-DEPLOYED PERPS: 311 markets, 164 with volume today
  xyz:SP500        OI $  402,508,957  funding    -12.7%/yr
  xyz:SKHX         OI $  359,527,760  funding    -99.6%/yr
  xyz:XYZ100       OI $  290,905,906  funding      5.5%/yr
  xyz:GOLD         OI $  276,567,694  funding      3.7%/yr
  xyz:BRENTOIL     OI $  211,426,957  funding      5.5%/yr
  xyz:SKHY         OI $  193,541,759  funding     -7.4%/yr
  xyz:GOOGL        OI $  178,236,735  funding     12.3%/yr
  xyz:CL           OI $  167,565,362  funding      4.6%/yr
  xyz:SILVER       OI $  159,396,200  funding      5.5%/yr
  xyz:MU           OI $  150,448,529  funding      5.5%/yr
```
