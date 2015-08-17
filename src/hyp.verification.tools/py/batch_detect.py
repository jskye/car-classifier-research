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
from __future__ import division
import os
import glob
import cv2
import sys
from scipy import misc
from PIL import Image


# Get user supplied values
if len(sys.argv) == 6:
    cwd = sys.argv[0][:-3]
    imageDir = sys.argv[1]
    cascadePath = sys.argv[2]
    labelPath = sys.argv[3]
    colorspace = sys.argv[4]
    min_neighbors = sys.argv[5]
# elif len(sys.argv) == 3:
#     imageDir = sys.argv[1]
#     cascadePath = sys.argv[2]
#     colorspace = "rgb"
else:
    print("check arguments!")



# initiate variables
tot_true_positives = 0
tot_false_positives = 0
tot_false_neg = 0

testset = os.path.basename(imageDir[:-1])
# cwd = os.path.dirname(os.path.realpath(cascadePath))
testPath = "/Users/juliusskye/Desktop/COMP.VISION/final.tests/final_testing/final.results/"
labelName = os.path.basename(labelPath)

print("current working dir: "+testPath)
cascadePathMinusEx = cascadePath[:-4]
cascadeName = os.path.basename(cascadePath)
cascadeNameMinusEx = cascadeName[:-4]

print("using cascade: "+cascadeNameMinusEx+": "+cascadePathMinusEx)
outputFilename=testset+"."+cascadeNameMinusEx+'_'+colorspace+"MN"+min_neighbors+'_'+'output.txt'


print("reading labelled rectangles from: ")
labelled_rectangles = {}
with open(testPath+labelName, "r") as rects:
# with open("testset_rgb_100.txt", "r") as rects:
    for rect in rects:
      labelled_rectangles[rect.split()[0]] = [rect.split()[1:][i:i+4]
      for i in range(0, len(rect.split()[1:]), 4)]
# print labelled_rectangles[0]

total_labelled_objects = len(labelled_rectangles)
print("total labelled objects: "+str(total_labelled_objects))


# load the trained cascade
print("loading classifier...")
trainedCascade = cv2.CascadeClassifier(cascadePath)
total_objects_detected = 0
print("writing to output file: "+outputFilename)
with open(outputFilename, 'w') as results:
    results.write("*********************************\n")
    results.write("Batch Detection results \n")
    results.write("*********************************\n")
results.close()

# for imagePath in imageDir:
imageNum=0
images = glob.glob(imageDir+'*.jpg')
for imagePath in images:
    img_true_positives=0
    img_false_positives=0
    img_false_neg =0
    imageName = os.path.basename(imagePath)
    print("loading image for detection: "+imageName +", image number {0}".format(imageNum))
    if imageNum<len(images):
        imageNum =imageNum+1
    else: break

    # Read the image
    image = cv2.imread(imagePath)

    print("labelname"+labelName)

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
    elif colorspace =="rgb":
        colorCVT = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        colorCVT = image

    print("using testset: " +testset)

    print('using color mode: '+colorspace)

    with open(outputFilename, 'a') as results:
        results.write("Running detection on image:  "+imagePath +"\n")
        results.write("Detecting using trained classifier: "+cascadePath +"\n")
    # results.close()


    # training PARAMS
    SCALE_FACTOR = 1.02
    MIN_NEIGHBORS = int(min_neighbors)
    MIN_SIZE = (10,10)
    MAX_SIZE = (128,128)

    # Detect objects in the image
    objects = trainedCascade.detectMultiScale(
        colorCVT,
        scaleFactor=SCALE_FACTOR,
        minNeighbors=MIN_NEIGHBORS,
        minSize=MIN_SIZE,
        maxSize=MAX_SIZE,
        flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    )


    # if we were in grayspace we want to convert back to rgb so we have green detection windows
    # (cos blacks hard to see on bw img)
    if colorspace == 'gray':
        colorCVT = cv2.cvtColor(colorCVT, cv2.COLOR_GRAY2BGR)
    #     # rgbimg = Image.new("RGBA", (colorCVT.width, colorCVT.height))
    #     # rgbimg.paste(colorCVT)
    #     # colorCVT = rgbimg

    expectedObjects=0


    #draw the labelled rectangles
    # print('imageNum: '+imageNum)
    for labRect in labelled_rectangles[str(imageNum)]:
        expectedObjects=+1
        x = int(labRect[0])
        y = int(labRect[1])
        w = int(labRect[2])
        h = int(labRect[3])
        print("printing rectangle: {0}: ({1},{2},{3},{4})".format(imageNum,x,y,w,h))

        if colorspace =='lab' or 'luv':
            groundColor = (0, 0, 255)
        else:
            groundColor = (255, 0, 0)

        cv2.rectangle(colorCVT, (x, y), (x+w, y+h), groundColor, 1)


    # Draw detected objects
    for (detx, dety, detectedWidth, detectedHeight) in objects:


        cv2.rectangle(colorCVT, (detx, dety), (detx+detectedWidth, dety+detectedHeight), (0, 255, 0), 2)
        detectedArea = detectedWidth*detectedHeight
        for trueRect in labelled_rectangles[str(imageNum)]:
            truex = int(trueRect[0])
            truey = int(trueRect[1])
            trueWidth = int(trueRect[2])
            trueHeight = int(trueRect[3])
            trueArea = trueWidth*trueHeight
            #check if detected rectangle is considered TP or FP

            # use simple_compare_rects to comapre similarity of true and detected rectangles
            # to determine true or false positive
            # TODO: move to function
            # TODO: replace with jaccard index
            #   this method has flaws where some dissimilar rectangles are marked as TP

            # if detected.area smaller than true.area but still bigger than half,
            # and side lengths are within 50% of eachother then rects are similar.
            # OR
            # if true.area smaller than detected.area  but still bigger than half,
            # and side lengths are within 50% of eachother then rects are similar.
            A = (detectedArea < trueArea)
            B = (detectedArea > 0.5*trueArea)
            C = (detectedWidth<2*trueWidth)
            D = (detectedWidth>0.5*trueWidth)
            E = (detectedHeight<2*trueHeight)
            F = (detectedHeight>0.5*trueHeight)

            G = (trueArea < detectedArea)
            H = (trueArea > 0.5*detectedArea)
            I = (detectedWidth<2*trueWidth)
            J = (detectedWidth>0.5*trueWidth)
            K = (detectedHeight<2*trueHeight)
            L = (detectedHeight>0.5*trueHeight)

            if (A and B and C and D and E and F) or (G and H and I and J and K and L ):
                img_true_positives +=1
            else: img_false_positives +=1

    # increment false negatives
    if expectedObjects>0 and len(objects)<1:
        img_false_neg = expectedObjects - img_true_positives
        tot_false_neg+=img_false_neg

    tot_true_positives +=img_true_positives
    tot_false_positives += img_false_positives

    print("TP:{0}, FP: {1}, FN: {2}".format(img_true_positives, img_false_positives, img_false_neg), colorCVT)


    # append to end of file
    with open(outputFilename, 'a') as results:
        results.write("TP:{0}, FP: {1}, FN: {2}".format(img_true_positives, img_false_positives, img_false_neg))
        results.write("\n")
    results.close()




    # create directory to save results
    resultsDir = testPath+"results."+testset+"."+cascadeNameMinusEx+"."+colorspace+"MN"+min_neighbors
    if not os.path.isdir(resultsDir):
        os.makedirs(resultsDir)

    # save image with detections drawn on
    outputDir = cascadePathMinusEx
    # misc.imsave(cwd+'/'+outputDir+'/detected_'+imagePath, colorCVT)
    misc.imsave(resultsDir+'/detected_'+imageName, colorCVT)

    #increment total detected objects
    total_objects_detected = total_objects_detected+len(objects)



# print("Total objects detected: {0}".format(len(objects)))
with open(outputFilename, 'a') as results:
    results.write("Total labelled objects: {0}".format(total_labelled_objects))
    results.write("Total objects detected: {0}".format(total_objects_detected))
    results.write("\n")
    results.write("Total TP:{0}, Total FP: {1}, Total FN: {2}".format(tot_true_positives, tot_false_positives, tot_false_neg))
    results.write("\n")

    if total_labelled_objects != 0:
        # true positive rate (sensitivity/hitrate/recall)
        tpr = tot_true_positives/total_labelled_objects
        # fall-out or false positive rate (FPR)
        fpr = tot_false_positives/total_labelled_objects
    else:
        tpr = 0
        fpr = 0
    results.write("Total TPR:{0}, Total FPR: {1}".format(tpr, fpr))
    results.write("\n")
    #Precision or positive predictive value (PPV) ­ Calculated using PPV = TPR/FPR.
    # ppv = tpr/fpr

    # precision is the number of correct positive results divided by the number of all positive results
    # recall is the number of correct positive results divided by the number of positive results that should have been returned.

    delta = 0.0001
    precision = tot_true_positives/(tot_true_positives+tot_false_positives+delta)
    recall = tot_true_positives/ (tot_true_positives + tot_false_neg+delta)
    #harmonic mean = 2 ((precisin x recall)/(precision + recall))
    harmonic_mean = ((precision*recall) / (precision+recall+delta))*2

    results.write("Precision: {0}".format(precision))
    results.write("Recall: {0}".format(recall))
    results.write("Harmonic Mean: {0}".format(harmonic_mean))

    results.write("\n")
results.close()

# print('total objects deteced: '+total_objects_detected)


    # cv2.imshow("Found {0} objects!".format(len(objects)), colorCVT)
    # cv2.waitKey(0)
