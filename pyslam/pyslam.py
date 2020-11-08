import cv2
import numpy as np
from display import Display
from extractor import Extractor

width = 1920//2
height = 1080//2
# display_name = 'SLAM'
disp = Display(width, height)
fe = Extractor()

def process_frame(img):
    img = cv2.resize(img, (width, height))
    matches = fe.extract(img)

    print("%d matches" % (len(matches)))

    def denoramlize(pt):
        return int(round(pt[0]+img.shape[0]/2)), int(round(pt[1]+img.shape[1]/2))

    for pt1, pt2 in matches:
        # de-normailze coords
        u1, v1 = denoramlize(pt1)
        u2, v2 = denoramlize(pt2)
        cv2.circle(img, (u1,v1), color=(0,255,0), radius=3)
        cv2.line(img, (u1,v1), (u2,v2), color=(255,0,0))
        
    # display
    # cv2.imshow(display_name, img)
    # cv2.waitKey(1)
    disp.paint(img)

if __name__ == "__main__":
    cap = cv2.VideoCapture("test.mp4")
    ret, frames = cap.read()
    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            process_frame(frame)
        else:
            break
