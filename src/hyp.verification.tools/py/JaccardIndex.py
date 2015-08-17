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
This class calculates the Jaccard Index of two rectangles.
The Jaccard Index is the best method for comparing similarity of two rectangles.

    jaccard_index = intersection / union

See PASCAL VOC challenge:
http://pascallin.ecs.soton.ac.uk/challenges/VOC/voc2012/htmldoc/devkit_doc.html#SECTION00054000000000000000
intersectionArea=rectint(gt,pr)
unionCoords=[min(x_g,x_p),min(y_g,y_p),max(x_g+width_g-1,x_p+width_p-1),max(y_g+height_g-1,y_p+height_p-1];
unionArea=(unionCoords(3)-unionCoords(1)+1)*(unionCoords(4)-unionCoords(2)+1);
overlapArea=intersectionArea/unionArea; This should be greater than 0.5 to consider it as a valid detection.
'''

#But we can make it more efficient.
#e really don't need to compute the union set, rather the cardinality. So this code works better:
# def compute_jaccard_index(set_1, set_2):
#     n = len(set_1.intersection(set_2))
#     return n / float(len(set_1) + len(set_2) - n)
# http://love-python.blogspot.com.au/2012/07/python-code-to-compute-jaccard-index.html

import Rectangle.py
import RectangleIntersection.py

#define simple jaccard index function
def compute_jaccard_index(r1, r2):
    # return len(set_1.intersection(set_2)) / float(len(set_1.union(set_2)))
    intersectArea = rect_intersection(r1,r2)
    unionArea = r1.getArea()+r2.getArea()
    return intersectArea / unionArea


if __name__ == '__main__':
    main()
