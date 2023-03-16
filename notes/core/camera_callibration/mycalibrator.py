import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os


class CameraCalibrator():
	def __init__(self, PATERN_SIZE:tuple=(8,6), calib_dir:str="./img/calib/"):
		self.PATERN_SIZE = PATERN_SIZE
		self.calib_dir = os.path.join( os.path.abspath(__file__), '../' , calib_dir )
		
		# termination criteria
		self.criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
		
		# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
		self.objp = np.zeros((self.PATERN_SIZE[0] * self.PATERN_SIZE[1], 3), np.float32)
		self.objp[:,:2] = np.mgrid[0:self.PATERN_SIZE[0], 0:self.PATERN_SIZE[1]].T.reshape(-1,2)
		
		# arrays to store object points and image points from all the images.
		self.objpoints = [] # 3d point in real world space
		self.imgpoints = [] # 2d points in image plane
		# self.imgs = []  # to store img w/ identified chessboard corner

		# calibration properties
		self.ret = None     # calibration return value
		self.mtx = None     # camera matrix
		self.dist = None    # distortion coefs
		self.rvecs = None   # rotational vector
		self.tvecs = None   # translation vector

		# reprojection error
		self.mean_err = None
	

	def get_calib_properties(self):
		# find the chessboard pattern
		for fname in os.listdir(self.calib_dir):
			img = cv.imread(os.path.join(self.calib_dir, fname))
			gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
			# find the chess board corners
			ret, corners = cv.findChessboardCorners(gray, self.PATERN_SIZE, corners=None)
			if ret == True:
				self.objpoints.append(self.objp)
				# increase accuracy
				corners2 = cv.cornerSubPix(gray, corners, winSize=(11,11), zeroZone=(-1,-1), criteria=self.criteria)
				self.imgpoints.append(corners2)
				# draw and display the corners
				cv.drawChessboardCorners(img, self.PATERN_SIZE, corners2, ret)

				plt.imshow( cv.cvtColor(img, cv.COLOR_BGR2RGB) ); plt.title(fname); plt.show()
		
		# calibrate to get intrinsic & extrinsic properties
		# mtx, dist are intrinsic | rvecs, tvecs are extrinsic
		self.ret, self.mtx, self.dist, self.rvecs, self.tvecs = cv.calibrateCamera(self.objpoints, self.imgpoints, gray.shape[::-1], \
																					cameraMatrix=None, distCoeffs=None, rvecs=None, tvecs=None)
		# convert tuple to numpy array
		self.rvecs, self.tvecs = np.asarray(self.rvecs), np.asarray(self.tvecs)

	
	def calculate_reprojection_error(self):
		self.mean_err = 0
		for i in range(len(self.objpoints)):
			imgpoints2, _ = cv.projectPoints(self.objpoints[i], self.rvecs[i], self.tvecs[i], self.mtx, self.dist)
			error = cv.norm(self.imgpoints[i], imgpoints2, cv.NORM_L2)/len(imgpoints2)
			self.mean_err += error
		self.mean_err = self.mean_err/len(self.objpoints)


	def print_calib_properties(self):
		print('========== CALIBRATION PROPERTIES ==========\n')
		print('Ret:', self.ret, end="\n\n")
		print('Camera matrix:'); print("Type:", type(self.mtx)); print("Shape:", self.mtx.shape); print(self.mtx, end="\n\n")
		print('Distortion coefficients:'); print("Type:", type(self.dist)); print("Shape:", self.dist.shape); print(self.dist, end="\n\n")
		print('Rotation vectors:'); print("Type:", type(self.rvecs)); print("Shape:", self.rvecs.shape); print(self.rvecs, end="\n\n")
		print('Translation vectors:'); print("Type:", type(self.tvecs)); print("Shape:", self.tvecs.shape); print(self.tvecs, end="\n\n")
		print('*) `rvecs` and `tvecs` contains (3x1) vector for every image.\n')

		print('Re-projection error:', self.mean_err)
		print('*) The closer the re-projection error is to zero, the more accurate the parameters we found are.\n')

	
	# if I already did the calibration once, i can save the calib properties
	def store_calib_properties(self, file_path:str='./data/calib_properties.npz'):
		file_path = os.path.join( os.path.abspath(__file__), '../' , file_path )
		np.savez(file_path, \
			objpoints=self.objpoints, \
			imgpoints=self.imgpoints, \
			ret=self.ret, \
			mtx=self.mtx, \
			dist=self.dist, \
			rvecs=self.rvecs, \
			tvecs=self.tvecs)
	

	def load_calib_properties(self, file_path:str='./data/calib_properties.npz'):
		file_path = os.path.join( os.path.abspath(__file__), '../' , file_path )
		data = np.load(file_path)
		
		self.objpoints = data['objpoints']
		self.imgpoints = data['imgpoints']
		self.ret = data['ret']
		self.mtx = data['mtx']
		self.dist = data['dist']
		self.rvecs = data['rvecs']
		self.tvecs = data['tvecs']


	def undistort_image(self, file_path:str="./img/test/left12.jpg", alpha=1):
		file_path = os.path.join( os.path.abspath(__file__), '../' , file_path )
		img = cv.imread(file_path)      # test image
		h,  w = img.shape[:2]
		
		# get optimum camera matrix
		newcameramtx, roi = cv.getOptimalNewCameraMatrix(self.mtx, self.dist, (w,h), alpha, newImgSize=(w,h))
		
		# use remapping to undistort image
		mapx, mapy = cv.initUndistortRectifyMap(self.mtx, self.dist, None, newcameramtx, (w,h), 5)
		dst = cv.remap(img, mapx, mapy, cv.INTER_LINEAR)
		
		# crop the image
		x, y, w, h = roi
		dst = dst[y:y+h, x:x+w]
		
		plt.imshow( cv.cvtColor(img, cv.COLOR_BGR2RGB) ); plt.title('im_distorted.jpg'); plt.show()
		plt.imshow( cv.cvtColor(dst, cv.COLOR_BGR2RGB) ); plt.title('im_undistorted.jpg'); plt.show()
		
		return img, dst


	def get_diff_image(self, im1, im2):
		im1_resized = cv.resize(im1, (im2.shape[1], im2.shape[0]))
		im_diff = cv.absdiff(im1_resized, im2)

		fig, axs = plt.subplots(1, 2, figsize=(12,6))
		axs[0].imshow( cv.cvtColor(im1, cv.COLOR_BGR2RGB) )
		axs[1].imshow( cv.cvtColor(im2, cv.COLOR_BGR2RGB) )
		plt.tight_layout(); plt.show()

		plt.imshow( cv.cvtColor(im_diff, cv.COLOR_BGR2RGB) ); plt.show()
		return im_diff

	
	def do_camera_calibration(self):
		self.get_calib_properties()
		self.calculate_reprojection_error()
		self.print_calib_properties()
		self.store_calib_properties()


	def do_image_undistortion(self, file_path:str="img/test/left12.jpg", alpha=1):
		self.load_calib_properties()
		img, dst = self.undistort_image(file_path, alpha)
		return img, dst