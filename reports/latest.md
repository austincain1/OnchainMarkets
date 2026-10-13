# 2026-10-13

## Market list changes
```
2026-10-12.json -> 2026-10-13.json

hl:abcd: no change (1 markets)
hl:cash: no change (17 markets)
hl:flx: no change (16 markets)
hl:hyna: no change (25 markets)
hl:io: 12 -> 13
  NEW     (1): io:H100

hl:km: no change (23 markets)
hl:mkts: no change (24 markets)
hl:para: no change (38 markets)
hl:vntl: no change (15 markets)
hl:xyz: no change (134 markets)
hyperliquid: no change (234 markets)
lighter: no change (235 markets)
variational: 568 -> 570
  NEW     (2): ADBE, HOILP

```

## Funding dispersion
```
205 symbols quoted on 2+ venues. Top 25 by dispersion.

sym             lighter  hyperliqu    binance      bybit     spread      ann  flag
----------------------------------------------------------------------------------
ARC             0.1352%          -   -0.5069%    0.1018%    0.6421%      703%/yr  SIGN SPLIT
CASHCAT         0.5112%    0.0100%          -    0.0100%    0.5012%      549%/yr
NATGAS          0.6848%    0.7009%    1.0000%          -    0.3152%      345%/yr
PRL            -0.2200%          -    0.0100%    0.0100%    0.2300%      252%/yr  SIGN SPLIT
AI              0.1768%    0.0000%    0.0000%          -    0.1768%      194%/yr
BRENTOIL       -0.1808%   -0.1935%   -0.2893%          -    0.1085%      119%/yr
MET             0.0096%   -0.0850%   -0.0323%   -0.0235%    0.0946%      104%/yr  SIGN SPLIT
PROVE          -0.0840%    0.0100%    0.0100%   -0.0287%    0.0940%      103%/yr  SIGN SPLIT
AVNT            0.0096%   -0.0358%    0.0100%   -0.0754%    0.0854%       94%/yr  SIGN SPLIT
WTI            -0.0904%   -0.0842%   -0.1360%   -0.1622%    0.0780%       85%/yr
CAP             0.0096%          -    0.0569%    0.0796%    0.0700%       77%/yr
HYUNDAI               -    0.0687%    0.0000%    0.0000%    0.0687%       75%/yr
TTWO            0.0664%          -    0.0192%    0.0000%    0.0664%       73%/yr
SAMSUNG               -    0.0658%    0.0000%    0.0000%    0.0658%       72%/yr
MRNA            0.0648%          -    0.0000%    0.0000%    0.0648%       71%/yr
LITE            0.0608%          -    0.0000%    0.0000%    0.0608%       67%/yr
TRX            -0.0032%   -0.0563%   -0.0272%   -0.0156%    0.0531%       58%/yr
SKHYNIX               -    0.0484%    0.0000%    0.0000%    0.0484%       53%/yr
CRO            -0.0376%          -          -    0.0100%    0.0476%       52%/yr  SIGN SPLIT
DUSK                  -          -   -0.0349%    0.0100%    0.0449%       49%/yr  SIGN SPLIT
CXMT            0.0032%          -    0.0000%    0.0448%    0.0448%       49%/yr
QNT            -0.0840%          -   -0.0418%   -0.0598%    0.0422%       46%/yr
CRV            -0.0312%    0.0100%    0.0013%   -0.0172%    0.0412%       45%/yr  SIGN SPLIT
ETHFI           0.0096%    0.0060%   -0.0049%   -0.0312%    0.0408%       45%/yr  SIGN SPLIT
XPD             0.0336%    0.0241%    0.0612%          -    0.0372%       41%/yr

44 symbols where one venue pays longs while another pays shorts:
  ARC, PRL, MET, PROVE, AVNT, CRO, DUSK, CRV, ETHFI, CHIP, S, PYTH, UNITREE, AVAX, PENGU, MEGA, PONS, 1000FLOKI, DYDX, XMR, XRP, EIGEN, AAVE, JUP, VIRTUAL, PUMP, 1000SHIB, LIT, ONDO, APT, WLD, XPL, SKR, ICP, 1000BONK, ZK, FIL, MSFT, SUI, ARB
```

## Builder-deployed markets
```
hl:xyz        134 mkts  OI $ 3,792,567,106  24h $ 2,978,274,267
             XYZ100, TSLA, NVDA, GOLD, HOOD, INTC, PLTR, COIN, META, AAPL, MSFT, ORCL, GOOGL, AMZN, AMD, MU, SNDK, MSTR
hl:io          13 mkts  OI $    62,962,476  24h $    91,008,383
             OAI, ANTH, SNDK, IONQ, NBIS, EWY, GPRO, SBE, TCNT, DRAM, PRL, XIAOMI, H100
hl:para        38 mkts  OI $    16,928,772  24h $     6,511,706
             TOTAL2, OTHERS, BTCD, H100, AVGO, COHR, GLW, CRDO, LRCX, NET, STX, IREN, VST, TER, AAOI, 10Y, CIEN, NAVER
hl:mkts        24 mkts  OI $    10,846,049  24h $     3,632,267
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

total 306 builder markets across 10 dexs
```

## Offchain reference rates (FRED)
```
OFFCHAIN REFERENCE RATES (FRED)

  SOFR      3.87%  2026-10-09     +0bp   Secured Overnight Financing Rate (what a desk funds at)
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
BTC             0.0%     10.0%      4.5%      0.6%     0.00%     0.00%
ETH             0.0%     10.9%      6.8%      5.4%     0.00%     0.00%
SOL             9.6%     10.9%      5.1%      9.8%         -         -
ENA            10.5%     10.9%     10.9%     10.9%         -         -
HYPE           10.5%     10.9%     10.9%      8.9%         -         -
LINK           10.5%     10.9%      3.9%      5.2%     0.00%     0.00%
AVAX            6.1%     -2.1%      5.4%    -24.7%         -         -
DOGE           10.5%     10.9%      7.0%     10.9%         -         -

STABLE BORROW COST (the cost of carrying a hedged position)
  aave   USDT     borrow  0.11%  supply  0.00%
  aave   GHO      borrow  3.11%  supply  1.70%
  aave   USDC     borrow  3.90%  supply  2.74%
  aave   GHO      borrow  4.06%  supply  3.26%
  aave   USDT     borrow  4.18%  supply  3.14%
  aave   USDC     borrow  4.35%  supply  3.13%
  aave   RLUSD    borrow  4.39%  supply  2.80%
  aave   USDT     borrow  4.60%  supply  3.50%
  morpho    cbBTC/USDC    borrow  5.01%  lltv 0.86  $337,714,085
  morpho     kBTC/RLUSD   borrow  3.49%  lltv 0.86  $250,054,654
  morpho    PRIME/PYUSD   borrow  5.07%  lltv 0.86  $209,753,902
  morpho     kBTC/PYUSD   borrow  5.11%  lltv 0.86  $173,450,377
  morpho   wstETH/USDT    borrow  3.04%  lltv 0.86  $142,738,470
  morpho     WBTC/USDC    borrow  4.88%  lltv 0.86  $129,247,151

OFFCHAIN BENCHMARK: SOFR 3.87% (2026-10-09)
  BTC perp funding 0.00% vs SOFR 3.87%: spread -3.87pp over the offchain cost of money

BUILDER-DEPLOYED PERPS: 306 markets, 160 with volume today
  xyz:SP500        OI $  390,736,692  funding     -3.5%/yr
  xyz:SKHX         OI $  308,634,553  funding     53.5%/yr
  xyz:GOLD         OI $  305,042,655  funding      5.5%/yr
  xyz:XYZ100       OI $  262,588,540  funding      5.5%/yr
  xyz:BRENTOIL     OI $  202,040,090  funding   -212.1%/yr
  xyz:GOOGL        OI $  181,207,726  funding     11.7%/yr
  xyz:SILVER       OI $  147,466,958  funding      5.5%/yr
  xyz:SNDK         OI $  141,003,262  funding      5.5%/yr
  xyz:SKHY         OI $  139,078,668  funding      5.5%/yr
  xyz:CL           OI $  130,695,346  funding    -92.4%/yr
```
