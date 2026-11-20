# 2026-11-20

## Market list changes
```
2026-11-19.json -> 2026-11-20.json

hl:abcd: no change (1 markets)
hl:cash: no change (17 markets)
hl:flx: no change (16 markets)
hl:hyna: no change (25 markets)
hl:io: 24 -> 25
  NEW     (1): io:SOXS

hl:km: no change (23 markets)
hl:mkts: no change (24 markets)
hl:para: no change (40 markets)
hl:vntl: no change (15 markets)
hl:xyz: no change (147 markets)
hyperliquid: no change (235 markets)
lighter: no change (235 markets)
variational: 594 -> 595
  NEW     (1): TENCENT

```

## Funding dispersion
```
206 symbols quoted on 2+ venues. Top 25 by dispersion.

sym             lighter  hyperliqu    binance      bybit     spread      ann  flag
----------------------------------------------------------------------------------
ZHIPU           0.0056%          -   -0.2952%   -0.0561%    0.3008%      329%/yr  SIGN SPLIT
FOLKS           0.0096%          -    0.2895%    0.2725%    0.2799%      307%/yr
CXMT            0.0376%          -   -0.2236%   -0.0523%    0.2612%      286%/yr  SIGN SPLIT
PRL            -0.1768%          -    0.0100%    0.0100%    0.1868%      205%/yr  SIGN SPLIT
SKHYNIX               -    0.0099%   -0.1587%   -0.1213%    0.1686%      185%/yr  SIGN SPLIT
MINIMAX         0.0032%          -   -0.1654%   -0.0532%    0.1686%      185%/yr  SIGN SPLIT
MET             0.0096%   -0.1320%   -0.0442%   -0.0662%    0.1416%      155%/yr  SIGN SPLIT
JUP            -0.0240%   -0.1327%   -0.0446%   -0.0014%    0.1313%      144%/yr
LIT            -0.1144%    0.0100%   -0.0032%    0.0100%    0.1244%      136%/yr  SIGN SPLIT
SAMSUNG               -   -0.0002%   -0.1205%   -0.1051%    0.1202%      132%/yr
HYUNDAI               -   -0.1042%    0.0000%    0.0000%    0.1042%      114%/yr
CRO             0.0096%          -          -   -0.0913%    0.1009%      110%/yr  SIGN SPLIT
HBAR           -0.0112%   -0.0838%   -0.0075%    0.0091%    0.0928%      102%/yr  SIGN SPLIT
1000BONK        0.0024%   -0.0891%   -0.0788%   -0.0620%    0.0915%      100%/yr  SIGN SPLIT
BIRB                  -          -   -0.1061%   -0.0170%    0.0891%       98%/yr
ROBO           -0.0688%          -    0.0100%    0.0100%    0.0788%       86%/yr  SIGN SPLIT
SKR             0.0096%    0.0100%   -0.0616%    0.0100%    0.0716%       78%/yr  SIGN SPLIT
CHIP           -0.0120%   -0.0726%   -0.0083%   -0.0022%    0.0704%       77%/yr
WLD            -0.0016%   -0.0625%   -0.0486%   -0.0432%    0.0609%       67%/yr
ICP            -0.0424%   -0.0482%   -0.0258%    0.0100%    0.0582%       64%/yr  SIGN SPLIT
BABA            0.0576%          -    0.0000%    0.0000%    0.0576%       63%/yr
EIGEN           0.0096%    0.0100%   -0.0462%   -0.0307%    0.0562%       61%/yr  SIGN SPLIT
CC              0.0096%   -0.0112%   -0.0457%    0.0100%    0.0557%       61%/yr  SIGN SPLIT
TAO            -0.0128%   -0.0590%   -0.0080%   -0.0104%    0.0510%       56%/yr
SOXL            0.0552%          -    0.0325%    0.0049%    0.0503%       55%/yr

67 symbols where one venue pays longs while another pays shorts:
  ZHIPU, CXMT, PRL, SKHYNIX, MINIMAX, MET, LIT, CRO, HBAR, 1000BONK, ROBO, SKR, ICP, EIGEN, CC, ARB, ADA, POL, 1000SHIB, PYTH, SEI, CASHCAT, STRC, MNT, AAVE, SHEIN, BCH, BERA, SKY, STRK, PENDLE, MON, DIA, ZORA, ZK, OP, EDGE, FIL, 1000PEPE, 2Z
```

## Builder-deployed markets
```
hl:xyz        147 mkts  OI $ 4,118,209,284  24h $ 6,416,567,484
             XYZ100, TSLA, NVDA, GOLD, HOOD, INTC, PLTR, COIN, META, AAPL, MSFT, ORCL, GOOGL, AMZN, AMD, MU, SNDK, MSTR
hl:io          25 mkts  OI $   124,160,533  24h $   178,672,626
             OAI, ANTH, SNDK, IONQ, NBIS, EWY, GPRO, SBE, TCNT, DRAM, PRL, XIAOMI, H100, MOONSHOT, NVDA, SKHX, AAPL, CRCL
hl:para        40 mkts  OI $    12,754,717  24h $     7,505,951
             TOTAL2, OTHERS, BTCD, H100, AVGO, COHR, GLW, CRDO, LRCX, NET, STX, IREN, VST, TER, AAOI, 10Y, CIEN, NAVER
hl:mkts        24 mkts  OI $       367,816  24h $       315,803
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

total 333 builder markets across 10 dexs
```

## Offchain reference rates (FRED)
```
OFFCHAIN REFERENCE RATES (FRED)

  SOFR      3.91%  2026-11-19     +1bp   Secured Overnight Financing Rate (what a desk funds at)
  DFF       3.88%  2026-11-18     +0bp   Effective fed funds
  IORB      3.90%  2026-11-20     +0bp   Interest on reserve balances
  DGS3MO    4.34%  2026-11-18     +1bp   3-month Treasury
  DGS10     5.07%  2026-11-18     -3bp   10-year Treasury
```

## Carry: funding vs borrow
```
PERP FUNDING (annualized from 8h feed) vs ONCHAIN BORROW

asset        lighter  hyperliq   binance     bybit  aave brw  aave sup
----------------------------------------------------------------------
BTC             0.9%     -8.9%     -1.6%      2.2%     0.00%     0.00%
ETH           -35.0%    -13.6%    -13.4%    -12.3%     0.00%     0.00%
SOL           -24.5%     -3.3%    -20.0%    -21.8%         -         -
ENA            10.5%      8.3%     -2.3%      0.0%         -         -
HYPE           10.5%     10.9%      6.0%     10.9%         -         -
LINK          -20.1%     -9.8%     -8.0%     -5.5%     0.00%     0.00%
AVAX          -16.6%     -0.2%    -24.3%     -4.6%         -         -
DOGE            7.0%      3.2%    -12.0%    -10.6%         -         -

STABLE BORROW COST (the cost of carrying a hedged position)
  aave   USDe     borrow  0.00%  supply  0.00%
  aave   USDC     borrow  3.75%  supply  2.52%
  aave   RLUSD    borrow  3.76%  supply  2.21%
  aave   GHO      borrow  3.78%  supply  2.83%
  aave   USDC     borrow  3.78%  supply  2.57%
  aave   GHO      borrow  4.03%  supply  3.22%
  aave   RLUSD    borrow  4.24%  supply  3.49%
  aave   GHO      borrow  4.36%  supply  3.33%
  morpho    cbBTC/USDC    borrow  4.94%  lltv 0.86  $332,901,004
  morpho     kBTC/RLUSD   borrow  3.45%  lltv 0.86  $161,880,185
  morpho    PRIME/PYUSD   borrow 10.17%  lltv 0.86  $138,485,301
  morpho     WBTC/USDC    borrow  4.88%  lltv 0.86  $130,608,439
  morpho PT-reUSD-10DEC2026/USDC    borrow  9.81%  lltv 0.92  $128,653,265
  morpho   wstETH/USDT    borrow  3.55%  lltv 0.86  $121,669,161

OFFCHAIN BENCHMARK: SOFR 3.91% (2026-11-19)
  BTC perp funding 0.88% vs SOFR 3.91%: spread -3.03pp over the offchain cost of money

BUILDER-DEPLOYED PERPS: 333 markets, 175 with volume today
  xyz:SP500        OI $  472,761,815  funding     11.7%/yr
  xyz:NVDA         OI $  436,285,641  funding     29.7%/yr
  xyz:XYZ100       OI $  364,460,396  funding      5.5%/yr
  xyz:BRENTOIL     OI $  302,942,487  funding      5.5%/yr
  xyz:GOLD         OI $  258,440,324  funding     11.1%/yr
  xyz:ANT          OI $  253,794,774  funding    -16.1%/yr
  xyz:SKHX         OI $  245,925,665  funding      6.7%/yr
  xyz:SILVER       OI $  168,658,215  funding     26.6%/yr
  xyz:MU           OI $  139,333,859  funding     12.1%/yr
  xyz:GOOGL        OI $  128,026,445  funding      5.5%/yr
```
