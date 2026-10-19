# 2026-10-19

## Market list changes
```
2026-10-18.json -> 2026-10-19.json

hl:abcd: no change (1 markets)
hl:cash: no change (17 markets)
hl:flx: no change (16 markets)
hl:hyna: no change (25 markets)
hl:io: 13 -> 14
  NEW     (1): io:MOONSHOT

hl:km: no change (23 markets)
hl:mkts: no change (24 markets)
hl:para: no change (39 markets)
hl:vntl: no change (15 markets)
hl:xyz: no change (136 markets)
hyperliquid: no change (234 markets)
lighter: no change (235 markets)
variational: 575 -> 576
  NEW     (1): MDB

```

## Funding dispersion
```
206 symbols quoted on 2+ venues. Top 25 by dispersion.

sym             lighter  hyperliqu    binance      bybit     spread      ann  flag
----------------------------------------------------------------------------------
SKHYNIX               -   -0.1919%   -0.0394%   -0.2152%    0.1759%      193%/yr
PRL            -0.1600%          -    0.0100%    0.0100%    0.1700%      186%/yr  SIGN SPLIT
DRV             0.0096%          -          -   -0.1431%    0.1527%      167%/yr  SIGN SPLIT
SAMSUNG               -   -0.1589%   -0.0346%   -0.1446%    0.1242%      136%/yr
MET             0.0096%   -0.0213%   -0.0319%   -0.0872%    0.0968%      106%/yr  SIGN SPLIT
HYUNDAI               -   -0.0917%    0.0000%    0.0000%    0.0917%      100%/yr
SKR             0.0008%    0.0100%    0.0100%   -0.0721%    0.0821%       90%/yr  SIGN SPLIT
1000BONK        0.0096%   -0.0063%   -0.0321%   -0.0675%    0.0771%       84%/yr  SIGN SPLIT
MON             0.0096%    0.0028%   -0.0613%   -0.0368%    0.0709%       78%/yr  SIGN SPLIT
BERA            0.0096%    0.0011%   -0.0438%   -0.0564%    0.0660%       72%/yr  SIGN SPLIT
TRUMP           0.0096%   -0.0056%    0.0100%   -0.0524%    0.0624%       68%/yr  SIGN SPLIT
ZHIPU           0.0032%          -    0.0631%    0.0015%    0.0616%       67%/yr
WTI            -0.0064%   -0.0053%   -0.0202%   -0.0666%    0.0613%       67%/yr
CAP             0.0096%          -    0.0100%   -0.0504%    0.0604%       66%/yr  SIGN SPLIT
CTR             0.0096%          -    0.0615%    0.0100%    0.0519%       57%/yr
JUP            -0.0200%   -0.0500%    0.0016%   -0.0056%    0.0515%       56%/yr  SIGN SPLIT
COIN            0.0152%    0.0145%    0.0000%    0.0474%    0.0474%       52%/yr
VVV             0.0040%    0.0100%    0.0100%   -0.0344%    0.0444%       49%/yr  SIGN SPLIT
EDGE            0.0096%          -    0.0100%   -0.0341%    0.0441%       48%/yr  SIGN SPLIT
EDEN                  -          -   -0.0339%    0.0100%    0.0439%       48%/yr  SIGN SPLIT
UNITREE         0.0032%          -    0.0000%    0.0423%    0.0423%       46%/yr
DIA                   -          -   -0.0297%    0.0100%    0.0397%       43%/yr  SIGN SPLIT
LDO             0.0096%   -0.0261%    0.0100%    0.0082%    0.0361%       39%/yr  SIGN SPLIT
ICP             0.0096%   -0.0252%   -0.0046%   -0.0053%    0.0348%       38%/yr  SIGN SPLIT
ASML            0.0032%          -    0.0000%    0.0320%    0.0320%       35%/yr

57 symbols where one venue pays longs while another pays shorts:
  PRL, DRV, MET, SKR, 1000BONK, MON, BERA, TRUMP, CAP, JUP, VVV, EDGE, EDEN, DIA, LDO, ICP, TENCENT, STABLE, WLFI, CXMT, HBAR, LIT, FF, TIA, DOT, 1000SHIB, MEGA, AVAX, CHIP, PLTR, PYTH, POL, TRX, PAXG, PENGU, S, EIGEN, BYD, APT, FIL
```

## Builder-deployed markets
```
hl:xyz        136 mkts  OI $ 3,792,643,103  24h $ 3,692,613,241
             XYZ100, TSLA, NVDA, GOLD, HOOD, INTC, PLTR, COIN, META, AAPL, MSFT, ORCL, GOOGL, AMZN, AMD, MU, SNDK, MSTR
hl:io          14 mkts  OI $    79,492,564  24h $    59,570,978
             OAI, ANTH, SNDK, IONQ, NBIS, EWY, GPRO, SBE, TCNT, DRAM, PRL, XIAOMI, H100, MOONSHOT
hl:para        39 mkts  OI $    21,167,004  24h $    12,475,576
             TOTAL2, OTHERS, BTCD, H100, AVGO, COHR, GLW, CRDO, LRCX, NET, STX, IREN, VST, TER, AAOI, 10Y, CIEN, NAVER
hl:mkts        24 mkts  OI $    10,747,514  24h $     4,955,851
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

total 310 builder markets across 10 dexs
```

## Offchain reference rates (FRED)
```
OFFCHAIN REFERENCE RATES (FRED)

  SOFR      3.88%  2026-10-16     -1bp   Secured Overnight Financing Rate (what a desk funds at)
  DFF       3.88%  2026-10-15     +0bp   Effective fed funds
  IORB      3.90%  2026-10-19     +0bp   Interest on reserve balances
  DGS3MO    4.28%  2026-10-15     +0bp   3-month Treasury
  DGS10     5.10%  2026-10-15     -9bp   10-year Treasury
```

## Carry: funding vs borrow
```
PERP FUNDING (annualized from 8h feed) vs ONCHAIN BORROW

asset        lighter  hyperliq   binance     bybit  aave brw  aave sup
----------------------------------------------------------------------
BTC            10.5%     10.9%     10.5%      6.4%     0.00%     0.00%
ETH            10.5%     10.1%      7.1%      9.7%     0.00%     0.00%
SOL            10.5%      1.8%      4.7%     -5.2%         -         -
ENA            10.5%     10.9%      6.8%     10.9%         -         -
HYPE           10.5%      2.1%     10.9%     -0.4%         -         -
LINK           10.5%     10.9%      7.4%     10.9%     0.00%     0.00%
AVAX           10.5%    -10.9%     -0.2%      5.6%         -         -
DOGE           10.5%      8.3%      1.9%      7.3%         -         -

STABLE BORROW COST (the cost of carrying a hedged position)
  aave   RLUSD    borrow  2.55%  supply  1.02%
  aave   GHO      borrow  4.08%  supply  3.30%
  aave   USDC     borrow  4.18%  supply  3.14%
  aave   GHO      borrow  4.53%  supply  3.60%
  aave   USDC     borrow  4.54%  supply  3.41%
  aave   USDC     borrow  4.60%  supply  3.41%
  aave   GHO      borrow  5.37%  supply  4.36%
  aave   USDC     borrow  6.62%  supply  5.49%
  morpho    cbBTC/USDC    borrow  5.02%  lltv 0.86  $344,204,615
  morpho     kBTC/RLUSD   borrow  3.50%  lltv 0.86  $242,241,988
  morpho    PRIME/PYUSD   borrow  5.56%  lltv 0.86  $205,677,594
  morpho   wstETH/USDT    borrow  2.94%  lltv 0.86  $150,142,183
  morpho     kBTC/PYUSD   borrow  4.00%  lltv 0.86  $141,155,286
  morpho PT-reUSD-10DEC2026/USDC    borrow  8.15%  lltv 0.92  $137,235,737

OFFCHAIN BENCHMARK: SOFR 3.88% (2026-10-16)
  BTC perp funding 10.51% vs SOFR 3.88%: spread +6.63pp over the offchain cost of money

BUILDER-DEPLOYED PERPS: 310 markets, 163 with volume today
  xyz:SP500        OI $  378,353,839  funding     -6.2%/yr
  xyz:SKHX         OI $  347,630,948  funding   -209.0%/yr
  xyz:XYZ100       OI $  300,246,833  funding      5.5%/yr
  xyz:GOLD         OI $  269,328,552  funding      5.5%/yr
  xyz:SKHY         OI $  187,243,566  funding     -1.6%/yr
  xyz:BRENTOIL     OI $  182,349,256  funding     -1.6%/yr
  xyz:GOOGL        OI $  180,206,139  funding      7.5%/yr
  xyz:SILVER       OI $  162,808,019  funding      5.5%/yr
  xyz:MU           OI $  151,963,601  funding      5.5%/yr
  xyz:CL           OI $  137,660,328  funding     -5.9%/yr
```
