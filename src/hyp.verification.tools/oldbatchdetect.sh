# ########## BELOW WILL RUN THE DETECTIONS ########
#
# ########  training set detection ##############
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET $CLASSIFIER_DIR_FB"/haar.gab.24x20s.xml" $LABELLED_DATA_DIR_FB_TRAIN $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET $CLASSIFIER_DIR_FB"/haar.rab.24x20s.xml" $LABELLED_DATA_DIR_FB_TRAIN $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET $CLASSIFIER_DIR_FB"/hog.gab.24x20s.xml" $LABELLED_DATA_DIR_FB_TRAIN $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET $CLASSIFIER_DIR_FB"/hog.rab.24x20s.xml" $LABELLED_DATA_DIR_FB_TRAIN $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET $CLASSIFIER_DIR_FB"/lbp.gab.24x20s.xml" $LABELLED_DATA_DIR_FB_TRAIN $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET $CLASSIFIER_DIR_FB"/lbp.rab.24x20s.xml" $LABELLED_DATA_DIR_FB_TRAIN $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET $CLASSIFIER_DIR_FB"/cars3.xml" $LABELLED_DATA_DIR_FB_TRAIN $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# #
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET $CLASSIFIER_DIR_FB"/haar.gab.24x20s.xml" $LABELLED_DATA_DIR_FB_TRAIN $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET $CLASSIFIER_DIR_FB"/haar.rab.24x20s.xml" $LABELLED_DATA_DIR_FB_TRAIN $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET $CLASSIFIER_DIR_FB"/hog.gab.24x20s.xml" $LABELLED_DATA_DIR_FB_TRAIN $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET $CLASSIFIER_DIR_FB"/hog.rab.24x20s.xml" $LABELLED_DATA_DIR_FB_TRAIN $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET $CLASSIFIER_DIR_FB"/lbp.gab.24x20s.xml" $LABELLED_DATA_DIR_FB_TRAIN $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET $CLASSIFIER_DIR_FB"/lbp.rab.24x20s.xml" $LABELLED_DATA_DIR_FB_TRAIN $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET $CLASSIFIER_DIR_FB"/cars3.xml" $LABELLED_DATA_DIR_FB_TRAIN $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
#
# # 35
# # python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET $LABELLED_DATA_DIR_FB"/classifiers/lbp.gab.24x35s.xml $LABELLED_DATA_DIR_FB_TRAIN $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# # python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET $LABELLED_DATA_DIR_FB"/classifiers/lbp.rab.24x35s.xml $LABELLED_DATA_DIR_FB_TRAIN $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# #
# #
# #########  testing set detection ##############
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET $CLASSIFIER_DIR_FB"/haar.gab.24x20s.xml" $LABELLED_DATA_DIR_FB_TEST $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET $CLASSIFIER_DIR_FB"/haar.rab.24x20s.xml" $LABELLED_DATA_DIR_FB_TEST $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET $CLASSIFIER_DIR_FB"/hog.gab.24x20s.xml" $LABELLED_DATA_DIR_FB_TEST $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET $CLASSIFIER_DIR_FB"/hog.rab.24x20s.xml" $LABELLED_DATA_DIR_FB_TEST $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET $CLASSIFIER_DIR_FB"/lbp.gab.24x20s.xml" $LABELLED_DATA_DIR_FB_TEST $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET $CLASSIFIER_DIR_FB"/lbp.rab.24x20s.xml" $LABELLED_DATA_DIR_FB_TEST $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET $CLASSIFIER_DIR_FB"/cars3.xml" $LABELLED_DATA_DIR_FB_TEST $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
#
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET $CLASSIFIER_DIR_FB"/haar.gab.24x20s.xml" $LABELLED_DATA_DIR_FB_TEST $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET $CLASSIFIER_DIR_FB"/haar.rab.24x20s.xml" $LABELLED_DATA_DIR_FB_TEST $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET $CLASSIFIER_DIR_FB"/hog.gab.24x20s.xml" $LABELLED_DATA_DIR_FB_TEST $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET $CLASSIFIER_DIR_FB"/hog.rab.24x20s.xml" $LABELLED_DATA_DIR_FB_TEST $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET $CLASSIFIER_DIR_FB"/lbp.gab.24x20s.xml" $LABELLED_DATA_DIR_FB_TEST $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET $CLASSIFIER_DIR_FB"/lbp.rab.24x20s.xml" $LABELLED_DATA_DIR_FB_TEST $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET $CLASSIFIER_DIR_FB"/cars3.xml" $LABELLED_DATA_DIR_FB_TEST $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
#
# # 35
# # python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET $LABELLED_DATA_DIR_FB"/classifiers/lbp.gab.24x35s.xml $LABELLED_DATA_DIR_FB_TEST $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# # python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET $LABELLED_DATA_DIR_FB"/classifiers/lbp.rab.24x35s.xml $LABELLED_DATA_DIR_FB_TEST $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
#
#
# ####### public domain set detection ##########
# #
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_PDSET $CLASSIFIER_DIR_FB"/haar.gab.24x20s.xml" $LABELLED_DATA_DIR_FB_PD $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_PDSET $CLASSIFIER_DIR_FB"/haar.rab.24x20s.xml" $LABELLED_DATA_DIR_FB_PD $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_PDSET $CLASSIFIER_DIR_FB"/hog.gab.24x20s.xml" $LABELLED_DATA_DIR_FB_PD $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_PDSET $CLASSIFIER_DIR_FB"/hog.rab.24x20s.xml" $LABELLED_DATA_DIR_FB_PD $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_PDSET $CLASSIFIER_DIR_FB"/lbp.gab.24x20s.xml" $LABELLED_DATA_DIR_FB_PD $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_PDSET $CLASSIFIER_DIR_FB"/lbp.rab.24x20s.xml" $LABELLED_DATA_DIR_FB_PD $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_PDSET $CLASSIFIER_DIR_FB"/cars3.xml" $LABELLED_DATA_DIR_FB_PD $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
#
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_PDSET $CLASSIFIER_DIR_FB"/haar.gab.24x20s.xml" $LABELLED_DATA_DIR_FB_PD $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_PDSET $CLASSIFIER_DIR_FB"/haar.rab.24x20s.xml" $LABELLED_DATA_DIR_FB_PD $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_PDSET $CLASSIFIER_DIR_FB"/hog.gab.24x20s.xml" $LABELLED_DATA_DIR_FB_PD $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_PDSET $CLASSIFIER_DIR_FB"/hog.rab.24x20s.xml" $LABELLED_DATA_DIR_FB_PD $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_PDSET $CLASSIFIER_DIR_FB"/lbp.gab.24x20s.xml" $LABELLED_DATA_DIR_FB_PD $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_PDSET $CLASSIFIER_DIR_FB"/lbp.rab.24x20s.xml" $LABELLED_DATA_DIR_FB_PD $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_PDSET $CLASSIFIER_DIR_FB"/cars3.xml" $LABELLED_DATA_DIR_FB_PD $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
#
# # 35
# # python $DETECT_SCRIPT $TESTDATA_IMG_FB_PDSET $LABELLED_DATA_DIR_FB"/classifiers/lbp.gab.24x35s.xml $LABELLED_DATA_DIR_FB_PD $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# #
# #
#
#
# ####### noisy sets ########## MN2
# # public domain set
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_PDSET_NOISY $CLASSIFIER_DIR_FB"/haar.rab.24x20s.xml" $LABELLED_DATA_DIR_FB_PD $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_PDSET_NOISY $CLASSIFIER_DIR_FB"/hog.rab.24x20s.xml" $LABELLED_DATA_DIR_FB_PD $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_PDSET_NOISY $CLASSIFIER_DIR_FB"/lbp.rab.24x20s.xml" $LABELLED_DATA_DIR_FB_PD $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_PDSET_NOISY $CLASSIFIER_DIR_FB"/haar.gab.24x20s.xml" $LABELLED_DATA_DIR_FB_PD $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_PDSET_NOISY $CLASSIFIER_DIR_FB"/hog.gab.24x20s.xml" $LABELLED_DATA_DIR_FB_PD $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_PDSET_NOISY $CLASSIFIER_DIR_FB"/lbp.gab.24x20s.xml" $LABELLED_DATA_DIR_FB_PD $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_PDSET_NOISY $CLASSIFIER_DIR_FB"/cars3.xml" $LABELLED_DATA_DIR_FB_PD $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
#
# # test set
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET_NOISY $CLASSIFIER_DIR_FB"/haar.rab.24x20s.xml" $LABELLED_DATA_DIR_FB_TEST $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET_NOISY $CLASSIFIER_DIR_FB"/hog.rab.24x20s.xml" $LABELLED_DATA_DIR_FB_TEST $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET_NOISY $CLASSIFIER_DIR_FB"/lbp.rab.24x20s.xml" $LABELLED_DATA_DIR_FB_TEST $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET_NOISY $CLASSIFIER_DIR_FB"/haar.gab.24x20s.xml" $LABELLED_DATA_DIR_FB_TEST $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET_NOISY $CLASSIFIER_DIR_FB"/hog.gab.24x20s.xml" $LABELLED_DATA_DIR_FB_TEST $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET_NOISY $CLASSIFIER_DIR_FB"/lbp.gab.24x20s.xml" $LABELLED_DATA_DIR_FB_TEST $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET_NOISY $CLASSIFIER_DIR_FB"/cars3.xml" $LABELLED_DATA_DIR_FB_TEST $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
#
# # training set
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET_NOISY $CLASSIFIER_DIR_FB"/haar.rab.24x20s.xml" $LABELLED_DATA_DIR_FB_TRAIN $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET_NOISY $CLASSIFIER_DIR_FB"/hog.rab.24x20s.xml" $LABELLED_DATA_DIR_FB_TRAIN $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET_NOISY $CLASSIFIER_DIR_FB"/lbp.rab.24x20s.xml" $LABELLED_DATA_DIR_FB_TRAIN $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET_NOISY $CLASSIFIER_DIR_FB"/haar.gab.24x20s.xml" $LABELLED_DATA_DIR_FB_TRAIN $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET_NOISY $CLASSIFIER_DIR_FB"/hog.gab.24x20s.xml" $LABELLED_DATA_DIR_FB_TRAIN $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET_NOISY $CLASSIFIER_DIR_FB"/lbp.gab.24x20s.xml" $LABELLED_DATA_DIR_FB_TRAIN $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET_NOISY $CLASSIFIER_DIR_FB"/cars3.xml" $LABELLED_DATA_DIR_FB_TRAIN $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
#
# ####### noisy sets ########## MN5
# # public domain set
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_PDSET_NOISY $CLASSIFIER_DIR_FB"/haar.rab.24x20s.xml" $LABELLED_DATA_DIR_FB_PD $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_PDSET_NOISY $CLASSIFIER_DIR_FB"/hog.rab.24x20s.xml" $LABELLED_DATA_DIR_FB_PD $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_PDSET_NOISY $CLASSIFIER_DIR_FB"/lbp.rab.24x20s.xml" $LABELLED_DATA_DIR_FB_PD $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_PDSET_NOISY $CLASSIFIER_DIR_FB"/haar.gab.24x20s.xml" $LABELLED_DATA_DIR_FB_PD $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_PDSET_NOISY $CLASSIFIER_DIR_FB"/hog.gab.24x20s.xml" $LABELLED_DATA_DIR_FB_PD $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_PDSET_NOISY $CLASSIFIER_DIR_FB"/lbp.gab.24x20s.xml" $LABELLED_DATA_DIR_FB_PD $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_PDSET_NOISY $CLASSIFIER_DIR_FB"/cars3.xml" $LABELLED_DATA_DIR_FB_PD $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
#
# # test set
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET_NOISY $CLASSIFIER_DIR_FB"/haar.rab.24x20s.xml" $LABELLED_DATA_DIR_FB_TEST $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET_NOISY $CLASSIFIER_DIR_FB"/hog.rab.24x20s.xml" $LABELLED_DATA_DIR_FB_TEST $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET_NOISY $CLASSIFIER_DIR_FB"/lbp.rab.24x20s.xml" $LABELLED_DATA_DIR_FB_TEST $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET_NOISY $CLASSIFIER_DIR_FB"/haar.gab.24x20s.xml" $LABELLED_DATA_DIR_FB_TEST $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET_NOISY $CLASSIFIER_DIR_FB"/hog.gab.24x20s.xml" $LABELLED_DATA_DIR_FB_TEST $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET_NOISY $CLASSIFIER_DIR_FB"/lbp.gab.24x20s.xml" $LABELLED_DATA_DIR_FB_TEST $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TESTSET_NOISY $CLASSIFIER_DIR_FB"/cars3.xml" $LABELLED_DATA_DIR_FB_TEST $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
#
# # training set
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET_NOISY $CLASSIFIER_DIR_FB"/haar.rab.24x20s.xml" $LABELLED_DATA_DIR_FB_TRAIN $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET_NOISY $CLASSIFIER_DIR_FB"/hog.rab.24x20s.xml" $LABELLED_DATA_DIR_FB_TRAIN $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET_NOISY $CLASSIFIER_DIR_FB"/lbp.rab.24x20s.xml" $LABELLED_DATA_DIR_FB_TRAIN $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET_NOISY $CLASSIFIER_DIR_FB"/haar.gab.24x20s.xml" $LABELLED_DATA_DIR_FB_TRAIN $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET_NOISY $CLASSIFIER_DIR_FB"/hog.gab.24x20s.xml" $LABELLED_DATA_DIR_FB_TRAIN $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET_NOISY $CLASSIFIER_DIR_FB"/lbp.gab.24x20s.xml" $LABELLED_DATA_DIR_FB_TRAIN $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET_NOISY $CLASSIFIER_DIR_FB"/cars3.xml" $LABELLED_DATA_DIR_FB_TRAIN $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 5 F


# run all side tests.

for MN in {2..10..2}
	do
		python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET $CLASSIFIER_S_HAAR $LABELLED_DATA_DIR_S"/uiuc_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE $MN S
		python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET $CLASSIFIER_S_HOG $LABELLED_DATA_DIR_S"/uiuc_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE $MN S
		python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET $CLASSIFIER_S_LBP $LABELLED_DATA_DIR_S"/uiuc_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE $MN S
		break
done




############### DO SAME TESTS FOR SIDES ###############

########## BELOW WILL RUN THE DETECTIONS ########

# ########  training set detection ##############
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TRAINSET $CLASSIFIER_DIR_S"/haar.gab.24x20s.xml" $LABELLED_DATA_DIR_S_TRAIN $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TRAINSET $CLASSIFIER_DIR_S"/haar.rab.24x20s.xml" $LABELLED_DATA_DIR_S_TRAIN $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TRAINSET $CLASSIFIER_DIR_S"/hog.gab.24x20s.xml" $LABELLED_DATA_DIR_S_TRAIN $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TRAINSET $CLASSIFIER_DIR_S"/hog.rab.24x20s.xml" $LABELLED_DATA_DIR_S_TRAIN $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TRAINSET $CLASSIFIER_DIR_S"/lbp.gab.24x20s.xml" $LABELLED_DATA_DIR_S_TRAIN $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TRAINSET $CLASSIFIER_DIR_S"/lbp.rab.24x20s.xml" $LABELLED_DATA_DIR_S_TRAIN $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TRAINSET $CLASSIFIER_DIR_S"/cars3.xml" $LABELLED_DATA_DIR_S_TRAIN $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# #
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TRAINSET $CLASSIFIER_DIR_S"/haar.gab.24x20s.xml" $LABELLED_DATA_DIR_S_TRAIN $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TRAINSET $CLASSIFIER_DIR_S"/haar.rab.24x20s.xml" $LABELLED_DATA_DIR_S_TRAIN $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TRAINSET $CLASSIFIER_DIR_S"/hog.gab.24x20s.xml" $LABELLED_DATA_DIR_S_TRAIN $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TRAINSET $CLASSIFIER_DIR_S"/hog.rab.24x20s.xml" $LABELLED_DATA_DIR_S_TRAIN $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TRAINSET $CLASSIFIER_DIR_S"/lbp.gab.24x20s.xml" $LABELLED_DATA_DIR_S_TRAIN $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TRAINSET $CLASSIFIER_DIR_S"/lbp.rab.24x20s.xml" $LABELLED_DATA_DIR_S_TRAIN $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TRAINSET $CLASSIFIER_DIR_S"/cars3.xml" $LABELLED_DATA_DIR_S_TRAIN $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
#
# # 35
# # python $DETECT_SCRIPT $TESTDATA_IMG_S_TRAINSET $LABELLED_DATA_DIR_S"/classifiers/lbp.gab.24x35s.xml $LABELLED_DATA_DIR_S_TRAIN $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# # python $DETECT_SCRIPT $TESTDATA_IMG_S_TRAINSET $LABELLED_DATA_DIR_S"/classifiers/lbp.rab.24x35s.xml $LABELLED_DATA_DIR_S_TRAIN $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# #
# #
# #########  testing set detection ##############
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET $CLASSIFIER_DIR_S"/haar.gab.24x20s.xml" $LABELLED_DATA_DIR_S_TEST $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET $CLASSIFIER_DIR_S"/haar.rab.24x20s.xml" $LABELLED_DATA_DIR_S_TEST $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET $CLASSIFIER_DIR_S"/hog.gab.24x20s.xml" $LABELLED_DATA_DIR_S_TEST $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET $CLASSIFIER_DIR_S"/hog.rab.24x20s.xml" $LABELLED_DATA_DIR_S_TEST $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET $CLASSIFIER_DIR_S"/lbp.gab.24x20s.xml" $LABELLED_DATA_DIR_S_TEST $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET $CLASSIFIER_DIR_S"/lbp.rab.24x20s.xml" $LABELLED_DATA_DIR_S_TEST $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET $CLASSIFIER_DIR_S"/cars3.xml" $LABELLED_DATA_DIR_S_TEST $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
#
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET $CLASSIFIER_DIR_S"/haar.gab.24x20s.xml" $LABELLED_DATA_DIR_S_TEST $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET $CLASSIFIER_DIR_S"/haar.rab.24x20s.xml" $LABELLED_DATA_DIR_S_TEST $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET $CLASSIFIER_DIR_S"/hog.gab.24x20s.xml" $LABELLED_DATA_DIR_S_TEST $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET $CLASSIFIER_DIR_S"/hog.rab.24x20s.xml" $LABELLED_DATA_DIR_S_TEST $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET $CLASSIFIER_DIR_S"/lbp.gab.24x20s.xml" $LABELLED_DATA_DIR_S_TEST $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET $CLASSIFIER_DIR_S"/lbp.rab.24x20s.xml" $LABELLED_DATA_DIR_S_TEST $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET $CLASSIFIER_DIR_S"/cars3.xml" $LABELLED_DATA_DIR_S_TEST $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
#
# # 35
# # python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET $LABELLED_DATA_DIR_S"/classifiers/lbp.gab.24x35s.xml $LABELLED_DATA_DIR_S_TEST $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# # python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET $LABELLED_DATA_DIR_S"/classifiers/lbp.rab.24x35s.xml $LABELLED_DATA_DIR_S_TEST $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
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
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET_NOISY $CLASSIFIER_DIR_S"/haar.rab.24x20s.xml" $LABELLED_DATA_DIR_S_TEST $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET_NOISY $CLASSIFIER_DIR_S"/hog.rab.24x20s.xml" $LABELLED_DATA_DIR_S_TEST $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET_NOISY $CLASSIFIER_DIR_S"/lbp.rab.24x20s.xml" $LABELLED_DATA_DIR_S_TEST $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET_NOISY $CLASSIFIER_DIR_S"/haar.gab.24x20s.xml" $LABELLED_DATA_DIR_S_TEST $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET_NOISY $CLASSIFIER_DIR_S"/hog.gab.24x20s.xml" $LABELLED_DATA_DIR_S_TEST $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET_NOISY $CLASSIFIER_DIR_S"/lbp.gab.24x20s.xml" $LABELLED_DATA_DIR_S_TEST $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET_NOISY $CLASSIFIER_DIR_S"/cars3.xml" $LABELLED_DATA_DIR_S_TEST $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
#
# # training set
# python $DETECT_SCRIPT $LABELLED_DATA_DIR_S"/trainingset.noisy/"$CLASSIFIER_DIR_S"/haar.rab.24x20s.xml" $LABELLED_DATA_DIR_S_TRAIN $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $LABELLED_DATA_DIR_S"/trainingset.noisy/"$CLASSIFIER_DIR_S"/hog.rab.24x20s.xml" $LABELLED_DATA_DIR_S_TRAIN $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $LABELLED_DATA_DIR_S"/trainingset.noisy/"$CLASSIFIER_DIR_S"/lbp.rab.24x20s.xml" $LABELLED_DATA_DIR_S_TRAIN $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $LABELLED_DATA_DIR_S"/trainingset.noisy/"$CLASSIFIER_DIR_S"/haar.gab.24x20s.xml" $LABELLED_DATA_DIR_S_TRAIN $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $LABELLED_DATA_DIR_S"/trainingset.noisy/"$CLASSIFIER_DIR_S"/hog.gab.24x20s.xml" $LABELLED_DATA_DIR_S_TRAIN $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $LABELLED_DATA_DIR_S"/trainingset.noisy/"$CLASSIFIER_DIR_S"/lbp.gab.24x20s.xml" $LABELLED_DATA_DIR_S_TRAIN $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $LABELLED_DATA_DIR_S"/trainingset.noisy/"$CLASSIFIER_DIR_S"/cars3.xml" $LABELLED_DATA_DIR_S_TRAIN $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
#

# $THIS_TESTDATA=$TESTDATA_IMG_S_PDSET_NOISY
# ####### noisy sets ########## MN5
# # public domain set
# python $DETECT_SCRIPT $TESTDATA_IMG_S_PDSET_NOISY $CLASSIFIER_DIR_S"/haar.rab.24x20s.xml" $LABELLED_DATA_DIR_S"/publicdomainset_25.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE $M S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_PDSET_NOISY $CLASSIFIER_DIR_S"/hog.rab.24x20s.xml" $LABELLED_DATA_DIR_S"/publicdomainset_25.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE $M S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_PDSET_NOISY $CLASSIFIER_DIR_S"/lbp.rab.24x20s.xml" $LABELLED_DATA_DIR_S"/publicdomainset_25.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE $M S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_PDSET_NOISY $CLASSIFIER_DIR_S"/haar.gab.24x20s.xml" $LABELLED_DATA_DIR_S"/publicdomainset_25.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE $M S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_PDSET_NOISY $CLASSIFIER_DIR_S"/hog.gab.24x20s.xml" $LABELLED_DATA_DIR_S"/publicdomainset_25.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE $M S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_PDSET_NOISY $CLASSIFIER_DIR_S"/lbp.gab.24x20s.xml" $LABELLED_DATA_DIR_S"/publicdomainset_25.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE $M S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_PDSET_NOISY $CLASSIFIER_DIR_S"/cars3.xml" $LABELLED_DATA_DIR_S"/publicdomainset_25.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE $M S
#
# # test set
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET_NOISY $CLASSIFIER_DIR_S"/haar.rab.24x20s.xml" $LABELLED_DATA_DIR_S_TEST $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET_NOISY $CLASSIFIER_DIR_S"/hog.rab.24x20s.xml" $LABELLED_DATA_DIR_S_TEST $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET_NOISY $CLASSIFIER_DIR_S"/lbp.rab.24x20s.xml" $LABELLED_DATA_DIR_S_TEST $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET_NOISY $CLASSIFIER_DIR_S"/haar.gab.24x20s.xml" $LABELLED_DATA_DIR_S_TEST $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET_NOISY $CLASSIFIER_DIR_S"/hog.gab.24x20s.xml" $LABELLED_DATA_DIR_S_TEST $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET_NOISY $CLASSIFIER_DIR_S"/lbp.gab.24x20s.xml" $LABELLED_DATA_DIR_S_TEST $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET_NOISY $CLASSIFIER_DIR_S"/cars3.xml" $LABELLED_DATA_DIR_S_TEST $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
#
# # training set
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TRAINSET_NOISY $CLASSIFIER_DIR_S"/haar.rab.24x20s.xml" $LABELLED_DATA_DIR_S_TRAIN $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TRAINSET_NOISY $CLASSIFIER_DIR_S"/hog.rab.24x20s.xml" $LABELLED_DATA_DIR_S_TRAIN $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TRAINSET_NOISY $CLASSIFIER_DIR_S"/lbp.rab.24x20s.xml" $LABELLED_DATA_DIR_S_TRAIN $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S

# python $DETECT_SCRIPT $TESTDATA_IMG_S_TRAINSET_NOISY $CLASSIFIER_DIR_S"/haar.gab.24x20s.xml" $LABELLED_DATA_DIR_S_TRAIN $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TRAINSET_NOISY $CLASSIFIER_DIR_S"/hog.gab.24x20s.xml" $LABELLED_DATA_DIR_S_TRAIN $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TRAINSET_NOISY $CLASSIFIER_DIR_S"/lbp.gab.24x20s.xml" $LABELLED_DATA_DIR_S_TRAIN $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TRAINSET_NOISY $CLASSIFIER_DIR_S"/cars3.xml" $LABELLED_DATA_DIR_S_TRAIN $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 5 S

# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET $CLASSIFIER_DIR_S"/cars3.xml" $LABELLED_DATA_DIR_S"/uiuc_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S



########testing setup
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET $CLASSIFIER_S_HAAR $LABELLED_DATA_DIR_S"/uiuc_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET $CLASSIFIER_DIR_S"/lbp1.gab.24x20s_side.xml" $LABELLED_DATA_DIR_S"/uiuc_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET $CLASSIFIER_S_HOG $LABELLED_DATA_DIR_S"/uiuc_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 8 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TESTSET $CLASSIFIER_S_HOG $LABELLED_DATA_DIR_S"/uiuc_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 10 S
# python $DETECT_SCRIPT $TESTDATA_IMG_S_TRAINSET $CLASSIFIER_S_HAAR $LABELLED_DATA_DIR_S"/uiuc_trainset_100.txt" $TEST_RESULTS_DIR_S $TEST_RESULTS_DIR_S $COLORSPACE 2 S
# python $DETECT_SCRIPT $TESTDATA_IMG_FB_TRAINSET $CLASSIFIER_DIR_FB"/haar.gab.24x20s_fb.xml" $LABELLED_DATA_DIR_FB_TRAIN $TEST_RESULTS_DIR_FB $TEST_RESULTS_DIR_FB $COLORSPACE 2 F
