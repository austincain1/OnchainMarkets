# 2026-11-18

## Market list changes
```
2026-11-17.json -> 2026-11-18.json

hl:abcd: no change (1 markets)
hl:cash: no change (17 markets)
hl:flx: no change (16 markets)
hl:hyna: no change (25 markets)
hl:io: no change (24 markets)
hl:km: no change (23 markets)
hl:mkts: no change (24 markets)
hl:para: no change (40 markets)
hl:vntl: no change (15 markets)
hl:xyz: 145 -> 146
  NEW     (1): xyz:SNOW

hyperliquid: no change (235 markets)
lighter: no change (235 markets)
variational: 590 -> 592
  NEW     (2): HUT, VRT

```

## Funding dispersion
```
206 symbols quoted on 2+ venues. Top 25 by dispersion.

sym             lighter  hyperliqu    binance      bybit     spread      ann  flag
----------------------------------------------------------------------------------
TENCENT         0.0032%          -    0.2049%    0.1683%    0.2017%      221%/yr
ZORA           -0.1744%   -0.0735%   -0.0770%    0.0100%    0.1844%      202%/yr  SIGN SPLIT
SKHYNIX               -   -0.1774%    0.0000%    0.0000%    0.1774%      194%/yr
FOLKS           0.1736%          -    0.0100%    0.0100%    0.1636%      179%/yr
PRL            -0.1480%          -    0.0100%    0.0100%    0.1580%      173%/yr  SIGN SPLIT
CXMT           -0.1312%          -   -0.0373%    0.0000%    0.1312%      144%/yr
SAMSUNG               -   -0.1132%    0.0000%    0.0000%    0.1132%      124%/yr
MNT            -0.0304%   -0.0891%          -    0.0100%    0.0991%      108%/yr  SIGN SPLIT
BERA            0.0096%   -0.0034%   -0.0563%    0.0100%    0.0663%       73%/yr  SIGN SPLIT
NOW             0.0032%          -    0.0136%    0.0608%    0.0576%       63%/yr
OP              0.0096%   -0.0443%   -0.0133%    0.0026%    0.0539%       59%/yr  SIGN SPLIT
POPCAT          0.0096%   -0.0400%    0.0100%    0.0100%    0.0500%       55%/yr  SIGN SPLIT
XPT             0.0232%    0.0050%    0.0524%          -    0.0474%       52%/yr
DRV             0.0096%          -          -   -0.0376%    0.0472%       52%/yr  SIGN SPLIT
PIPPIN                -          -    0.0569%    0.0100%    0.0469%       51%/yr
HYUNDAI               -   -0.0450%    0.0000%    0.0017%    0.0467%       51%/yr  SIGN SPLIT
WLD             0.0096%    0.0100%   -0.0226%   -0.0362%    0.0462%       51%/yr  SIGN SPLIT
AAVE           -0.0336%   -0.0141%    0.0096%    0.0049%    0.0432%       47%/yr  SIGN SPLIT
XPD             0.0072%    0.0105%    0.0463%          -    0.0391%       43%/yr
BIRB                  -          -   -0.0280%    0.0100%    0.0380%       42%/yr  SIGN SPLIT
GMX             0.0096%    0.0100%    0.0100%   -0.0278%    0.0378%       41%/yr  SIGN SPLIT
NVDA            0.0080%    0.0050%    0.0234%    0.0420%    0.0370%       40%/yr
BOT             0.0360%          -    0.0000%    0.0000%    0.0360%       39%/yr
SEI             0.0096%    0.0049%   -0.0079%   -0.0249%    0.0345%       38%/yr  SIGN SPLIT
BABA            0.0368%          -    0.0025%    0.0169%    0.0343%       38%/yr

60 symbols where one venue pays longs while another pays shorts:
  ZORA, PRL, MNT, BERA, OP, POPCAT, DRV, HYUNDAI, WLD, AAVE, BIRB, GMX, SEI, AERO, LINEA, 1000BONK, JUP, MSFT, 1000FLOKI, WLFI, 1000SHIB, CC, ADA, S, GRAM, SUI, PYTH, LINK, WIF, NEAR, MON, LTC, TRX, DOGE, DOT, FIL, BIO, ZK, ASTER, AVAX
```

## Builder-deployed markets
```
hl:xyz        146 mkts  OI $ 4,053,443,546  24h $ 4,859,217,536
             XYZ100, TSLA, NVDA, GOLD, HOOD, INTC, PLTR, COIN, META, AAPL, MSFT, ORCL, GOOGL, AMZN, AMD, MU, SNDK, MSTR
hl:io          24 mkts  OI $   232,560,300  24h $   115,074,901
             OAI, ANTH, SNDK, IONQ, NBIS, EWY, GPRO, SBE, TCNT, DRAM, PRL, XIAOMI, H100, MOONSHOT, NVDA, SKHX, AAPL, CRCL
hl:para        40 mkts  OI $    13,828,295  24h $     4,066,523
             TOTAL2, OTHERS, BTCD, H100, AVGO, COHR, GLW, CRDO, LRCX, NET, STX, IREN, VST, TER, AAOI, 10Y, CIEN, NAVER
hl:mkts        24 mkts  OI $       259,876  24h $       135,426
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

total 331 builder markets across 10 dexs
```

## Offchain reference rates (FRED)
```
OFFCHAIN REFERENCE RATES (FRED)

  SOFR      3.92%  2026-11-17     -1bp   Secured Overnight Financing Rate (what a desk funds at)
  DFF       3.88%  2026-11-16     +0bp   Effective fed funds
  IORB      3.90%  2026-11-18     +0bp   Interest on reserve balances
  DGS3MO    4.34%  2026-11-16     +2bp   3-month Treasury
  DGS10     5.12%  2026-11-16     -3bp   10-year Treasury
```

## Carry: funding vs borrow
```
PERP FUNDING (annualized from 8h feed) vs ONCHAIN BORROW

asset        lighter  hyperliq   binance     bybit  aave brw  aave sup
----------------------------------------------------------------------
BTC            10.5%      9.9%      7.1%      1.4%     0.00%     0.00%
ETH            10.5%      5.4%      4.4%      1.4%     0.00%     0.00%
SOL            10.5%      4.7%     -1.2%     10.3%         -         -
ENA            10.5%     10.9%      3.8%     -1.5%         -         -
HYPE           10.5%     10.9%     10.9%      8.0%         -         -
LINK           -1.8%     10.9%      1.9%    -13.1%     0.00%     0.00%
AVAX           10.5%      1.4%      0.2%     -7.2%         -         -
DOGE           10.5%      7.5%     -0.5%     -8.2%         -         -

STABLE BORROW COST (the cost of carrying a hedged position)
  aave   USDe     borrow  0.00%  supply  0.00%
  aave   RLUSD    borrow  3.76%  supply  2.21%
  aave   USDC     borrow  3.78%  supply  2.57%
  aave   RLUSD    borrow  3.86%  supply  2.70%
  aave   GHO      borrow  3.91%  supply  3.03%
  aave   GHO      borrow  3.92%  supply  3.04%
  aave   GHO      borrow  4.36%  supply  3.33%
  aave   USDC     borrow  4.40%  supply  3.14%
  morpho    cbBTC/USDC    borrow  5.10%  lltv 0.86  $333,148,730
  morpho    PRIME/PYUSD   borrow  6.08%  lltv 0.86  $170,639,719
  morpho     kBTC/RLUSD   borrow  3.30%  lltv 0.86  $166,138,543
  morpho PT-reUSD-10DEC2026/USDC    borrow 11.00%  lltv 0.92  $135,876,986
  morpho     WBTC/USDC    borrow  5.11%  lltv 0.86  $123,131,086
  morpho   wstETH/USDT    borrow  3.58%  lltv 0.86  $120,367,779

OFFCHAIN BENCHMARK: SOFR 3.92% (2026-11-17)
  BTC perp funding 10.51% vs SOFR 3.92%: spread +6.59pp over the offchain cost of money

BUILDER-DEPLOYED PERPS: 331 markets, 173 with volume today
  xyz:SP500        OI $  452,926,882  funding      5.5%/yr
  xyz:NVDA         OI $  398,539,430  funding      5.5%/yr
  xyz:BRENTOIL     OI $  308,567,928  funding      5.5%/yr
  xyz:XYZ100       OI $  273,048,093  funding      5.5%/yr
  xyz:SKHX         OI $  260,687,291  funding   -192.3%/yr
  xyz:GOLD         OI $  241,812,612  funding     19.2%/yr
  io:ANTH          OI $  199,018,956  funding     -2.9%/yr
  xyz:ANT          OI $  161,064,206  funding     -0.0%/yr
  xyz:SILVER       OI $  151,934,559  funding     19.7%/yr
  xyz:MU           OI $  136,874,228  funding      5.5%/yr
```
