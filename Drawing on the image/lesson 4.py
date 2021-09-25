import cv2
import numpy as np

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*"XVID")


while(True):
    ret, frame = cap.read()
    #frame = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    cv2.line(frame , (100,200),(200,300),(0,0,255) , 10)
    cv2.imshow("frame" , frame)
    if cv2.waitKey(1) & 0XFF == ord("x"):
        break

cap.release()

cv2.destroyAllWindows()
