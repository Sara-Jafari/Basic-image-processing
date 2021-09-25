import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while(1):
    _,frame = cap.read()
    hsv =  cv2.cvtColor(frame , cv2.COLOR_BGR2HSV)
    lower_red=np.array([50,20,50])
    upper_red=np.array([255,255,255])
    mask = cv2.inRange(hsv  ,  lower_red,upper_red)
    mask =cv2.bitwise_not(mask)
    res = cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow("frame1", frame)
    cv2.imshow("frame2", mask)
    cv2.imshow("frame3", res)
    if cv2.waitKey(5) & 0XFF==27:
        break



cv2.destroyAllWindows()
cap.release()
