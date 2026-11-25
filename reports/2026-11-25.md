# 2026-11-25

## Market list changes
```
2026-11-24.json -> 2026-11-25.json

hl:abcd: no change (1 markets)
hl:cash: no change (17 markets)
hl:flx: no change (16 markets)
hl:hyna: no change (25 markets)
hl:io: no change (26 markets)
hl:km: no change (23 markets)
hl:mkts: no change (24 markets)
hl:para: no change (40 markets)
hl:vntl: no change (15 markets)
hl:xyz: 149 -> 150
  NEW     (1): xyz:RBLX

hyperliquid: no change (235 markets)
lighter: no change (235 markets)
variational: 595 -> 597
  NEW     (2): PATH, TEM

```

## Funding dispersion
```
206 symbols quoted on 2+ venues. Top 25 by dispersion.

sym             lighter  hyperliqu    binance      bybit     spread      ann  flag
----------------------------------------------------------------------------------
PRL             0.4048%          -    0.0100%   -0.1104%    0.5152%      564%/yr  SIGN SPLIT
CXMT            0.0192%          -    0.4886%    0.4825%    0.4694%      514%/yr
ZHIPU           0.1248%          -    0.2462%    0.4106%    0.2858%      313%/yr
SAMSUNG               -    0.0831%    0.3107%    0.3000%    0.2275%      249%/yr
MINIMAX         0.2560%          -    0.2481%    0.4370%    0.1889%      207%/yr
SKHYNIX               -    0.2003%    0.3740%    0.1877%    0.1863%      204%/yr
CC             -0.0280%   -0.0271%   -0.0123%   -0.1719%    0.1596%      175%/yr
TENCENT         0.0032%          -    0.1212%    0.1018%    0.1180%      129%/yr
FOLKS           0.1200%          -    0.0100%    0.0100%    0.1100%      120%/yr
UNITREE         0.0408%          -    0.1483%    0.1409%    0.1075%      118%/yr
LIT            -0.0048%    0.0100%   -0.0157%   -0.0815%    0.0915%      100%/yr  SIGN SPLIT
CHIP            0.0096%   -0.0195%    0.0050%   -0.0746%    0.0842%       92%/yr  SIGN SPLIT
1000BONK        0.0096%    0.0100%   -0.0136%   -0.0646%    0.0746%       82%/yr  SIGN SPLIT
MET             0.0024%   -0.0643%   -0.0064%    0.0100%    0.0743%       81%/yr  SIGN SPLIT
HYUNDAI               -    0.0522%    0.0497%    0.1230%    0.0733%       80%/yr
ARC             0.0392%          -    0.0114%    0.0837%    0.0723%       79%/yr
XPD             0.0256%    0.0780%    0.0089%          -    0.0691%       76%/yr
STABLE          0.0752%    0.0100%    0.0286%    0.0100%    0.0652%       71%/yr
SKY            -0.0496%    0.0100%   -0.0021%    0.0061%    0.0596%       65%/yr  SIGN SPLIT
BERA            0.0000%   -0.0440%   -0.0066%    0.0100%    0.0540%       59%/yr  SIGN SPLIT
1000SHIB        0.0096%   -0.0402%    0.0031%    0.0068%    0.0498%       55%/yr  SIGN SPLIT
ZRO             0.0584%    0.0243%    0.0100%    0.0100%    0.0484%       53%/yr
EIGEN           0.0096%    0.0100%    0.0067%   -0.0384%    0.0484%       53%/yr  SIGN SPLIT
XMR             0.0512%    0.0544%    0.0100%    0.0100%    0.0444%       49%/yr
1000PEPE        0.0096%    0.0024%   -0.0344%    0.0100%    0.0444%       49%/yr  SIGN SPLIT

51 symbols where one venue pays longs while another pays shorts:
  PRL, LIT, CHIP, 1000BONK, MET, SKY, BERA, 1000SHIB, EIGEN, 1000PEPE, WLD, DRV, ZK, PUMP, ONDO, ETHFI, GRAM, SEI, ENA, TRUMP, SPCX, 1000FLOKI, 0G, APT, VIRTUAL, SUI, TIA, DYDX, FF, ARB, OP, MORPHO, SYRUP, QNT, HBAR, AVAX, BCH, HYPE, LTC, TAO
```

## Builder-deployed markets
```
hl:xyz        150 mkts  OI $ 4,029,270,358  24h $ 5,757,246,650
             XYZ100, TSLA, NVDA, GOLD, HOOD, INTC, PLTR, COIN, META, AAPL, MSFT, ORCL, GOOGL, AMZN, AMD, MU, SNDK, MSTR
hl:io          26 mkts  OI $    97,755,581  24h $    95,308,095
             OAI, ANTH, SNDK, IONQ, NBIS, EWY, GPRO, SBE, TCNT, DRAM, PRL, XIAOMI, H100, MOONSHOT, NVDA, SKHX, AAPL, CRCL
hl:para        40 mkts  OI $    11,493,039  24h $     4,212,665
             TOTAL2, OTHERS, BTCD, H100, AVGO, COHR, GLW, CRDO, LRCX, NET, STX, IREN, VST, TER, AAOI, 10Y, CIEN, NAVER
hl:mkts        24 mkts  OI $       198,982  24h $       129,398
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

total 337 builder markets across 10 dexs
```

## Offchain reference rates (FRED)
```
OFFCHAIN REFERENCE RATES (FRED)

  SOFR      3.94%  2026-11-24     +2bp   Secured Overnight Financing Rate (what a desk funds at)
  DFF       3.88%  2026-11-23     +0bp   Effective fed funds
  IORB      3.90%  2026-11-25     +0bp   Interest on reserve balances
  DGS3MO    4.37%  2026-11-23     +5bp   3-month Treasury
  DGS10     4.92%  2026-11-23     +0bp   10-year Treasury
```

## Carry: funding vs borrow
```
PERP FUNDING (annualized from 8h feed) vs ONCHAIN BORROW

asset        lighter  hyperliq   binance     bybit  aave brw  aave sup
----------------------------------------------------------------------
BTC            10.5%     10.9%     10.9%      8.9%     0.00%     0.00%
ETH            10.5%     10.9%      7.7%     10.9%     0.00%     0.00%
SOL            -0.9%     10.9%     -0.1%     10.9%         -         -
ENA            10.5%     10.9%      1.4%    -16.1%         -         -
HYPE            1.8%     10.9%     10.9%     -3.6%         -         -
LINK            0.9%     10.9%      3.8%      3.5%     0.00%     0.00%
AVAX           10.5%      7.4%     -5.1%     -1.9%         -         -
DOGE           10.5%     10.9%      1.8%     10.9%         -         -

STABLE BORROW COST (the cost of carrying a hedged position)
  aave   USDe     borrow  0.00%  supply  0.00%
  aave   USDC     borrow  3.90%  supply  2.73%
  aave   GHO      borrow  4.03%  supply  3.22%
  aave   RLUSD    borrow  4.18%  supply  3.58%
  aave   USDC     borrow  4.31%  supply  3.34%
  aave   GHO      borrow  4.36%  supply  3.33%
  aave   USDC     borrow  4.70%  supply  3.50%
  aave   USDC     borrow  4.79%  supply  3.35%
  morpho    cbBTC/USDC    borrow  3.50%  lltv 0.86  $264,637,142
  morpho     kBTC/RLUSD   borrow  3.30%  lltv 0.86  $160,436,762
  morpho     WBTC/USDC    borrow  3.51%  lltv 0.86  $153,020,747
  morpho PT-reUSD-10DEC2026/USDC    borrow  8.68%  lltv 0.92  $135,880,899
  morpho    PRIME/PYUSD   borrow  6.20%  lltv 0.86  $129,216,869
  morpho   wstETH/USDT    borrow  3.48%  lltv 0.86  $119,355,929

OFFCHAIN BENCHMARK: SOFR 3.94% (2026-11-24)
  BTC perp funding 10.51% vs SOFR 3.94%: spread +6.57pp over the offchain cost of money

BUILDER-DEPLOYED PERPS: 337 markets, 178 with volume today
  xyz:SP500        OI $  412,307,874  funding      5.5%/yr
  xyz:XYZ100       OI $  389,051,478  funding     10.0%/yr
  xyz:SKHX         OI $  362,005,326  funding    218.2%/yr
  xyz:NVDA         OI $  346,278,794  funding     15.9%/yr
  xyz:GOLD         OI $  266,537,769  funding     31.1%/yr
  xyz:ANT          OI $  221,860,357  funding      5.5%/yr
  xyz:MU           OI $  154,674,143  funding     14.0%/yr
  xyz:SKHY         OI $  153,239,376  funding    -14.8%/yr
  xyz:GOOGL        OI $  139,039,014  funding     20.0%/yr
  xyz:BRENTOIL     OI $  138,287,194  funding      3.8%/yr
```
