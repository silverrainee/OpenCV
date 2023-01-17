import cv2 as cv

img_gray = cv.imread("./Lenna.jpg", cv.IMREAD_GRAYSCALE)

img_copyed1 = img_gray

print(id(img_gray), id(img_copyed1))  # 주소값이 같음

cv.line(img_gray, (0, 0), (100, 100), 0, 10)

ret, img_copyed1 = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY)

print(id(img_gray), id(img_copyed1))  # 이진화 후 주소값이 다름

cv.imshow("img_gray", img_gray)
cv.imshow("img_copyed1", img_copyed1)

cv.waitKey(0)
