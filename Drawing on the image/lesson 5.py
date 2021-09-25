import cv2
import numpy as np

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*"XVID")


while(True):
    ret, frame = cap.read()
    #frame = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    pts=np.array([[20,25] , [26 , 30] , [25 , 20]])
    cv2.polylines(frame,[pts] , True , (150 , 0, 32), 6)
    font = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(frame , "sara",(100 , 200),font,5,(100,200),5)
    cv2.imshow("frame" , frame)
    if cv2.waitKey(1) & 0XFF == ord("x"):
        break

cap.release()

cv2.destroyAllWindows()
