# cv模块
import cv2 as cv
# 建立检测函数
def face_detect_demo():
    gary = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    # 调用已训练的分类器(斜杠改为向左划)
    face_detect = cv.CascadeClassifier('C:/Users/Lenovo/Downloads/opencv/sources/data/haarcascades/haarcascade_frontalface_alt2.xml')
    
    face = face_detect.detectMultiScale(gary,1.1,5,0,(100,100),(300,300))
    for x,y,w,h in face:
        cv.rectangle(img,(x,y),(x+w,y+h),color=(0,0,255),thickness=2)
    cv.imshow('result',img)

# 读取图像
img = cv.imread('D:\\python\\opencv\\Curry.jpg')
# 检测函数
face_detect_demo()


# 显示图像
#cv.imshow('Image', img)
while True:
    if ord('q') == cv.waitKey(0):
        break
# 等待
cv.waitKey(0)
# 释放内存
cv.destroyAllWindows()