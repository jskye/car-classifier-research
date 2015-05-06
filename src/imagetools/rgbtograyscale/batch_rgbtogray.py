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
File: rgbtogray_intensity.py
Author: julius.skye@gmail.com
Date: 1.05.2015
File Description:
This program converts all images in current dir
from rgb color space to grayscale.



TODO: Methods
    # @param = 0      Intensity
    # @param = 1      Luma

# dependencies
sudo apt-get install python-pip python-dev build-essential
sudo pip install numpy
sudo apt-get install libatlas-base-dev gfortran
# scipy
sudo pip install scipy
sudo pip install matplotlib
sudo pip install -U scikit-learn # optional, recommended
'''

import glob
from scipy import misc
import numpy as np
import matplotlib.pyplot as plt # import
import matplotlib.cm as cm


# image = misc.imread('bananas.jpg')
# # print image.shape
# # plt.imshow(image) #load
# # plt.show()  # show the window

def average(pixel):
    return (pixel[0] + pixel[1] + pixel[2]) / 3
    #return np.average(pixel)

def weightedAverage(pixel):
    return 0.299*pixel[0] + 0.587*pixel[1] + 0.114*pixel[2]


# # do conversion

import sys

# get argument list using sys module

# def main(argv):
#
    # method = argv[0]
    # print method

files = glob.glob('*.jpg')
for file in files:
    file = open(file)
    filename = file.name
    image = misc.imread(filename)
    grey = np.zeros((image.shape[0], image.shape[1])) # init 2D numpy array
    # get row number
    rownum = 0
    colnum = 0
    for rownum in range(len(image)):
       for colnum in range(len(image[rownum])):
        #    if(method ==0):
        #         grey[rownum][colnum] = average(image[rownum][colnum])
        #    elif(method==1):
                grey[rownum][colnum] = weightedAverage(image[rownum][colnum])

    # plt.imshow(grey, cmap = cm.Greys_r)
    # plt.show()
    # if(method ==0):
        # misc.imsave(filename+'-gray_intensity.jpg', grey)
    # elif(method ==1):
    misc.imsave(filename+'-gray_luma.jpg', grey)
    #file.close()


# if __name__ == "__main__":
#    main(sys.argv[1:])
