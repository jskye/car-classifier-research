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

'''

import cv2
import sys

# Get user supplied values
imagePath = sys.argv[1]
cascPath = sys.argv[2]
colorspace = sys.argv[3]

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
    colorCVT = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)
elif colorspace == "luv":
    colorCVT = cv2.cvtColor(image, cv2.COLOR_BGR2Luv)
elif colorspace == "luv":
    colorCVT = cv2.cvtColor(image, cv2.COLOR_BGR2Luv)
elif colorspace == "yuv":
    colorCVT = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
else:
    colorCVT = None

# if using rgb space, dont pass conversion param
if colorCVT is None:
    objects = trainedCascade.detectMultiScale(
    # Detect objects in the image
        scaleFactor=1.05,
        minNeighbors=4,
        minSize=(30, 30),
        flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    )
# otherwise pass colorCVT
else:
    # Detect objects in the image
    objects = trainedCascade.detectMultiScale(
        colorCVT,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    )



print "Found {0} objects!".format(len(objects))

# Draw a rectangle around the faces
for (x, y, w, h) in objects:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Objects found", image)
cv2.waitKey(0)
