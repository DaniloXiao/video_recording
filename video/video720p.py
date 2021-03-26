#-*- coding:utf-8 -*-
# author:danio
# datetime:2021/3/14 下午4:57
# software: PyCharm
import cv2
from datetime import datetime
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('M', 'J', 'P', 'G'))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (1280, 720))
start_time = datetime.now()
while True:
    ret, frame = cap.read()
    out.write(frame) 
    cv2.imshow("test", frame)
    if (datetime.now() - start_time).seconds == 5:
        cap.release()
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
cv2.destroyAllWindows()

