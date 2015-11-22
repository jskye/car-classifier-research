__author__ = 'juliusskye'

import os, sys
sys.path.append('..')
from py.Rectangle import Rectangle
from py.CompareRectangles import CompareRectangles

# things = [0,1,2,3,4,5]
# for thing in things:
#
#     if thing>2:
#         print(str(thing) + ' is greater than two')
#         break
#     else: 'no things greater than two'

# det_jaccard_index = 50
# sw_jaccard_index = 100
# print("hypothesis_JI: {0}, slidingwindow_JI: {1}".format(det_jaccard_index, sw_jaccard_index))

# x=[0,0,0,1]
# print(not any(x))


# imageDir = "this.noisy"
# if imageDir[-5:] == "noisy":
# 	noisytest = True
# 	print("noisytest: "+str(noisytest))

import numpy as np
import cv2
import copy

JI_THRESH = 0.35

# r1 = cv2.rectangle((0,0),(100,100))
# r2 = cv2.rectangle((20,20),(40,40))
r1 = (0,0,100,100)
r2 = (20,20,40,40)
r3 = (40,40,80,80)
r4 = (10,10,10,10)
r5 = (20,20,10,10)


detected_objects = []
# print(detected_objects)
detected_objects = [r1,r2,r3,r4,r5]
# detected_objects.append(r1)
# detected_objects.append(r2)
# detected_objects.append(r3)
# detected_objects.append(r4)
# detected_objects.append(r5)
detected_numpy = np.array(detected_objects)
detected_objects_clone = detected_numpy
print(detected_objects_clone)


# get rid of hypotheses that are contained inside others
# because ... there shouldnt be a car within a car...
# detected_objects_clone = copy.copy(detected_objects)
iterations = int(len(detected_objects_clone))-1


for this_index, this_detected_object in enumerate(detected_objects_clone[:-1]):
	# use the opencv returned rectangle and create our own.
	this_detected_rect = Rectangle(this_detected_object[0], this_detected_object[1], this_detected_object[2], this_detected_object[3])

	print("this index (before second loop) is: {0}".format(this_index))

	# compare with those in front of this index.
	for that_index in range((this_index+1), len(detected_objects_clone)):
		# print(detected_objects_clone)
		# print("that index (before we get object) is: {0}".format(that_index))
		if that_index >= len(detected_objects_clone):
			break
		that_detected_object = detected_objects_clone[that_index]
		that_detected_rect = Rectangle(that_detected_object[0], that_detected_object[1], that_detected_object[2], that_detected_object[3])
		# get comparison of this and that rectangle.
		comparison_hypotheses = CompareRectangles(this_detected_rect, that_detected_rect, JI_THRESH)
		# print("this index is: {0}".format(this_index))
		# print("this rect is: {0}".format(this_detected_rect))
		# print("that index is: {0}".format(that_index))
		# print("that rect is: {0}".format(that_detected_rect))
		# if one of them is contained.
		if comparison_hypotheses.is_full_containment():
			# keep the container and remove the contained.
			contained = comparison_hypotheses.rect_fully_contained()
			print("contained is: {0}".format(contained))
			print("this detected rect is: {0}".format(this_detected_rect))
			print("that detected rect is: {0}".format(that_detected_rect))
			# determine which is the contained.
			print(contained == this_detected_rect)
			print(contained == that_detected_rect)

			if contained == this_detected_rect:
				# detected_objects_clone.pop(this_index)
				detected_objects_clone = np.delete(detected_objects_clone, this_index, 0)
				print("this rect is contained. removed this rectangle.")
			elif contained == that_detected_rect:
				# detected_objects_clone.delete(that_index)
				detected_objects_clone = np.delete(detected_objects_clone, that_index, 0)
				print("that rect is contained. removed that rectangle")
			else:
				pass
				if debugging:
					print("hypothese not contained")

# set resultant clone as the new list with contained hypotheses removed.
detected_objects = detected_objects_clone
print(detected_objects_clone)
