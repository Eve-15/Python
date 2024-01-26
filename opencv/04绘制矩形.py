# cv模块
import cv2 as cv
# 读取图像
img = cv.imread('D:\\python\\opencv\\face2.jpg')
# 坐标
x,y,w,h = 100,100,100,100
# 绘制矩形
cv.rectangle(img,(x,y,x+w,y+h),color=(0,0,255),thickness=1)
#绘制圆形
cv.circle(img,center=(x+w,y+h),radius=100,color=(255,0,0),thickness=2)
#显示
cv.imshow('Image', img)
while True:
    if ord('q') == cv.waitKey(0):
        break
# 等待
cv.waitKey(0)
# 释放内存
cv.destroyAllWindows()