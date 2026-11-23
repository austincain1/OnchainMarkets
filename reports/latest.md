# 2026-11-23

## Market list changes
```
2026-11-22.json -> 2026-11-23.json

hl:abcd: no change (1 markets)
hl:cash: no change (17 markets)
hl:flx: no change (16 markets)
hl:hyna: no change (25 markets)
hl:io: no change (26 markets)
hl:km: no change (23 markets)
hl:mkts: no change (24 markets)
hl:para: no change (40 markets)
hl:vntl: no change (15 markets)
hl:xyz: 147 -> 148
  NEW     (1): xyz:SOXS

hyperliquid: no change (235 markets)
lighter: no change (235 markets)
variational: 595 -> 594
  REMOVED (1): TAC

```

## Funding dispersion
```
206 symbols quoted on 2+ venues. Top 25 by dispersion.

sym             lighter  hyperliqu    binance      bybit     spread      ann  flag
----------------------------------------------------------------------------------
BOT             0.4152%          -    0.1721%    0.1367%    0.2785%      305%/yr
SAMSUNG               -    0.2124%    0.0748%    0.0045%    0.2079%      228%/yr
MNT            -0.0072%   -0.1811%          -   -0.0004%    0.1807%      198%/yr
ROBO           -0.1648%          -   -0.0416%    0.0100%    0.1748%      191%/yr  SIGN SPLIT
BB              0.0032%          -   -0.1112%    0.0100%    0.1212%      133%/yr  SIGN SPLIT
STRC           -0.1048%          -    0.0000%          -    0.1048%      115%/yr
SKHYNIX               -    0.1766%    0.0760%    0.0930%    0.1006%      110%/yr
DRV             0.0096%          -          -   -0.0822%    0.0918%      100%/yr  SIGN SPLIT
BERA            0.0096%   -0.0076%   -0.0794%    0.0100%    0.0894%       98%/yr  SIGN SPLIT
CAP            -0.0096%          -    0.0751%    0.0100%    0.0847%       93%/yr  SIGN SPLIT
HYUNDAI               -    0.0791%    0.0000%    0.0000%    0.0791%       87%/yr
CC              0.0096%   -0.0475%   -0.0660%   -0.0542%    0.0756%       83%/yr  SIGN SPLIT
KAITO           0.0096%    0.0100%   -0.0645%   -0.0452%    0.0745%       82%/yr  SIGN SPLIT
XMR             0.0832%    0.0739%    0.0100%    0.0100%    0.0732%       80%/yr
1000PEPE        0.0096%   -0.0365%   -0.0606%   -0.0116%    0.0702%       77%/yr  SIGN SPLIT
WLFI           -0.0584%   -0.0141%    0.0100%   -0.0349%    0.0684%       75%/yr  SIGN SPLIT
SHEIN           0.0600%          -          -    0.0000%    0.0600%       66%/yr
MORPHO          0.0096%   -0.0301%    0.0100%   -0.0492%    0.0592%       65%/yr  SIGN SPLIT
TRUMP          -0.0336%   -0.0592%   -0.0434%   -0.0007%    0.0585%       64%/yr
MET             0.0096%   -0.0488%   -0.0440%   -0.0470%    0.0584%       64%/yr  SIGN SPLIT
LINEA           0.0096%    0.0100%   -0.0037%   -0.0466%    0.0566%       62%/yr  SIGN SPLIT
ZHIPU           0.0400%          -   -0.0144%    0.0000%    0.0544%       60%/yr  SIGN SPLIT
QCOM            0.0032%          -    0.0498%    0.0000%    0.0498%       55%/yr
ZORA           -0.0344%    0.0100%   -0.0395%    0.0100%    0.0495%       54%/yr  SIGN SPLIT
CXMT           -0.0408%          -   -0.0902%   -0.0707%    0.0494%       54%/yr

64 symbols where one venue pays longs while another pays shorts:
  ROBO, BB, DRV, BERA, CAP, CC, KAITO, 1000PEPE, WLFI, MORPHO, MET, LINEA, ZHIPU, ZORA, ARB, SKR, SEI, 2Z, 1000TOSHI, BIRB, BCH, VIRTUAL, MON, PONS, POL, 1000SHIB, 1000BONK, ICP, AERO, LIT, FIL, BIO, ENA, XLM, USELESS, DASH, S, LTC, ZK, XCU
```

## Builder-deployed markets
```
hl:xyz        148 mkts  OI $ 3,930,051,487  24h $ 8,104,595,986
             XYZ100, TSLA, NVDA, GOLD, HOOD, INTC, PLTR, COIN, META, AAPL, MSFT, ORCL, GOOGL, AMZN, AMD, MU, SNDK, MSTR
hl:io          26 mkts  OI $   104,733,585  24h $   171,494,039
             OAI, ANTH, SNDK, IONQ, NBIS, EWY, GPRO, SBE, TCNT, DRAM, PRL, XIAOMI, H100, MOONSHOT, NVDA, SKHX, AAPL, CRCL
hl:para        40 mkts  OI $    11,830,584  24h $    15,606,530
             TOTAL2, OTHERS, BTCD, H100, AVGO, COHR, GLW, CRDO, LRCX, NET, STX, IREN, VST, TER, AAOI, 10Y, CIEN, NAVER
hl:mkts        24 mkts  OI $       169,104  24h $       210,536
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

total 335 builder markets across 10 dexs
```

## Offchain reference rates (FRED)
```
OFFCHAIN REFERENCE RATES (FRED)

  SOFR      3.92%  2026-11-20     +1bp   Secured Overnight Financing Rate (what a desk funds at)
  DFF       3.88%  2026-11-20     +0bp   Effective fed funds
  IORB      3.90%  2026-11-24     +0bp   Interest on reserve balances
  DGS3MO    4.32%  2026-11-20     -2bp   3-month Treasury
  DGS10     4.92%  2026-11-20    -12bp   10-year Treasury
```

## Carry: funding vs borrow
```
PERP FUNDING (annualized from 8h feed) vs ONCHAIN BORROW

asset        lighter  hyperliq   binance     bybit  aave brw  aave sup
----------------------------------------------------------------------
BTC            10.5%     10.9%      7.2%      4.4%     0.00%     0.00%
ETH            -3.5%     -9.4%     -6.0%     -6.3%     0.00%     0.00%
SOL           -14.9%     -8.2%     -7.8%     -9.3%         -         -
ENA            10.5%     10.9%     -5.2%    -18.9%         -         -
HYPE           10.5%     10.9%      4.0%     -6.1%         -         -
LINK           -5.3%     10.9%     -1.9%      6.5%     0.00%     0.00%
AVAX          -32.4%    -14.1%    -16.4%     -4.0%         -         -
DOGE            4.4%     -0.1%     -9.6%     -7.0%         -         -

STABLE BORROW COST (the cost of carrying a hedged position)
  aave   USDe     borrow  0.00%  supply  0.00%
  aave   RLUSD    borrow  3.78%  supply  2.23%
  aave   USDC     borrow  3.78%  supply  2.57%
  aave   GHO      borrow  4.07%  supply  3.28%
  aave   GHO      borrow  4.07%  supply  3.28%
  aave   RLUSD    borrow  4.08%  supply  3.47%
  aave   USDC     borrow  4.34%  supply  3.38%
  aave   GHO      borrow  4.35%  supply  3.32%
  morpho    cbBTC/USDC    borrow  3.77%  lltv 0.86  $262,239,526
  morpho     kBTC/RLUSD   borrow  3.50%  lltv 0.86  $161,760,891
  morpho     WBTC/USDC    borrow  3.78%  lltv 0.86  $150,546,985
  morpho PT-reUSD-10DEC2026/USDC    borrow  8.75%  lltv 0.92  $136,858,754
  morpho    PRIME/PYUSD   borrow  6.21%  lltv 0.86  $129,186,782
  morpho   wstETH/USDT    borrow  3.51%  lltv 0.86  $119,257,315

OFFCHAIN BENCHMARK: SOFR 3.92% (2026-11-20)
  BTC perp funding 10.51% vs SOFR 3.92%: spread +6.59pp over the offchain cost of money

BUILDER-DEPLOYED PERPS: 335 markets, 175 with volume today
  xyz:SP500        OI $  422,078,928  funding      5.5%/yr
  xyz:NVDA         OI $  339,313,503  funding      5.5%/yr
  xyz:SKHX         OI $  331,829,618  funding    197.0%/yr
  xyz:XYZ100       OI $  278,951,342  funding      5.5%/yr
  xyz:ANT          OI $  268,563,318  funding    -64.1%/yr
  xyz:GOLD         OI $  249,271,790  funding      5.5%/yr
  xyz:BRENTOIL     OI $  195,763,090  funding      8.0%/yr
  xyz:GOOGL        OI $  151,692,046  funding      5.5%/yr
  xyz:MU           OI $  151,449,037  funding      5.5%/yr
  xyz:SILVER       OI $  130,102,206  funding      8.7%/yr
```
