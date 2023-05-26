# Resize


I realize that the image size affect the intrinsic and extrinsic parameters in camera calibration process.

Because my video is taken in 1920x1080, while my chessboard images in 4928x3264, so i have to crop the chessboard image into 1920x1080.

```
c=1.1   size=(4480, 2967)
c=1.2000000000000002    size=(4106, 2719)
c=1.3000000000000003    size=(3790, 2510)
c=1.4000000000000004    size=(3519, 2331)
c=1.5000000000000004    size=(3285, 2175)
c=1.6000000000000005    size=(3079, 2039)
c=1.7000000000000006    size=(2898, 1919)
c=1.8000000000000007    size=(2737, 1813)
c=1.9000000000000008    size=(2593, 1717)
c=2.000000000000001     size=(2463, 1631)
c=2.100000000000001     size=(2346, 1554)
c=2.200000000000001     size=(2239, 1483)
c=2.300000000000001     size=(2142, 1419)
c=2.4000000000000012    size=(2053, 1359)
c=2.5000000000000013    size=(1971, 1305)
c=2.6000000000000014    size=(1895, 1255)
c=2.5000000000000013    size=(1971, 1305)
```