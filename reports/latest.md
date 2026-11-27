# 2026-11-27

## Market list changes
```
2026-11-26.json -> 2026-11-27.json

hl:abcd: no change (1 markets)
hl:cash: no change (17 markets)
hl:flx: no change (16 markets)
hl:hyna: no change (25 markets)
hl:io: no change (26 markets)
hl:km: no change (23 markets)
hl:mkts: no change (24 markets)
hl:para: 40 -> 41
  NEW     (1): para:VAR

hl:vntl: no change (15 markets)
hl:xyz: no change (150 markets)
hyperliquid: no change (235 markets)
lighter: no change (235 markets)
variational: 597 -> 595
  REMOVED (2): STORJ, TOWNS

```

## Funding dispersion
```
205 symbols quoted on 2+ venues. Top 25 by dispersion.

sym             lighter  hyperliqu    binance      bybit     spread      ann  flag
----------------------------------------------------------------------------------
SKHY           -0.4072%          -    0.0256%   -0.3000%    0.4328%      474%/yr  SIGN SPLIT
PRL             0.1200%          -    0.0100%    0.0100%    0.1100%      120%/yr
XPD             0.0480%    0.1368%    0.0698%          -    0.0888%       97%/yr
CXMT            0.0672%          -    0.1359%    0.1512%    0.0840%       92%/yr
CC             -0.1144%   -0.0348%   -0.0965%   -0.1022%    0.0796%       87%/yr
SKY             0.0096%   -0.0603%   -0.0225%   -0.0366%    0.0699%       76%/yr  SIGN SPLIT
CHIP            0.0096%   -0.0544%    0.0100%    0.0100%    0.0644%       71%/yr  SIGN SPLIT
ASTER          -0.0512%    0.0100%    0.0092%    0.0042%    0.0612%       67%/yr  SIGN SPLIT
ARC             0.0696%          -    0.0100%    0.0123%    0.0596%       65%/yr
STABLE          0.0096%    0.0100%    0.0100%   -0.0449%    0.0549%       60%/yr  SIGN SPLIT
BIRB                  -          -    0.0100%   -0.0447%    0.0547%       60%/yr  SIGN SPLIT
WLD            -0.0088%    0.0007%   -0.0175%   -0.0528%    0.0536%       59%/yr  SIGN SPLIT
MET             0.0096%   -0.0422%    0.0020%   -0.0178%    0.0518%       57%/yr  SIGN SPLIT
ANT            -0.0064%          -   -0.0054%   -0.0564%    0.0510%       56%/yr
ZORA           -0.0400%   -0.0114%    0.0100%    0.0100%    0.0500%       55%/yr  SIGN SPLIT
HYUNDAI               -    0.0498%    0.0000%    0.0000%    0.0498%       55%/yr
EDGE                  -          -    0.0100%   -0.0391%    0.0491%       54%/yr  SIGN SPLIT
EURUSD          0.0000%    0.0071%          -    0.0483%    0.0483%       53%/yr
XMR             0.0536%    0.0100%    0.0100%    0.0100%    0.0436%       48%/yr
CRV            -0.0512%   -0.0222%   -0.0087%   -0.0214%    0.0425%       47%/yr
S               0.0032%   -0.0331%    0.0072%    0.0094%    0.0425%       46%/yr  SIGN SPLIT
ICP             0.0040%   -0.0316%    0.0100%   -0.0007%    0.0416%       46%/yr  SIGN SPLIT
XPL             0.0096%    0.0100%    0.0044%   -0.0311%    0.0411%       45%/yr  SIGN SPLIT
SKHYNIX               -    0.0409%    0.0134%    0.0522%    0.0389%       43%/yr
COIN            0.0384%    0.0344%    0.0000%    0.0000%    0.0384%       42%/yr

65 symbols where one venue pays longs while another pays shorts:
  SKHY, SKY, CHIP, ASTER, STABLE, BIRB, WLD, MET, ZORA, EDGE, S, ICP, XPL, BOT, TRX, AVNT, TIA, 1000PEPE, CRO, MORPHO, WLFI, TRUMP, ENA, PENDLE, SPCX, KAITO, JTO, PENGU, ETHFI, ONDO, XLM, AXS, GMX, FIL, VVV, EIGEN, NATGAS, LINEA, POL, BCH
```

## Builder-deployed markets
```
hl:xyz        150 mkts  OI $ 4,057,832,816  24h $ 4,104,034,550
             XYZ100, TSLA, NVDA, GOLD, HOOD, INTC, PLTR, COIN, META, AAPL, MSFT, ORCL, GOOGL, AMZN, AMD, MU, SNDK, MSTR
hl:io          26 mkts  OI $   106,820,711  24h $    62,615,214
             OAI, ANTH, SNDK, IONQ, NBIS, EWY, GPRO, SBE, TCNT, DRAM, PRL, XIAOMI, H100, MOONSHOT, NVDA, SKHX, AAPL, CRCL
hl:para        41 mkts  OI $    13,570,741  24h $     5,808,672
             TOTAL2, OTHERS, BTCD, H100, AVGO, COHR, GLW, CRDO, LRCX, NET, STX, IREN, VST, TER, AAOI, 10Y, CIEN, NAVER
hl:mkts        24 mkts  OI $       129,283  24h $        68,140
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

total 338 builder markets across 10 dexs
```

## Offchain reference rates (FRED)
```
OFFCHAIN REFERENCE RATES (FRED)

  SOFR      3.95%  2026-11-25     +1bp   Secured Overnight Financing Rate (what a desk funds at)
  DFF       3.88%  2026-11-24     +0bp   Effective fed funds
  IORB      3.90%  2026-11-27     +0bp   Interest on reserve balances
  DGS3MO    4.36%  2026-11-24     -1bp   3-month Treasury
  DGS10     4.91%  2026-11-24     -1bp   10-year Treasury
```

## Carry: funding vs borrow
```
PERP FUNDING (annualized from 8h feed) vs ONCHAIN BORROW

asset        lighter  hyperliq   binance     bybit  aave brw  aave sup
----------------------------------------------------------------------
BTC            10.5%      8.3%      6.7%      6.9%     0.00%     0.00%
ETH             7.9%     10.9%      3.5%     -1.2%     0.00%     0.00%
SOL            10.5%      2.1%     -2.9%      8.9%         -         -
ENA            10.5%     -8.9%     -5.6%    -21.3%         -         -
HYPE           10.5%     10.9%     10.9%      7.8%         -         -
LINK           -5.3%     -5.0%     -2.0%     -5.3%     0.00%     0.00%
AVAX            1.8%     -8.3%    -12.6%    -10.5%         -         -
DOGE           10.5%     -1.7%     -3.9%      8.4%         -         -

STABLE BORROW COST (the cost of carrying a hedged position)
  aave   USDe     borrow  0.00%  supply  0.00%
  aave   RLUSD    borrow  3.61%  supply  2.03%
  aave   RLUSD    borrow  3.80%  supply  3.10%
  aave   USDC     borrow  3.90%  supply  2.73%
  aave   GHO      borrow  4.03%  supply  3.22%
  aave   USDC     borrow  4.29%  supply  3.30%
  aave   GHO      borrow  4.36%  supply  3.33%
  aave   USDC     borrow  4.69%  supply  3.49%
  morpho    cbBTC/USDC    borrow  3.87%  lltv 0.86  $220,562,334
  morpho     kBTC/RLUSD   borrow  3.30%  lltv 0.86  $158,719,409
  morpho PT-reUSD-10DEC2026/USDC    borrow  8.33%  lltv 0.92  $135,683,337
  morpho    PRIME/PYUSD   borrow  6.03%  lltv 0.86  $128,834,275
  morpho     WBTC/USDC    borrow  3.88%  lltv 0.86  $126,573,462
  morpho     kBTC/PYUSD   borrow  4.20%  lltv 0.86  $119,322,143

OFFCHAIN BENCHMARK: SOFR 3.95% (2026-11-25)
  BTC perp funding 10.51% vs SOFR 3.95%: spread +6.56pp over the offchain cost of money

BUILDER-DEPLOYED PERPS: 338 markets, 178 with volume today
  xyz:SP500        OI $  423,515,515  funding     10.8%/yr
  xyz:NVDA         OI $  371,936,781  funding      7.3%/yr
  xyz:XYZ100       OI $  348,459,889  funding      5.5%/yr
  xyz:GOLD         OI $  269,516,561  funding     31.1%/yr
  xyz:ANT          OI $  254,115,878  funding     -0.0%/yr
  xyz:SKHX         OI $  240,838,316  funding     44.7%/yr
  xyz:GOOGL        OI $  184,995,591  funding      5.5%/yr
  xyz:MU           OI $  153,911,386  funding      5.5%/yr
  xyz:SKHY         OI $  153,592,908  funding   -572.3%/yr
  xyz:SILVER       OI $  137,433,200  funding      5.5%/yr
```
