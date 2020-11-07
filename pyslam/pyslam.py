import cv2

width = 1920//2
height = 1080//2
display_name = 'SLAM'

class FeatureExtractor(object):
    GX = 16//2
    GY = 12//2
    def __init__(self):
        self.orb = cv2.ORB_create(1000)

    def extract(self, img):
        # run detect in grid
        sy = img.shape[0]//self.GY
        sx = img.shape[1]//self.GX
        akp = []
        for ry in range(0, img.shape[0], sy):
            for rx in range(0, img.shape[1], sx):
                img_chunk = img[ry:ry+sy, rx:rx+sx]
                kp = self.orb.detect(img_chunk, None)
                for p in kp:
                    p.pt = (p.pt[0]+rx, p.pt[1]+ry)
                    akp.append(p)
        return akp
                

fe = FeatureExtractor()
def process_frame(img):
    # load
    img = cv2.resize(img, (width, height))

    # feature ORB
    kp = fe.extract(img)
    print(kp)
    for p in kp:
        u, v = map(lambda x: int(round(x)), p.pt)
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
