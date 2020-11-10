# PySLAM

## Goody

1. Try `print(dir())`! You won't regret for not having the doc for function calls.

## Display

First time to try PyGame for display purpose. 

1. `screen` object is a canvas with frame to hold everything; the `surface` is like a (separate) paper for drawing
2. `.blit()` is used to copy the contents of one `Surface` to another display like `screen`

## Feature detectors

1. **ORB** is first chosen for speed reason, but the features are not so evenly distributed. Note, `cv2.ORB_create()` instead of `cv2.ORB()` to initiate it. Then tried detect features in grids. Namely, decomposite the frame into small grids, and detect orb features in each of the grid. This can somehow ensure distribution. However, not so many useful features are detected.
2. **Good Features to Track** is chosen as an alternative. It is a modified **Harris Corner Detector**. As `goodFeaturesToTrack` doesn't automatically give the descriptors, we need to compute them manually through `orb.compute`.
3. After extracting features, we need to match them between consecutive frames. `cv2.BFMatcher` is the brute force matcher, as usual, we choose `NORM_HAMMING` as match metric. Normally, ratio test is applied along with `knnMatch`, check [Brute-Force Matching with SIFT Descriptors and Ratio Test](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_feature2d/py_matcher/py_matcher.html#brute-force-matching-with-sift-descriptors-and-ratio-test).
4. Filter the bad matches using RNANSAC and fundamental matrix from `skimage`, works like a charm.
5. Now, switch to essential matrix to mitigate the heavy workload on estimating parameters, and it requires matches from calibrated images. So we need to estimate the intrinsics through the fundamental matrix.