# 2026-10-17

## Market list changes
```
2026-10-16.json -> 2026-10-17.json

hl:abcd: no change (1 markets)
hl:cash: no change (17 markets)
hl:flx: no change (16 markets)
hl:hyna: no change (25 markets)
hl:io: no change (13 markets)
hl:km: no change (23 markets)
hl:mkts: no change (24 markets)
hl:para: no change (38 markets)
hl:vntl: no change (15 markets)
hl:xyz: 135 -> 136
  NEW     (1): xyz:SNAP

hyperliquid: no change (234 markets)
lighter: no change (235 markets)
variational: no change (575 markets)
```

## Funding dispersion
```
206 symbols quoted on 2+ venues. Top 25 by dispersion.

sym             lighter  hyperliqu    binance      bybit     spread      ann  flag
----------------------------------------------------------------------------------
DRV             0.0096%          -          -   -0.1916%    0.2012%      220%/yr  SIGN SPLIT
FOLKS           0.1696%          -    0.0100%    0.0100%    0.1596%      175%/yr
BERA            0.0096%   -0.0128%   -0.0850%   -0.1290%    0.1386%      152%/yr  SIGN SPLIT
AAOI            0.0032%          -    0.0000%   -0.1053%    0.1085%      119%/yr  SIGN SPLIT
USDJPY          0.0000%    0.0000%          -   -0.1051%    0.1051%      115%/yr
MET             0.0096%   -0.0637%   -0.0171%   -0.0710%    0.0806%       88%/yr  SIGN SPLIT
CHIP           -0.0680%    0.0100%    0.0058%    0.0100%    0.0780%       85%/yr  SIGN SPLIT
MORPHO          0.0096%    0.0100%   -0.0010%   -0.0620%    0.0720%       79%/yr  SIGN SPLIT
MON             0.0096%   -0.0335%   -0.0610%   -0.0392%    0.0706%       77%/yr  SIGN SPLIT
WTI             0.0392%    0.0647%    0.0000%    0.0000%    0.0647%       71%/yr
NMR             0.0096%          -   -0.0296%   -0.0545%    0.0641%       70%/yr  SIGN SPLIT
TRUMP           0.0096%   -0.0449%   -0.0278%   -0.0519%    0.0615%       67%/yr  SIGN SPLIT
WDC             0.0032%          -   -0.0509%   -0.0355%    0.0541%       59%/yr  SIGN SPLIT
AXTI            0.0032%          -   -0.0074%   -0.0475%    0.0507%       55%/yr  SIGN SPLIT
XPL            -0.0400%    0.0100%    0.0100%    0.0058%    0.0500%       55%/yr  SIGN SPLIT
BRENTOIL        0.0320%    0.0494%    0.0000%          -    0.0494%       54%/yr
PROVE           0.0096%   -0.0364%   -0.0295%   -0.0230%    0.0460%       50%/yr  SIGN SPLIT
VIRTUAL        -0.0456%   -0.0004%    0.0002%   -0.0187%    0.0458%       50%/yr  SIGN SPLIT
2Z              0.0096%   -0.0324%    0.0100%    0.0000%    0.0424%       46%/yr  SIGN SPLIT
AVAX           -0.0328%   -0.0221%    0.0079%   -0.0060%    0.0407%       45%/yr  SIGN SPLIT
ZORA            0.0096%    0.0100%   -0.0284%    0.0039%    0.0384%       42%/yr  SIGN SPLIT
AAVE            0.0080%   -0.0285%    0.0039%    0.0050%    0.0365%       40%/yr  SIGN SPLIT
FIL             0.0096%    0.0100%   -0.0078%   -0.0216%    0.0316%       35%/yr  SIGN SPLIT
WIF             0.0096%    0.0100%    0.0100%   -0.0211%    0.0311%       34%/yr  SIGN SPLIT
JTO             0.0096%    0.0100%    0.0069%   -0.0209%    0.0309%       34%/yr  SIGN SPLIT

63 symbols where one venue pays longs while another pays shorts:
  DRV, BERA, AAOI, MET, CHIP, MORPHO, MON, NMR, TRUMP, WDC, AXTI, XPL, PROVE, VIRTUAL, 2Z, AVAX, ZORA, AAVE, FIL, WIF, JTO, SEI, 1000PEPE, CRV, XLM, ONDO, SKY, TIA, CC, TAO, POL, ADA, ICP, 1000FLOKI, APT, BE, LIT, JUP, SKHY, PENGU
```

## Builder-deployed markets
```
hl:xyz        136 mkts  OI $ 3,749,249,572  24h $ 2,027,952,065
             XYZ100, TSLA, NVDA, GOLD, HOOD, INTC, PLTR, COIN, META, AAPL, MSFT, ORCL, GOOGL, AMZN, AMD, MU, SNDK, MSTR
hl:io          13 mkts  OI $    67,973,360  24h $    46,850,599
             OAI, ANTH, SNDK, IONQ, NBIS, EWY, GPRO, SBE, TCNT, DRAM, PRL, XIAOMI, H100
hl:para        38 mkts  OI $    15,227,981  24h $     2,005,804
             TOTAL2, OTHERS, BTCD, H100, AVGO, COHR, GLW, CRDO, LRCX, NET, STX, IREN, VST, TER, AAOI, 10Y, CIEN, NAVER
hl:mkts        24 mkts  OI $     9,664,210  24h $     5,556,718
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

total 308 builder markets across 10 dexs
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
BTC            10.5%     10.9%      4.3%      8.0%     0.00%     0.00%
ETH            10.5%     10.9%      8.3%      9.9%     0.00%     0.00%
SOL            -4.4%     -2.2%      1.7%      1.7%         -         -
ENA             4.4%     10.9%      9.8%     10.9%         -         -
HYPE            0.0%     10.9%      4.2%      5.1%         -         -
LINK            0.0%     10.9%     -4.2%      3.5%     0.00%     0.00%
AVAX          -35.9%    -24.2%      8.6%     -6.5%         -         -
DOGE           10.5%     10.9%      1.1%      7.0%         -         -

STABLE BORROW COST (the cost of carrying a hedged position)
  aave   GHO      borrow  3.11%  supply  1.70%
  aave   RLUSD    borrow  3.85%  supply  2.31%
  aave   USDT     borrow  4.00%  supply  2.88%
  aave   USDT     borrow  4.31%  supply  3.33%
  aave   USDC     borrow  4.32%  supply  3.34%
  aave   USDC     borrow  4.52%  supply  3.38%
  aave   USDT     borrow  4.64%  supply  3.56%
  aave   USDC     borrow  4.94%  supply  3.92%
  morpho    cbBTC/USDC    borrow  5.01%  lltv 0.86  $343,015,997
  morpho     kBTC/RLUSD   borrow  3.52%  lltv 0.86  $242,029,504
  morpho    PRIME/PYUSD   borrow  7.45%  lltv 0.86  $204,336,646
  morpho     kBTC/PYUSD   borrow  4.00%  lltv 0.86  $149,298,795
  morpho   wstETH/USDT    borrow  2.97%  lltv 0.86  $144,880,766
  morpho PT-reUSD-10DEC2026/USDC    borrow  8.37%  lltv 0.92  $132,762,007

OFFCHAIN BENCHMARK: SOFR 3.89% (2026-10-15)
  BTC perp funding 10.51% vs SOFR 3.89%: spread +6.62pp over the offchain cost of money

BUILDER-DEPLOYED PERPS: 308 markets, 162 with volume today
  xyz:SKHX         OI $  375,495,598  funding      5.5%/yr
  xyz:SP500        OI $  336,124,039  funding      5.5%/yr
  xyz:XYZ100       OI $  317,807,380  funding    -12.1%/yr
  xyz:GOLD         OI $  290,961,381  funding      5.5%/yr
  xyz:BRENTOIL     OI $  197,290,832  funding     52.8%/yr
  xyz:SKHY         OI $  188,805,505  funding      5.5%/yr
  xyz:SILVER       OI $  160,115,686  funding      5.5%/yr
  xyz:MU           OI $  156,386,568  funding      5.5%/yr
  xyz:CL           OI $  154,005,688  funding     68.4%/yr
  xyz:SPCX         OI $  127,066,416  funding     19.2%/yr
```
