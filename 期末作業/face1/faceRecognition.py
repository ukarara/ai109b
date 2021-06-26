# 來源 -- https://blog.gtwang.org/programming/python-opencv-dlib-face-detection-implementation-tutorial/
import dlib
import cv2
import imutils

img = cv2.imread('image.jpg')               # cv2.imread讀取照片圖檔
img = imutils.resize(img, width=1280)       # imutils縮小圖片
detector = dlib.get_frontal_face_detector() # Dlib 的人臉偵測器

# 偵測人臉
face_rects = detector(img, 0)   #無設定score所以只會出現0以上之人臉判定
## print("face_rects=",face_rects)

# 取出所有偵測的結果
for i, d in enumerate(face_rects):
  x1 = d.left()
  y1 = d.top()
  x2 = d.right()
  y2 = d.bottom()


  # 以方框標示偵測的人臉(圖片,左上角,右下角)
  cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 4, cv2.LINE_AA)

# 顯示結果
cv2.imshow("Face Detection", img)

cv2.waitKey(0)              #等待與讀取使用者按下的按鍵,0代表持續等待至使用者按下按鍵
cv2.destroyAllWindows()     #關閉 OpenCV視窗