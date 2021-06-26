import dlib
import cv2
import imutils

img = cv2.imread('image3.jpg')                   #讀取圖片
img = imutils.resize(img, width=1280)           #imutils縮放圖片
detector = dlib.get_frontal_face_detector()     #dlib獲取人臉資料進行偵測

# 偵測人臉，輸出分數
face_rects, scores, idx = detector.run(img, 0, -1) # 超過 -1 分的人臉都算 ,無標示則會默認為0 

for i, d in enumerate(face_rects):    #取出所有偵測的結果
  x1 = d.left()
  y1 = d.top()
  x2 = d.right()
  y2 = d.bottom()
  text = "%2.2f(%d)" % (scores[i], idx[i])

  cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 4, cv2.LINE_AA)   ##標出人臉

  # 標示分數
  # cv2.putText(影像, 文字, 座標, 字型, 大小, 顏色, 線條寬度, 線條種類)
  cv2.putText(img, text, (x1, y1), cv2.FONT_HERSHEY_DUPLEX,
          0.7, (255, 255, 255), 1, cv2.LINE_AA)

cv2.imshow("Face Detection", img)

cv2.waitKey(0)
cv2.destroyAllWindows()