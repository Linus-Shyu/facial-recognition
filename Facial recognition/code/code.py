#导入cv2
import cv2
#导入人脸识别的模块
import face_recognition
#读取照片
img=cv2.imread('face/face7.jpg')
#获取人脸位置
locations=face_recognition.face_locations(img)
#连续标记人脸位置
for top,right,bottom,left in locations:
    cv2.rectangle(img,(left,top),(right,bottom),(0,255,0),2)
#展示图片
cv2.imshow('Window',img)
#等待键盘时间
cv2.waitKey(0)
#释放窗口
cv2.destroyAllWindows
