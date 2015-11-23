#!/usr/bin/python
# -*- coding: utf-8 -*-
###############################################################################
# Copyright (c) 2015, Julius Sky
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
###############################################################################


'''
File: detect.py
Author: julius.skye@gmail.com
Date: 1.05.2015
File Description:
This program uses opencv's cascade function: detectMuliScale
to perfom detection with a given detector on a given image.
The image can be preprocessed for diff color spaces:
grayscale, YUV, HSV, HLS, CIELAB, CIELUV
Note: by default, im.read outputs in BGR order not RGB

For more info about convesion algorithms see:
http://docs.opencv.org/master/de/d25/
imgproc_color_conversions.html#color_convert_rgb_hls

For good default values see:
http://www.searchalleasy.com/q/20801015/2589776
    Means checking scales 10percent of size increments
    scaleFactor=1.1
    Higher value results in less detections but with higher quality
    minNeighbors=5

    minSize=(30, 30)
    flags = cv2.cv.CV_HAAR_SCALE_IMAGE

    maxSize by default assumed size of image but can be set.

    use like this:

    python cardetect.py image/path/image.extension cascade/path/cascade.xml colorspace

'''

import cv2
import sys

# Get user supplied values
if len(sys.argv) == 4:
    imagePath = sys.argv[1]
    cascPath = sys.argv[2]
    colorspace = sys.argv[3]
elif len(sys.argv) == 3:
    imagePath = sys.argv[1]
    cascPath = sys.argv[2]
    colorspace = "rgb"
else:
    print("check arguments!")


# Create the haar cascade
trainedCascade = cv2.CascadeClassifier(cascPath)



# Read the image
image = cv2.imread(imagePath)

# convert to grayscale (default algorithm)
if colorspace == "gray":
    colorCVT = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
elif colorspace == "hsv":
    colorCVT = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
elif colorspace == "hls":
    colorCVT = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)
elif colorspace == "lab":
    colorCVT = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
elif colorspace == "luv":
    colorCVT = cv2.cvtColor(image, cv2.COLOR_BGR2LUV)
elif colorspace == "yuv":
    colorCVT = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
else:
    colorCVT = image

print('using color mode: '+colorspace)

with open('Output.txt', 'w') as text_file:
    text_file.write("Purchase Amount: {0}".format(colorspace))
text_file.close()

# training PARAMS
SCALE_FACTOR = 1.02
MIN_NEIGHBORS = 1
MIN_SIZE = (10,10)
MAX_SIZE = (100,100)

# Detect objects in the image
objects = trainedCascade.detectMultiScale(
    colorCVT,
    scaleFactor=SCALE_FACTOR,
    minNeighbors=MIN_NEIGHBORS,
    minSize=MIN_SIZE,
    maxSize=MAX_SIZE,
    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
)



print "Found {0} objects!".format(len(objects))

# Draw a rectangle around the faces
for (x, y, w, h) in objects:
    #cv2.rectangle(colorCVT, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)


#cv2.imshow("Found {0} objects!".format(len(objects)), colorCVT)
cv2.imshow("Found {0} objects!".format(len(objects)), colorCVT)

cv2.waitKey(0)
