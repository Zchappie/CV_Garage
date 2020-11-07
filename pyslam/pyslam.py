import cv2
import numpy as np

width = 1920//2
height = 1080//2
display_name = 'SLAM'

class FeatureExtractor(object):
    def __init__(self):
        self.orb = cv2.ORB_create(200) # num features

    def extract(self, img):
        feats = cv2.goodFeaturesToTrack(np.mean(img, axis=2).astype(np.uint8), 3000, qualityLevel=0.01, minDistance=3)
        return feats

fe = FeatureExtractor()
def process_frame(img):
    # load
    img = cv2.resize(img, (width, height))

    # features
    kp = fe.extract(img)
    print(kp)
    for p in kp:
        u, v = map(lambda x: int(round(x)), p[0])
        cv2.circle(img, (u,v), color=(0,255,0), radius=3)

    # display
    cv2.imshow(display_name, img)
    cv2.waitKey(1)

if __name__ == "__main__":
    cap = cv2.VideoCapture("test.mp4")
    ret, frames = cap.read()
    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            process_frame(frame)
        else:
            break
