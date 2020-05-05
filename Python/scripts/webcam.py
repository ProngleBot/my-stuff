from cv2 import cv2
video=cv2.VideoCapture(0)

video.release()
check, frame = video.read()
print(check)
print(frame)
cv2.imshow("Capturing")
