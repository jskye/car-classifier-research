#!/bin/sh
# This file is called ~/batchdetect.sh
# This is a batch script to run the detections with the following params:

PROJ_ROOT="/Users/juliusskye/COMP4120.Car.Detection.Research/car-classifier-research"

# the detection script to use
DETECT_SCRIPT=$PROJ_ROOT"/src/hyp.verification.tools/py/detect.py"
# the testdata location
TESTDATA_DIR=$PROJ_ROOT"/testdata"

# the locations of the test sets of images
TESTDATA_IMG_FB_TRAINSET=$TESTDATA_DIR"/frontbacks/trainingset/"
TESTDATA_IMG_FB_TESTSET=$TESTDATA_DIR"/frontbacks/testset/"
TESTDATA_IMG_FB_PDSET=$TESTDATA_DIR"/frontbacks/publicdomainset/"
TESTDATA_IMG_S_TRAINSET=$TESTDATA_DIR"/sides/trainingset/"
TESTDATA_IMG_S_TESTSET=$TESTDATA_DIR"/sides/testset/"
TESTDATA_IMG_S_PDSET=$TESTDATA_DIR"/sides/publicdomainset/"
# with noise added
TESTDATA_IMG_FB_TRAINSET_NOISY=$TESTDATA_DIR"/frontbacks/trainingset.noisy/"
TESTDATA_IMG_FB_TESTSET_NOISY=$TESTDATA_DIR"/frontbacks/testset.noisy/"
TESTDATA_IMG_FB_PDSET_NOISY=$TESTDATA_DIR"/frontbacks/publicdomainset.noisy/"
TESTDATA_IMG_S_TRAINSET_NOISY=$TESTDATA_DIR"/sides/trainingset.noisy/"
TESTDATA_IMG_S_TESTSET_NOISY=$TESTDATA_DIR"/sides/testset.noisy/"
TESTDATA_IMG_S_PDSET_NOISY=$TESTDATA_DIR"/sides/publicdomainset.noisy/"

# where to put the results
TEST_RESULTS_DIR=$PROJ_ROOT"/testresults"
TEST_RESULTS_DIR_FB=$PROJ_ROOT"/testresults/frontbacks/"
TEST_RESULTS_DIR_S=$PROJ_ROOT"/testresults/sides/"

LOG_RESULTS_DIR=$TEST_RESULTS_DIR
IMG_RESULTS_DIR=$TEST_RESULTS_DIR

# path to trained classifiers
CLASSIFIER_DIR_S=$PROJ_ROOT"/trained_classifiers/sides"
CLASSIFIER_DIR_FB=$PROJ_ROOT"/trained_classifiers/sides"

# path to groundtruth labelled data
LABELLED_DATA_DIR_FB=$TESTDATA_DIR"/frontbacks/labelled.groundtruths"
LABELLED_DATA_DIR_S=$TESTDATA_DIR"/sides/labelled.groundtruths"

# the colorspace to detect in (default should be $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE others mightnt be accurate.)
COLORSPACE="gray"


# ########## BELOW WILL RUN THE DETECTIONS ########
#
# ########  training set detection ##############
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET $CLASSIFIER_DIR_FB"/haar.gab.24x20s.xml" $LABELLED_DATA_DIR_FB"/trainingset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET $CLASSIFIER_DIR_FB"/haar.rab.24x20s.xml" $LABELLED_DATA_DIR_FB"/trainingset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET $CLASSIFIER_DIR_FB"/hog.gab.24x20s.xml" $LABELLED_DATA_DIR_FB"/trainingset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET $CLASSIFIER_DIR_FB"/hog.rab.24x20s.xml" $LABELLED_DATA_DIR_FB"/trainingset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET $CLASSIFIER_DIR_FB"/lbp.gab.24x20s.xml" $LABELLED_DATA_DIR_FB"/trainingset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET $CLASSIFIER_DIR_FB"/lbp.rab.24x20s.xml" $LABELLED_DATA_DIR_FB"/trainingset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET $CLASSIFIER_DIR_FB"/cars3.xml" $LABELLED_DATA_DIR_FB"/trainingset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# #
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET $CLASSIFIER_DIR_FB"/haar.gab.24x20s.xml" $LABELLED_DATA_DIR_FB"/trainingset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET $CLASSIFIER_DIR_FB"/haar.rab.24x20s.xml" $LABELLED_DATA_DIR_FB"/trainingset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET $CLASSIFIER_DIR_FB"/hog.gab.24x20s.xml" $LABELLED_DATA_DIR_FB"/trainingset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET $CLASSIFIER_DIR_FB"/hog.rab.24x20s.xml" $LABELLED_DATA_DIR_FB"/trainingset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET $CLASSIFIER_DIR_FB"/lbp.gab.24x20s.xml" $LABELLED_DATA_DIR_FB"/trainingset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET $CLASSIFIER_DIR_FB"/lbp.rab.24x20s.xml" $LABELLED_DATA_DIR_FB"/trainingset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET $CLASSIFIER_DIR_FB"/cars3.xml" $LABELLED_DATA_DIR_FB"/trainingset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
#
# # 35
# # python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET $LABELLED_DATA_DIR_FB"/classifiers/lbp.gab.24x35s.xml $LABELLED_DATA_DIR_FB"/trainingset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# # python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET $LABELLED_DATA_DIR_FB"/classifiers/lbp.rab.24x35s.xml $LABELLED_DATA_DIR_FB"/trainingset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# #
# #
# #########  testing set detection ##############
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET $CLASSIFIER_DIR_FB"/haar.gab.24x20s.xml" $LABELLED_DATA_DIR_FB"/testset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET $CLASSIFIER_DIR_FB"/haar.rab.24x20s.xml" $LABELLED_DATA_DIR_FB"/testset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET $CLASSIFIER_DIR_FB"/hog.gab.24x20s.xml" $LABELLED_DATA_DIR_FB"/testset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET $CLASSIFIER_DIR_FB"/hog.rab.24x20s.xml" $LABELLED_DATA_DIR_FB"/testset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET $CLASSIFIER_DIR_FB"/lbp.gab.24x20s.xml" $LABELLED_DATA_DIR_FB"/testset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET $CLASSIFIER_DIR_FB"/lbp.rab.24x20s.xml" $LABELLED_DATA_DIR_FB"/testset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET $CLASSIFIER_DIR_FB"/cars3.xml" $LABELLED_DATA_DIR_FB"/testset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
#
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET $CLASSIFIER_DIR_FB"/haar.gab.24x20s.xml" $LABELLED_DATA_DIR_FB"/testset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET $CLASSIFIER_DIR_FB"/haar.rab.24x20s.xml" $LABELLED_DATA_DIR_FB"/testset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET $CLASSIFIER_DIR_FB"/hog.gab.24x20s.xml" $LABELLED_DATA_DIR_FB"/testset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET $CLASSIFIER_DIR_FB"/hog.rab.24x20s.xml" $LABELLED_DATA_DIR_FB"/testset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET $CLASSIFIER_DIR_FB"/lbp.gab.24x20s.xml" $LABELLED_DATA_DIR_FB"/testset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET $CLASSIFIER_DIR_FB"/lbp.rab.24x20s.xml" $LABELLED_DATA_DIR_FB"/testset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET $CLASSIFIER_DIR_FB"/cars3.xml" $LABELLED_DATA_DIR_FB"/testset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
#
# # 35
# # python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET $LABELLED_DATA_DIR_FB"/classifiers/lbp.gab.24x35s.xml $LABELLED_DATA_DIR_FB"/testset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# # python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET $LABELLED_DATA_DIR_FB"/classifiers/lbp.rab.24x35s.xml $LABELLED_DATA_DIR_FB"/testset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
#
#
# ####### public domain set detection ##########
# #
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_PDSET $CLASSIFIER_DIR_FB"/haar.gab.24x20s.xml" $LABELLED_DATA_DIR_FB"/publicdomainset_25.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_PDSET $CLASSIFIER_DIR_FB"/haar.rab.24x20s.xml" $LABELLED_DATA_DIR_FB"/publicdomainset_25.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_PDSET $CLASSIFIER_DIR_FB"/hog.gab.24x20s.xml" $LABELLED_DATA_DIR_FB"/publicdomainset_25.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_PDSET $CLASSIFIER_DIR_FB"/hog.rab.24x20s.xml" $LABELLED_DATA_DIR_FB"/publicdomainset_25.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_PDSET $CLASSIFIER_DIR_FB"/lbp.gab.24x20s.xml" $LABELLED_DATA_DIR_FB"/publicdomainset_25.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_PDSET $CLASSIFIER_DIR_FB"/lbp.rab.24x20s.xml" $LABELLED_DATA_DIR_FB"/publicdomainset_25.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_PDSET $CLASSIFIER_DIR_FB"/cars3.xml" $LABELLED_DATA_DIR_FB"/publicdomainset_25.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
#
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_PDSET $CLASSIFIER_DIR_FB"/haar.gab.24x20s.xml" $LABELLED_DATA_DIR_FB"/publicdomainset_25.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_PDSET $CLASSIFIER_DIR_FB"/haar.rab.24x20s.xml" $LABELLED_DATA_DIR_FB"/publicdomainset_25.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_PDSET $CLASSIFIER_DIR_FB"/hog.gab.24x20s.xml" $LABELLED_DATA_DIR_FB"/publicdomainset_25.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_PDSET $CLASSIFIER_DIR_FB"/hog.rab.24x20s.xml" $LABELLED_DATA_DIR_FB"/publicdomainset_25.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_PDSET $CLASSIFIER_DIR_FB"/lbp.gab.24x20s.xml" $LABELLED_DATA_DIR_FB"/publicdomainset_25.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_PDSET $CLASSIFIER_DIR_FB"/lbp.rab.24x20s.xml" $LABELLED_DATA_DIR_FB"/publicdomainset_25.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_PDSET $CLASSIFIER_DIR_FB"/cars3.xml" $LABELLED_DATA_DIR_FB"/publicdomainset_25.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
#
# # 35
# # python $DETECT_SCRIPT $TESTDATA_IMG_FB_PDSET $LABELLED_DATA_DIR_FB"/classifiers/lbp.gab.24x35s.xml $LABELLED_DATA_DIR_FB"/publicdomainset_25.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# #
# #
#
#
# ####### noisy sets ########## MN2
# # public domain set
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_PDSET_NOISY $CLASSIFIER_DIR_FB"/haar.rab.24x20s.xml" $LABELLED_DATA_DIR_FB"/publicdomainset_25.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_PDSET_NOISY $CLASSIFIER_DIR_FB"/hog.rab.24x20s.xml" $LABELLED_DATA_DIR_FB"/publicdomainset_25.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_PDSET_NOISY $CLASSIFIER_DIR_FB"/lbp.rab.24x20s.xml" $LABELLED_DATA_DIR_FB"/publicdomainset_25.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_PDSET_NOISY $CLASSIFIER_DIR_FB"/haar.gab.24x20s.xml" $LABELLED_DATA_DIR_FB"/publicdomainset_25.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_PDSET_NOISY $CLASSIFIER_DIR_FB"/hog.gab.24x20s.xml" $LABELLED_DATA_DIR_FB"/publicdomainset_25.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_PDSET_NOISY $CLASSIFIER_DIR_FB"/lbp.gab.24x20s.xml" $LABELLED_DATA_DIR_FB"/publicdomainset_25.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_PDSET_NOISY $CLASSIFIER_DIR_FB"/cars3.xml" $LABELLED_DATA_DIR_FB"/publicdomainset_25.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
#
# # test set
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET_NOISY $CLASSIFIER_DIR_FB"/haar.rab.24x20s.xml" $LABELLED_DATA_DIR_FB"/testset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET_NOISY $CLASSIFIER_DIR_FB"/hog.rab.24x20s.xml" $LABELLED_DATA_DIR_FB"/testset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET_NOISY $CLASSIFIER_DIR_FB"/lbp.rab.24x20s.xml" $LABELLED_DATA_DIR_FB"/testset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET_NOISY $CLASSIFIER_DIR_FB"/haar.gab.24x20s.xml" $LABELLED_DATA_DIR_FB"/testset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET_NOISY $CLASSIFIER_DIR_FB"/hog.gab.24x20s.xml" $LABELLED_DATA_DIR_FB"/testset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET_NOISY $CLASSIFIER_DIR_FB"/lbp.gab.24x20s.xml" $LABELLED_DATA_DIR_FB"/testset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET_NOISY $CLASSIFIER_DIR_FB"/cars3.xml" $LABELLED_DATA_DIR_FB"/testset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
#
# # training set
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET_NOISY $CLASSIFIER_DIR_FB"/haar.rab.24x20s.xml" $LABELLED_DATA_DIR_FB"/trainingset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET_NOISY $CLASSIFIER_DIR_FB"/hog.rab.24x20s.xml" $LABELLED_DATA_DIR_FB"/trainingset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET_NOISY $CLASSIFIER_DIR_FB"/lbp.rab.24x20s.xml" $LABELLED_DATA_DIR_FB"/trainingset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET_NOISY $CLASSIFIER_DIR_FB"/haar.gab.24x20s.xml" $LABELLED_DATA_DIR_FB"/trainingset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET_NOISY $CLASSIFIER_DIR_FB"/hog.gab.24x20s.xml" $LABELLED_DATA_DIR_FB"/trainingset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET_NOISY $CLASSIFIER_DIR_FB"/lbp.gab.24x20s.xml" $LABELLED_DATA_DIR_FB"/trainingset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET_NOISY $CLASSIFIER_DIR_FB"/cars3.xml" $LABELLED_DATA_DIR_FB"/trainingset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
#
# ####### noisy sets ########## MN5
# # public domain set
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_PDSET_NOISY $CLASSIFIER_DIR_FB"/haar.rab.24x20s.xml" $LABELLED_DATA_DIR_FB"/publicdomainset_25.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_PDSET_NOISY $CLASSIFIER_DIR_FB"/hog.rab.24x20s.xml" $LABELLED_DATA_DIR_FB"/publicdomainset_25.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_PDSET_NOISY $CLASSIFIER_DIR_FB"/lbp.rab.24x20s.xml" $LABELLED_DATA_DIR_FB"/publicdomainset_25.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_PDSET_NOISY $CLASSIFIER_DIR_FB"/haar.gab.24x20s.xml" $LABELLED_DATA_DIR_FB"/publicdomainset_25.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_PDSET_NOISY $CLASSIFIER_DIR_FB"/hog.gab.24x20s.xml" $LABELLED_DATA_DIR_FB"/publicdomainset_25.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_PDSET_NOISY $CLASSIFIER_DIR_FB"/lbp.gab.24x20s.xml" $LABELLED_DATA_DIR_FB"/publicdomainset_25.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_PDSET_NOISY $CLASSIFIER_DIR_FB"/cars3.xml" $LABELLED_DATA_DIR_FB"/publicdomainset_25.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
#
# # test set
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET_NOISY $CLASSIFIER_DIR_FB"/haar.rab.24x20s.xml" $LABELLED_DATA_DIR_FB"/testset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET_NOISY $CLASSIFIER_DIR_FB"/hog.rab.24x20s.xml" $LABELLED_DATA_DIR_FB"/testset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET_NOISY $CLASSIFIER_DIR_FB"/lbp.rab.24x20s.xml" $LABELLED_DATA_DIR_FB"/testset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET_NOISY $CLASSIFIER_DIR_FB"/haar.gab.24x20s.xml" $LABELLED_DATA_DIR_FB"/testset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET_NOISY $CLASSIFIER_DIR_FB"/hog.gab.24x20s.xml" $LABELLED_DATA_DIR_FB"/testset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET_NOISY $CLASSIFIER_DIR_FB"/lbp.gab.24x20s.xml" $LABELLED_DATA_DIR_FB"/testset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET_NOISY $CLASSIFIER_DIR_FB"/cars3.xml" $LABELLED_DATA_DIR_FB"/testset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
#
# # training set
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET_NOISY $CLASSIFIER_DIR_FB"/haar.rab.24x20s.xml" $LABELLED_DATA_DIR_FB"/trainingset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET_NOISY $CLASSIFIER_DIR_FB"/hog.rab.24x20s.xml" $LABELLED_DATA_DIR_FB"/trainingset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET_NOISY $CLASSIFIER_DIR_FB"/lbp.rab.24x20s.xml" $LABELLED_DATA_DIR_FB"/trainingset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET_NOISY $CLASSIFIER_DIR_FB"/haar.gab.24x20s.xml" $LABELLED_DATA_DIR_FB"/trainingset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET_NOISY $CLASSIFIER_DIR_FB"/hog.gab.24x20s.xml" $LABELLED_DATA_DIR_FB"/trainingset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET_NOISY $CLASSIFIER_DIR_FB"/lbp.gab.24x20s.xml" $LABELLED_DATA_DIR_FB"/trainingset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET_NOISY $CLASSIFIER_DIR_FB"/cars3.xml" $LABELLED_DATA_DIR_FB"/trainingset_100.txt" $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F





############### DO SAME TESTS FOR SIDES ###############

########## BELOW WILL RUN THE DETECTIONS ########

# ########  training set detection ##############
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TRAINSET $CLASSIFIER_DIR_S"/haar.gab.24x20s.xml" $LABELLED_DATA_DIR_S"/trainingset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TRAINSET $CLASSIFIER_DIR_S"/haar.rab.24x20s.xml" $LABELLED_DATA_DIR_S"/trainingset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TRAINSET $CLASSIFIER_DIR_S"/hog.gab.24x20s.xml" $LABELLED_DATA_DIR_S"/trainingset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TRAINSET $CLASSIFIER_DIR_S"/hog.rab.24x20s.xml" $LABELLED_DATA_DIR_S"/trainingset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TRAINSET $CLASSIFIER_DIR_S"/lbp.gab.24x20s.xml" $LABELLED_DATA_DIR_S"/trainingset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TRAINSET $CLASSIFIER_DIR_S"/lbp.rab.24x20s.xml" $LABELLED_DATA_DIR_S"/trainingset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TRAINSET $CLASSIFIER_DIR_S"/cars3.xml" $LABELLED_DATA_DIR_S"/trainingset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# #
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TRAINSET $CLASSIFIER_DIR_S"/haar.gab.24x20s.xml" $LABELLED_DATA_DIR_S"/trainingset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TRAINSET $CLASSIFIER_DIR_S"/haar.rab.24x20s.xml" $LABELLED_DATA_DIR_S"/trainingset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TRAINSET $CLASSIFIER_DIR_S"/hog.gab.24x20s.xml" $LABELLED_DATA_DIR_S"/trainingset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TRAINSET $CLASSIFIER_DIR_S"/hog.rab.24x20s.xml" $LABELLED_DATA_DIR_S"/trainingset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TRAINSET $CLASSIFIER_DIR_S"/lbp.gab.24x20s.xml" $LABELLED_DATA_DIR_S"/trainingset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TRAINSET $CLASSIFIER_DIR_S"/lbp.rab.24x20s.xml" $LABELLED_DATA_DIR_S"/trainingset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TRAINSET $CLASSIFIER_DIR_S"/cars3.xml" $LABELLED_DATA_DIR_S"/trainingset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
#
# # 35
# # python $DETECT_SCRIPT $TESTDATA_IMG_S_TRAINSET $LABELLED_DATA_DIR_S"/classifiers/lbp.gab.24x35s.xml $LABELLED_DATA_DIR_S"/trainingset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# # python $DETECT_SCRIPT $TESTDATA_IMG_S_TRAINSET $LABELLED_DATA_DIR_S"/classifiers/lbp.rab.24x35s.xml $LABELLED_DATA_DIR_S"/trainingset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# #
# #
# #########  testing set detection ##############
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET $CLASSIFIER_DIR_S"/haar.gab.24x20s.xml" $LABELLED_DATA_DIR_S"/testset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET $CLASSIFIER_DIR_S"/haar.rab.24x20s.xml" $LABELLED_DATA_DIR_S"/testset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET $CLASSIFIER_DIR_S"/hog.gab.24x20s.xml" $LABELLED_DATA_DIR_S"/testset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET $CLASSIFIER_DIR_S"/hog.rab.24x20s.xml" $LABELLED_DATA_DIR_S"/testset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET $CLASSIFIER_DIR_S"/lbp.gab.24x20s.xml" $LABELLED_DATA_DIR_S"/testset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET $CLASSIFIER_DIR_S"/lbp.rab.24x20s.xml" $LABELLED_DATA_DIR_S"/testset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET $CLASSIFIER_DIR_S"/cars3.xml" $LABELLED_DATA_DIR_S"/testset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
#
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET $CLASSIFIER_DIR_S"/haar.gab.24x20s.xml" $LABELLED_DATA_DIR_S"/testset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET $CLASSIFIER_DIR_S"/haar.rab.24x20s.xml" $LABELLED_DATA_DIR_S"/testset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET $CLASSIFIER_DIR_S"/hog.gab.24x20s.xml" $LABELLED_DATA_DIR_S"/testset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET $CLASSIFIER_DIR_S"/hog.rab.24x20s.xml" $LABELLED_DATA_DIR_S"/testset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET $CLASSIFIER_DIR_S"/lbp.gab.24x20s.xml" $LABELLED_DATA_DIR_S"/testset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET $CLASSIFIER_DIR_S"/lbp.rab.24x20s.xml" $LABELLED_DATA_DIR_S"/testset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET $CLASSIFIER_DIR_S"/cars3.xml" $LABELLED_DATA_DIR_S"/testset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
#
# # 35
# # python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET $LABELLED_DATA_DIR_S"/classifiers/lbp.gab.24x35s.xml $LABELLED_DATA_DIR_S"/testset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# # python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET $LABELLED_DATA_DIR_S"/classifiers/lbp.rab.24x35s.xml $LABELLED_DATA_DIR_S"/testset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
#
#
# ####### public domain set detection ##########
# #
# python $DETECT_SCRIPT $TESTDATA_IMG_S_PDSET $CLASSIFIER_DIR_S"/haar.gab.24x20s.xml" $LABELLED_DATA_DIR_S"/publicdomainset_25.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_PDSET $CLASSIFIER_DIR_S"/haar.rab.24x20s.xml" $LABELLED_DATA_DIR_S"/publicdomainset_25.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_PDSET $CLASSIFIER_DIR_S"/hog.gab.24x20s.xml" $LABELLED_DATA_DIR_S"/publicdomainset_25.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_PDSET $CLASSIFIER_DIR_S"/hog.rab.24x20s.xml" $LABELLED_DATA_DIR_S"/publicdomainset_25.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_PDSET $CLASSIFIER_DIR_S"/lbp.gab.24x20s.xml" $LABELLED_DATA_DIR_S"/publicdomainset_25.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_PDSET $CLASSIFIER_DIR_S"/lbp.rab.24x20s.xml" $LABELLED_DATA_DIR_S"/publicdomainset_25.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_PDSET $CLASSIFIER_DIR_S"/cars3.xml" $LABELLED_DATA_DIR_S"/publicdomainset_25.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
#
# python $DETECT_SCRIPT $TESTDATA_IMG_S_PDSET $CLASSIFIER_DIR_S"/haar.gab.24x20s.xml" $LABELLED_DATA_DIR_S"/publicdomainset_25.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_PDSET $CLASSIFIER_DIR_S"/haar.rab.24x20s.xml" $LABELLED_DATA_DIR_S"/publicdomainset_25.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_PDSET $CLASSIFIER_DIR_S"/hog.gab.24x20s.xml" $LABELLED_DATA_DIR_S"/publicdomainset_25.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_PDSET $CLASSIFIER_DIR_S"/hog.rab.24x20s.xml" $LABELLED_DATA_DIR_S"/publicdomainset_25.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_PDSET $CLASSIFIER_DIR_S"/lbp.gab.24x20s.xml" $LABELLED_DATA_DIR_S"/publicdomainset_25.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_PDSET $CLASSIFIER_DIR_S"/lbp.rab.24x20s.xml" $LABELLED_DATA_DIR_S"/publicdomainset_25.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_PDSET $CLASSIFIER_DIR_S"/cars3.xml" $LABELLED_DATA_DIR_S"/publicdomainset_25.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
#
# # 35
# # python $DETECT_SCRIPT $TESTDATA_IMG_S_PDSET $LABELLED_DATA_DIR_S"/classifiers/lbp.gab.24x35s.xml $LABELLED_DATA_DIR_S"/publicdomainset_25.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# #
# #
#
#
# ####### noisy sets ########## MN2
# # public domain set
# python $DETECT_SCRIPT $TESTDATA_IMG_S_PDSET_NOISY $CLASSIFIER_DIR_S"/haar.rab.24x20s.xml" $LABELLED_DATA_DIR_S"/publicdomainset_25.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_PDSET_NOISY $CLASSIFIER_DIR_S"/hog.rab.24x20s.xml" $LABELLED_DATA_DIR_S"/publicdomainset_25.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_PDSET_NOISY $CLASSIFIER_DIR_S"/lbp.rab.24x20s.xml" $LABELLED_DATA_DIR_S"/publicdomainset_25.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_PDSET_NOISY $CLASSIFIER_DIR_S"/haar.gab.24x20s.xml" $LABELLED_DATA_DIR_S"/publicdomainset_25.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_PDSET_NOISY $CLASSIFIER_DIR_S"/hog.gab.24x20s.xml" $LABELLED_DATA_DIR_S"/publicdomainset_25.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_PDSET_NOISY $CLASSIFIER_DIR_S"/lbp.gab.24x20s.xml" $LABELLED_DATA_DIR_S"/publicdomainset_25.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_PDSET_NOISY $CLASSIFIER_DIR_S"/cars3.xml" $LABELLED_DATA_DIR_S"/publicdomainset_25.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
#
# # test set
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET_NOISY $CLASSIFIER_DIR_S"/haar.rab.24x20s.xml" $LABELLED_DATA_DIR_S"/testset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET_NOISY $CLASSIFIER_DIR_S"/hog.rab.24x20s.xml" $LABELLED_DATA_DIR_S"/testset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET_NOISY $CLASSIFIER_DIR_S"/lbp.rab.24x20s.xml" $LABELLED_DATA_DIR_S"/testset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET_NOISY $CLASSIFIER_DIR_S"/haar.gab.24x20s.xml" $LABELLED_DATA_DIR_S"/testset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET_NOISY $CLASSIFIER_DIR_S"/hog.gab.24x20s.xml" $LABELLED_DATA_DIR_S"/testset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET_NOISY $CLASSIFIER_DIR_S"/lbp.gab.24x20s.xml" $LABELLED_DATA_DIR_S"/testset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET_NOISY $CLASSIFIER_DIR_S"/cars3.xml" $LABELLED_DATA_DIR_S"/testset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
#
# # training set
# python $DETECT_SCRIPT $LABELLED_DATA_DIR_S"/trainingset.noisy/"$CLASSIFIER_DIR_S"/haar.rab.24x20s.xml" $LABELLED_DATA_DIR_S"/trainingset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $LABELLED_DATA_DIR_S"/trainingset.noisy/"$CLASSIFIER_DIR_S"/hog.rab.24x20s.xml" $LABELLED_DATA_DIR_S"/trainingset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $LABELLED_DATA_DIR_S"/trainingset.noisy/"$CLASSIFIER_DIR_S"/lbp.rab.24x20s.xml" $LABELLED_DATA_DIR_S"/trainingset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $LABELLED_DATA_DIR_S"/trainingset.noisy/"$CLASSIFIER_DIR_S"/haar.gab.24x20s.xml" $LABELLED_DATA_DIR_S"/trainingset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $LABELLED_DATA_DIR_S"/trainingset.noisy/"$CLASSIFIER_DIR_S"/hog.gab.24x20s.xml" $LABELLED_DATA_DIR_S"/trainingset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $LABELLED_DATA_DIR_S"/trainingset.noisy/"$CLASSIFIER_DIR_S"/lbp.gab.24x20s.xml" $LABELLED_DATA_DIR_S"/trainingset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $LABELLED_DATA_DIR_S"/trainingset.noisy/"$CLASSIFIER_DIR_S"/cars3.xml" $LABELLED_DATA_DIR_S"/trainingset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
#
# ####### noisy sets ########## MN5
# # public domain set
# python $DETECT_SCRIPT $TESTDATA_IMG_S_PDSET_NOISY $CLASSIFIER_DIR_S"/haar.rab.24x20s.xml" $LABELLED_DATA_DIR_S"/publicdomainset_25.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_PDSET_NOISY $CLASSIFIER_DIR_S"/hog.rab.24x20s.xml" $LABELLED_DATA_DIR_S"/publicdomainset_25.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_PDSET_NOISY $CLASSIFIER_DIR_S"/lbp.rab.24x20s.xml" $LABELLED_DATA_DIR_S"/publicdomainset_25.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_PDSET_NOISY $CLASSIFIER_DIR_S"/haar.gab.24x20s.xml" $LABELLED_DATA_DIR_S"/publicdomainset_25.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_PDSET_NOISY $CLASSIFIER_DIR_S"/hog.gab.24x20s.xml" $LABELLED_DATA_DIR_S"/publicdomainset_25.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_PDSET_NOISY $CLASSIFIER_DIR_S"/lbp.gab.24x20s.xml" $LABELLED_DATA_DIR_S"/publicdomainset_25.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_PDSET_NOISY $CLASSIFIER_DIR_S"/cars3.xml" $LABELLED_DATA_DIR_S"/publicdomainset_25.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
#
# # test set
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET_NOISY $CLASSIFIER_DIR_S"/haar.rab.24x20s.xml" $LABELLED_DATA_DIR_S"/testset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET_NOISY $CLASSIFIER_DIR_S"/hog.rab.24x20s.xml" $LABELLED_DATA_DIR_S"/testset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET_NOISY $CLASSIFIER_DIR_S"/lbp.rab.24x20s.xml" $LABELLED_DATA_DIR_S"/testset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET_NOISY $CLASSIFIER_DIR_S"/haar.gab.24x20s.xml" $LABELLED_DATA_DIR_S"/testset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET_NOISY $CLASSIFIER_DIR_S"/hog.gab.24x20s.xml" $LABELLED_DATA_DIR_S"/testset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET_NOISY $CLASSIFIER_DIR_S"/lbp.gab.24x20s.xml" $LABELLED_DATA_DIR_S"/testset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET_NOISY $CLASSIFIER_DIR_S"/cars3.xml" $LABELLED_DATA_DIR_S"/testset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
#
# # training set
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TRAINSET_NOISY $CLASSIFIER_DIR_S"/haar.rab.24x20s.xml" $LABELLED_DATA_DIR_S"/trainingset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TRAINSET_NOISY $CLASSIFIER_DIR_S"/hog.rab.24x20s.xml" $LABELLED_DATA_DIR_S"/trainingset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TRAINSET_NOISY $CLASSIFIER_DIR_S"/lbp.rab.24x20s.xml" $LABELLED_DATA_DIR_S"/trainingset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TRAINSET_NOISY $CLASSIFIER_DIR_S"/haar.gab.24x20s.xml" $LABELLED_DATA_DIR_S"/trainingset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TRAINSET_NOISY $CLASSIFIER_DIR_S"/hog.gab.24x20s.xml" $LABELLED_DATA_DIR_S"/trainingset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TRAINSET_NOISY $CLASSIFIER_DIR_S"/lbp.gab.24x20s.xml" $LABELLED_DATA_DIR_S"/trainingset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TRAINSET_NOISY $CLASSIFIER_DIR_S"/cars3.xml" $LABELLED_DATA_DIR_S"/trainingset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET $CLASSIFIER_DIR_S"/cars3.xml" $LABELLED_DATA_DIR_S"/uiuc_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S

# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET $CLASSIFIER_DIR_S"/haar.gab.24x16s_side.xml" $LABELLED_DATA_DIR_S"/uiuc_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TRAINSET $CLASSIFIER_DIR_S"/haar.gab.24x16s_side.xml" $LABELLED_DATA_DIR_S"/uiuc_trainset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET $CLASSIFIER_DIR_S"/hog.gab.24x20s_side.xml" $LABELLED_DATA_DIR_S"/uiuc_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
python $DETECT_SCRIPT $TESTDATA_IMG_S_TRAINSET $CLASSIFIER_DIR_S"/hog.gab.24x20s_side.xml" $LABELLED_DATA_DIR_S"/uiuc_trainset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
