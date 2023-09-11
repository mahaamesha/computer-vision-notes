When processing video, each operation for a frame with N x M dimensions, will be high cost in computation.

ROI (Region of Interest) will be usefull to be used, then the image processing operation only applied on it, and at the end of the processing, the ROI will be placed over the original image (N x M).