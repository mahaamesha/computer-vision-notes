import mycalibrator as c


if __name__ == "__main__":
    CamCalib = c.CameraCalibrator(PATERN_SIZE=(8,6), calib_dir='./img/calib_/')
    # CamCalib = c.CameraCalibrator(PATERN_SIZE=(7,5), calib_dir='./img/calib/')

    CamCalib.compress_calib_imgs(isResize=0)

    CamCalib.do_camera_calibration()

    im1, im2 = CamCalib.do_image_undistortion('./img/test_/left12.jpg', alpha=0)
    # im1, im2 = CamCalib.do_image_undistortion('./img/test/DSC_2937.JPG', alpha=0)
    im_diff = CamCalib.get_diff_image(im1, im2)