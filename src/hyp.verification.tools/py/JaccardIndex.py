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
File: JaccardIndex.py
Author: julius.skye@gmail.com
Date: 15.08.2015
File Description:
This class calculates the Jaccard Index of the area of two rectangles.
which is the best method for comparing similarity of two rectangles.

    Formula: jaccard_index = intersection / union

'''

#But we can make it more efficient.
#e really don't need to compute the union set, rather the cardinality. So this code works better:
# def compute_jaccard_index(set_1, set_2):
#     n = len(set_1.intersection(set_2))
#     return n / float(len(set_1) + len(set_2) - n)
# http://love-python.blogspot.com.au/2012/07/python-code-to-compute-jaccard-index.html

import Rectangle.py
import CompareRectangles.py

#define simple jaccard index function
def compute_jaccard_index(r1, r2):
    # return len(set_1.intersection(set_2)) / float(len(set_1.union(set_2)))
    intersectArea = rect_intersection(r1,r2).getArea()
    unionArea = r1.getArea()+r2.getArea()
    return intersectArea / unionArea


#TODO: add test data


if __name__ == '__main__':
    main()
