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
File: batch_addnoisetoimage.py
Author: julius.skye@gmail.com
Date: 1.05.2015
File Description:
This program adds noise to all images in current dir.
'''

import glob
from scipy import misc
import numpy as np
import sys


def flip_vert(picture):
    width = getWidth(picture)
    height = getHeight(picture)
    print('flipping image vertically')
    for y in range(0, height/2):
        for x in range(0, width):
            sourcePixel = getPixel(picture, x, y)
            targetPixel = getPixel(picture, x, height - y - 1)
            color = getColor(sourcePixel)
            setColor(sourcePixel, getColor(targetPixel))
            setColor(targetPixel, color)

    return picture


def flip_horiz(picture):
    width = getWidth(picture)
    height = getHeight(picture)
    print('flipping image horizontally')
    for y in range(0, height):
        for x in range(0, width/2):
            sourcePixel = getPixel(picture, x, y)
            targetPixel = getPixel(picture, width - x - 1, y)
            color = getColor(sourcePixel)
            setColor(sourcePixel, getColor(targetPixel))
            setColor(targetPixel, color)

    return picture


# Get user supplied values
if len(sys.argv) == 2:
    flip_direction = sys.argv[1]
else:
    print("check arguments! "+ str(len(sys.argv)))

files=glob.glob("*.jpg")
for file in files:
    f=open(file)
    filename=f.name
    image = Image.open(file)
    # imResized = image.resize((128,128), Image.ANTIALIAS)
    if flip_direction == "x":
        imFlipped = flip_horiz(image)
    elif flip_direction == "y":
        imFlipped = flip_vert(image)
    else:
        print("no direction given")
        exit()
    imFlipped.save(filename + '_flipped_'+flip_direction+'.jpg', 'JPEG', quality=100)
    # image.save(filename+".jpg")
    f.close()
