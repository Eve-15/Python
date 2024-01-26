# cv模块
import cv2 as cv
# 建立检测函数
def face_detect_demo(img):
    gary = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    # 调用已训练的分类器(斜杠改为向左划)
    face_detect = cv.CascadeClassifier('C:/Users/Lenovo/Downloads/opencv/sources/data/haarcascades/haarcascade_frontalface_alt2.xml')
    
    face = face_detect.detectMultiScale(gary,1.1,10,0,(140,140),(250,250))
    for x,y,w,h in face:
        cv.rectangle(img,(x,y),(x+w,y+h),color=(0,0,255),thickness=2)
    cv.imshow('result',img)

# 读取摄像头
cap = cv.VideoCapture(0)

# 循环
while True:
    flag,frame = cap.read()
    if not flag:
        break
    face_detect_demo(frame)
    if ord('q') == cv.waitKey(10):
        break
# 释放内存
cv.destroyAllWindows()
# 释放摄像头
cap.release()