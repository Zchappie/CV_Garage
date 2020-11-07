import cv2

width = 1920//2
height = 1080//2
display_name = 'SLAM'
orb = cv2.ORB_create()

def process_frame(img):
    # load
    img = cv2.resize(img, (width, height))

    # feature ORB
    kp, des = orb.detectAndCompute(img, None)
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
