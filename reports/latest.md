# 2026-11-06

## Market list changes
```
2026-11-05.json -> 2026-11-06.json

hl:abcd: no change (1 markets)
hl:cash: no change (17 markets)
hl:flx: no change (16 markets)
hl:hyna: no change (25 markets)
hl:io: 19 -> 20
  NEW     (1): io:MU

hl:km: no change (23 markets)
hl:mkts: no change (24 markets)
hl:para: no change (40 markets)
hl:vntl: no change (15 markets)
hl:xyz: no change (143 markets)
hyperliquid: no change (235 markets)
lighter: 235 -> 235
  NEW     (1): ASELS
  REMOVED (1): URA

variational: no change (588 markets)
```

## Funding dispersion
```
205 symbols quoted on 2+ venues. Top 25 by dispersion.

sym             lighter  hyperliqu    binance      bybit     spread      ann  flag
----------------------------------------------------------------------------------
PRL             0.4056%          -    0.0100%    0.0100%    0.3956%      433%/yr
NATGAS          1.2568%    1.3332%    1.0000%          -    0.3332%      365%/yr
FOLKS           0.2752%          -    0.0100%    0.0100%    0.2652%      290%/yr
BIRB                  -          -   -1.1167%   -1.3685%    0.2518%      276%/yr
BRENTOIL       -0.2304%   -0.2486%   -0.3432%          -    0.1128%      124%/yr
SAMSUNG               -   -0.1983%   -0.1031%   -0.1737%    0.0952%      104%/yr
XCU             0.0640%    0.0751%    0.1488%          -    0.0848%       93%/yr
STONK           0.0896%          -          -    0.0100%    0.0796%       87%/yr
CXMT           -0.0640%          -   -0.1339%   -0.1355%    0.0715%       78%/yr
BB              0.0032%          -    0.0100%   -0.0517%    0.0617%       68%/yr  SIGN SPLIT
WTI            -0.1224%   -0.1299%   -0.1703%   -0.1840%    0.0616%       67%/yr
SKHYNIX               -   -0.2050%   -0.1466%   -0.1542%    0.0584%       64%/yr
ZHIPU          -0.0936%          -   -0.1508%   -0.1221%    0.0572%       63%/yr
NOW             0.0536%          -    0.0000%    0.0000%    0.0536%       59%/yr
KAITO          -0.0136%   -0.0424%    0.0100%    0.0100%    0.0524%       57%/yr  SIGN SPLIT
XPT             0.0032%   -0.0480%   -0.0059%          -    0.0512%       56%/yr  SIGN SPLIT
DELL            0.0496%          -    0.0000%    0.0095%    0.0496%       54%/yr
XMR             0.0192%    0.0598%    0.0115%    0.0387%    0.0483%       53%/yr
XIAOMI          0.0032%          -          -   -0.0443%    0.0475%       52%/yr  SIGN SPLIT
ASML            0.0456%          -    0.0000%    0.0000%    0.0456%       50%/yr
ICP             0.0096%   -0.0342%    0.0100%    0.0096%    0.0442%       48%/yr  SIGN SPLIT
HYUNDAI               -   -0.0435%    0.0000%    0.0000%    0.0435%       48%/yr
LITE            0.0416%          -    0.0034%    0.0000%    0.0416%       46%/yr
LIT             0.0048%   -0.0164%    0.0092%   -0.0316%    0.0407%       45%/yr  SIGN SPLIT
STABLE          0.0096%    0.0100%    0.0100%   -0.0303%    0.0403%       44%/yr  SIGN SPLIT

42 symbols where one venue pays longs while another pays shorts:
  BB, KAITO, XPT, XIAOMI, ICP, LIT, STABLE, LINEA, GRAM, S, WLFI, CHIP, XLM, PONS, ETHFI, 1000SHIB, MEGA, VIRTUAL, SOXS, AERO, ZEC, MET, MORPHO, BCH, CC, TRX, SUI, TIA, NEAR, APT, HBAR, ZK, XRP, DOGE, ARB, AVAX, DYDX, CRV, ANTHROPIC, 1000BONK
```

## Builder-deployed markets
```
hl:xyz        143 mkts  OI $ 4,312,276,070  24h $ 7,786,357,591
             XYZ100, TSLA, NVDA, GOLD, HOOD, INTC, PLTR, COIN, META, AAPL, MSFT, ORCL, GOOGL, AMZN, AMD, MU, SNDK, MSTR
hl:io          20 mkts  OI $   155,006,242  24h $   140,453,887
             OAI, ANTH, SNDK, IONQ, NBIS, EWY, GPRO, SBE, TCNT, DRAM, PRL, XIAOMI, H100, MOONSHOT, NVDA, SKHX, AAPL, CRCL
hl:para        40 mkts  OI $    15,000,261  24h $     6,480,227
             TOTAL2, OTHERS, BTCD, H100, AVGO, COHR, GLW, CRDO, LRCX, NET, STX, IREN, VST, TER, AAOI, 10Y, CIEN, NAVER
hl:mkts        24 mkts  OI $       167,091  24h $       224,911
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

total 324 builder markets across 10 dexs
```

## Offchain reference rates (FRED)
```
OFFCHAIN REFERENCE RATES (FRED)

  SOFR      3.92%  2026-11-05     -2bp   Secured Overnight Financing Rate (what a desk funds at)
  DFF       3.88%  2026-11-04     +0bp   Effective fed funds
  IORB      3.90%  2026-11-06     +0bp   Interest on reserve balances
  DGS3MO    4.21%  2026-11-04     +0bp   3-month Treasury
  DGS10     4.90%  2026-11-04     -5bp   10-year Treasury
```

## Carry: funding vs borrow
```
PERP FUNDING (annualized from 8h feed) vs ONCHAIN BORROW

asset        lighter  hyperliq   binance     bybit  aave brw  aave sup
----------------------------------------------------------------------
BTC            10.5%     10.9%     10.9%      8.7%     0.00%     0.00%
ETH            10.5%     10.9%      4.1%      3.2%     0.00%     0.00%
SOL            10.5%     10.9%     10.4%     -0.3%         -         -
ENA            10.5%     10.9%     10.9%      8.3%         -         -
HYPE           10.5%     10.9%     10.9%      6.0%         -         -
LINK            6.1%     10.9%     10.9%     10.9%     0.00%     0.00%
AVAX           -1.8%     -2.1%      9.2%     10.9%         -         -
DOGE           10.5%      9.3%      5.8%     -6.9%         -         -

STABLE BORROW COST (the cost of carrying a hedged position)
  aave   USDe     borrow  0.00%  supply  0.00%
  aave   RLUSD    borrow  3.50%  supply  1.91%
  aave   RLUSD    borrow  3.75%  supply  2.59%
  aave   USDC     borrow  3.79%  supply  2.58%
  aave   GHO      borrow  4.04%  supply  3.23%
  aave   GHO      borrow  4.53%  supply  3.60%
  aave   USDC     borrow  4.60%  supply  3.80%
  aave   USDC     borrow  5.61%  supply  4.59%
  morpho    cbBTC/USDC    borrow  9.05%  lltv 0.86  $326,211,653
  morpho     kBTC/RLUSD   borrow  3.69%  lltv 0.86  $255,058,131
  morpho    PRIME/PYUSD   borrow  6.11%  lltv 0.86  $186,983,255
  morpho PT-reUSD-10DEC2026/USDC    borrow 12.21%  lltv 0.92  $146,331,688
  morpho     WBTC/USDC    borrow  7.87%  lltv 0.86  $134,289,205
  morpho   wstETH/USDT    borrow 12.72%  lltv 0.86  $118,005,495

OFFCHAIN BENCHMARK: SOFR 3.92% (2026-11-05)
  BTC perp funding 10.51% vs SOFR 3.92%: spread +6.59pp over the offchain cost of money

BUILDER-DEPLOYED PERPS: 324 markets, 168 with volume today
  xyz:SP500        OI $  385,859,251  funding      5.5%/yr
  xyz:BRENTOIL     OI $  380,675,726  funding   -272.5%/yr
  xyz:SKHX         OI $  354,704,818  funding   -224.1%/yr
  xyz:GOLD         OI $  298,613,419  funding      5.5%/yr
  xyz:XYZ100       OI $  293,662,076  funding      5.5%/yr
  xyz:SILVER       OI $  205,569,750  funding      5.5%/yr
  xyz:GOOGL        OI $  200,973,783  funding      5.5%/yr
  xyz:MU           OI $  181,848,752  funding      5.9%/yr
  xyz:CL           OI $  172,782,260  funding   -142.3%/yr
  xyz:SPCX         OI $  162,582,705  funding      9.5%/yr
```
