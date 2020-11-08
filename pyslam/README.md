# PySLAM

## Display

First time to try PyGam for display purpose. 

1. `screen` object is a canvas with frame to hold everything; the `surface` is like a (separate) paper for drawing
2. `.blit()` is used to copy the contents of one `Surface` to another display like `screen`

## Feature detectors

1. **ORB** is first chosen for speed reason, but the features are not so evenly distributed. Note, `cv2.ORB_create()` instead of `cv2.ORB()` to initiate it. Then tried detect features in grids. Namely, decomposite the frame into small grids, and detect orb features in each of the grid. This can somehow ensure distribution. However, not so many useful features are detected.
2. **Good Features to Track** is chosen as an alternative. It is a modified **Harris Corner Detector**. As `goodFeaturesToTrack` doesn't automatically give the descriptors, we need to compute them manually through `orb.compute`.
3. After extracting features, we need to match them between consecutive frames. `cv2.BFMatcher` is the brute force matcher, as usual, we choose `NORM_HAMMING` as match metric. Normally, ratio test is applied along with `knnMatch`, check [Brute-Force Matching with SIFT Descriptors and Ratio Test](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_feature2d/py_matcher/py_matcher.html#brute-force-matching-with-sift-descriptors-and-ratio-test).