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

"""
File: rgbtograygleam.py
Author: julius.skye@gmail.com
Date: 1.05.2015
File Description:
This program converts images from rgb color space to grayscale with
pixel intensity calculated using gammar correction function tau.

"""

import sys
import os
import glob
import numpy as np
from PIL import Image

# path = os.path.dirname(os.path.realpath(__file__))
# path = path +'/*.ppm'

def tau_gamma_correct(pixel_channel):
    pixel_channel = (pixel_channel/255)**(1/2.2)*255
    return pixel_channel

#@param: rgb
#@result: returns grayscale value
def gleam(rgb):
    #convert rgb tuple to list
    rgblist = list(rgb)
    #gamma correct each rgb channel
    rgblist[0] = tau_gamma_correct(rgblist[0])
    print('gleamed red ' + str(rgblist[0]))
    rgblist[1] = tau_gamma_correct(rgblist[1])
    print('gleamed green ' + str(rgblist[1]))
    rgblist[2] = tau_gamma_correct(rgblist[2])
    print('gleamed blue ' + str(rgblist[2]))
    grayscale = (rgblist[0] + rgblist[1] + rgblist[2])/3
    print('grayscale '+ str(grayscale))
    return grayscale

def printimg(img):
    pix = img.load()
    (width,height) = img.size
    for x in range(0, width-1):
        for y in range(0, height-1):
            if(x==width-1 and y==height-1):
                break
            print('pixel: ('+str(x)+', '+str(y)+')')
            rgb = pix[x,y]
            print('current pixel value: '+str(rgb))
            break


# get a glob list of jpg filenames
files = glob.glob('*.jpg')
for file in files:
    file = open(file)
    filename = file.name
    image = Image.open(file)
    width, height = image.size
    pix = image.load()
    #new_img = Image.new('L', image.size)
    new_pixel_data = np.zeros((width,height), dtype=np.uint8)
    #new_pixel_data = np.array(range(width*height)).reshape((width, height))
    print(width,height)
    for x in range(0, width-1):
        for y in range(0, height-1):
            if(x==width-1 and y==height-1):
                #new_img = Image.fromarray(new_pixel_data)
                #new_image.putdata(new_pixel_data)
                break
            print('pixel: ('+str(x)+', '+str(y)+')')
            rgb = pix[x,y]
            print('current pixel value: '+str(rgb))
            # calc new pixel value and set to pixel
            #print(gleam(rgb))
            gray = gleam(rgb)
            print('changing pixel value to: '+str(gray))
            print('')
            new_pixel_data[x,y] = int(gray)
    print(width,height)
    print(pix)
    print(new_pixel_data)
    #print(new_pixel_data[3,3])
    new_img = Image.fromarray(new_pixel_data, 'L')
    #new_image.putdata(new_pixel_data)
    printimg(new_img)
    new_img.show()
    new_img.save(filename + '_grayscale.gleam'+'.jpg')
    #printimg(new_image)
    break
file.close()
new_img.close()
