import cv2 as cv

# 加载训练数据集文件
recognizer = cv.face.LBPHFaceRecognizer_create()
recognizer.read('D:\\python\\03shibie\\data\\trainer.yml')

# 创建人脸级联分类器
face_detector = cv.CascadeClassifier('C:/Users/Lenovo/Downloads/opencv/sources/data/haarcascades/haarcascade_frontalface_alt2.xml')

# 打开摄像头
cap = cv.VideoCapture(0)

while True:
    # 读取视频帧
    ret, frame = cap.read()
    
    if not ret:
        break
    
    # 转换为灰度图像
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    # 人脸检测
    faces = face_detector.detectMultiScale(gray)
    
    for (x, y, w, h) in faces:
        # cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        # 进行人脸识别
        id, confidence = recognizer.predict(gray[y:y+h, x:x+w])
        # print('标签id:', id, '置信评分:', confidence)
        
        if confidence > 80:
            cv.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
            cv.putText(frame, 'It is NOT U', (x+10, y-10), cv.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 1)
        else:
            cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv.putText(frame, 'It is U', (x+10, y-10), cv.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1)
    # 显示结果
    cv.imshow('result', frame)
    
    # 按下 'q' 键退出循环
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# 释放资源
cap.release()
cv.destroyAllWindows()