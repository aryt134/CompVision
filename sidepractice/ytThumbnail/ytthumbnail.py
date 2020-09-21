
import cv2
import sys
import colors

#youtube thumbnail resizer

imgaes = sys.argv[1:]

for a in imgaes:

	print(a)

	img  = cv2.imread(str(a))

	imgResize = cv2.resize(img, (1280,720))  #width, height

	bw = input("Make the thumbnail Black and White (y/n)?")

	if bw == 'y':
		imgResize = cv2.cvtColor(imgResize, cv2.COLOR_BGR2GRAY)

	wording = input("Wording on the image (y/n)?")

	if wording == 'y':
		text = input("Type the text ")
		text_color = input("What color text? ba - black / w - white / r - red / bu - blue / g - green / y - yellow / pu - purple / pi - pink")
		#call the color tuple
		color_tuple = colors.color_choice(text_color)
		length_text = 1280 - (30*int(len(text)/2))

		cv2.putText(imgResize, text, (int(length_text/2),int(720/2)), cv2.FONT_HERSHEY_COMPLEX,1,color_tuple,2) #w, h, last one is thickness


	cv2.imwrite("resize" + str(a), imgResize)



