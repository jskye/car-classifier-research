# def simple_compare_rects(rect1, rect2)


        #     # use simple_compare_rects to comapre similarity of True and detected rectangles
        #     # to determine True or False positive
        #     # TODO: move to function
        #     # TODO: replace with jaccard index
        #     #   this method has flaws where some dissimilar rectangles are marked as TP
        #
        #     # if detected.area smaller than True.area but still bigger than half,
        #     # and side lengths are within 50% of eachother then rects are similar.
        #     # OR
        #     # if True.area smaller than detected.area  but still bigger than half,
        #     # and side lengths are within 50% of eachother then rects are similar.
        #     A = (detectedArea < TrueArea)
        #     B = (detectedArea > 0.5*TrueArea)
        #     C = (detectedWidth<2*TrueWidth)
        #     D = (detectedWidth>0.5*TrueWidth)
        #     E = (detectedHeight<2*TrueHeight)
        #     F = (detectedHeight>0.5*TrueHeight)
        #
        #     G = (TrueArea < detectedArea)
        #     H = (TrueArea > 0.5*detectedArea)
        #     I = (detectedWidth<2*TrueWidth)
        #     J = (detectedWidth>0.5*TrueWidth)
        #     K = (detectedHeight<2*TrueHeight)
        #     L = (detectedHeight>0.5*TrueHeight)

            # if (A and B and C and D and E and F) or (G and H and I and J and K and L ):
            #     img_True_positives +=1
            # else: img_False_positives +=1
