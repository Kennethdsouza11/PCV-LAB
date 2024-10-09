import cv2

cap = cv2.VideoCapture('PCV-LAB\Basic_Operations\sample_video.mp4')

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        cv2.imshow('Video',frame)
        if cv2.waitKey(0) == ord('q'):
            break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()