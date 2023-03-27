<h3 align="center">Camera Calibration</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/kylelobo/The-Documentation-Compendium.svg)](https://github.com/mahaamesha/image-processing-notes/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/mahaamesha/image-processing-notes/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> I want to do camera calibration to get calibration properties. In addition, after i have these, i can undistort my test image.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Tests](#tests)
- [Result](#result)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>
Some pinhole cameras introduce significant distortion to images. Two major kinds of distortion are radial distortion and tangential distortion.

<img width="50%" align="center" src="https://docs.opencv.org/4.x/calib_radial.jpg"></img>

**Radial distortion** causes straight lines to appear curved. Radial distortion becomes larger the farther points are from the center of the image.

Radial distortion can be represented as follows:

$$
    x_{distorted} = x(1 + k_1 r^2 + k_2 r^4 + k_3 r^6) \\
    y_{distorted} = y(1 + k_1 r^2 + k_2 r^4 + k_3 r^6)
$$

**Tangential distortion** occurs because the image-taking lense is not aligned perfectly parallel to the imaging plane. So, some areas in the image may look nearer than expected. The amount of tangential distortion can be represented as below:

$$
    x_{distorted} = x + [2 p_1 xy + p_2 (r^2 + 2x^2)] \\
    y_{distorted} = y + [p_1 (r^2 + 2y^2) + 2p_2 xy]
$$

In short, we need to find five parameters, known as **distortion coefficients** given by:

$$
    Distortion coefficients = (
        \begin{matrix}
            k_1 & k_2 & p_1 & p_2 & k_3
        \end{matrix}
    )
$$

**Intrinsic parameters** are specific to a camera. They include information like focal length $(f_x,f_y)$ and optical centers $(c_x,c_y)$. It can be used to remove distortion due to the lenses of a specific camera. The camera matrix is unique to a specific camera, so once calculated, it can be reused on other images taken by the same camera. It is expressed as a 3x3 matrix:

$$
    camera matrix = \left[
        \begin{matrix}
            f_x & 0 & c_x \\
            0   & f_y & c_y \\
            0   & 0 & 1
        \end{matrix}
    \right]
$$

**Extrinsic parameters** corresponds to rotation and translation vectors which translates a coordinates of a 3D point to a coordinate system.


## 🏁 Getting Started <a name = "getting_started"></a>

To run the main program, we need to provide some chessboard images with variation of distance and angle. The documentation stated that its good to has at least 10 images.


## 🔧 Tests <a name = "tests"></a>

Test program architecture
``` py
camera_calibration/:
    data/:
        calib_properties_.npz
    img/:
        calib_/:
            <calibration_images.jpg>
        result_/:
            <result_images.jpg>
        test_/:
            <test_images.jpg>
    test.py
```

[`im_found.jpg`](./img/result_/im_found.jpg)\
<img width="49%" src="./img/result_/im_found.jpg"></img>\
**Fig x.** Distorted image with pattern drawn on it

[`im_compare.jpg`](./img/result_/im_compare.jpg)\
<img width="100%" src="./img/result_/im_compare.jpg"></img>\
**Fig x.** Comparison between (a) distorted image and (b) undistorted image

[`im_absdiff.jpg`](./img/result_/im_absdiff.jpg)\
<img width="49%" src="./img/result_/im_absdiff.jpg"></img>\
**Fig x.** Absolute difference between distorted and undistorted image


Below is the summary of the result of calibration
``` py
========== CALIBRATION PROPERTIES ==========

Ret: 0.17989164670236782

Camera matrix:
Type: <class 'numpy.ndarray'>
Shape: (3, 3)
[[532.89681128   0.         342.22771903]
 [  0.         533.00943292 234.53947215]
 [  0.           0.           1.        ]]

Distortion coefficients:
Type: <class 'numpy.ndarray'>
Shape: (1, 5)
[[-2.79126350e-01  1.93660883e-02  1.25547927e-03 -2.25070411e-05
   1.55094873e-01]]

Rotation vectors:
Type: <class 'numpy.ndarray'>
Shape: (11, 3, 1)
[[[ 0.41769431]
  [ 0.65664191]
  [-1.33641378]]

 [[-0.27889177]
  [ 0.18739243]
  [ 0.3550305 ]]

 [[-0.11259054]
  [ 0.23956433]
  [-0.00220022]]

 [[-0.29450616]
  [ 0.4294765 ]
  [ 1.31272903]]

 [[-0.31865366]
  [ 0.16151149]
  [-1.24092914]]

 [[-0.45412108]
  [-0.08749953]
  [-1.33600718]]

 [[ 0.20093673]
  [-0.42513057]
  [ 0.13269691]]

 [[-0.42041729]
  [-0.49797817]
  [ 1.33626276]]

 [[-0.24102689]
  [ 0.34810989]
  [ 1.53050812]]

 [[ 0.46557428]
  [-0.28487706]
  [ 1.23869442]]

 [[-0.17178584]
  [-0.46906138]
  [ 1.34672731]]]

Translation vectors:
Type: <class 'numpy.ndarray'>
Shape: (11, 3, 1)
[[[-2.23666129]
  [ 2.5622497 ]
  [13.44999205]]

 [[-0.67045742]
  [-3.67691725]
  [12.4334818 ]]

 [[-2.96370777]
  [-2.68343933]
  [12.92773712]]

 [[ 2.53669438]
  [-3.72122477]
  [12.16826045]]

 [[-5.96206956]
  [ 2.34449236]
  [16.74475248]]

 [[-3.53620898]
  [ 3.04104607]
  [11.40052829]]

 [[-2.65071568]
  [-3.21774998]
  [11.05664752]]

 [[ 1.87828973]
  [-4.41288962]
  [13.45290403]]

 [[ 2.03640781]
  [-3.14861165]
  [12.45879143]]

 [[ 1.35002774]
  [-3.63304008]
  [11.56754428]]

 [[ 1.80215329]
  [-4.30164281]
  [12.43104036]]]

*) `rvecs` and `tvecs` contains (3x1) vector for every image.

Re-projection error: 0.025770447672861817
*) The closer the re-projection error is to zero, the more accurate the parameters we found are.
```


## 🎈 Result <a name="result"></a>

Calibration program architecture
``` py
camera_calibration/:
    data/:
        calib_properties_.npz
    img/:
        calib/:
            <calibration_images.jpg>
        result/:
            <result_images.jpg>
        test/:
            <test_images.jpg>
    main.py
```

[`im_found.jpg`](./img/result/im_found.jpg)\
<img width="49%" src="./img/result/im_found.jpg"></img>\
**Fig x.** Distorted image with pattern drawn on it

[`im_compare.jpg`](./img/result/im_compare.jpg)\
<img width="100%" src="./img/result/im_compare.jpg"></img>\
**Fig x.** Comparison between (a) distorted image and (b) undistorted image

[`im_absdiff.jpg`](./img/result/im_absdiff.jpg)\
<img width="49%" src="./img/result/im_absdiff.jpg"></img>\
**Fig x.** Absolute difference between distorted and undistorted image


Below is the summary of the result of calibration
``` py
========== CALIBRATION PROPERTIES ==========

Ret: 2.2273378247359656

Camera matrix:
Type: <class 'numpy.ndarray'>
Shape: (3, 3)
[[4.79178739e+03 0.00000000e+00 2.45773350e+03]
 [0.00000000e+00 4.79063518e+03 1.67017424e+03]
 [0.00000000e+00 0.00000000e+00 1.00000000e+00]]

Distortion coefficients:
Type: <class 'numpy.ndarray'>
Shape: (1, 5)
[[-1.74972915e-01  2.16815563e+00 -2.44442227e-03 -3.68081560e-04
  -1.21993025e+01]]

Rotation vectors:
Type: <class 'numpy.ndarray'>
Shape: (10, 3, 1)
[[[ 1.91184032e-02]
  [ 4.16063283e-01]
  [-2.00889733e-04]]

 [[ 3.71437541e-03]
  [-4.19413375e-01]
  [-4.14966762e-02]]

 [[ 5.28309027e-01]
  [-2.43449955e-02]
  [ 7.25295006e-03]]

 [[-3.48692256e-01]
  [-3.74968342e-01]
  [-4.00435927e-01]]

 [[ 4.71750087e-01]
  [-3.37848908e-01]
  [ 2.20689011e-01]]

 [[-5.78758381e-02]
  [ 2.45516732e-02]
  [ 9.93441497e-03]]

 [[-5.53075533e-02]
  [-3.59019561e-01]
  [-1.79653267e-02]]

 [[ 3.44079645e-01]
  [ 3.34715088e-02]
  [-4.15244044e-03]]

 [[ 3.58487837e-01]
  [ 1.68458391e-01]
  [-2.68087562e-01]]

 [[-4.37596290e-01]
  [-3.40124988e-01]
  [-4.16784597e-01]]]

Translation vectors:
Type: <class 'numpy.ndarray'>
Shape: (10, 3, 1)
[[[-2.84720239]
  [-1.03240987]
  [25.82907615]]

 [[-3.12217721]
  [-1.205349  ]
  [24.13282751]]

 [[-2.86115246]
  [-0.89573268]
  [24.873983  ]]

 [[-4.13335084]
  [ 0.66106401]
  [24.82131959]]

 [[-2.67022109]
  [-1.98506557]
  [24.59988559]]

 [[-2.73465667]
  [-2.64394261]
  [12.72419144]]

 [[-2.44226156]
  [-2.02571237]
  [10.98798656]]

 [[-2.80315449]
  [-2.00208526]
  [11.39020653]]

 [[-3.5323531 ]
  [-0.58039975]
  [12.80553938]]

 [[-3.99942997]
  [-0.39512997]
  [13.75880625]]]

*) `rvecs` and `tvecs` contains (3x1) vector for every image.

Re-projection error: 0.3558704252807704
*) The closer the re-projection error is to zero, the more accurate the parameters we found are.

======= (END) CALIBRATION PROPERTIES =======
```

## ✍️ Authors <a name = "authors"></a>

- [@mahaamesha](https://github.com/mahaamesha) - Modified program

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

In this topic, I create more modular program for camera calibration using class.

### References
- [OpenCV Documentation: Camera Calibration](https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html)
