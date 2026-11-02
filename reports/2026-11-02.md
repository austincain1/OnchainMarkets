# 2026-11-02

## Market list changes
```
2026-11-01.json -> 2026-11-02.json

hl:abcd: no change (1 markets)
hl:cash: no change (17 markets)
hl:flx: no change (16 markets)
hl:hyna: no change (25 markets)
hl:io: no change (18 markets)
hl:km: no change (23 markets)
hl:mkts: no change (24 markets)
hl:para: 39 -> 40
  NEW     (1): para:HYPE2

hl:vntl: no change (15 markets)
hl:xyz: 141 -> 142
  NEW     (1): xyz:MELI

hyperliquid: no change (235 markets)
lighter: no change (235 markets)
variational: no change (581 markets)
```

## Funding dispersion
```
205 symbols quoted on 2+ venues. Top 25 by dispersion.

sym             lighter  hyperliqu    binance      bybit     spread      ann  flag
----------------------------------------------------------------------------------
PRL             1.0168%          -    0.0100%    0.0100%    1.0068%     1102%/yr
FOLKS           0.3864%          -    0.0100%    0.0100%    0.3764%      412%/yr
ZHIPU          -0.0576%          -   -0.2482%   -0.2103%    0.1906%      209%/yr
HYUNDAI               -   -0.1785%    0.0000%   -0.0720%    0.1785%      195%/yr
STONK           0.0064%          -          -    0.1482%    0.1418%      155%/yr
SKHYNIX               -   -0.0800%   -0.2053%   -0.2202%    0.1403%      154%/yr
CAP             0.1280%          -    0.0100%    0.0100%    0.1180%      129%/yr
CXMT           -0.1688%          -   -0.2690%   -0.1836%    0.1002%      110%/yr
ZK             -0.0112%    0.0100%   -0.0076%   -0.0816%    0.0916%      100%/yr  SIGN SPLIT
AAVE           -0.0816%   -0.0057%    0.0100%    0.0100%    0.0916%      100%/yr  SIGN SPLIT
CHIP           -0.0272%    0.0100%   -0.0135%   -0.0768%    0.0868%       95%/yr  SIGN SPLIT
DATA            0.0096%          -          -   -0.0735%    0.0831%       91%/yr  SIGN SPLIT
MNT            -0.0864%   -0.0933%          -   -0.0177%    0.0756%       83%/yr
MINIMAX        -0.0192%          -   -0.0747%    0.0000%    0.0747%       82%/yr
SAMSUNG               -   -0.1938%   -0.2058%   -0.2667%    0.0728%       80%/yr
STABLE          0.0096%    0.0100%    0.0100%   -0.0593%    0.0693%       76%/yr  SIGN SPLIT
BIO             0.0096%    0.0100%   -0.0190%   -0.0578%    0.0678%       74%/yr  SIGN SPLIT
ZORA           -0.0544%    0.0100%    0.0100%    0.0100%    0.0644%       71%/yr  SIGN SPLIT
MON             0.0080%    0.0100%   -0.0431%   -0.0485%    0.0585%       64%/yr  SIGN SPLIT
AVNT            0.0096%    0.0100%    0.0100%   -0.0464%    0.0564%       62%/yr  SIGN SPLIT
TIA            -0.0448%    0.0100%    0.0100%    0.0100%    0.0548%       60%/yr  SIGN SPLIT
1000BONK        0.0096%    0.0100%   -0.0024%   -0.0445%    0.0545%       60%/yr  SIGN SPLIT
BERA            0.0048%    0.0100%   -0.0282%   -0.0417%    0.0517%       57%/yr  SIGN SPLIT
AERO           -0.0408%    0.0070%    0.0100%    0.0100%    0.0508%       56%/yr  SIGN SPLIT
MET            -0.0376%    0.0100%    0.0041%    0.0007%    0.0476%       52%/yr  SIGN SPLIT

48 symbols where one venue pays longs while another pays shorts:
  ZK, AAVE, CHIP, DATA, STABLE, BIO, ZORA, MON, AVNT, TIA, 1000BONK, BERA, AERO, MET, GRAM, CC, SEI, OP, GMX, GRASS, DOT, NEAR, BNB, CRO, DOGE, FIL, 1000SHIB, SKR, FF, XRP, BCH, VVV, XPL, ARB, POL, APT, AXS, PLTR, XTEN, LTC
```

## Builder-deployed markets
```
hl:xyz        142 mkts  OI $ 4,176,876,614  24h $ 4,603,407,707
             XYZ100, TSLA, NVDA, GOLD, HOOD, INTC, PLTR, COIN, META, AAPL, MSFT, ORCL, GOOGL, AMZN, AMD, MU, SNDK, MSTR
hl:io          18 mkts  OI $   114,065,311  24h $    48,083,853
             OAI, ANTH, SNDK, IONQ, NBIS, EWY, GPRO, SBE, TCNT, DRAM, PRL, XIAOMI, H100, MOONSHOT, NVDA, SKHX, AAPL, CRCL
hl:para        40 mkts  OI $    16,155,700  24h $     5,543,147
             TOTAL2, OTHERS, BTCD, H100, AVGO, COHR, GLW, CRDO, LRCX, NET, STX, IREN, VST, TER, AAOI, 10Y, CIEN, NAVER
hl:mkts        24 mkts  OI $       110,108  24h $       134,520
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

  SOFR      3.95%  2026-10-30     +1bp   Secured Overnight Financing Rate (what a desk funds at)
  DFF       3.88%  2026-10-29     +0bp   Effective fed funds
  IORB      3.90%  2026-11-02     +0bp   Interest on reserve balances
  DGS3MO    4.18%  2026-10-29     +0bp   3-month Treasury
  DGS10     4.98%  2026-10-29     -7bp   10-year Treasury
```

## Carry: funding vs borrow
```
PERP FUNDING (annualized from 8h feed) vs ONCHAIN BORROW

asset        lighter  hyperliq   binance     bybit  aave brw  aave sup
----------------------------------------------------------------------
BTC            10.5%     10.9%     10.9%     10.9%     0.00%     0.00%
ETH            10.5%     10.9%      0.8%      8.4%     0.00%     0.00%
SOL            10.5%     10.9%     10.9%      9.8%         -         -
ENA            10.5%     10.9%     10.9%     10.9%         -         -
HYPE           10.5%     10.9%     10.9%      5.2%         -         -
LINK            1.8%      8.7%     10.9%     10.9%     0.00%     0.00%
AVAX           -0.9%     10.9%      9.4%      4.7%         -         -
DOGE          -14.9%      9.7%      4.5%    -12.2%         -         -

STABLE BORROW COST (the cost of carrying a hedged position)
  aave   USDe     borrow  0.00%  supply  0.00%
  aave   RLUSD    borrow  0.57%  supply  0.01%
  aave   RLUSD    borrow  3.24%  supply  1.64%
  aave   USDC     borrow  4.02%  supply  2.90%
  aave   GHO      borrow  4.05%  supply  3.25%
  aave   GHO      borrow  4.09%  supply  3.31%
  aave   GHO      borrow  4.53%  supply  3.60%
  aave   USDC     borrow  4.91%  supply  3.88%
  morpho    cbBTC/USDC    borrow  6.41%  lltv 0.86  $333,276,733
  morpho     kBTC/RLUSD   borrow  3.72%  lltv 0.86  $254,964,274
  morpho    PRIME/PYUSD   borrow  5.07%  lltv 0.86  $198,924,785
  morpho PT-reUSD-10DEC2026/USDC    borrow 11.49%  lltv 0.92  $137,466,021
  morpho     WBTC/USDC    borrow 10.69%  lltv 0.86  $130,879,275
  morpho   wstETH/USDT    borrow  3.66%  lltv 0.86  $127,024,913

OFFCHAIN BENCHMARK: SOFR 3.95% (2026-10-30)
  BTC perp funding 10.51% vs SOFR 3.95%: spread +6.56pp over the offchain cost of money

BUILDER-DEPLOYED PERPS: 321 markets, 167 with volume today
  xyz:SP500        OI $  375,217,084  funding      3.5%/yr
  xyz:BRENTOIL     OI $  338,431,714  funding      5.5%/yr
  xyz:GOLD         OI $  317,474,251  funding     12.3%/yr
  xyz:XYZ100       OI $  290,999,660  funding      7.9%/yr
  xyz:GOOGL        OI $  283,239,716  funding     14.4%/yr
  xyz:SKHX         OI $  260,471,976  funding    -88.0%/yr
  xyz:CL           OI $  220,440,812  funding      5.5%/yr
  xyz:SILVER       OI $  204,773,604  funding     16.8%/yr
  xyz:SPCX         OI $  167,893,354  funding     13.0%/yr
  xyz:SNDK         OI $  147,497,923  funding     25.5%/yr
```
