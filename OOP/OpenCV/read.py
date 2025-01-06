import cv2 as cv
img = cv.imread('D:\Py_Private\OOP\OpenCV\TFT.png')
# anh goc
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow("TFT", img)
#cv.imshow("gray", gray_img)
# Scaling
cv.waitKey(0)
cv.imwrite('D:\Py_Private\OOP\OpenCV\TFT.png',gray_img)
#