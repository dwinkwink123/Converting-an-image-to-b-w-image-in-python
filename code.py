import cv2

image_color = cv2.imread("butterfly.png",cv2.IMREAD_GRAYSCALE)

thres=128

img_bw=cv2.threshold(image_color,thres,255,cv2.THRESH_BINARY)[1]

cv2.imwrite("bw.png",img_bw)


