import cv2
import numpy as np

img = cv2.imread("rscrs/bosscat.jpg")
kernel = np.ones((5,5), np.uint8) #5 by 5 matrix

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)
imgCanny = cv2.Canny(img, 100, 100)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=5)
imgEroded = cv2.erode(imgDialation, kernel, iterations=10)

while True:
	# cv2.imshow("Gray Image", imgGray)
	# cv2.imshow("Blur Image", imgBlur)
	cv2.imshow("Canny Image", imgCanny)
	cv2.imshow("Dilation Image", imgDialation)
	cv2.imshow("Eroded Image", imgEroded)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break


# cv2.waitKey(0)

# cv2.imshow("Boss Cat", img) #window name, image 
# cv2.waitKey(0) #0 is infinite delay, value is mile

# cap = cv2.VideoCapture("rscrs/Aerial Shot Of Sunset.mp4")

# cap = cv2.VideoCapture(0)
# cap.set(3,640)#width
# cap.set(4,480)#height
# cap.set(10,0) #brihgtness


# while True:
# 	success, img1 = cap.read()
# 	cv2.imshow("Video", img1)
# 	if cv2.waitKey(1) & 0xFF == ord('q'):
# 		break