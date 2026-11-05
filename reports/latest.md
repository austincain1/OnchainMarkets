# 2026-11-05

## Market list changes
```
2026-11-04.json -> 2026-11-05.json

hl:abcd: no change (1 markets)
hl:cash: no change (17 markets)
hl:flx: no change (16 markets)
hl:hyna: no change (25 markets)
hl:io: no change (19 markets)
hl:km: no change (23 markets)
hl:mkts: no change (24 markets)
hl:para: no change (40 markets)
hl:vntl: no change (15 markets)
hl:xyz: 142 -> 143
  NEW     (1): xyz:STX

hyperliquid: no change (235 markets)
lighter: no change (235 markets)
variational: 586 -> 588
  NEW     (2): MARA, MCD

```

## Funding dispersion
```
205 symbols quoted on 2+ venues. Top 25 by dispersion.

sym             lighter  hyperliqu    binance      bybit     spread      ann  flag
----------------------------------------------------------------------------------
PRL             0.5360%          -    0.0100%    0.0100%    0.5260%      576%/yr
STONK           0.3064%          -          -    0.0100%    0.2964%      325%/yr
FOLKS           0.2920%          -    0.0187%    0.0581%    0.2733%      299%/yr
CXMT            0.0032%          -   -0.2615%   -0.0746%    0.2647%      290%/yr  SIGN SPLIT
ZHIPU           0.0000%          -   -0.1929%   -0.0395%    0.1929%      211%/yr
CAP             0.0096%          -    0.1941%    0.1131%    0.1845%      202%/yr
HYUNDAI               -   -0.1460%    0.0000%    0.0000%    0.1460%      160%/yr
UNITREE        -0.0344%          -   -0.1607%   -0.1649%    0.1305%      143%/yr
DRV             0.0096%          -          -   -0.1148%    0.1244%      136%/yr  SIGN SPLIT
BERA            0.0080%   -0.1079%   -0.0351%   -0.0087%    0.1159%      127%/yr  SIGN SPLIT
XMR             0.1128%    0.1769%    0.0687%    0.1493%    0.1082%      118%/yr
MINIMAX        -0.0544%          -   -0.0971%    0.0000%    0.0971%      106%/yr
SKHYNIX               -   -0.2483%   -0.1895%   -0.1698%    0.0785%       86%/yr
MET            -0.0264%   -0.0653%    0.0049%    0.0030%    0.0702%       77%/yr  SIGN SPLIT
XLM             0.0096%    0.0048%   -0.0105%   -0.0570%    0.0666%       73%/yr  SIGN SPLIT
QQQ             0.0296%          -    0.0570%    0.0921%    0.0625%       68%/yr
HANMI                 -          -   -0.0692%   -0.0079%    0.0613%       67%/yr
ONDO           -0.0512%   -0.0038%   -0.0069%   -0.0633%    0.0595%       65%/yr
NATGAS          0.3192%    0.3378%    0.3787%          -    0.0595%       65%/yr
SOXL            0.0656%          -    0.0956%    0.0383%    0.0572%       63%/yr
KORU            0.0032%          -    0.0599%    0.0043%    0.0567%       62%/yr
XPD             0.0032%   -0.0514%    0.0000%          -    0.0546%       60%/yr  SIGN SPLIT
HBAR           -0.0360%    0.0100%   -0.0042%   -0.0432%    0.0532%       58%/yr  SIGN SPLIT
GRAM            0.0096%   -0.0360%   -0.0261%   -0.0436%    0.0532%       58%/yr  SIGN SPLIT
ARB             0.0016%    0.0100%   -0.0125%   -0.0403%    0.0503%       55%/yr  SIGN SPLIT

57 symbols where one venue pays longs while another pays shorts:
  CXMT, DRV, BERA, MET, XLM, XPD, HBAR, GRAM, ARB, ETHFI, SEI, LIT, 1000BONK, VIRTUAL, 1000SHIB, APT, TIA, WLFI, DOGE, KAITO, SUI, AXS, TRUMP, LDO, LINK, ENA, PENDLE, ADA, GRASS, FIL, TAO, JUP, BIRB, LTC, MON, CRV, PENGU, OP, JTO, BIO
```

## Builder-deployed markets
```
hl:xyz        143 mkts  OI $ 4,386,973,052  24h $ 7,362,728,894
             XYZ100, TSLA, NVDA, GOLD, HOOD, INTC, PLTR, COIN, META, AAPL, MSFT, ORCL, GOOGL, AMZN, AMD, MU, SNDK, MSTR
hl:io          19 mkts  OI $   157,447,778  24h $   133,838,427
             OAI, ANTH, SNDK, IONQ, NBIS, EWY, GPRO, SBE, TCNT, DRAM, PRL, XIAOMI, H100, MOONSHOT, NVDA, SKHX, AAPL, CRCL
hl:para        40 mkts  OI $    15,017,809  24h $     9,579,854
             TOTAL2, OTHERS, BTCD, H100, AVGO, COHR, GLW, CRDO, LRCX, NET, STX, IREN, VST, TER, AAOI, 10Y, CIEN, NAVER
hl:mkts        24 mkts  OI $       114,200  24h $       143,825
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

total 323 builder markets across 10 dexs
```

## Offchain reference rates (FRED)
```
OFFCHAIN REFERENCE RATES (FRED)

  SOFR      3.94%  2026-11-04     -3bp   Secured Overnight Financing Rate (what a desk funds at)
  DFF       3.88%  2026-11-03     +0bp   Effective fed funds
  IORB      3.90%  2026-11-05     +0bp   Interest on reserve balances
  DGS3MO    4.21%  2026-11-03     +0bp   3-month Treasury
  DGS10     4.95%  2026-11-03     +4bp   10-year Treasury
```

## Carry: funding vs borrow
```
PERP FUNDING (annualized from 8h feed) vs ONCHAIN BORROW

asset        lighter  hyperliq   binance     bybit  aave brw  aave sup
----------------------------------------------------------------------
BTC            10.5%     10.9%     10.9%      6.2%     0.00%     0.00%
ETH             7.0%      7.1%     10.9%    -12.3%     0.00%     0.00%
SOL            10.5%      3.1%     -3.6%     -7.4%         -         -
ENA            10.5%     10.9%     10.9%    -27.0%         -         -
HYPE           10.5%     10.9%     10.9%     10.9%         -         -
LINK          -29.8%     10.9%      8.7%    -23.1%     0.00%     0.00%
AVAX           -2.6%     -1.2%     -2.9%     -2.9%         -         -
DOGE           10.5%      8.9%      4.5%    -35.1%         -         -

STABLE BORROW COST (the cost of carrying a hedged position)
  aave   USDe     borrow  0.00%  supply  0.00%
  aave   RLUSD    borrow  3.24%  supply  1.64%
  aave   USDC     borrow  3.96%  supply  2.81%
  aave   GHO      borrow  4.04%  supply  3.23%
  aave   RLUSD    borrow  4.06%  supply  3.08%
  aave   GHO      borrow  4.53%  supply  3.60%
  aave   USDC     borrow  4.57%  supply  3.75%
  aave   USDC     borrow  4.64%  supply  3.49%
  morpho    cbBTC/USDC    borrow  5.33%  lltv 0.86  $333,986,934
  morpho     kBTC/RLUSD   borrow  3.65%  lltv 0.86  $255,051,545
  morpho    PRIME/PYUSD   borrow  6.30%  lltv 0.86  $186,554,973
  morpho PT-reUSD-10DEC2026/USDC    borrow 13.55%  lltv 0.92  $147,395,105
  morpho   wstETH/USDT    borrow  3.59%  lltv 0.86  $144,626,721
  morpho     WBTC/USDC    borrow  5.42%  lltv 0.86  $136,138,698

OFFCHAIN BENCHMARK: SOFR 3.94% (2026-11-04)
  BTC perp funding 10.51% vs SOFR 3.94%: spread +6.57pp over the offchain cost of money

BUILDER-DEPLOYED PERPS: 323 markets, 168 with volume today
  xyz:SP500        OI $  409,262,983  funding     20.6%/yr
  xyz:XYZ100       OI $  380,323,889  funding     46.1%/yr
  xyz:BRENTOIL     OI $  348,880,432  funding    -58.6%/yr
  xyz:SKHX         OI $  327,944,073  funding   -272.5%/yr
  xyz:GOLD         OI $  311,325,411  funding      5.5%/yr
  xyz:SILVER       OI $  213,966,520  funding      5.5%/yr
  xyz:GOOGL        OI $  199,536,532  funding      5.5%/yr
  xyz:MU           OI $  168,052,070  funding     31.4%/yr
  xyz:SPCX         OI $  165,941,864  funding     38.5%/yr
  xyz:SNDK         OI $  165,909,320  funding     34.2%/yr
```
