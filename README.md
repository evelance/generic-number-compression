# Comparison of compression of binary numbers

For more information, see https://lemire.me/blog/2022/11/28/generic-number-compression-zstd/
(loop count has been increased to 1,000,000).

This script additionally checks the compression ratio for all levels of gzip, zstd and brotli.

 - Dependencies: make, g++, python3, xxd, gzip, brotli, zstd
 - Tested on 6.0.8-1-MANJARO/zen3
 - License: Public domain

## Running

On Linux, simply run `make`.

## Example results

```
Versions: gzip 1.12, brotli 1.0.9, zstd 1.5.2

Checking compression for file 'testfloat.dat'
00000000: 0000 00c0 128d e63f 0000 00a0 f321 cf3f  .......?.....!.?
00000010: 0000 00a0 2580 eb3f 0000 00e0 012a ea3f  ....%..?.....*.?
00000020: 0000 00a0 9cdf eb3f 0000 00c0 2ca4 e53f  .......?....,..?
00000030: 0000 0020 2dea da3f 0000 00e0 83e4 b03f  ... -..?.......?

gzip-1      0.14s    4497086  56.21%
gzip-2      0.15s    4405250  55.07%
gzip-3      0.20s    4226521  52.83%
gzip-4      0.18s    4293399  53.67%
gzip-5      0.26s    4217599  52.72%
gzip-6      0.65s    4145749  51.82%
gzip-7      0.92s    4135614  51.70%
gzip-8      1.79s    4119466  51.49%
gzip-9      5.50s    4093342  51.17%
brotli-0    0.02s    4835457  60.44%
brotli-1    0.04s    4487415  56.09%
brotli-2    0.06s    4248298  53.10%
brotli-3    0.09s    4269716  53.37%
brotli-4    0.18s    3934549  49.18%
brotli-5    0.31s    4045934  50.57%
brotli-6    0.45s    4021443  50.27%
brotli-7    0.72s    4002639  50.03%
brotli-8    1.07s    3990338  49.88%
brotli-9    1.55s    3986579  49.83%
brotli-10   5.16s    3595443  44.94%
brotli-11  10.15s    3517421  43.97%
zstd-1      0.02s    4508213  56.35%
zstd-2      0.03s    3981746  49.77%
zstd-3      0.04s    4190227  52.38%
zstd-4      0.04s    4197801  52.47%
zstd-5      0.06s    4133128  51.66%
zstd-6      0.12s    4178830  52.24%
zstd-7      0.13s    4161813  52.02%
zstd-8      0.17s    3878348  48.48%
zstd-9      0.18s    3895284  48.69%
zstd-10     0.26s    3893702  48.67%
zstd-11     0.51s    3892228  48.65%
zstd-12     0.58s    3892783  48.66%
zstd-13     1.02s    3914410  48.93%
zstd-14     1.42s    3909841  48.87%
zstd-15     1.57s    3907928  48.85%
zstd-16     1.56s    3754120  46.93%
zstd-17     2.01s    3754058  46.93%
zstd-18     2.21s    3756331  46.95%
zstd-19     2.31s    3755501  46.94%
zstd-20     2.29s    3755501  46.94%
zstd-21     2.30s    3755501  46.94%
zstd-22     2.31s    3755501  46.94%

Checking compression for file 'testint.dat'
00000000: 7e00 0000 0000 0000 f1ff ffff ffff ffff  ~...............
00000010: 2200 0000 0000 0000 2100 0000 0000 0000  ".......!.......
00000020: 6d00 0000 0000 0000 c6ff ffff ffff ffff  m...............
00000030: 1f00 0000 0000 0000 2100 0000 0000 0000  ........!.......

gzip-1      0.06s    1896180  23.70%
gzip-2      0.07s    1763936  22.05%
gzip-3      0.12s    1664324  20.80%
gzip-4      0.09s    1688014  21.10%
gzip-5      0.15s    1675779  20.95%
gzip-6      0.34s    1660675  20.76%
gzip-7      0.42s    1655394  20.69%
gzip-8      1.90s    1584857  19.81%
gzip-9      7.20s    1519492  18.99%
brotli-0    0.01s    1743049  21.79%
brotli-1    0.02s    1968485  24.61%
brotli-2    0.02s    1681265  21.02%
brotli-3    0.03s    1795770  22.45%
brotli-4    0.07s    1851423  23.14%
brotli-5    0.15s    1523142  19.04%
brotli-6    0.16s    1532965  19.16%
brotli-7    0.22s    1543315  19.29%
brotli-8    0.31s    1545633  19.32%
brotli-9    0.48s    1521837  19.02%
brotli-10   4.14s    1289744  16.12%
brotli-11   9.44s    1234645  15.43%
zstd-1      0.02s    1593200  19.91%
zstd-2      0.02s    1520067  19.00%
zstd-3      0.02s    1656052  20.70%
zstd-4      0.02s    1655583  20.69%
zstd-5      0.04s    1653395  20.67%
zstd-6      0.07s    1658168  20.73%
zstd-7      0.09s    1657940  20.72%
zstd-8      0.12s    1675177  20.94%
zstd-9      0.12s    1675023  20.94%
zstd-10     0.17s    1663486  20.79%
zstd-11     0.30s    1631235  20.39%
zstd-12     0.30s    1630672  20.38%
zstd-13     0.46s    1467802  18.35%
zstd-14     0.79s    1403527  17.54%
zstd-15     1.07s    1314785  16.43%
zstd-16     1.56s    1323872  16.55%
zstd-17     1.80s    1322193  16.53%
zstd-18     2.52s    1297167  16.21%
zstd-19     2.60s    1297221  16.22%
zstd-20     2.64s    1297221  16.22%
zstd-21     2.67s    1297221  16.22%
zstd-22     2.67s    1297221  16.22%
```

