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
File: CompareRectangles.py
Author: julius.skye@gmail.com
Date: 15.08.2015
File Description:
This class compares two rectangles r1 and r2.
It also contains a function to calculate the intersection of two rectangles.
'''

def __init__(self, r1,r2):
    # global variables for boundary tests
    boundary_tests = [rect_lowest(r1,r2), rect_highest(r1,r2), rect_leftmost(r1,r2), rect_rightmost(r1,r2)]
    b0 = boundary_tests[0]
    b1 = boundary_tests[1]
    b2 = boundary_tests[2]
    b3 = boundary_tests[3]

# two rectangles are vertically parrallel
def vert_parrallel(r1,r2):
    if r1.getLeftXCoord()==r2.getLeftXCoord() and \
        r1.getRightXCoord==r2.getRightXCoord():
            return True
    else:
        return False

# two rectangles are horizontally parrallel
def horiz_parallel(r1,r2):
    if r1.getTopYCoord()==r2.getTopYCoord() and \
        r1.getBottomYCoord==r2.getBottomYCoord():
            return True
    else:
        return False

# two rectangles have same bottom Y coord
def same_bottom_y(r1,r2):
    if r1.getBottomYCoord() == r2.getBottomYCoord():
        return True

def same_top_y(r1,r2):
    if r1.getTopYCoord() == r2.getTopYCoord():
        return True

def same_left_x(r1,r2):
    if r1.getLeftXCoord() == r2.getLeftXCoord():
        return True

def same_right_x(r1,r2):
    if r1.getRightXCoord() == r2.getRightXCoord():
        return True

# TODO: combine above functions into one check given the side.
# def equal_side(r1,r2,side):
#     if side == 'left':
#         if r1.getLeftXCoord == r2.get

def equals(r1,r2):
    if horiz_parallel(r1,r2) and vert_parrallel(r1,r2):
        return True
    else: return False

# returns leftmost rectangle
# where leftest has leftest LeftXCoord
def rect_leftmost(r1,r2):
    if r1.getLeftXCoord() < r2.getLeftXCoord():
        return r1
    elif r2.getLeftXCoord()<r2.getLeftXCoord():
        return r2
    else: return False

# returns 1 if r1 is leftmost, -1 if not
# where leftest has leftest LeftXCoord
def is_leftmost(r1,r2):
    if r1.getLeftXCoord() < r2.getLeftXCoord():
        return 1
    elif r2.getLeftXCoord()<r2.getLeftXCoord():
        return -1
    else: return 0

# returns rightmost rectangle
# where rightest has highest RightXCoord
def rect_rightmost(r1,r2):
    if r1.getRightXCoord() > r2.getRightXCoord():
        return r1
    elif r2.getRightXCoord() > r2.getRightXCoord():
        return r2
    else: return False

# returns 1 if r1 is rightmost, -1 if not
# where rightest has highest RightXCoord
def is_rightmost(r1,r2):
    if r1.getRightXCoord() > r2.getRightXCoord():
        return 1
    elif r2.getRightXCoord() > r2.getRightXCoord():
        return -1
    else: return 0

# returns highest rectangle
# where highest has lowest TopYCoord
def rect_highest(r1,r2):
    if r1.getTopYCoord() > r2.getTopYCoord():
        return r1
    elif r2.getTopYCoord() > r1.getTopYCoord():
        return r2
    else: return False

# returns 1 if r1 is highest, -1 if not
# where highest has lowest TopYCoord
def is_highest(r1,r2):
    if r1.getTopYCoord() < r2.getTopYCoord():
        return 1
    elif r2.getTopYCoord() < r2.getTopYCoord():
        return -1
    else: return 0

# returns strictly lowest rectangle
# where lowest has highest TopYCoord
def rect_lowest(r1,r2):
    if r1.getBottomYCoord() > r2.getBottomYCoord():
        return r1
    elif r2.getBottomYCoord() > r2.getBottomYCoord():
        return r2
    else: return False

# returns 1 if r1 is lowest, -1 if not
# where lowest has highest TopYCoord
def is_lowest(r1,r2):
    if r1.getTopYCoord() > r2.getTopYCoord():
        return 1
    elif r2.getTopYCoord()<r2.getTopYCoord():
        return -1
    else: return 0


# returns True if rectangles have an x gap
def dont_x_overlap(r1,r2):
    if rect_rightmost(r1,r2).getLeft() >= rect_leftmost(r1,r2).getRight():
        return True
    else: return False

# returns True if rectangles have an y gap
def dont_y_overlap(r1,r2):
    if rect_highest(r1,r2).getBottomYCoord() <= rect_lowest(r1,r2).getTopYCoord():
        return True
    else: return False

# returns True if rectangles dont intersect
def rect_dont_intersect(r1, r2):
    # same rectangles mean they do intersect so return False
    if equals(r1,r2):
        return False
    #  parall in x but gap
    elif horiz_parallel(r1,r2) and dont_x_overlap(r1,r2):
        return True
    #  parall in y but gap
    elif vert_parrallel(r1,r2) and dont_y_overlap(r1,r2):
        return True
    # not parall (and gap in both)
    elif !horiz_parallel(r1,r2) and !vert_parrallel(r1,r2) and \
        dont_x_overlap(r1,r2) and dont_y_overlap(r1,r2):
        return True

# returns the rectangle that fully contains the other
def rect_fully_contains(r1,r2):

    # no containment if equal
    if equals(r1,r2):
        return False

    # rectangle fully contains other if all nonzeroes are ones.
    boundary_tests = [rect_lowest(r1,r2), rect_highest(r1,r2), rect_leftmost(r1,r2), rect_rightmost(r1,r2)]
    inverse_boundary_tests = [rect_lowest(r2,r1), rect_highest(r2,r1), rect_leftmost(r2,r1), rect_rightmost(r2,r1)]

    # test r1 fully contains r2
    fullyContains = True
    for boundary in boundary_tests:
        if boundary != 0 and boundary == 1:
            continue
        else:
            fullyContains = False
            break

    if fullyContains:
        return r1

    # test r2 fully contains r1
    fullyContains = True
    for boundary in inverse_boundary_tests:
        if boundary != 0 and boundary == 1:
            continue
        else:
            fullyContains = False
            break

    if fullyContains:
        return r2
    else:
        return False


# returns the rectangle fully contained by the other
def rect_fully_contained(r1,r2):
    if rect_fully_contained(r1,r2) == r1:
        return r2
    elif rect_fully_contained(r1,r2) == r2:
        return r1
    else: return None



def is_xcontained_overlap(r1,r2):
    if ((b0 == -1 or b1 == -1) and (b2 == 1 and b3 == 1)):
        return True

# returns the rectangle overlap that is contained in x
# this happens when tests have one differing result in y (no zeroes)
def rect_xcontained_overlap(r1,r2):
    # boundary_tests = [lowest, highest, leftest, rightest]

    # r2 is not bound at top
    if b0 != -1 and b1 == -1 and b2 == 1 and b3 == 1:
        overlap_left = r2.getLeftXCoord()
        overlap_right = r2.getRightXCoord()
        overlap_bottom = r2.getBottomYCoord()
        overlap_top = r1.getTopYCoord()
        overlap_width = overlap_right - overlap_left
        overlap_height = overlap_bottom - overlap_top
        return Rectangle(overlap_left, overlap_top, overlap_width, overlap_height)

    # r2 is not bound at bottom
    elif b0 == -1 and b1 != -1 and b2 == 1 and b3 == 1:
        overlap_left = r2.getLeftXCoord()
        overlap_right = r2.getRightXCoord()
        overlap_bottom = r1.getBottomYCoord()
        overlap_top = r2.getTopYCoord()
        overlap_width = overlap_right - overlap_left
        overlap_height = overlap_bottom - overlap_top
        return Rectangle(overlap_left, overlap_top, overlap_width, overlap_height)

    # r2 is not bound at top or bottom
    elif b0 == -1 and b1 == -1 and b2 == 1 and b3 == 1:
        overlap_left = r2.getLeftXCoord()
        overlap_right = r2.getRightXCoord()
        overlap_bottom = r1.getBottomYCoord()
        overlap_top = r1.getTopYCoord()
        overlap_width = overlap_right - overlap_left
        overlap_height = overlap_bottom - overlap_top
        return Rectangle(overlap_left, overlap_top, overlap_width, overlap_height)

    # test inverse
    elif rect_xcontained_overlap(r2,r1) != None:
        return rect_xcontained_overlap(r2,r1)

    else return None


def is_ycontained_overlap:
    if ((b0 == 1 and b1 == 1) and (b2 == -1 or b3 == -1)):
        return True

# returns the rectangle overlap that is contained in y
# this happens when tests have one differing result in x (no zeroes)
def rect_ycontained_overlap(r1,r2):
    # boundary_tests = [lowest, highest, leftest, rightest]

        # r2 is not bound at left
        if b0 == 1 and b1 == 1 and b2 == -1 and b3 != -1:
            overlap_left = r1.getLeftXCoord()
            overlap_right = r2.getRightXCoord()
            overlap_bottom = r2.getBottomYCoord()
            overlap_top = r2.getTopYCoord()
            overlap_width = overlap_right - overlap_left
            overlap_height = overlap_bottom - overlap_top
            return Rectangle(overlap_left, overlap_top, overlap_width, overlap_height)

        # r2 is not bound at right
        elif b0 == 1 and b1 == 1 and b2 != -1 and b3 == -1:
            overlap_left = r2.getLeftXCoord()
            overlap_right = r1.getRightXCoord()
            overlap_bottom = r2.getBottomYCoord()
            overlap_top = r2.getTopYCoord()
            overlap_width = overlap_right - overlap_left
            overlap_height = overlap_bottom - overlap_top
            return Rectangle(overlap_left, overlap_top, overlap_width, overlap_height)

        # r2 is not bound at left or right
        elif b0 == 1 and b1 == 1 and b2 == -1 and b3 == -1:
            overlap_left = r1.getLeftXCoord()
            overlap_right = r1.getRightXCoord()
            overlap_bottom = r2.getBottomYCoord()
            overlap_top = r2.getTopYCoord()
            overlap_width = overlap_right - overlap_left
            overlap_height = overlap_bottom - overlap_top
            return Rectangle(overlap_left, overlap_top, overlap_width, overlap_height)

        # test inverse
        elif rect_ycontained_overlap(r2,r1) != None:
            return rect_xcontained_overlap(r2,r1)

        else return None

def is_xparrallel_overlap(r1,r2):
    if horiz_parallel(r1,r2) and !dont_x_overlap(r1,r2):
        return True

def rect_xparrallel_overlap(r1,r2):
    overlap_right = rect_leftmost(r1,r2).getRightXCoord()
    overlap_left = rect_rightmost(r1,r2).getLeftXCoord()
    overlap_bottom = r1.getBottomYCoord()
    overlap_top = r1.getTopYCoord()
    overlap_width = overlap_right - overlap_left
    overlap_height = overlap_bottom - overlap_top
    return Rectangle(overlap_left, overlap_top, overlap_width, overlap_height)


def is_yparrallel_overlap(r1,r2):
    if vert_parallel(r1,r2) and !dont_y_overlap(r1,r2):
        return True

def rect_yparrallel_overlap(r1,r2):
    overlap_top = rect_highest(r1,r2).getTopYCoord()
    overlap_bottom = rect_lowest(r1,r2).getBottomYCoord()
    overlap_left = r1.getLeftXCoord()
    overlap_right = r1.getRightXCoord()
    overlap_width = overlap_right - overlap_left
    overlap_height = overlap_bottom - overlap_top
    return Rectangle(overlap_left, overlap_top, overlap_width, overlap_height)

def is_nocontainment_notparrallel_overlap(r1,r2):
    vert_tests = [b0 b1]
    horiz_tests = [b2 b3]
    if sum(vert_tests)==0 and sum(horiz_tests)==0 and !equals(r1,r2):
        return True

def rect_nocontainment_notparrallel_overlap(r1,r2):
    overlap_top = rect_highest(r1,r2).getTopYCoord()
    overlap_bottom = rect_lowest(r1,r2).getBottomYCoord()
    overlap_right = rect_leftmost(r1,r2).getRightXCoord()
    overlap_left = rect_rightmost(r1,r2).getLeftXCoord()
    overlap_width = overlap_right - overlap_left
    overlap_height = overlap_bottom - overlap_top
    return Rectangle(overlap_left, overlap_top, overlap_width, overlap_height)



# returns the intersection rectangle, of two rectangles.
def rect_intersection(r1,r2):
    # if rectangles equal then intersect is either.
    if equals(r1,r2):
        return r1
    # if rectangles dont intersect then return None.
    elif rect_dont_intersect(r1,r2):
        return None
    # they do intersect
    else:
        # if one fully contains the other, then the intersection area is the contained.
        contained_rectangle = rect_contained(r1,r2)
        if contained_rectangle != None:
            return contained_rectangle

        # else they overlap
        # construct intersectRect by testing bounds
        else :

            # they x contained overlap
            if is_xcontained_overlap(r1,r2):
                return rect_xcontained_overlap(r1,r2)

            # they y contained overlap
            elif is_ycontained_overlap(r1,r2):
                return rect_ycontained_overlap(r1,r2)

            # they x parrallel overlap
            elif is_xparrallel_overlap(r1,r2):
                return rect_xparrallel_overlap(r1,r2)

            # they y parrallel overlap
            elif is_yparrallel_overlap(r1,r2):
                return rect_yparrallel_overlap(r1,r2)

            # otherwise no containment overlap
            elif is_nocontainment_notparrallel_overlap(r1,r2):
                return rect_nocontainment__notparrallel_overlap(r1,r2)
