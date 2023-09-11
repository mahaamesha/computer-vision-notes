import cv2 as cv
import numpy as np


# tips: use `w, h, c = get_frame_shape(frame)` before
def region_of_interest(frame, range_row=[0,0], range_col=[0,0]):
	start_row, end_row = int( range_row[0] ), int( range_row[1] )     # row : heigth
	start_col, end_col = int( range_col[0] ), int( range_col[1] )     # col : width

	point1 = (start_col, start_row)
	point2 = (end_col, end_row)
	
	# blank, same size with frame
	blank = np.zeros(frame.shape[:2], dtype="uint8")
	# create masking with white color
	mask = cv.rectangle(blank, pt1=point1, pt2=point2, color=255, thickness=-1)
	# get only the region of interest
	roi_full = cv.bitwise_and(frame, frame, mask=mask)
	roi = roi_full[start_row:end_row, start_col:end_col]

	return roi, roi_full, mask