# 2026-10-23

## Market list changes
```
2026-10-22.json -> 2026-10-23.json

hl:abcd: no change (1 markets)
hl:cash: no change (17 markets)
hl:flx: no change (16 markets)
hl:hyna: no change (25 markets)
hl:io: 14 -> 15
  NEW     (1): io:NVDA

hl:km: no change (23 markets)
hl:mkts: no change (24 markets)
hl:para: no change (39 markets)
hl:vntl: no change (15 markets)
hl:xyz: no change (138 markets)
hyperliquid: no change (234 markets)
lighter: no change (235 markets)
variational: 580 -> 582
  NEW     (2): BSP, IBKR

```

## Funding dispersion
```
205 symbols quoted on 2+ venues. Top 25 by dispersion.

sym             lighter  hyperliqu    binance      bybit     spread      ann  flag
----------------------------------------------------------------------------------
BIRB                  -          -   -1.9177%    0.0147%    1.9324%     2116%/yr  SIGN SPLIT
AI              0.2600%    0.0000%    0.0000%          -    0.2600%      285%/yr
CASHCAT        -0.2264%    0.0100%          -    0.0022%    0.2364%      259%/yr  SIGN SPLIT
CXMT            0.0048%          -    0.1103%    0.0079%    0.1055%      115%/yr
SAMSUNG               -    0.0719%    0.0345%    0.0000%    0.0719%       79%/yr
BERA            0.0096%   -0.0218%   -0.0285%   -0.0566%    0.0662%       72%/yr  SIGN SPLIT
PRL            -0.0456%          -    0.0100%    0.0100%    0.0556%       61%/yr  SIGN SPLIT
ARC             0.0096%          -    0.0100%    0.0600%    0.0504%       55%/yr
SMIC            0.0472%          -          -    0.0000%    0.0472%       52%/yr
WLFI            0.0080%   -0.0370%    0.0100%   -0.0141%    0.0470%       51%/yr  SIGN SPLIT
SKHYNIX               -    0.0412%    0.0000%    0.0000%    0.0412%       45%/yr
QNT            -0.0512%          -   -0.0167%   -0.0103%    0.0409%       45%/yr
MET             0.0096%   -0.0175%   -0.0256%   -0.0308%    0.0404%       44%/yr  SIGN SPLIT
WEN             0.0032%          -   -0.0359%          -    0.0391%       43%/yr  SIGN SPLIT
ETHFI          -0.0256%    0.0100%    0.0059%   -0.0054%    0.0356%       39%/yr  SIGN SPLIT
LITE            0.0328%          -    0.0000%    0.0000%    0.0328%       36%/yr
PIPPIN                -          -    0.0468%    0.0793%    0.0326%       36%/yr
GEV             0.0032%          -    0.0206%    0.0348%    0.0316%       35%/yr
PROVE           0.0096%    0.0100%    0.0100%   -0.0211%    0.0311%       34%/yr  SIGN SPLIT
1000FLOKI       0.0096%    0.0100%   -0.0198%    0.0037%    0.0298%       33%/yr  SIGN SPLIT
AAPL            0.0032%   -0.0094%   -0.0085%   -0.0262%    0.0294%       32%/yr  SIGN SPLIT
ZRO             0.0096%    0.0347%    0.0057%    0.0100%    0.0291%       32%/yr
CC              0.0096%    0.0100%   -0.0181%    0.0100%    0.0281%       31%/yr  SIGN SPLIT
COIN            0.0032%    0.0059%    0.0000%    0.0278%    0.0278%       30%/yr
TRX             0.0048%   -0.0090%   -0.0183%   -0.0218%    0.0266%       29%/yr  SIGN SPLIT

42 symbols where one venue pays longs while another pays shorts:
  BIRB, CASHCAT, BERA, PRL, WLFI, MET, WEN, ETHFI, PROVE, 1000FLOKI, AAPL, CC, TRX, ADA, MORPHO, MEGA, NMR, 2Z, PAXG, BOT, PUMP, ICP, APT, OP, GRAM, BCH, WIF, PENDLE, MNT, NEAR, TRUMP, EIGEN, LINEA, CRV, TIA, GMX, LTC, DIA, SOXS, OPENAI
```

## Builder-deployed markets
```
hl:xyz        138 mkts  OI $ 3,887,705,391  24h $ 3,772,842,236
             XYZ100, TSLA, NVDA, GOLD, HOOD, INTC, PLTR, COIN, META, AAPL, MSFT, ORCL, GOOGL, AMZN, AMD, MU, SNDK, MSTR
hl:io          15 mkts  OI $    77,566,572  24h $    64,534,629
             OAI, ANTH, SNDK, IONQ, NBIS, EWY, GPRO, SBE, TCNT, DRAM, PRL, XIAOMI, H100, MOONSHOT, NVDA
hl:para        39 mkts  OI $    17,276,624  24h $     7,053,375
             TOTAL2, OTHERS, BTCD, H100, AVGO, COHR, GLW, CRDO, LRCX, NET, STX, IREN, VST, TER, AAOI, 10Y, CIEN, NAVER
hl:mkts        24 mkts  OI $     9,740,186  24h $     2,341,677
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

total 313 builder markets across 10 dexs
```

## Offchain reference rates (FRED)
```
OFFCHAIN REFERENCE RATES (FRED)

  SOFR      3.90%  2026-10-22     +2bp   Secured Overnight Financing Rate (what a desk funds at)
  DFF       3.88%  2026-10-21     +0bp   Effective fed funds
  IORB      3.90%  2026-10-23     +0bp   Interest on reserve balances
  DGS3MO    4.25%  2026-10-21     -1bp   3-month Treasury
  DGS10     5.13%  2026-10-21     +1bp   10-year Treasury
```

## Carry: funding vs borrow
```
PERP FUNDING (annualized from 8h feed) vs ONCHAIN BORROW

asset        lighter  hyperliq   binance     bybit  aave brw  aave sup
----------------------------------------------------------------------
BTC            10.5%     10.9%     10.9%      4.8%     0.00%     0.00%
ETH            10.5%     10.9%      6.9%      6.3%     0.00%     0.00%
SOL            10.5%     10.9%     10.9%      9.8%         -         -
ENA            10.5%     10.9%      8.1%     10.9%         -         -
HYPE           10.5%     10.9%     10.9%     10.9%         -         -
LINK           10.5%     10.9%      6.1%      1.9%     0.00%     0.00%
AVAX           -8.8%     -8.6%     -1.7%     -0.3%         -         -
DOGE           10.5%      9.3%     10.3%      1.7%         -         -

STABLE BORROW COST (the cost of carrying a hedged position)
  aave   USDe     borrow  0.00%  supply  0.00%
  aave   RLUSD    borrow  0.50%  supply  0.00%
  aave   RLUSD    borrow  2.73%  supply  1.17%
  aave   GHO      borrow  4.05%  supply  3.24%
  aave   GHO      borrow  4.08%  supply  3.30%
  aave   USDC     borrow  4.09%  supply  3.00%
  aave   GHO      borrow  4.53%  supply  3.60%
  aave   USDC     borrow  4.56%  supply  3.44%
  morpho    cbBTC/USDC    borrow  4.88%  lltv 0.86  $343,621,957
  morpho     kBTC/RLUSD   borrow  4.29%  lltv 0.86  $265,002,725
  morpho    PRIME/PYUSD   borrow  5.07%  lltv 0.86  $210,067,665
  morpho   wstETH/USDT    borrow  2.97%  lltv 0.86  $162,934,065
  morpho PT-reUSD-10DEC2026/USDC    borrow  8.48%  lltv 0.92  $135,102,179
  morpho     WBTC/USDC    borrow  4.92%  lltv 0.86  $128,663,244

OFFCHAIN BENCHMARK: SOFR 3.90% (2026-10-22)
  BTC perp funding 10.51% vs SOFR 3.90%: spread +6.61pp over the offchain cost of money

BUILDER-DEPLOYED PERPS: 313 markets, 164 with volume today
  xyz:SP500        OI $  388,388,197  funding     -0.6%/yr
  xyz:GOLD         OI $  330,061,926  funding     26.3%/yr
  xyz:SKHX         OI $  316,174,720  funding     44.9%/yr
  xyz:XYZ100       OI $  288,556,705  funding      5.5%/yr
  xyz:BRENTOIL     OI $  232,971,369  funding    -14.0%/yr
  xyz:CL           OI $  213,036,346  funding     -9.9%/yr
  xyz:SILVER       OI $  170,526,931  funding      5.5%/yr
  xyz:SPCX         OI $  156,245,794  funding      5.5%/yr
  xyz:MU           OI $  155,801,444  funding      5.5%/yr
  xyz:SKHY         OI $  144,638,377  funding      5.5%/yr
```
