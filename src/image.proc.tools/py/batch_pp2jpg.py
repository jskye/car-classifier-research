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
File: convertppm2jpg.py
Author: julius.skye@gmail.com
Date: 1.05.2015
File Description:

    This file contains a function that converts images from PPM format to JPG.


"""

import sys
import os
import glob
from PIL import Image

filetypes = ("*.ppm", "*.pgm")
#TODO: test with pbm and pnm files.
files_grabbed = []
for files in filetypes:
    files_grabbed.extend(glob.glob(files))
# files=glob.glob("*.ppm") glob.glob("*.pgm")
print(files_grabbed)
for file in files_grabbed:
    f = open(file)
    filename = f.name
    image = Image.open(file)
    image.save(filename + '.jpg', 'JPEG', quality=100)
    f.close()
