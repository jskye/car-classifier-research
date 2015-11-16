# USAGE
# python click_and_crop.py --image jurassic_park_kitchen.jpg

# import the necessary packages
import argparse
import cv2
import glob
# from gi.repository import Gtk


# initialize the list of reference points and boolean indicating
# whether cropping is being performed or not
refPt = []
cropping = False
outputimageFile = "labels.txt"
imgcounter = 0
roicounter = 0
lastroi = ""
lastImage = None

def click_and_crop(event, x, y, flags, param):
	# grab references to the global variables
	global refPt, cropping, imgcounter, roicounter, lastroi, lastImage
	# if the left mouse button was clicked, record the starting
	# (x, y) coordinates and indicate that cropping is being
	# performed
	if event == cv2.EVENT_LBUTTONDOWN:
		#keep copy of current Image in case roi drawn wrong
		lastImage = image.copy()
		refPt = [(x, y)]
		cropping = True
		# write last roi to file. (assumes that a new roi means last was good)
		with open(outputimageFile, 'a') as results:
			results.write(lastroi)
			lastroi = ""

	# check to see if the left mouse button was released
	elif event == cv2.EVENT_LBUTTONUP:
		# increment roicounter
		roicounter+=1
		# record the ending (x, y) coordinates and indicate that
		# the cropping operation is finished
		refPt.append((x, y))
		cropping = False

		# draw a rectangle around the region of interest
		cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
		cv2.imshow("image", image)
		print(globalimageFile)
		print("imgcounter: "+str(imgcounter))
		print("roicounter: "+str(roicounter))
		# with open(outputimageFile, 'a') as results:
		# 	if roicounter>1:
		# 		# print("writingtab")
		# 		results.write("\t")
		# 	results.write(str(refPt[0][0]) + " " \
		# 	+ str(refPt[0][1]) + " " \
		# 	+ str(refPt[1][0] - refPt[0][0]) + " " \
		# 	+ str(refPt[1][1] - refPt[0][1]))
		# results.close()
		if roicounter>1:
			lastroi+="\t"
		lastroi+=str(refPt[0][0]) + " "
		lastroi+=str(refPt[0][1]) + " "
		lastroi+=str(refPt[1][0] - refPt[0][0]) + " "
		lastroi+=str(refPt[1][1] - refPt[0][1])

# construct the argument parser and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True, help="Path to the image")
# args = vars(ap.parse_args())

imageFiles=sorted(glob.glob("*.jpg"))
for imageFile in imageFiles:
	imgcounter+=1
	roicounter = 0
	globalimageFile = imageFile
	with open(outputimageFile, 'a') as results:
		if imgcounter>1:
			results.write("\n")
		results.write(globalimageFile + " "+str(imgcounter) + " ")
	results.close()
	# load the image, originalImage it, and setup the mouse callback function
	# image = cv2.imread(args["image"])
	image = cv2.imread(imageFile)
	originalImage = image.copy()
	cv2.namedWindow("image")
	cv2.setMouseCallback("image", click_and_crop)

	# keep looping until the 'q' key is pressed
	while True:
		# display the image and wait for a keypress
		cv2.imshow("image", image)
		key = cv2.waitKey(1) & 0xFF

		# if the 'o' key is pressed, reset the image
		# if key == ord("o"):
		# 	# restore to original copy
		# 	image = originalImage.copy()
		# 	# delete last roi
		# 	lastroi = ""
		# if the 'r' key is pressed, reset the image to last copy lastroi
		if key == ord("r"):
			#TODO: remove last line of output file.
			# copy image after every Rectangle
			# restore to last copy
			image = lastImage.copy()
			cv2.imshow("image", image)
			# delete last roi
			lastroi = ""
		# if the 'c' key is pressed, break from the loop
		elif key == ord("c"):
			# write last roi to file. (assumes that a new roi means last was good)
			with open(outputimageFile, 'a') as results:
				results.write(lastroi)
				lastroi = ""
			break
		elif key == ord("q"):
			#TODO: warn user quitting without a roi on an Image
			# can use GTK crossplatform dialog
			# http://python-gtk-3-tutorial.readthedocs.org/en/latest/dialogs.html
			exit()

	# # if there are two reference points, then crop the region of interest
	# # from teh image and display it
	# if len(refPt) == 2:
	# 	roi = originalImage[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
	# 	cv2.imshow("ROI", roi)
	# 	cv2.waitKey(0)

	# close all open windows
	cv2.destroyAllWindows()
