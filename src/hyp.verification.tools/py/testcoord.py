#!/usr/bin/python
from PIL import Image
import os, sys
import glob
import cv2
from Rectangle import Rectangle
from scipy import misc
import numpy as np
import os.path


filepath = "/Users/juliusskye/COMP4120 Car Detection/car-classifier-research/src/hyp.verification.tools/py/test.png"
if os.path.exists(filepath):
    image = cv2.imread(filepath)
else:
    height = 250
    width = 250
    image = np.zeros((height,width,3), np.uint8)

r1 = Rectangle(0,0,100,100)
r2 = Rectangle(0,100,20,20)
r3 = Rectangle(0,200,20,20)
cv2.rectangle(image, (r1.getLeftXCoord(), r1.getTopYCoord()), (r1.getLeftXCoord()+r1.getWidth(), r1.getTopYCoord()+r1.getHeight()), (0, 255, 0), 1)
cv2.rectangle(image, (r2.getLeftXCoord(), r2.getTopYCoord()), (r2.getLeftXCoord()+r2.getWidth(), r2.getTopYCoord()+r2.getHeight()), (255, 255, 0), 1)
cv2.rectangle(image, (r3.getLeftXCoord(), r3.getTopYCoord()), (r3.getLeftXCoord()+r3.getWidth(), r3.getTopYCoord()+r2.getHeight()), (255, 255, 0), 1)
# cv2.circle(image, (r2.getLeftXCoord(), r2.getTopYCoord()), 5, (255, 0, 0), 1)
# cv2.circle(image, (40, r2.getTopYCoord()), 5, (255, 0, 0), 1)
# cv2.circle(image, (80, r2.getTopYCoord()), 5, (255, 0, 0), 1)


misc.imsave(filepath, image)
f.close()
