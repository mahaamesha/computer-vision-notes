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
- [Usage](#usage)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>
Some pinhole cameras introduce significant distortion to images. Two major kinds of distortion are radial distortion and tangential distortion.

![](https://docs.opencv.org/4.x/calib_radial.jpg)

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

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them.

```
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running.

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo.

## 🔧 Running the tests <a name = "tests"></a>

Test program architecture
```
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




## 🎈 Usage <a name="usage"></a>

Add notes about how to use the system.

## 🚀 Deployment <a name = "deployment"></a>

Add additional notes about how to deploy this on a live system.

## ✍️ Authors <a name = "authors"></a>

- [@mahaamesha](https://github.com/mahaamesha) - Idea & Initial work

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- Hat tip to anyone whose code was used
### Inspiration
### References