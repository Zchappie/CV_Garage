import cv2

width = 1920//2
height = 1080//2

def process_frame(img):
    img = cv2.resize(img, (width, height))
    cv2.imshow('SLAM', img)
    cv2.waitKey(1)
    print(img.shape)


if __name__ == "__main__":
    cap = cv2.VideoCapture("test.mp4")
    ret, frames = cap.read()
    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            process_frame(frame)
        else:
            break
