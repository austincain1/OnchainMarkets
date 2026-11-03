# 2026-11-03

## Market list changes
```
2026-11-02.json -> 2026-11-03.json

hl:abcd: no change (1 markets)
hl:cash: no change (17 markets)
hl:flx: no change (16 markets)
hl:hyna: no change (25 markets)
hl:io: no change (18 markets)
hl:km: no change (23 markets)
hl:mkts: no change (24 markets)
hl:para: no change (40 markets)
hl:vntl: no change (15 markets)
hl:xyz: no change (142 markets)
hyperliquid: no change (235 markets)
lighter: no change (235 markets)
variational: 581 -> 584
  NEW     (3): DRV, EIDO, XOM

```

## Funding dispersion
```
205 symbols quoted on 2+ venues. Top 25 by dispersion.

sym             lighter  hyperliqu    binance      bybit     spread      ann  flag
----------------------------------------------------------------------------------
STONK           0.2536%          -          -    0.0135%    0.2401%      263%/yr
SKY             0.1368%    0.0100%    0.0100%    0.0100%    0.1268%      139%/yr
BOT            -0.0240%          -   -0.0123%   -0.1190%    0.1066%      117%/yr
RAY            -0.0992%          -    0.0000%          -    0.0992%      109%/yr
ZORA           -0.0752%    0.0100%    0.0100%   -0.0008%    0.0852%       93%/yr  SIGN SPLIT
1000BONK        0.0000%   -0.0244%   -0.0232%   -0.0722%    0.0722%       79%/yr
AZTEC          -0.0592%   -0.0117%    0.0100%    0.0100%    0.0692%       76%/yr  SIGN SPLIT
AERO           -0.0584%    0.0091%    0.0030%    0.0000%    0.0675%       74%/yr  SIGN SPLIT
2Z              0.0096%    0.0100%    0.0059%   -0.0539%    0.0639%       70%/yr  SIGN SPLIT
XPD             0.0032%    0.0050%    0.0662%          -    0.0630%       69%/yr
STRC           -0.0544%          -    0.0000%          -    0.0544%       60%/yr
LITE            0.0536%          -    0.0000%    0.0000%    0.0536%       59%/yr
AXS            -0.0008%    0.0100%    0.0059%   -0.0433%    0.0533%       58%/yr  SIGN SPLIT
CBRS            0.0088%          -    0.0000%    0.0447%    0.0447%       49%/yr
GRASS           0.0472%    0.0100%    0.0100%    0.0100%    0.0372%       41%/yr
USDJPY         -0.0176%   -0.0118%          -   -0.0484%    0.0367%       40%/yr
STRK            0.0096%    0.0100%    0.0100%   -0.0217%    0.0317%       35%/yr  SIGN SPLIT
FOLKS           0.0408%          -    0.0100%    0.0100%    0.0308%       34%/yr
LDO             0.0096%    0.0100%    0.0100%   -0.0202%    0.0302%       33%/yr  SIGN SPLIT
XAU             0.0144%    0.0195%    0.0245%    0.0446%    0.0302%       33%/yr
CAP             0.0096%          -    0.0397%    0.0100%    0.0301%       33%/yr
TIA            -0.0192%    0.0100%   -0.0013%    0.0100%    0.0292%       32%/yr  SIGN SPLIT
TTWO            0.0224%          -    0.0062%    0.0337%    0.0275%       30%/yr
GRAM            0.0096%   -0.0166%   -0.0097%    0.0095%    0.0262%       29%/yr  SIGN SPLIT
AAOI            0.0032%          -    0.0223%    0.0293%    0.0261%       29%/yr

22 symbols where one venue pays longs while another pays shorts:
  ZORA, AZTEC, AERO, 2Z, AXS, STRK, LDO, TIA, GRAM, CRO, CRV, OP, MET, ICP, BIRB, PAXG, MNT, MON, DASH, FIL, SPY, MSFT
```

## Builder-deployed markets
```
hl:xyz        142 mkts  OI $ 4,276,493,035  24h $ 4,071,012,124
             XYZ100, TSLA, NVDA, GOLD, HOOD, INTC, PLTR, COIN, META, AAPL, MSFT, ORCL, GOOGL, AMZN, AMD, MU, SNDK, MSTR
hl:io          18 mkts  OI $   126,507,793  24h $    68,897,269
             OAI, ANTH, SNDK, IONQ, NBIS, EWY, GPRO, SBE, TCNT, DRAM, PRL, XIAOMI, H100, MOONSHOT, NVDA, SKHX, AAPL, CRCL
hl:para        40 mkts  OI $    16,059,563  24h $     4,115,951
             TOTAL2, OTHERS, BTCD, H100, AVGO, COHR, GLW, CRDO, LRCX, NET, STX, IREN, VST, TER, AAOI, 10Y, CIEN, NAVER
hl:mkts        24 mkts  OI $       127,489  24h $        95,688
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

total 321 builder markets across 10 dexs
```

## Offchain reference rates (FRED)
```
OFFCHAIN REFERENCE RATES (FRED)

  SOFR      3.95%  2026-11-02     +0bp   Secured Overnight Financing Rate (what a desk funds at)
  DFF       3.88%  2026-10-30     +0bp   Effective fed funds
  IORB      3.90%  2026-11-03     +0bp   Interest on reserve balances
  DGS3MO    4.16%  2026-10-30     -2bp   3-month Treasury
  DGS10     4.94%  2026-10-30     -4bp   10-year Treasury
```

## Carry: funding vs borrow
```
PERP FUNDING (annualized from 8h feed) vs ONCHAIN BORROW

asset        lighter  hyperliq   binance     bybit  aave brw  aave sup
----------------------------------------------------------------------
BTC            10.5%     10.9%     10.9%     10.9%     0.00%     0.00%
ETH            10.5%     10.9%     10.9%     10.9%     0.00%     0.00%
SOL            10.5%     10.9%     10.9%      4.2%         -         -
ENA            10.5%     10.9%     10.9%     10.9%         -         -
HYPE           10.5%     10.9%     10.9%     10.9%         -         -
LINK           10.5%     10.9%     10.9%     10.9%     0.00%     0.00%
AVAX           10.5%     10.9%     10.9%      4.5%         -         -
DOGE           10.5%     10.9%     10.9%     10.9%         -         -

STABLE BORROW COST (the cost of carrying a hedged position)
  aave   USDe     borrow  0.00%  supply  0.00%
  aave   RLUSD    borrow  0.89%  supply  0.08%
  aave   RLUSD    borrow  3.24%  supply  1.64%
  aave   USDC     borrow  4.02%  supply  2.90%
  aave   GHO      borrow  4.05%  supply  3.24%
  aave   USDC     borrow  4.46%  supply  3.23%
  aave   GHO      borrow  4.53%  supply  3.60%
  aave   USDC     borrow  4.90%  supply  3.86%
  morpho    cbBTC/USDC    borrow  5.06%  lltv 0.86  $334,103,479
  morpho     kBTC/RLUSD   borrow  3.70%  lltv 0.86  $254,958,958
  morpho    PRIME/PYUSD   borrow  5.07%  lltv 0.86  $197,690,777
  morpho PT-reUSD-10DEC2026/USDC    borrow  9.20%  lltv 0.92  $146,724,133
  morpho     WBTC/USDC    borrow  5.44%  lltv 0.86  $135,361,128
  morpho   wstETH/USDT    borrow  3.64%  lltv 0.86  $127,130,047

OFFCHAIN BENCHMARK: SOFR 3.95% (2026-11-02)
  BTC perp funding 10.51% vs SOFR 3.95%: spread +6.56pp over the offchain cost of money

BUILDER-DEPLOYED PERPS: 321 markets, 168 with volume today
  xyz:SP500        OI $  385,246,928  funding     -2.7%/yr
  xyz:BRENTOIL     OI $  336,854,173  funding      5.5%/yr
  xyz:GOLD         OI $  317,252,839  funding     21.2%/yr
  xyz:XYZ100       OI $  287,677,558  funding      5.5%/yr
  xyz:GOOGL        OI $  287,402,668  funding     15.2%/yr
  xyz:CL           OI $  265,012,895  funding      5.5%/yr
  xyz:SKHX         OI $  248,686,357  funding     -0.9%/yr
  xyz:SILVER       OI $  214,376,757  funding      5.9%/yr
  xyz:SPCX         OI $  164,388,157  funding      5.5%/yr
  xyz:SNDK         OI $  162,579,172  funding     11.0%/yr
```
