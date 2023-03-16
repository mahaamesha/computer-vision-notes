import mycalibrator as c


if __name__ == "__main__":
    CamCalib = c.CameraCalibrator(PATERN_SIZE=(8,6), calib_dir='./img/calib/')

    CamCalib.do_camera_calibration()

    im1, im2 = CamCalib.do_image_undistortion('./img/test/left12.jpg')
    im_diff = CamCalib.get_diff_image(im1, im2)