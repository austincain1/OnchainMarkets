# 2026-10-22

## Market list changes
```
2026-10-21.json -> 2026-10-22.json

hl:abcd: no change (1 markets)
hl:cash: no change (17 markets)
hl:flx: no change (16 markets)
hl:hyna: no change (25 markets)
hl:io: no change (14 markets)
hl:km: no change (23 markets)
hl:mkts: no change (24 markets)
hl:para: no change (39 markets)
hl:vntl: no change (15 markets)
hl:xyz: 137 -> 138
  NEW     (1): xyz:MUU

hyperliquid: no change (234 markets)
lighter: no change (235 markets)
variational: 578 -> 580
  NEW     (2): CVNA, ZCSH

```

## Funding dispersion
```
205 symbols quoted on 2+ venues. Top 25 by dispersion.

sym             lighter  hyperliqu    binance      bybit     spread      ann  flag
----------------------------------------------------------------------------------
AI              0.4368%    0.0000%    0.0000%          -    0.4368%      478%/yr
ZHIPU          -0.4400%          -   -0.3931%   -0.1833%    0.2567%      281%/yr
SAMSUNG               -   -0.2483%   -0.1366%   -0.0605%    0.1878%      206%/yr
SKHYNIX               -   -0.2381%   -0.1289%   -0.0517%    0.1864%      204%/yr
BOT             0.0032%          -   -0.1655%   -0.1241%    0.1687%      185%/yr  SIGN SPLIT
HYUNDAI               -   -0.1337%    0.0000%    0.0000%    0.1337%      146%/yr
CXMT           -0.0672%          -   -0.1688%   -0.0426%    0.1262%      138%/yr
MINIMAX        -0.0856%          -   -0.0902%    0.0000%    0.0902%       99%/yr
CHIP            0.0096%    0.0100%    0.0012%   -0.0529%    0.0629%       69%/yr  SIGN SPLIT
MET             0.0096%   -0.0532%   -0.0231%   -0.0173%    0.0628%       69%/yr  SIGN SPLIT
XMR             0.0160%    0.0765%    0.0455%    0.0473%    0.0605%       66%/yr
TRUMP           0.0096%   -0.0507%   -0.0028%   -0.0305%    0.0603%       66%/yr  SIGN SPLIT
FOLKS           0.0096%          -    0.0100%    0.0653%    0.0557%       61%/yr
AAOI            0.0032%          -    0.0359%    0.0534%    0.0502%       55%/yr
XAU             0.0120%    0.0050%    0.0321%    0.0511%    0.0461%       51%/yr
PRL             0.0528%          -    0.0100%    0.0100%    0.0428%       47%/yr
PYTH           -0.0016%    0.0100%    0.0070%   -0.0289%    0.0389%       43%/yr  SIGN SPLIT
FIL             0.0096%   -0.0038%   -0.0293%   -0.0253%    0.0389%       43%/yr  SIGN SPLIT
DOT             0.0096%   -0.0293%   -0.0094%    0.0035%    0.0389%       43%/yr  SIGN SPLIT
BIRB                  -          -   -0.0272%    0.0100%    0.0372%       41%/yr  SIGN SPLIT
XAG             0.0336%    0.0157%    0.0352%    0.0496%    0.0340%       37%/yr
JUP            -0.0232%    0.0052%    0.0077%    0.0100%    0.0332%       36%/yr  SIGN SPLIT
POL             0.0096%    0.0003%   -0.0233%    0.0035%    0.0329%       36%/yr  SIGN SPLIT
TTWO            0.0328%          -    0.0000%    0.0000%    0.0328%       36%/yr
XPD             0.0112%    0.0050%    0.0377%          -    0.0327%       36%/yr

67 symbols where one venue pays longs while another pays shorts:
  BOT, CHIP, MET, TRUMP, PYTH, FIL, DOT, BIRB, JUP, POL, GMX, AAPL, WLFI, SEI, 1000SHIB, NMR, ZK, MORPHO, OP, PAXG, ASTER, 1000FLOKI, ONDO, 2Z, JTO, SPX, GRAM, EIGEN, XLM, BNB, TAO, CASHCAT, ICP, PROVE, 1000PEPE, AAVE, S, 1000BONK, BIO, NEAR
```

## Builder-deployed markets
```
hl:xyz        138 mkts  OI $ 3,910,289,995  24h $ 3,611,445,068
             XYZ100, TSLA, NVDA, GOLD, HOOD, INTC, PLTR, COIN, META, AAPL, MSFT, ORCL, GOOGL, AMZN, AMD, MU, SNDK, MSTR
hl:io          14 mkts  OI $    76,043,369  24h $    55,867,759
             OAI, ANTH, SNDK, IONQ, NBIS, EWY, GPRO, SBE, TCNT, DRAM, PRL, XIAOMI, H100, MOONSHOT
hl:para        39 mkts  OI $    16,101,768  24h $     5,064,108
             TOTAL2, OTHERS, BTCD, H100, AVGO, COHR, GLW, CRDO, LRCX, NET, STX, IREN, VST, TER, AAOI, 10Y, CIEN, NAVER
hl:mkts        24 mkts  OI $     9,466,320  24h $     2,074,805
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

total 312 builder markets across 10 dexs
```

## Offchain reference rates (FRED)
```
OFFCHAIN REFERENCE RATES (FRED)

  SOFR      3.88%  2026-10-21     +0bp   Secured Overnight Financing Rate (what a desk funds at)
  DFF       3.88%  2026-10-20     +0bp   Effective fed funds
  IORB      3.90%  2026-10-22     +0bp   Interest on reserve balances
  DGS3MO    4.26%  2026-10-20     -1bp   3-month Treasury
  DGS10     5.12%  2026-10-20     -3bp   10-year Treasury
```

## Carry: funding vs borrow
```
PERP FUNDING (annualized from 8h feed) vs ONCHAIN BORROW

asset        lighter  hyperliq   binance     bybit  aave brw  aave sup
----------------------------------------------------------------------
BTC            10.5%     10.9%      1.0%      2.6%     0.00%     0.00%
ETH            10.5%     10.9%      5.4%      1.9%     0.00%     0.00%
SOL            10.5%     10.9%      3.8%     10.9%         -         -
ENA             7.0%     10.9%     -1.1%      6.1%         -         -
HYPE           10.5%     10.9%      7.6%      4.7%         -         -
LINK           10.5%     10.9%      2.6%      2.2%     0.00%     0.00%
AVAX          -11.4%    -14.5%    -14.0%     -5.5%         -         -
DOGE           10.5%     10.9%     -4.2%     -1.6%         -         -

STABLE BORROW COST (the cost of carrying a hedged position)
  aave   USDe     borrow  0.00%  supply  0.00%
  aave   RLUSD    borrow  0.50%  supply  0.00%
  aave   RLUSD    borrow  2.73%  supply  1.17%
  aave   GHO      borrow  4.03%  supply  3.22%
  aave   GHO      borrow  4.08%  supply  3.30%
  aave   USDC     borrow  4.15%  supply  3.09%
  aave   GHO      borrow  4.53%  supply  3.60%
  aave   USDC     borrow  4.56%  supply  3.45%
  morpho    cbBTC/USDC    borrow  5.01%  lltv 0.86  $342,389,019
  morpho     kBTC/RLUSD   borrow  3.49%  lltv 0.86  $264,532,528
  morpho    PRIME/PYUSD   borrow  5.08%  lltv 0.86  $210,015,723
  morpho   wstETH/USDT    borrow  6.80%  lltv 0.86  $146,290,746
  morpho PT-reUSD-10DEC2026/USDC    borrow  8.95%  lltv 0.92  $136,521,136
  morpho     WBTC/USDC    borrow  4.96%  lltv 0.86  $130,557,989

OFFCHAIN BENCHMARK: SOFR 3.88% (2026-10-21)
  BTC perp funding 10.51% vs SOFR 3.88%: spread +6.63pp over the offchain cost of money

BUILDER-DEPLOYED PERPS: 312 markets, 163 with volume today
  xyz:SP500        OI $  396,777,958  funding     -5.4%/yr
  xyz:SKHX         OI $  342,516,417  funding   -259.8%/yr
  xyz:GOLD         OI $  332,900,942  funding      5.5%/yr
  xyz:XYZ100       OI $  293,964,512  funding     10.0%/yr
  xyz:BRENTOIL     OI $  220,772,290  funding      3.1%/yr
  xyz:SILVER       OI $  188,214,687  funding     17.2%/yr
  xyz:CL           OI $  184,396,030  funding      2.1%/yr
  xyz:SKHY         OI $  165,811,218  funding      5.5%/yr
  xyz:SPCX         OI $  147,190,338  funding     22.3%/yr
  xyz:MU           OI $  142,326,844  funding      6.8%/yr
```
