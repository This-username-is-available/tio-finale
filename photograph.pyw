import cv2
from datetime import datetime
import time

for i in range(10):
    cap = cv2.VideoCapture(0)  # 打开摄像头
    t = datetime.utcnow().strftime("%Y%m%d%H%M%S%f")[:-3]
    ret, frame = cap.read()
    cv2.imwrite("D:/" + t + ".png", frame)  # 保存路径
    cap.release()
    cv2.destroyAllWindows()
    time.sleep(0.1)
