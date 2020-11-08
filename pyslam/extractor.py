import cv2
import numpy as np
# from skimage.feature import match_descriptors, ORB, plot_matches
from skimage.measure import ransac
from skimage.transform import FundamentalMatrixTransform

class Extractor(object):
    def __init__(self):
        self.orb = cv2.ORB_create() # num features
        self.bf = cv2.BFMatcher(cv2.NORM_HAMMING) # brute force match
        self.last = None

    def extract(self, img):
        # detection
        feats = cv2.goodFeaturesToTrack(np.mean(img, axis=2).astype(np.uint8), 3000, qualityLevel=0.01, minDistance=3)
        
        # extraction
        kps = [cv2.KeyPoint(x=f[0][0], y=f[0][1], _size=20) for f in feats]
        kps, des = self.orb.compute(img, kps)

        # matching
        ret = []
        if self.last is not None:
            matches = self.bf.knnMatch(des, self.last['des'], k=2) # returns 2 best matches
            # keep significant matches by ration test
            for m, n in matches:
                if m.distance < 0.75*n.distance:
                    kp1 = kps[m.queryIdx].pt
                    kp2 = self.last['kps'][m.trainIdx].pt
                    ret.append((kp1, kp2))
        if len(ret) > 0:
            ret = np.array(ret)
            # filtering the bad matches, use the ransac and fundamental mat
            model, inliers = ransac((ret[:, 0] , ret[:, 1]),
                        FundamentalMatrixTransform, min_samples=8,
                        residual_threshold=0.01, max_trials=100)

            print(sum(inliers))

        # return
        self.last = {'kps':kps, 'des':des}
        return ret