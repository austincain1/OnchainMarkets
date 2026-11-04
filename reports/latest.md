# 2026-11-04

## Market list changes
```
2026-11-03.json -> 2026-11-04.json

hl:abcd: no change (1 markets)
hl:cash: no change (17 markets)
hl:flx: no change (16 markets)
hl:hyna: no change (25 markets)
hl:io: 18 -> 19
  NEW     (1): io:GOOGL

hl:km: no change (23 markets)
hl:mkts: no change (24 markets)
hl:para: no change (40 markets)
hl:vntl: no change (15 markets)
hl:xyz: no change (142 markets)
hyperliquid: no change (235 markets)
lighter: 235 -> 235
  NEW     (1): IREN
  REMOVED (1): PROVE

variational: 584 -> 586
  NEW     (2): SQQQ, TBT

```

## Funding dispersion
```
205 symbols quoted on 2+ venues. Top 25 by dispersion.

sym             lighter  hyperliqu    binance      bybit     spread      ann  flag
----------------------------------------------------------------------------------
CXMT            0.0032%          -   -0.1138%    0.0000%    0.1170%      128%/yr  SIGN SPLIT
SKHYNIX               -   -0.1163%   -0.0543%    0.0000%    0.1163%      127%/yr
SHEIN           0.0032%          -          -   -0.1001%    0.1033%      113%/yr  SIGN SPLIT
MET            -0.0904%    0.0100%    0.0100%   -0.0437%    0.1004%      110%/yr  SIGN SPLIT
CAP             0.0096%          -    0.1037%    0.0184%    0.0941%      103%/yr
CASHCAT         0.0416%    0.1035%          -    0.0100%    0.0935%      102%/yr
SMIC           -0.0800%          -          -    0.0000%    0.0800%       88%/yr
SAMSUNG               -   -0.0788%   -0.0049%    0.0000%    0.0788%       86%/yr
USDJPY         -0.0104%   -0.0136%          -   -0.0887%    0.0783%       86%/yr
ZHIPU           0.0032%          -   -0.0726%    0.0000%    0.0758%       83%/yr  SIGN SPLIT
CHIP            0.0096%    0.0100%    0.0100%   -0.0642%    0.0742%       81%/yr  SIGN SPLIT
VVV            -0.0224%    0.0100%   -0.0544%   -0.0582%    0.0682%       75%/yr  SIGN SPLIT
NATGAS          0.0656%    0.0567%    0.0000%          -    0.0656%       72%/yr
TRUMP          -0.0320%   -0.0847%   -0.0893%   -0.0244%    0.0649%       71%/yr
SKR             0.0096%    0.0100%    0.0100%   -0.0481%    0.0581%       64%/yr  SIGN SPLIT
LITE            0.0560%          -    0.0172%    0.0032%    0.0528%       58%/yr
S              -0.0408%   -0.0174%   -0.0416%    0.0100%    0.0516%       56%/yr  SIGN SPLIT
JUP            -0.0008%    0.0100%   -0.0138%   -0.0381%    0.0481%       53%/yr  SIGN SPLIT
GRAM            0.0096%   -0.0349%   -0.0385%   -0.0047%    0.0481%       53%/yr  SIGN SPLIT
GEV             0.0032%          -    0.0499%    0.0229%    0.0467%       51%/yr
SOXL            0.0408%          -    0.0634%    0.0189%    0.0445%       49%/yr
PUMP            0.0096%    0.0100%    0.0100%   -0.0317%    0.0417%       46%/yr  SIGN SPLIT
LIT             0.0096%    0.0100%    0.0088%   -0.0308%    0.0408%       45%/yr  SIGN SPLIT
STRC           -0.0400%          -    0.0000%          -    0.0400%       44%/yr
CBRS            0.0048%          -    0.0095%    0.0445%    0.0397%       43%/yr

38 symbols where one venue pays longs while another pays shorts:
  CXMT, SHEIN, MET, ZHIPU, CHIP, VVV, SKR, S, JUP, GRAM, PUMP, LIT, HBAR, AVNT, AZTEC, WLFI, TRX, STRK, ARB, BERA, GRASS, AAPL, LINEA, SOXS, 1000FLOKI, MNT, 1000PEPE, TIA, CRO, AAVE, XRP, DOT, MEGA, MSFT, XPT, BTC, APT, MINIMAX
```

## Builder-deployed markets
```
hl:xyz        142 mkts  OI $ 4,410,562,180  24h $ 6,774,152,938
             XYZ100, TSLA, NVDA, GOLD, HOOD, INTC, PLTR, COIN, META, AAPL, MSFT, ORCL, GOOGL, AMZN, AMD, MU, SNDK, MSTR
hl:io          19 mkts  OI $   147,939,144  24h $   116,760,001
             OAI, ANTH, SNDK, IONQ, NBIS, EWY, GPRO, SBE, TCNT, DRAM, PRL, XIAOMI, H100, MOONSHOT, NVDA, SKHX, AAPL, CRCL
hl:para        40 mkts  OI $    15,938,739  24h $    10,480,554
             TOTAL2, OTHERS, BTCD, H100, AVGO, COHR, GLW, CRDO, LRCX, NET, STX, IREN, VST, TER, AAOI, 10Y, CIEN, NAVER
hl:mkts        24 mkts  OI $       100,045  24h $       119,892
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

total 322 builder markets across 10 dexs
```

## Offchain reference rates (FRED)
```
OFFCHAIN REFERENCE RATES (FRED)

  SOFR      3.97%  2026-11-03     +2bp   Secured Overnight Financing Rate (what a desk funds at)
  DFF       3.88%  2026-11-02     +0bp   Effective fed funds
  IORB      3.90%  2026-11-04     +0bp   Interest on reserve balances
  DGS3MO    4.21%  2026-11-02     +5bp   3-month Treasury
  DGS10     4.91%  2026-11-02     -3bp   10-year Treasury
```

## Carry: funding vs borrow
```
PERP FUNDING (annualized from 8h feed) vs ONCHAIN BORROW

asset        lighter  hyperliq   binance     bybit  aave brw  aave sup
----------------------------------------------------------------------
BTC            10.5%     -0.9%     10.9%     -0.6%     0.00%     0.00%
ETH             4.4%     10.9%     10.9%      9.0%     0.00%     0.00%
SOL            10.5%     10.9%     10.9%     10.2%         -         -
ENA            10.5%     10.9%     10.9%     10.9%         -         -
HYPE           10.5%     10.9%     10.9%     10.4%         -         -
LINK            7.9%     10.9%     10.9%      8.8%     0.00%     0.00%
AVAX           10.5%     10.9%     10.9%     10.9%         -         -
DOGE           10.5%     10.9%     10.9%      8.2%         -         -

STABLE BORROW COST (the cost of carrying a hedged position)
  aave   USDe     borrow  0.00%  supply  0.00%
  aave   RLUSD    borrow  2.90%  supply  1.48%
  aave   RLUSD    borrow  3.24%  supply  1.64%
  aave   USDC     borrow  3.96%  supply  2.81%
  aave   GHO      borrow  4.04%  supply  3.23%
  aave   USDC     borrow  4.46%  supply  3.23%
  aave   USDC     borrow  4.48%  supply  3.60%
  aave   GHO      borrow  4.53%  supply  3.60%
  morpho    cbBTC/USDC    borrow  5.06%  lltv 0.86  $336,920,856
  morpho     kBTC/RLUSD   borrow  3.67%  lltv 0.86  $254,983,194
  morpho    PRIME/PYUSD   borrow  5.13%  lltv 0.86  $191,448,588
  morpho PT-reUSD-10DEC2026/USDC    borrow  8.81%  lltv 0.92  $161,809,972
  morpho     WBTC/USDC    borrow  5.05%  lltv 0.86  $139,201,278
  morpho   wstETH/USDT    borrow  3.62%  lltv 0.86  $138,122,157

OFFCHAIN BENCHMARK: SOFR 3.97% (2026-11-03)
  BTC perp funding 10.51% vs SOFR 3.97%: spread +6.54pp over the offchain cost of money

BUILDER-DEPLOYED PERPS: 322 markets, 168 with volume today
  xyz:SP500        OI $  394,308,391  funding      3.5%/yr
  xyz:GOLD         OI $  317,386,429  funding      5.5%/yr
  xyz:BRENTOIL     OI $  308,279,294  funding      5.5%/yr
  xyz:SKHX         OI $  296,060,192  funding   -127.6%/yr
  xyz:XYZ100       OI $  266,948,480  funding      5.5%/yr
  xyz:CL           OI $  232,848,836  funding      5.5%/yr
  xyz:SILVER       OI $  228,836,735  funding     16.6%/yr
  xyz:GOOGL        OI $  225,826,831  funding      5.5%/yr
  xyz:SNDK         OI $  197,072,681  funding     22.2%/yr
  xyz:SPCX         OI $  163,490,835  funding     15.1%/yr
```
