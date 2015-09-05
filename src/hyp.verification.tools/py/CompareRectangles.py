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

from Rectangle import Rectangle

#class compares two rectangles.
class CompareRectangles(object):

    basicdebugging = True
    basicdebugging = False
    debugging = True
    debugging = False

    if debugging:
        basicdebugging = True


    def __init__(self,r1,r2):
        self.r1 = r1
        self.r2 = r2
        self.initialise_boundary_tests()

    # two rectangles are vertically parrallel
    def vert_parrallel(self):
        if self.debugging:
            print("r1.left "+str(self.r1.getLeftXCoord()))
            print("r2.left "+str(self.r2.getLeftXCoord()))
            print("r1.right "+str(self.r1.getRightXCoord()))
            print("r2.right "+str(self.r2.getRightXCoord()))
        if self.r1.getLeftXCoord() == self.r2.getLeftXCoord() and \
            self.r1.getRightXCoord()==self.r2.getRightXCoord():
            if self.debugging:
                print("rects are vert. parra")
            return True
        else:
            if self.debugging:
                print("rects are not vert. parra")
            return False

    # two rectangles are horizontally parrallel
    def horiz_parallel(self):

        if self.r1.getTopYCoord()==self.r2.getTopYCoord() and \
            self.r1.getBottomYCoord()==self.r2.getBottomYCoord():
            if self.debugging:
                print("rects are horiz. parra")
                return True
        else:
            if self.debugging:
                print("rects are not horiz. parra")
            return False

    # two rectangles have same bottom Y coord
    def same_bottom_y(self):

        if self.r1.getBottomYCoord() == self.r2.getBottomYCoord():
            return True

    def same_top_y(self):

        if self.r1.getTopYCoord() == self.r2.getTopYCoord():
            return True

    def same_left_x(self):

        if self.r1.getLeftXCoord() == self.r2.getLeftXCoord():
            return True

    def same_right_x(self):

        if self.r1.getRightXCoord() == self.r2.getRightXCoord():
            return True

    # TODO: consider combined above functions into one check given the side.
    # def equal_side(r1,r2,side):
    #     if side == 'left':
    #         if r1.getLeftXCoord == r2.get

    def equals(self):

        if self.horiz_parallel() and self.vert_parrallel():
            return True
        else:
            return False

    # returns leftmost rectangle
    # where leftest has leftest LeftXCoord
    def rect_leftmost(self):

        if self.r1.getLeftXCoord() < self.r2.getLeftXCoord():
            return self.r1
        elif self.r2.getLeftXCoord() < self.r1.getLeftXCoord():
            return self.r2
        else:
            return None

    # returns 1 if r1 is leftmost, -1 if not
    # where leftest has leftest LeftXCoord
    def is_leftmost(self):

        if self.r1.getLeftXCoord() < self.r2.getLeftXCoord():
            return 1
        elif self.r2.getLeftXCoord() < self.r1.getLeftXCoord():
            return -1
        else: return 0

    # returns rightmost rectangle
    # where rightest has highest RightXCoord
    def rect_rightmost(self):

        if self.r1.getRightXCoord() > self.r2.getRightXCoord():
            return self.r1
        elif self.r2.getRightXCoord() > self.r1.getRightXCoord():
            return self.r2
        else:
            return None

    # returns 1 if r1 is rightmost, -1 if not
    # where rightest has highest RightXCoord
    def is_rightmost(self):

        if self.r1.getRightXCoord() > self.r2.getRightXCoord():
            return 1
        elif self.r2.getRightXCoord() > self.r1.getRightXCoord():
            return -1
        else: return 0

    # returns highest rectangle
    # where highest has lowest TopYCoord
    def rect_highest(self):
        if self.r1.getTopYCoord() < self.r2.getTopYCoord():
            return self.r1
        elif self.r2.getTopYCoord() < self.r1.getTopYCoord():
            return self.r2
        else:
            return None

    # returns 1 if r1 is highest, -1 if not
    # where highest has lowest TopYCoord
    def is_highest(self):
        if self.r1.getTopYCoord() < self.r2.getTopYCoord():
            return 1
        elif self.r2.getTopYCoord() < self.r1.getTopYCoord():
            return -1
        else:
            return 0

    # returns strictly lowest rectangle
    # where lowest has highest TopYCoord
    def rect_lowest(self):
        if self.r1.getBottomYCoord() > self.r2.getBottomYCoord():
            return self.r1
        elif self.r2.getBottomYCoord() > self.r1.getBottomYCoord():
            return self.r2
        else:
            return None

    # returns 1 if r1 is lowest, -1 if not
    # where lowest has highest TopYCoord
    def is_lowest(self):

        if self.r1.getBottomYCoord() > self.r2.getBottomYCoord():
            return 1
        elif self.r2.getBottomYCoord() > self.r1.getBottomYCoord():
            return -1
        else:
            return 0


    # returns True if rectangles have an x gap
    def dont_x_overlap(self):

        if not self.equals() and self.is_rightmost()!=0 and self.is_leftmost()!=0:
            if self.rect_rightmost().getLeftXCoord() >= self.rect_leftmost().getRightXCoord():
                return True
            else:
                return False
        else:
            return False

    # TODO: fix. non-interscting rectnagles should not overlap but they do.
    # returns True if rectangles have an y gap
    def dont_y_overlap(self):
        if self.debugging:
            print("testing if they dont y overlap")
            print("highest rect is: "+str(self.rect_highest()))
            print("lowest rect is: "+str(self.rect_lowest()))
            print("highest rect bottomY: "+str(self.rect_highest().getBottomYCoord()))
            print("lowest rect topY: "+str(self.rect_lowest().getTopYCoord()))
        if self.rect_highest() != None and self.rect_lowest() != None and \
            self.rect_highest().getBottomYCoord() <= self.rect_lowest().getTopYCoord():
            if self.debugging:
                print("they dont y overlap")
            return True
        else:
            if self.debugging:
                print("they do y overlap")
            return False

    # returns True if rectangles dont intersect
    def rect_dont_intersect(self):
        if self.basicdebugging:
            print("testing if they dont intersect")
        # same rectangles mean they do intersect so return False
        if self.equals():
            return False
        #  parall in x but gap
        elif self.horiz_parallel() and self.dont_x_overlap():
            if self.debugging:
                print("parall in x but gapx")
            return True
        #  parall in y but gap
        elif self.vert_parrallel() and self.dont_y_overlap():
            if self.basicdebugging:
                print("parall in y but gap")
            return True
        # not parall (and gap in both)
        elif self.horiz_parallel()==False and self.vert_parrallel() == False and \
            self.dont_x_overlap() and self.dont_y_overlap():
            if self.debugging:
                print("not parall and gap in both")
            return True
        else:
            if self.basicdebugging:
                print("they must intersect..")
            return False

    # initalise boundary tests used in other functions
    def initialise_boundary_tests(self):

        # print("initialising boundary test array")
        # class variables for boundary tests
        self.boundary_tests = \
            [self.is_lowest(),
             self.is_highest(),
             self.is_leftmost(),
             self.is_rightmost()]

        # if self.debugging:
        #     print("boundary test: " + str(self.boundary_tests))

        # TODO: replace with private vars _b
        self.b0 = self.boundary_tests[0]
        self.b1 = self.boundary_tests[1]
        self.b2 = self.boundary_tests[2]
        self.b3 = self.boundary_tests[3]

        self.set_inverse_bounds()

        if self.debugging:
            print("boundary test: " + str(self.boundary_tests))
            print("inverse boundary test: " + str(self.inverse_boundary_tests))

#initialise inverse results as results
    def set_inverse_bounds(self):
        if self.debugging:
            print("setting inverse boundary tests")
            print("boundary test: " + str(self.boundary_tests))
        self.inverse_boundary_tests = list(self.boundary_tests)
        # temp = self.boundary_tests
        # self.inverse_boundary_tests = temp
        # print("boundary test: " + str(self.boundary_tests))
        # print("inverse boundary test: " + str(self.inverse_boundary_tests))
        for index in range(len(self.inverse_boundary_tests)):
            # print("index" + str(index))
            if self.inverse_boundary_tests[index] != 0:
                # print("before change: "+str(self.inverse_boundary_tests[index]))
                self.inverse_boundary_tests[index] = self.inverse_boundary_tests[index] * -1
                # print(self.inverse_boundary_tests[index])
        self.i0 = self.inverse_boundary_tests[0]
        self.i1 = self.inverse_boundary_tests[1]
        self.i2 = self.inverse_boundary_tests[2]
        self.i3 = self.inverse_boundary_tests[3]


    # returns the rectangle that fully contains the other
    def rect_fully_contains(self):

        # no containment if equal
        if self.equals():
            return None

        # r1 fully contains r2 if all nonzeroes in boundary tests are 1.
        # that is, if 0 or 1
        # test r1 fully contains r2

        # print(str(self.boundary_tests))

        if self.debugging:
            print("testing if r1 fully contains r2")

        fullyContains = True
        for boundary in self.boundary_tests:
            if boundary == 0 or boundary == 1:
                # print("boundary 1 continue")
                continue
            else:
                # print("boundary not 1 break")
                if self.debugging:
                    print("r1 does not fully contain r2")
                fullyContains = False
                break

        if fullyContains:
            if self.debugging:
                print("r1 fully contains r2:" + str(fullyContains))
            return self.r1

        # r2 fully contains r1 if all nonzeroes in inverse boundary tests are 1.
        if self.debugging:
            print("testing if r2 fully contains r1")

        fullyContains = True
        for boundary in self.inverse_boundary_tests:
            if boundary == 0 or boundary == 1:
                continue
            else:
                if self.debugging:
                    print("r2 does not fully contain r1")
                fullyContains = False
                break

        if fullyContains:
            if self.debugging:
                print("r2 fully contains r1:" + str(fullyContains))
            return self.r2
        else:
            return False


    # returns the rectangle fully contained by the other
    def rect_fully_contained(self):
        fully_container = self.rect_fully_contains()
        if fully_container == self.r1:
            return self.r2
        elif fully_container == self.r2:
            return self.r1
        else:
            return None


    # for x contained overlap, x containing rectangle must be leftest and rightest
    # and not both lowest and highest
    def is_xcontained_overlap(self):
        if not(self.b0 == 1 and self.b1 == 1) and self.b2 == 1 and self.b3 == 1:
            if self.debugging:
                print("r1 x contains r2")
            return True
        elif not(self.i0 == 1 and self.i1 == 1) and self.i2 == 1 and self.i3 == 1:
            if self.debugging:
                print("r2 x contains r1")
            return True
        else:
            if self.debugging:
                print("is not x contained overlap")
            return False

    # returns the rectangle overlap that is strictly contained in x
    # this happens when tests have one differing result in y (no zeroes)
    def rect_xcontained_overlap(self,r1,r2):
        # boundary_tests = [lowest, highest, leftest, rightest]
                # b0 = 1 , r1 lower than r2
                # b1 = 1 , r1 higher than r2
                # b2 = 1 , r1 lefter than r2
                # b3 = 1 , r1 righter than r2

        # r2 is not bound at top
        # r1: level bottom or lowest and not highest and leftest and rightest
        if self.b0 != -1 and self.b1 == -1 and self.b2 == 1 and self.b3 == 1:
            overlap_left = r2.getLeftXCoord()
            overlap_right = r2.getRightXCoord()
            overlap_bottom = r2.getBottomYCoord()
            overlap_top = r1.getTopYCoord()
            overlap_width = overlap_right - overlap_left
            overlap_height = overlap_bottom - overlap_top
            return Rectangle(overlap_left, overlap_top, overlap_width, overlap_height)

        # r2 is not bound at bottom
        elif self.b0 == -1 and self.b1 != -1 and self.b2 == 1 and self.b3 == 1:
            overlap_left = r2.getLeftXCoord()
            overlap_right = r2.getRightXCoord()
            overlap_bottom = r1.getBottomYCoord()
            overlap_top = r2.getTopYCoord()
            overlap_width = overlap_right - overlap_left
            overlap_height = overlap_bottom - overlap_top
            return Rectangle(overlap_left, overlap_top, overlap_width, overlap_height)

        # r2 is not bound at top or bottom
        elif self.b0 == -1 and self.b1 == -1 and self.b2 == 1 and self.b3 == 1:
            overlap_left = r2.getLeftXCoord()
            overlap_right = r2.getRightXCoord()
            overlap_bottom = r1.getBottomYCoord()
            overlap_top = r1.getTopYCoord()
            overlap_width = overlap_right - overlap_left
            overlap_height = overlap_bottom - overlap_top
            return Rectangle(overlap_left, overlap_top, overlap_width, overlap_height)

        # test inverse
        elif  r1 == self.r1 and self.rect_xcontained_overlap(r2,r1) != None:
            return self.rect_xcontained_overlap(r2,r1)

        else:
            if self.debugging:
                print("was meant to return x contained overlap, but didnt")
            return None

    # for y contained overlap, y containing rectangle must be lowest and highest
    # and not both leftest and rightest
    def is_ycontained_overlap(self):
        if self.b0 == 1 and self.b1 == 1 and not(self.b2 == 1 and self.b3 == 1):
            if self.debugging:
                print("r1 y contains r2")
            return True
        elif self.i0 == 1 and self.i1 == 1 and not(self.i2 == 1 and self.i3 == 1):
            if self.debugging:
                print("r2 y contains r1")
            return True
        else:
            if self.debugging:
                print("is not x contained overlap")
            return False

    # returns the rectangle overlap that is contained in y
    # this happens when tests have one differing result in x (no zeroes)
    def rect_ycontained_overlap(self,r1,r2):
        # boundary_tests = [lowest, highest, leftest, rightest]

            # r2 is not bound at left
            if self.b0 == 1 and self.b1 == 1 and self.b2 == -1 and self.b3 != -1:
                if self.debugging:
                    print("r2 is not bound at left")
                overlap_left = r1.getLeftXCoord()
                overlap_right = r2.getRightXCoord()
                overlap_bottom = r2.getBottomYCoord()
                overlap_top = r2.getTopYCoord()
                overlap_width = overlap_right - overlap_left
                overlap_height = overlap_bottom - overlap_top
                return Rectangle(overlap_left, overlap_top, overlap_width, overlap_height)

            # r2 is not bound at right
            elif self.b0 == 1 and self.b1 == 1 and self.b2 != -1 and self.b3 == -1:
                if self.debugging:
                    print("r2 is not bound at right")
                overlap_left = r2.getLeftXCoord()
                overlap_right = r1.getRightXCoord()
                overlap_bottom = r2.getBottomYCoord()
                overlap_top = r2.getTopYCoord()
                overlap_width = overlap_right - overlap_left
                overlap_height = overlap_bottom - overlap_top
                return Rectangle(overlap_left, overlap_top, overlap_width, overlap_height)

            # r2 is not bound at left or right
            elif self.b0 == 1 and self.b1 == 1 and self.b2 == -1 and self.b3 == -1:
                if self.debugging:
                    print("r2 is not bound at left or right")
                overlap_left = r1.getLeftXCoord()
                overlap_right = r1.getRightXCoord()
                overlap_bottom = r2.getBottomYCoord()
                overlap_top = r2.getTopYCoord()
                overlap_width = overlap_right - overlap_left
                overlap_height = overlap_bottom - overlap_top
                return Rectangle(overlap_left, overlap_top, overlap_width, overlap_height)

            # test inverse
            elif r1 == self.r1 and self.rect_ycontained_overlap(r2,r1) != None:
                return self.rect_xcontained_overlap(r2,r1)

            else:
                if self.debugging:
                    print("not y contained overlap")
                return None

    # true if the rectnagles are parrallel in x
    def is_xparrallel_overlap(self):
        if self.horiz_parallel() and not self.dont_x_overlap():
            return True

    # get the rectangle from the overlap when two rectangles are parrallel in x
    def rect_xparrallel_overlap(self):
        overlap_right = self.rect_leftmost().getRightXCoord()
        overlap_left = self.rect_rightmost().getLeftXCoord()
        overlap_bottom = self.r1.getBottomYCoord()
        overlap_top = self.r1.getTopYCoord()
        overlap_width = overlap_right - overlap_left
        overlap_height = overlap_bottom - overlap_top
        return Rectangle(overlap_left, overlap_top, overlap_width, overlap_height)

    # true if the rectnagles are parrallel in y
    def is_yparrallel_overlap(self):
        if self.vert_parrallel() and not self.dont_y_overlap():
            return True

    # get the rectangle from the overlap when two rectangles are parrallel in y
    def rect_yparrallel_overlap(self):
        overlap_top = self.rect_highest().getTopYCoord()
        overlap_bottom = self.rect_lowest().getBottomYCoord()
        overlap_left = self.r1.getLeftXCoord()
        overlap_right = self.r1.getRightXCoord()
        overlap_width = overlap_right - overlap_left
        overlap_height = overlap_bottom - overlap_top
        return Rectangle(overlap_left, overlap_top, overlap_width, overlap_height)

    # returns true if the rectnagles are not parrallel or contained by other.
    def is_nocontainment_notparrallel_overlap(self):

        vert_tests = [self.b0, self.b1]
        horiz_tests = [self.b2, self.b3]
        if sum(vert_tests)==0 and sum(horiz_tests)==0 and not self.equals():
            return True

    # gets the rectangle from the overlap when two rectangles are not parrallel or contained by other.
    def rect_nocontainment_notparrallel_overlap(self):

        overlap_top = self.rect_lowest().getTopYCoord()
        overlap_bottom = self.rect_highest().getBottomYCoord()
        overlap_right = self.rect_leftmost().getRightXCoord()
        overlap_left = self.rect_rightmost().getLeftXCoord()
        overlap_width = overlap_right - overlap_left
        overlap_height = overlap_bottom - overlap_top
        return Rectangle(overlap_left, overlap_top, overlap_width, overlap_height)


    # returns the intersection rectangle, of two rectangles.
    def rect_intersection(self):
        # if rectangles equal then intersect is either.
        if self.equals():
            if self.basicdebugging:
                print("rectangles are equal")
            # just return first one.
            return self.r1
        # if rectangles dont intersect then return None.
        elif self.rect_dont_intersect():
            if self.basicdebugging:
                print("rectangles dont intersect")
            return None
        # they do intersect
        else:
            if self.basicdebugging:
                print("rectangles intersect")

            # if one fully contains the other, then the intersection area is the contained.
            contained_rectangle = self.rect_fully_contained()
            containing_rectangle = self.rect_fully_contains()

            if contained_rectangle is not None:
                # print(str(contained_rectangle)+"is fully contained by other")
                # print("containing rectangles area: "+str(containing_rectangle.area()))
                # print("contained rectangles area: "+str(contained_rectangle.area()))
                # remaining_area = containing_rectangle.area() - contained_rectangle.area()
                # return Rectangle(0,0,10, remaining_area/10.0)
                return contained_rectangle
                # return Rectangle(containing_rectangle.area() - contained_rectangle.area())
                    #TODO: need to return series of rectangles for remaining area here.
                    # or just rectangle of equivalent area. all we need is area.

            # else they overlap
            # construct intersectRect by testing bounds
            else :
                if self.basicdebugging:
                    print("no rectangle fully contains other")

                # # otherwise no containment overlap
                # elif self.is_nocontainment_notparrallel_overlap():
                #     # print("they are not parrallel in x or y and overlap")
                #     return self.rect_nocontainment_notparrallel_overlap()
                # if no containment overlap
                if self.is_nocontainment_notparrallel_overlap():
                    if self.basicdebugging:
                        print("they are not parrallel in x or y and overlap")
                    return self.rect_nocontainment_notparrallel_overlap()

                # they x contained overlap
                elif self.is_xcontained_overlap():
                    if self.basicdebugging:
                        print("they xcontained overlap")
                    return self.rect_xcontained_overlap(self.r1,self.r2)

                # they y contained overlap
                elif self.is_ycontained_overlap():
                    if self.basicdebugging:
                        print("they ycontained overlap")
                    return self.rect_ycontained_overlap(self.r1, self.r2)

                # they x parrallel overlap
                elif self.is_xparrallel_overlap():
                    if self.basicdebugging:
                        print("they are parrallel in x and overlap")
                    return self.rect_xparrallel_overlap()

                # they y parrallel overlap
                elif self.is_yparrallel_overlap():
                    if self.basicdebugging:
                        print("they are parrallel in y and overlap")
                    return self.rect_yparrallel_overlap()
                else:
                    if self.basicdebugging:
                        print("huh?..")
                    return None

 # returns the intersection (overlap) area, of the two rectangles.
    def area_intersection(self):
        if self.rect_intersection() is not None:
            return self.rect_intersection().area()
        else:
            return None

    # returns the union rectangle, of two rectangles.
    def area_union(self):
        # union(r1.r2).area = r1.area + r2.area - int(r1,r2)
        if self.area_intersection() is not None:
            return self.r1.area() + self.r2.area() - self.area_intersection()
        else:
            return None

    # returns jaccard index of two rectangles
    # Formula: jaccard_index = intersection / union
    def jaccard_index(self):
        if self.area_intersection() != None and \
            self.area_union() != None:
            return self.area_intersection() / float(self.area_union())
        else:
            return None

    # define similar rectangles if JI > 0.5
    def similar_rectangles(self):
        if self.jaccard_index() != None:
            return self.jaccard_index() > 0.5
        else:
             return None
