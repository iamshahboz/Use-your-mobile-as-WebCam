#import needed libraries
import requests 
import cv2
import numpy as np
import imutils

#Replace url with your own[download ip webcam and start server]
url = 'http://192.168.43.240:8080/shot.jpg'

while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr,-1)
    img = imutils.resize(img, width=1000, height=1800)
    cv2.imshow("Sony_cam", img)

    #press Esc to exit
    if cv2.waitKey(1)== 27:
        break

cv2.destroyAllWindows()
