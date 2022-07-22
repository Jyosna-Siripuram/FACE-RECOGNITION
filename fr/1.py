
import cv2
import os

cam = cv2.VideoCapture(0)
i=0
while True:
    isTrue,frame = cam.read()
    dir = f'C:\\Users\\RamyaJyosna\\Desktop\\fr\\New folder\\validation'
    path = os.path.join(dir+'frame'+str(i)+'.jpg')
    cv2.imwrite('frame'+str(i)+'.jpg')
    i+=1
    if cv2.waitKey(0) & 0xFF==ord('d'):
        break
cam.release()
cv2.destroyAllWindows()

