# 2026-11-01

## Market list changes
```
2026-10-31.json -> 2026-11-01.json

hl:abcd: no change (1 markets)
hl:cash: no change (17 markets)
hl:flx: no change (16 markets)
hl:hyna: no change (25 markets)
hl:io: 17 -> 18
  NEW     (1): io:CRCL

hl:km: no change (23 markets)
hl:mkts: no change (24 markets)
hl:para: no change (39 markets)
hl:vntl: no change (15 markets)
hl:xyz: no change (141 markets)
hyperliquid: no change (235 markets)
lighter: no change (235 markets)
variational: no change (581 markets)
```

## Funding dispersion
```
205 symbols quoted on 2+ venues. Top 25 by dispersion.

sym             lighter  hyperliqu    binance      bybit     spread      ann  flag
----------------------------------------------------------------------------------
MET            -0.1192%    0.0100%    0.0100%    0.0100%    0.1292%      141%/yr  SIGN SPLIT
BOT             0.0032%          -    0.0000%    0.0924%    0.0924%      101%/yr
MEGA            0.0720%    0.0981%    0.0100%    0.0100%    0.0881%       97%/yr
ZK              0.0096%    0.0100%   -0.0039%   -0.0671%    0.0771%       84%/yr  SIGN SPLIT
INTC            0.0056%    0.0192%    0.0000%    0.0743%    0.0743%       81%/yr
RAY            -0.0720%          -    0.0000%          -    0.0720%       79%/yr
UNITREE         0.0032%          -    0.0000%   -0.0680%    0.0712%       78%/yr  SIGN SPLIT
DRV             0.0808%          -          -    0.0100%    0.0708%       78%/yr
PRL            -0.0176%          -    0.0100%    0.0361%    0.0537%       59%/yr  SIGN SPLIT
SKHYNIX               -   -0.0519%    0.0000%    0.0000%    0.0519%       57%/yr
S               0.0096%   -0.0398%   -0.0048%   -0.0284%    0.0494%       54%/yr  SIGN SPLIT
ZRO             0.0448%    0.0100%    0.0100%   -0.0023%    0.0471%       52%/yr  SIGN SPLIT
MON             0.0096%    0.0100%    0.0100%   -0.0371%    0.0471%       52%/yr  SIGN SPLIT
AERO           -0.0336%    0.0100%    0.0100%    0.0100%    0.0436%       48%/yr  SIGN SPLIT
GOOGL           0.0104%    0.0311%    0.0000%    0.0417%    0.0417%       46%/yr
BIO             0.0096%   -0.0306%    0.0046%    0.0100%    0.0406%       44%/yr  SIGN SPLIT
SKR             0.0096%    0.0100%    0.0100%   -0.0275%    0.0375%       41%/yr  SIGN SPLIT
BERA            0.0096%    0.0100%   -0.0200%   -0.0251%    0.0351%       38%/yr  SIGN SPLIT
XAG             0.0152%    0.0316%    0.0000%    0.0000%    0.0316%       35%/yr
MNT             0.0096%    0.0028%          -   -0.0203%    0.0299%       33%/yr  SIGN SPLIT
PLTR            0.0032%    0.0050%    0.0000%    0.0286%    0.0286%       31%/yr
PUMP            0.0096%    0.0370%    0.0100%    0.0100%    0.0274%       30%/yr
LIT             0.0096%    0.0100%    0.0100%   -0.0162%    0.0262%       29%/yr  SIGN SPLIT
BMNR            0.0032%          -    0.0000%    0.0251%    0.0251%       28%/yr
APT            -0.0008%    0.0100%    0.0100%   -0.0151%    0.0251%       27%/yr  SIGN SPLIT

31 symbols where one venue pays longs while another pays shorts:
  MET, ZK, UNITREE, PRL, S, ZRO, MON, AERO, BIO, SKR, BERA, MNT, LIT, APT, CC, SOXS, FF, SUI, SNDK, EWY, ICP, HBAR, KAITO, TIA, FIL, KORU, XLM, ETH, DOT, WTI, AAPL
```

## Builder-deployed markets
```
hl:xyz        141 mkts  OI $ 4,084,860,284  24h $   295,302,442
             XYZ100, TSLA, NVDA, GOLD, HOOD, INTC, PLTR, COIN, META, AAPL, MSFT, ORCL, GOOGL, AMZN, AMD, MU, SNDK, MSTR
hl:io          18 mkts  OI $   107,151,838  24h $    27,462,023
             OAI, ANTH, SNDK, IONQ, NBIS, EWY, GPRO, SBE, TCNT, DRAM, PRL, XIAOMI, H100, MOONSHOT, NVDA, SKHX, AAPL, CRCL
hl:para        39 mkts  OI $    15,071,280  24h $       718,590
             TOTAL2, OTHERS, BTCD, H100, AVGO, COHR, GLW, CRDO, LRCX, NET, STX, IREN, VST, TER, AAOI, 10Y, CIEN, NAVER
hl:mkts        24 mkts  OI $       130,056  24h $        71,630
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

total 319 builder markets across 10 dexs
```

## Offchain reference rates (FRED)
```
OFFCHAIN REFERENCE RATES (FRED)

  SOFR      3.94%  2026-10-29     +0bp   Secured Overnight Financing Rate (what a desk funds at)
  DFF       3.88%  2026-10-29     +0bp   Effective fed funds
  IORB      3.90%  2026-11-02     +0bp   Interest on reserve balances
  DGS3MO    4.18%  2026-10-29     +0bp   3-month Treasury
  DGS10     4.98%  2026-10-29     -7bp   10-year Treasury
```

## Carry: funding vs borrow
```
PERP FUNDING (annualized from 8h feed) vs ONCHAIN BORROW

asset        lighter  hyperliq   binance     bybit  aave brw  aave sup
----------------------------------------------------------------------
BTC            10.5%     10.9%     10.9%     10.5%     0.00%     0.00%
ETH             0.9%      8.7%     -1.6%     -4.1%     0.00%     0.00%
SOL            10.5%     10.9%     10.9%     10.9%         -         -
ENA            10.5%     10.9%     10.9%     10.9%         -         -
HYPE           18.4%     33.0%     10.9%     10.9%         -         -
LINK           10.5%     10.9%     10.9%     10.9%     0.00%     0.00%
AVAX           10.5%     10.9%     10.9%     10.9%         -         -
DOGE           10.5%     10.9%     10.9%      2.9%         -         -

STABLE BORROW COST (the cost of carrying a hedged position)
  aave   USDe     borrow  0.00%  supply  0.00%
  aave   RLUSD    borrow  0.62%  supply  0.02%
  aave   RLUSD    borrow  3.24%  supply  1.64%
  aave   USDC     borrow  4.08%  supply  2.99%
  aave   GHO      borrow  4.09%  supply  3.31%
  aave   GHO      borrow  4.43%  supply  3.58%
  aave   USDC     borrow  4.49%  supply  3.27%
  aave   GHO      borrow  4.53%  supply  3.60%
  morpho     kBTC/RLUSD   borrow  3.85%  lltv 0.86  $244,251,341
  morpho    cbBTC/USDC    borrow  4.88%  lltv 0.86  $241,725,579
  morpho    PRIME/PYUSD   borrow  4.94%  lltv 0.86  $206,460,598
  morpho PT-reUSD-10DEC2026/USDC    borrow  9.58%  lltv 0.92  $140,174,518
  morpho     WBTC/USDC    borrow  4.91%  lltv 0.86  $139,963,364
  morpho   wstETH/USDT    borrow  3.69%  lltv 0.86  $130,426,236

OFFCHAIN BENCHMARK: SOFR 3.94% (2026-10-29)
  BTC perp funding 10.51% vs SOFR 3.94%: spread +6.57pp over the offchain cost of money

BUILDER-DEPLOYED PERPS: 319 markets, 165 with volume today
  xyz:SP500        OI $  373,769,835  funding      5.5%/yr
  xyz:GOLD         OI $  313,379,622  funding      5.5%/yr
  xyz:GOOGL        OI $  287,579,949  funding     33.4%/yr
  xyz:XYZ100       OI $  276,211,480  funding      5.5%/yr
  xyz:SKHX         OI $  271,889,543  funding    -58.3%/yr
  xyz:SILVER       OI $  212,818,086  funding     33.2%/yr
  xyz:BRENTOIL     OI $  212,356,614  funding      5.5%/yr
  xyz:CL           OI $  203,092,383  funding      5.5%/yr
  xyz:SPCX         OI $  175,768,837  funding      5.5%/yr
  xyz:SNDK         OI $  133,270,498  funding     -2.2%/yr
```
