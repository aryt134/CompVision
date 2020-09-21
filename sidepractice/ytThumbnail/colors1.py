
def color_choice(color):

	color_tuple = (0,0,0)

	if color == "ba":
		color_tuple = (0,0,0)
	elif color == "w":
		color_tuple = (255,255,255)
	elif color == "r":
		color_tuple = (0,0,255)
	elif color == "bu":
		color_tuple = (255,0,0)
	elif color == "g":
		color_tuple = (0,255,0) 
	elif color == "y":
		color_tuple = (0,255,255)
	elif color == "pu":
		color_tuple = (102,0,102)
	elif color == "pi":
		color_tuple = (153,51,255)
	
	return color_tuple