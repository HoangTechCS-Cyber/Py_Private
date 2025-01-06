import cv2 as cv    

img = cv.imread("D:\Py_Private\OOP\OpenCV\HITOD_2024.jpg")

# thay doi kich thuoc
resize_img = cv.resize(img, (300, 300))

# cat anh 

crop_img = img[50:200, 100:300] # cat tu toa do (100, 50) den (300, 200)

cv.imshow("resize", resize_img)
cv.imshow("crop", crop_img)
cv.waitKey(0)

# 