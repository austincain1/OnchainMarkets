# 2026-10-16

## Market list changes
```
2026-10-15.json -> 2026-10-16.json

hl:abcd: no change (1 markets)
hl:cash: no change (17 markets)
hl:flx: no change (16 markets)
hl:hyna: no change (25 markets)
hl:io: no change (13 markets)
hl:km: no change (23 markets)
hl:mkts: no change (24 markets)
hl:para: no change (38 markets)
hl:vntl: no change (15 markets)
hl:xyz: no change (135 markets)
hyperliquid: no change (234 markets)
lighter: no change (235 markets)
variational: 574 -> 575
  NEW     (2): PENG, US2KS
  REMOVED (1): PROMPT

```

## Funding dispersion
```
206 symbols quoted on 2+ venues. Top 25 by dispersion.

sym             lighter  hyperliqu    binance      bybit     spread      ann  flag
----------------------------------------------------------------------------------
CASHCAT        -0.5464%    0.0100%          -    0.0100%    0.5564%      609%/yr  SIGN SPLIT
SAMSUNG               -   -0.2536%   -0.0449%   -0.0272%    0.2264%      248%/yr
SKHYNIX               -   -0.2205%   -0.0801%   -0.0086%    0.2119%      232%/yr
ROBO           -0.1400%          -    0.0073%    0.0100%    0.1500%      164%/yr  SIGN SPLIT
APEX            0.0096%    0.1485%          -    0.0100%    0.1389%      152%/yr
BERA            0.0096%   -0.0644%   -0.1216%   -0.0847%    0.1312%      144%/yr  SIGN SPLIT
AI              0.1176%    0.0000%    0.0000%          -    0.1176%      129%/yr
USDJPY          0.0000%   -0.0096%          -   -0.1027%    0.1027%      112%/yr
HYUNDAI               -   -0.1007%    0.0000%    0.0000%    0.1007%      110%/yr
MINIMAX        -0.0752%          -    0.0000%    0.0000%    0.0752%       82%/yr
CXMT           -0.0968%          -   -0.1624%   -0.1133%    0.0656%       72%/yr
S               0.0096%   -0.0330%   -0.0183%   -0.0516%    0.0612%       67%/yr  SIGN SPLIT
ZHIPU          -0.0568%          -    0.0000%    0.0000%    0.0568%       62%/yr
MORPHO          0.0096%    0.0100%   -0.0035%   -0.0375%    0.0475%       52%/yr  SIGN SPLIT
RIVER           0.0096%          -    0.0126%    0.0524%    0.0428%       47%/yr
SKY             0.0096%   -0.0314%    0.0051%   -0.0033%    0.0410%       45%/yr  SIGN SPLIT
XPT             0.0400%    0.0050%    0.0000%          -    0.0400%       44%/yr
LITE            0.0360%          -    0.0000%    0.0000%    0.0360%       39%/yr
HYPE            0.0096%   -0.0256%   -0.0011%    0.0005%    0.0352%       39%/yr  SIGN SPLIT
UNITREE         0.0032%          -    0.0000%   -0.0312%    0.0344%       38%/yr  SIGN SPLIT
SKR             0.0096%    0.0100%    0.0100%   -0.0219%    0.0319%       35%/yr  SIGN SPLIT
AMD             0.0312%    0.0152%    0.0000%          -    0.0312%       34%/yr
MET             0.0096%   -0.0145%    0.0059%   -0.0213%    0.0309%       34%/yr  SIGN SPLIT
MEGA            0.0096%    0.0100%    0.0027%   -0.0204%    0.0304%       33%/yr  SIGN SPLIT
SOXL            0.0624%          -    0.0325%    0.0346%    0.0299%       33%/yr

50 symbols where one venue pays longs while another pays shorts:
  CASHCAT, ROBO, BERA, S, MORPHO, SKY, HYPE, UNITREE, SKR, MET, MEGA, ADA, LIT, WIF, JUP, WTI, POL, PYTH, XLM, ASTER, BRENTOIL, MON, MNT, 1000PEPE, CHIP, LINK, XCU, SEI, STRK, SOL, ONDO, PLTR, BOT, AXS, DUSK, AAVE, BNB, DOGE, NEAR, OP
```

## Builder-deployed markets
```
hl:xyz        135 mkts  OI $ 3,782,892,605  24h $ 3,459,735,783
             XYZ100, TSLA, NVDA, GOLD, HOOD, INTC, PLTR, COIN, META, AAPL, MSFT, ORCL, GOOGL, AMZN, AMD, MU, SNDK, MSTR
hl:io          13 mkts  OI $    67,529,913  24h $    91,200,549
             OAI, ANTH, SNDK, IONQ, NBIS, EWY, GPRO, SBE, TCNT, DRAM, PRL, XIAOMI, H100
hl:para        38 mkts  OI $    15,529,322  24h $     7,173,856
             TOTAL2, OTHERS, BTCD, H100, AVGO, COHR, GLW, CRDO, LRCX, NET, STX, IREN, VST, TER, AAOI, 10Y, CIEN, NAVER
hl:mkts        24 mkts  OI $    10,075,214  24h $     3,379,798
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

total 307 builder markets across 10 dexs
```

## Offchain reference rates (FRED)
```
OFFCHAIN REFERENCE RATES (FRED)

  SOFR      3.89%  2026-10-15     +1bp   Secured Overnight Financing Rate (what a desk funds at)
  DFF       3.88%  2026-10-14     +0bp   Effective fed funds
  IORB      3.90%  2026-10-16     +0bp   Interest on reserve balances
  DGS3MO    4.28%  2026-10-14     +2bp   3-month Treasury
  DGS10     5.19%  2026-10-14     -2bp   10-year Treasury
```

## Carry: funding vs borrow
```
PERP FUNDING (annualized from 8h feed) vs ONCHAIN BORROW

asset        lighter  hyperliq   binance     bybit  aave brw  aave sup
----------------------------------------------------------------------
BTC            10.5%     10.9%      3.4%      2.1%     0.00%     0.00%
ETH            10.5%      8.8%      4.4%      4.3%     0.00%     0.00%
SOL             9.6%     -5.4%     -1.9%     -6.1%         -         -
ENA             6.1%     10.9%      7.6%     10.9%         -         -
HYPE           10.5%    -28.0%     -1.2%      0.5%         -         -
LINK          -17.5%     -5.8%     -2.1%      0.3%     0.00%     0.00%
AVAX           10.5%      6.7%      5.4%      4.2%         -         -
DOGE           10.5%     10.9%     -0.1%     -3.2%         -         -

STABLE BORROW COST (the cost of carrying a hedged position)
  aave   GHO      borrow  3.11%  supply  1.70%
  aave   RLUSD    borrow  3.85%  supply  2.31%
  aave   GHO      borrow  4.08%  supply  3.29%
  aave   USDT     borrow  4.09%  supply  3.01%
  aave   USDT     borrow  4.28%  supply  3.29%
  aave   USDC     borrow  4.32%  supply  3.34%
  aave   USDC     borrow  4.55%  supply  3.43%
  aave   USDT     borrow  4.62%  supply  3.53%
  morpho    cbBTC/USDC    borrow  5.02%  lltv 0.86  $343,060,312
  morpho     kBTC/RLUSD   borrow  3.50%  lltv 0.86  $245,605,839
  morpho    PRIME/PYUSD   borrow  5.04%  lltv 0.86  $205,232,809
  morpho     kBTC/PYUSD   borrow  4.00%  lltv 0.86  $150,223,491
  morpho   wstETH/USDT    borrow  2.99%  lltv 0.86  $144,493,198
  morpho     WBTC/USDC    borrow  4.99%  lltv 0.86  $129,863,296

OFFCHAIN BENCHMARK: SOFR 3.89% (2026-10-15)
  BTC perp funding 10.51% vs SOFR 3.89%: spread +6.62pp over the offchain cost of money

BUILDER-DEPLOYED PERPS: 307 markets, 162 with volume today
  xyz:SKHX         OI $  381,940,974  funding   -246.8%/yr
  xyz:SP500        OI $  336,892,121  funding      2.0%/yr
  xyz:XYZ100       OI $  327,712,609  funding     16.7%/yr
  xyz:GOLD         OI $  305,007,679  funding      8.4%/yr
  xyz:SKHY         OI $  188,807,729  funding     -6.7%/yr
  xyz:SILVER       OI $  180,820,040  funding      6.2%/yr
  xyz:MU           OI $  167,231,446  funding     11.5%/yr
  xyz:BRENTOIL     OI $  162,059,054  funding     -5.2%/yr
  xyz:CL           OI $  137,923,304  funding      0.2%/yr
  xyz:SPCX         OI $  134,202,700  funding      5.5%/yr
```
