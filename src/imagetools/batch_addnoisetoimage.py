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
import matplotlib.pyplot as plt # import
import matplotlib.cm as cm

files = glob.glob('*.jpg')
for file in files:
    file = open(file)
    filename = file.name


    imagea = (misc.imread(filename)).astype(float)

    poissonNoise = np.random.poisson(4000,imagea.shape).astype(float)
    # for i in range(10):
    noisy = imagea + poissonNoise

    misc.imsave(filename+'-noisy.jpg', noisy)

    file.close()
