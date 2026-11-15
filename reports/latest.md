# 2026-11-15

## Market list changes
```
2026-11-14.json -> 2026-11-15.json

hl:abcd: no change (1 markets)
hl:cash: no change (17 markets)
hl:flx: no change (16 markets)
hl:hyna: no change (25 markets)
hl:io: 23 -> 24
  NEW     (1): io:AMD

hl:km: no change (23 markets)
hl:mkts: no change (24 markets)
hl:para: no change (40 markets)
hl:vntl: no change (15 markets)
hl:xyz: no change (144 markets)
hyperliquid: no change (235 markets)
lighter: no change (235 markets)
variational: no change (589 markets)
```

## Funding dispersion
```
204 symbols quoted on 2+ venues. Top 25 by dispersion.

sym             lighter  hyperliqu    binance      bybit     spread      ann  flag
----------------------------------------------------------------------------------
SOXL           -0.0080%          -    0.0641%    0.2909%    0.2989%      327%/yr  SIGN SPLIT
SOXS                  -          -   -0.0549%   -0.1903%    0.1354%      148%/yr
KORU           -0.0784%          -    0.0384%    0.0000%    0.1168%      128%/yr  SIGN SPLIT
NVDA            0.0032%    0.0050%    0.0000%    0.0994%    0.0994%      109%/yr
DRV             0.0096%          -          -   -0.0859%    0.0955%      105%/yr  SIGN SPLIT
MSTR            0.0344%    0.0560%   -0.0307%    0.0006%    0.0867%       95%/yr  SIGN SPLIT
ZORA           -0.0808%   -0.0831%   -0.0566%    0.0030%    0.0861%       94%/yr  SIGN SPLIT
XPL             0.0096%   -0.0756%    0.0076%   -0.0294%    0.0852%       93%/yr  SIGN SPLIT
IREN            0.0032%          -    0.0000%    0.0814%    0.0814%       89%/yr
NBIS            0.0032%          -    0.0000%    0.0795%    0.0795%       87%/yr
ROBO           -0.0664%          -    0.0100%    0.0100%    0.0764%       84%/yr  SIGN SPLIT
MRVL            0.0032%          -    0.0000%    0.0725%    0.0725%       79%/yr
POPCAT          0.0096%   -0.0223%   -0.0554%    0.0100%    0.0654%       72%/yr  SIGN SPLIT
SKR             0.0096%    0.0100%    0.0089%   -0.0552%    0.0652%       71%/yr  SIGN SPLIT
BERA           -0.0520%   -0.0879%   -0.1008%   -0.0376%    0.0632%       69%/yr
1000BONK        0.0096%   -0.0533%   -0.0342%   -0.0291%    0.0629%       69%/yr  SIGN SPLIT
AERO           -0.0328%    0.0100%   -0.0009%   -0.0528%    0.0628%       69%/yr  SIGN SPLIT
BMNR            0.0032%          -   -0.0116%    0.0503%    0.0619%       68%/yr  SIGN SPLIT
FF              0.0096%          -    0.0100%   -0.0451%    0.0551%       60%/yr  SIGN SPLIT
AXS             0.0096%    0.0100%    0.0024%   -0.0443%    0.0543%       59%/yr  SIGN SPLIT
1000FLOKI      -0.0120%    0.0100%   -0.0432%   -0.0088%    0.0532%       58%/yr  SIGN SPLIT
MINIMAX         0.0032%          -    0.0000%    0.0523%    0.0523%       57%/yr
KAITO          -0.0120%   -0.0544%   -0.0022%   -0.0410%    0.0523%       57%/yr
AZTEC          -0.0416%    0.0100%   -0.0275%    0.0100%    0.0516%       57%/yr  SIGN SPLIT
TIA            -0.0072%   -0.0413%   -0.0140%    0.0100%    0.0513%       56%/yr  SIGN SPLIT

77 symbols where one venue pays longs while another pays shorts:
  SOXL, KORU, DRV, MSTR, ZORA, XPL, ROBO, POPCAT, SKR, 1000BONK, AERO, BMNR, FF, AXS, 1000FLOKI, AZTEC, TIA, VVV, PYTH, PENDLE, MET, ICP, 1000PEPE, JUP, 1000SHIB, AVNT, PONS, CHIP, LINEA, OP, ETHFI, BB, WIF, PENGU, DIA, ARB, MNT, XLM, AVAX, POL
```

## Builder-deployed markets
```
hl:xyz        144 mkts  OI $ 4,194,638,205  24h $ 1,044,285,752
             XYZ100, TSLA, NVDA, GOLD, HOOD, INTC, PLTR, COIN, META, AAPL, MSFT, ORCL, GOOGL, AMZN, AMD, MU, SNDK, MSTR
hl:io          24 mkts  OI $   231,762,039  24h $    21,854,551
             OAI, ANTH, SNDK, IONQ, NBIS, EWY, GPRO, SBE, TCNT, DRAM, PRL, XIAOMI, H100, MOONSHOT, NVDA, SKHX, AAPL, CRCL
hl:para        40 mkts  OI $    15,316,444  24h $     5,015,028
             TOTAL2, OTHERS, BTCD, H100, AVGO, COHR, GLW, CRDO, LRCX, NET, STX, IREN, VST, TER, AAOI, 10Y, CIEN, NAVER
hl:mkts        24 mkts  OI $       172,848  24h $       417,472
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

total 329 builder markets across 10 dexs
```

## Offchain reference rates (FRED)
```
OFFCHAIN REFERENCE RATES (FRED)

  SOFR      3.90%  2026-11-12     +1bp   Secured Overnight Financing Rate (what a desk funds at)
  DFF       3.88%  2026-11-12     +0bp   Effective fed funds
  IORB      3.90%  2026-11-16     +0bp   Interest on reserve balances
  DGS3MO    4.32%  2026-11-12     +2bp   3-month Treasury
  DGS10     5.10%  2026-11-12    +12bp   10-year Treasury
```

## Carry: funding vs borrow
```
PERP FUNDING (annualized from 8h feed) vs ONCHAIN BORROW

asset        lighter  hyperliq   binance     bybit  aave brw  aave sup
----------------------------------------------------------------------
BTC            10.5%      0.5%     -1.7%     -4.1%     0.00%     0.00%
ETH            10.5%     -0.6%     -5.5%     -3.3%     0.00%     0.00%
SOL            -8.8%    -13.1%     -7.6%    -11.9%         -         -
ENA            10.5%      5.0%      0.7%     -4.3%         -         -
HYPE           10.5%      6.6%     10.9%      8.2%         -         -
LINK           -8.8%     -4.6%     -0.4%    -10.5%     0.00%     0.00%
AVAX           10.5%    -15.4%    -12.1%    -19.4%         -         -
DOGE            2.6%    -12.5%     -4.9%     -1.7%         -         -

STABLE BORROW COST (the cost of carrying a hedged position)
  aave   USDe     borrow  0.00%  supply  0.00%
  aave   RLUSD    borrow  3.61%  supply  2.03%
  aave   GHO      borrow  3.73%  supply  2.76%
  aave   RLUSD    borrow  3.75%  supply  2.54%
  aave   USDC     borrow  3.89%  supply  2.72%
  aave   GHO      borrow  4.03%  supply  3.22%
  aave   USDC     borrow  4.43%  supply  3.53%
  aave   USDC     borrow  4.51%  supply  3.30%
  morpho    cbBTC/USDC    borrow  5.13%  lltv 0.86  $335,076,598
  morpho    PRIME/PYUSD   borrow 15.79%  lltv 0.86  $174,510,419
  morpho     kBTC/RLUSD   borrow  3.30%  lltv 0.86  $173,200,537
  morpho PT-reUSD-10DEC2026/USDC    borrow 11.68%  lltv 0.92  $139,538,122
  morpho     WBTC/USDC    borrow  5.13%  lltv 0.86  $122,816,575
  morpho   wstETH/USDT    borrow  3.63%  lltv 0.86  $115,709,326

OFFCHAIN BENCHMARK: SOFR 3.90% (2026-11-12)
  BTC perp funding 10.51% vs SOFR 3.90%: spread +6.61pp over the offchain cost of money

BUILDER-DEPLOYED PERPS: 329 markets, 171 with volume today
  xyz:SP500        OI $  495,794,909  funding     -2.5%/yr
  xyz:NVDA         OI $  373,779,237  funding      5.5%/yr
  xyz:XYZ100       OI $  314,200,466  funding      5.5%/yr
  xyz:BRENTOIL     OI $  296,282,932  funding    -12.6%/yr
  xyz:GOLD         OI $  288,959,263  funding      5.5%/yr
  xyz:SKHX         OI $  270,746,886  funding      3.9%/yr
  io:ANTH          OI $  201,179,042  funding      1.4%/yr
  xyz:GOOGL        OI $  152,362,694  funding      5.5%/yr
  xyz:SILVER       OI $  150,071,775  funding      5.5%/yr
  xyz:MU           OI $  150,003,658  funding      5.5%/yr
```
