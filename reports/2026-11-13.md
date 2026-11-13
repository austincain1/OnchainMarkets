# 2026-11-13

## Market list changes
```
2026-11-12.json -> 2026-11-13.json

hl:abcd: no change (1 markets)
hl:cash: no change (17 markets)
hl:flx: no change (16 markets)
hl:hyna: no change (25 markets)
hl:io: 22 -> 23
  NEW     (1): io:NVDL

hl:km: no change (23 markets)
hl:mkts: no change (24 markets)
hl:para: no change (40 markets)
hl:vntl: no change (15 markets)
hl:xyz: no change (144 markets)
hyperliquid: no change (235 markets)
lighter: no change (235 markets)
variational: 590 -> 589
  REMOVED (1): AGI

```

## Funding dispersion
```
204 symbols quoted on 2+ venues. Top 25 by dispersion.

sym             lighter  hyperliqu    binance      bybit     spread      ann  flag
----------------------------------------------------------------------------------
PRL             0.4624%          -    0.0100%    0.0100%    0.4524%      495%/yr
CAP             0.0096%          -    0.1103%    0.0100%    0.1007%      110%/yr
IREN            0.1128%          -    0.0307%    0.0208%    0.0920%      101%/yr
BERA           -0.0824%   -0.1070%   -0.0161%   -0.0409%    0.0909%      100%/yr
RIVER           0.1080%          -    0.0213%    0.0620%    0.0867%       95%/yr
CXMT            0.1176%          -    0.0323%    0.1024%    0.0853%       93%/yr
GRAM           -0.0176%   -0.0682%   -0.0497%    0.0027%    0.0709%       78%/yr  SIGN SPLIT
GMX             0.0096%    0.0100%    0.0100%   -0.0600%    0.0700%       77%/yr  SIGN SPLIT
USDJPY         -0.0304%   -0.0089%          -   -0.0746%    0.0657%       72%/yr
ZORA           -0.0328%   -0.0108%   -0.0478%    0.0100%    0.0578%       63%/yr  SIGN SPLIT
0G              0.0096%    0.0100%    0.0100%   -0.0472%    0.0572%       63%/yr  SIGN SPLIT
TIA             0.0000%    0.0086%   -0.0166%   -0.0467%    0.0553%       61%/yr  SIGN SPLIT
SKHYNIX               -    0.0050%    0.0000%    0.0535%    0.0535%       59%/yr
SAMSUNG               -    0.0511%    0.0000%    0.0133%    0.0511%       56%/yr
STRC           -0.0488%          -   -0.0052%          -    0.0436%       48%/yr
BB              0.0032%          -    0.0100%   -0.0288%    0.0388%       43%/yr  SIGN SPLIT
NVDA            0.0296%    0.0050%    0.0346%    0.0438%    0.0388%       42%/yr
BYD                   -          -    0.0000%    0.0354%    0.0354%       39%/yr
AAPL           -0.0176%   -0.0088%    0.0000%   -0.0353%    0.0353%       39%/yr
COIN            0.0152%    0.0353%    0.0000%    0.0000%    0.0353%       39%/yr
JUP             0.0096%   -0.0177%   -0.0131%   -0.0220%    0.0316%       35%/yr  SIGN SPLIT
DELL            0.0288%          -    0.0000%    0.0000%    0.0288%       32%/yr
SKY             0.0096%    0.0100%    0.0100%   -0.0180%    0.0280%       31%/yr  SIGN SPLIT
AVAX           -0.0168%    0.0050%    0.0100%   -0.0015%    0.0268%       29%/yr  SIGN SPLIT
FIL             0.0096%    0.0100%    0.0031%   -0.0167%    0.0267%       29%/yr  SIGN SPLIT

47 symbols where one venue pays longs while another pays shorts:
  GRAM, GMX, ZORA, 0G, TIA, BB, JUP, SKY, AVAX, FIL, GRASS, MET, 1000FLOKI, WLD, 1000PEPE, PYTH, ETHFI, LTC, ENA, CRV, APT, XLM, UNITREE, CHIP, BCH, ARB, SEI, AAVE, UNI, AXS, AERO, WLFI, DOGE, POL, QNT, TRUMP, HYPE, OP, MNT, LINK
```

## Builder-deployed markets
```
hl:xyz        144 mkts  OI $ 4,171,259,572  24h $ 4,673,577,951
             XYZ100, TSLA, NVDA, GOLD, HOOD, INTC, PLTR, COIN, META, AAPL, MSFT, ORCL, GOOGL, AMZN, AMD, MU, SNDK, MSTR
hl:io          23 mkts  OI $   230,464,135  24h $    67,653,486
             OAI, ANTH, SNDK, IONQ, NBIS, EWY, GPRO, SBE, TCNT, DRAM, PRL, XIAOMI, H100, MOONSHOT, NVDA, SKHX, AAPL, CRCL
hl:para        40 mkts  OI $    15,417,166  24h $     4,290,536
             TOTAL2, OTHERS, BTCD, H100, AVGO, COHR, GLW, CRDO, LRCX, NET, STX, IREN, VST, TER, AAOI, 10Y, CIEN, NAVER
hl:mkts        24 mkts  OI $       114,364  24h $       207,068
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

total 328 builder markets across 10 dexs
```

## Offchain reference rates (FRED)
```
OFFCHAIN REFERENCE RATES (FRED)

  SOFR      3.90%  2026-11-12     +1bp   Secured Overnight Financing Rate (what a desk funds at)
  DFF       3.88%  2026-11-11     +0bp   Effective fed funds
  IORB      3.90%  2026-11-13     +0bp   Interest on reserve balances
  DGS3MO    4.30%  2026-11-10     +6bp   3-month Treasury
  DGS10     4.98%  2026-11-10    +10bp   10-year Treasury
```

## Carry: funding vs borrow
```
PERP FUNDING (annualized from 8h feed) vs ONCHAIN BORROW

asset        lighter  hyperliq   binance     bybit  aave brw  aave sup
----------------------------------------------------------------------
BTC            10.5%     10.9%      9.9%      5.7%     0.00%     0.00%
ETH            10.5%      6.8%      5.9%      4.6%     0.00%     0.00%
SOL             7.0%      6.2%     10.9%      4.8%         -         -
ENA            10.5%     10.6%     -2.2%    -13.4%         -         -
HYPE           10.5%     10.9%     10.9%     -3.8%         -         -
LINK           10.5%      5.3%     10.9%     -2.3%     0.00%     0.00%
AVAX          -18.4%      5.6%     10.9%     -1.7%         -         -
DOGE           10.5%      0.4%     10.9%     -5.4%         -         -

STABLE BORROW COST (the cost of carrying a hedged position)
  aave   USDe     borrow  0.00%  supply  0.00%
  aave   RLUSD    borrow  2.73%  supply  1.30%
  aave   RLUSD    borrow  3.61%  supply  2.03%
  aave   GHO      borrow  3.86%  supply  2.95%
  aave   USDC     borrow  3.89%  supply  2.72%
  aave   USDC     borrow  4.51%  supply  3.30%
  aave   GHO      borrow  4.51%  supply  3.57%
  aave   GHO      borrow  4.67%  supply  3.78%
  morpho    cbBTC/USDC    borrow  5.13%  lltv 0.86  $345,700,991
  morpho     kBTC/RLUSD   borrow  3.30%  lltv 0.86  $248,349,422
  morpho    PRIME/PYUSD   borrow  6.22%  lltv 0.86  $186,920,294
  morpho PT-reUSD-10DEC2026/USDC    borrow  9.55%  lltv 0.92  $152,405,834
  morpho     WBTC/USDC    borrow  5.14%  lltv 0.86  $139,830,483
  morpho    sUSDe/PYUSD   borrow  4.23%  lltv 0.92  $115,090,741

OFFCHAIN BENCHMARK: SOFR 3.90% (2026-11-12)
  BTC perp funding 10.51% vs SOFR 3.90%: spread +6.61pp over the offchain cost of money

BUILDER-DEPLOYED PERPS: 328 markets, 171 with volume today
  xyz:SP500        OI $  448,875,973  funding      5.5%/yr
  xyz:NVDA         OI $  394,457,915  funding      5.5%/yr
  xyz:BRENTOIL     OI $  296,901,092  funding      5.5%/yr
  xyz:GOLD         OI $  290,031,283  funding      8.3%/yr
  xyz:SKHX         OI $  278,757,901  funding      5.5%/yr
  xyz:XYZ100       OI $  270,026,975  funding     -7.1%/yr
  io:ANTH          OI $  201,004,136  funding      1.4%/yr
  xyz:GOOGL        OI $  162,144,068  funding      5.5%/yr
  xyz:SILVER       OI $  154,814,650  funding      5.5%/yr
  xyz:MU           OI $  146,074,830  funding     15.1%/yr
```
