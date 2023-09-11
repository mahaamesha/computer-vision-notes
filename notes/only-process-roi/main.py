import cv2 as cv
import numpy as np
import func as f

if __name__ == '__main__':
    # capture video
    file_path = r"E:\_TUGAS\_ITBOneDrive\OneDrive - Institut Teknologi Bandung\_Kuliah\_sem8\8_tugas akhir 2\data\230909 data paper\simpangan kecil 01.mp4"
    cap = cv.VideoCapture(file_path)
    
    # read
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret: print('No frame left'); break

        # PROCESSING
        # get roi
        h,w,c = frame.shape
        range_row, range_col = [h//3, h//2], [w//3, w//2]
        roi = frame[range_row[0]:range_row[1], range_col[0]:range_col[1]]
        # process the ROI
        hsv = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
        # overlay the roi into the original frame
        frame[range_row[0]:range_row[1], range_col[0]:range_col[1]] = hsv

        # display, then wait or exit
        cv.imshow('output', frame)
        if cv.waitKey(1) & 0xFF == ord('q'): break
    

    # release
    cap.release(); cap = None
