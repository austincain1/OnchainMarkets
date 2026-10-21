# 2026-10-21

## Market list changes
```
2026-10-20.json -> 2026-10-21.json

hl:abcd: no change (1 markets)
hl:cash: no change (17 markets)
hl:flx: no change (16 markets)
hl:hyna: no change (25 markets)
hl:io: no change (14 markets)
hl:km: no change (23 markets)
hl:mkts: no change (24 markets)
hl:para: no change (39 markets)
hl:vntl: no change (15 markets)
hl:xyz: no change (137 markets)
hyperliquid: no change (234 markets)
lighter: 235 -> 235
  NEW     (1): TUR30
  REMOVED (1): EDEN

variational: 577 -> 578
  NEW     (1): IONQ

```

## Funding dispersion
```
205 symbols quoted on 2+ venues. Top 25 by dispersion.

sym             lighter  hyperliqu    binance      bybit     spread      ann  flag
----------------------------------------------------------------------------------
BIRB                  -          -   -1.9513%   -0.0432%    1.9081%     2089%/yr
STONK           0.3968%          -          -    0.0493%    0.3475%      381%/yr
PRL             0.2352%          -    0.0100%    0.0100%    0.2252%      247%/yr
SMIC            0.1680%          -          -    0.0000%    0.1680%      184%/yr
1000TOSHI             -          -   -0.0601%    0.0040%    0.0641%       70%/yr  SIGN SPLIT
BERA            0.0096%   -0.0526%    0.0002%    0.0100%    0.0626%       69%/yr  SIGN SPLIT
SKHYNIX               -    0.0418%   -0.0183%   -0.0074%    0.0602%       66%/yr  SIGN SPLIT
CAP             0.0656%          -    0.0100%    0.0100%    0.0556%       61%/yr
SAMSUNG               -    0.0540%    0.0000%    0.0000%    0.0540%       59%/yr
NEAR            0.0096%    0.0619%    0.0100%    0.0100%    0.0523%       57%/yr
PIPPIN                -          -    0.0558%    0.0100%    0.0458%       50%/yr
BMNR            0.0032%          -    0.0135%    0.0478%    0.0446%       49%/yr
CXMT            0.0520%          -    0.0169%    0.0108%    0.0412%       45%/yr
FF              0.0096%          -    0.0100%   -0.0284%    0.0384%       42%/yr  SIGN SPLIT
HYUNDAI               -    0.0382%    0.0000%    0.0000%    0.0382%       42%/yr
STRK            0.0096%    0.0392%    0.0015%    0.0100%    0.0377%       41%/yr
S               0.0096%   -0.0270%   -0.0061%    0.0100%    0.0370%       40%/yr  SIGN SPLIT
EDGE            0.0096%          -    0.0458%    0.0100%    0.0362%       40%/yr
XAU             0.0168%    0.0054%    0.0168%    0.0391%    0.0336%       37%/yr
CASHCAT         0.0432%    0.0100%          -    0.0100%    0.0332%       36%/yr
ZRO             0.0280%    0.0100%    0.0005%    0.0033%    0.0275%       30%/yr
VVV             0.0368%    0.0357%    0.0100%    0.0100%    0.0268%       29%/yr
CTR             0.0096%          -   -0.0167%    0.0100%    0.0267%       29%/yr  SIGN SPLIT
AERO            0.0096%    0.0100%    0.0100%   -0.0158%    0.0258%       28%/yr  SIGN SPLIT
POL             0.0096%    0.0071%    0.0002%   -0.0148%    0.0244%       27%/yr  SIGN SPLIT

37 symbols where one venue pays longs while another pays shorts:
  1000TOSHI, BERA, SKHYNIX, FF, S, CTR, AERO, POL, ZEC, TIA, WLD, ONDO, TRX, BNB, PUMP, PENDLE, WLFI, AAVE, DASH, EIGEN, SOL, SKY, UNI, XMR, LINK, MEGA, HYPE, SEI, JUP, 1000FLOKI, ADA, XLM, SUI, PLTR, WTI, QNT, AAPL
```

## Builder-deployed markets
```
hl:xyz        137 mkts  OI $ 3,881,781,550  24h $ 3,536,968,638
             XYZ100, TSLA, NVDA, GOLD, HOOD, INTC, PLTR, COIN, META, AAPL, MSFT, ORCL, GOOGL, AMZN, AMD, MU, SNDK, MSTR
hl:io          14 mkts  OI $    80,591,474  24h $   115,718,767
             OAI, ANTH, SNDK, IONQ, NBIS, EWY, GPRO, SBE, TCNT, DRAM, PRL, XIAOMI, H100, MOONSHOT
hl:para        39 mkts  OI $    16,209,021  24h $     4,894,696
             TOTAL2, OTHERS, BTCD, H100, AVGO, COHR, GLW, CRDO, LRCX, NET, STX, IREN, VST, TER, AAOI, 10Y, CIEN, NAVER
hl:mkts        24 mkts  OI $     9,202,100  24h $     5,146,336
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

total 311 builder markets across 10 dexs
```

## Offchain reference rates (FRED)
```
OFFCHAIN REFERENCE RATES (FRED)

  SOFR    unavailable: JSONDecodeError: Expecting value: line 1 column 1 (char 0)
  DFF     unavailable: JSONDecodeError: Expecting value: line 1 column 1 (char 0)
  IORB    unavailable: JSONDecodeError: Expecting value: line 1 column 1 (char 0)
  DGS3MO  unavailable: JSONDecodeError: Expecting value: line 1 column 1 (char 0)
  DGS10   unavailable: JSONDecodeError: Expecting value: line 1 column 1 (char 0)
```

## Carry: funding vs borrow
```
PERP FUNDING (annualized from 8h feed) vs ONCHAIN BORROW

asset        lighter  hyperliq   binance     bybit  aave brw  aave sup
----------------------------------------------------------------------
BTC             0.9%      8.9%      5.5%     10.9%     0.00%     0.00%
ETH            10.5%     10.9%      9.4%      9.6%     0.00%     0.00%
SOL            10.5%     10.9%      5.3%     -3.3%         -         -
ENA            10.5%     32.0%     10.9%     10.9%         -         -
HYPE           -7.0%     -5.8%      0.6%      5.2%         -         -
LINK           10.5%     10.9%     -1.5%     -2.0%     0.00%     0.00%
AVAX           10.5%     10.9%      3.2%     10.9%         -         -
DOGE           10.5%     10.9%      5.2%      2.5%         -         -

STABLE BORROW COST (the cost of carrying a hedged position)
  aave   USDe     borrow  0.00%  supply  0.00%
  aave   RLUSD    borrow  0.50%  supply  0.00%
  aave   RLUSD    borrow  3.32%  supply  1.72%
  aave   GHO      borrow  4.08%  supply  3.30%
  aave   USDC     borrow  4.15%  supply  3.09%
  aave   USDC     borrow  4.51%  supply  3.37%
  aave   GHO      borrow  4.53%  supply  3.60%
  aave   USDC     borrow  4.78%  supply  3.68%
  morpho    cbBTC/USDC    borrow  5.01%  lltv 0.86  $343,424,555
  morpho     kBTC/RLUSD   borrow  3.50%  lltv 0.86  $264,523,826
  morpho    PRIME/PYUSD   borrow  5.07%  lltv 0.86  $205,851,418
  morpho   wstETH/USDT    borrow  2.93%  lltv 0.86  $153,307,469
  morpho PT-reUSD-10DEC2026/USDC    borrow  8.47%  lltv 0.92  $134,011,981
  morpho     WBTC/USDC    borrow  5.05%  lltv 0.86  $130,047,202

BUILDER-DEPLOYED PERPS: 311 markets, 163 with volume today
  xyz:SP500        OI $  381,019,007  funding      3.7%/yr
  xyz:SKHX         OI $  346,254,216  funding     47.6%/yr
  xyz:XYZ100       OI $  294,064,795  funding      5.5%/yr
  xyz:GOLD         OI $  288,145,265  funding      5.9%/yr
  xyz:BRENTOIL     OI $  205,651,384  funding      5.5%/yr
  xyz:SKHY         OI $  184,458,568  funding     -1.7%/yr
  xyz:SILVER       OI $  173,371,538  funding     12.4%/yr
  xyz:CL           OI $  169,268,205  funding     -0.1%/yr
  xyz:SPCX         OI $  150,870,002  funding      5.5%/yr
  xyz:MU           OI $  148,957,362  funding      5.5%/yr
```
