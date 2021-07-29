import cv2
video = cv2.VideoCapture('video2.mp4')

while video.isOpened():
    ret, frame1 = video.read()
    if ret:
        gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
        canny = cv2.Canny(frame1, 125,175)
        contours, _ = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            (x, y, w, h) = cv2.boundingRect(contour)
            if cv2.contourArea(contour) < 800:
                continue
            cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 0)

        cv2.imshow("Video", frame1)
    else:
        break

    if cv2.waitKey(40) == 27:
        break
