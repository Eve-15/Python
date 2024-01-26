# 导入cv模块
import cv2 as cv
# 摄像头
cap = cv.VideoCapture(0)
flag = 1
num = 1

# 录入信息
while(cap.isOpened()):  # 检测是否在开启状态
    ret_flag,Vshow = cap.read()  # 得到每帧图像
    cv.imshow("Capture_test",Vshow)  # 显示图像
    k = cv.waitKey(1) & 0xFF  # 按键判断
    if k ==ord('s'):  # 保存
        cv.imwrite("D:\\python\\03shibie\\data\\"+str(num)+".name"+".jpg",Vshow)# 注意此处路径名必须全英文
        print("success to save"+str(num)+".jpg")
        print('--------------------成功采集-------------------')
        num += 1
    elif k == ord('q'):  # 退出
        break
# 释放摄像头
cap.release
# 释放内存
cv.destroyAllWindows()