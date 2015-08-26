#!/bin/sh
# This file is called ~/batchdetect.sh

#detect.script dir.to.images dir.to.classifier path.to.label.file colorspace


#run training set detection
python batch_detect.py /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/trainingset/ /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/classifiers/haar.gab.24x20s.xml /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/trainingset_100.txt gray 2
python batch_detect.py /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/trainingset/ /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/classifiers/haar.rab.24x20s.xml /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/trainingset_100.txt gray 2
python batch_detect.py /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/trainingset/ /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/classifiers/hog.gab.24x20s.xml /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/trainingset_100.txt gray 2
python batch_detect.py /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/trainingset/ /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/classifiers/hog.rab.24x20s.xml /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/trainingset_100.txt gray 2
python batch_detect.py /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/trainingset/ /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/classifiers/lbp.gab.24x20s.xml /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/trainingset_100.txt gray 2
python batch_detect.py /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/trainingset/ /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/classifiers/lbp.rab.24x20s.xml /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/trainingset_100.txt gray 2
python batch_detect.py /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/trainingset/ /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/classifiers/lbp.gab.24x35s.xml /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/trainingset_100.txt gray 2
python batch_detect.py /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/trainingset/ /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/classifiers/lbp.rab.24x35s.xml /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/trainingset_100.txt gray 2





# run testing set detection
python batch_detect.py /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/testset/ /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/classifiers/haar.gab.24x20s.xml /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/testset_100.txt gray 2
python batch_detect.py /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/testset/ /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/classifiers/haar.rab.24x20s.xml /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/testset_100.txt gray 2
python batch_detect.py /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/testset/ /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/classifiers/hog.gab.24x20s.xml /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/testset_100.txt gray 2
python batch_detect.py /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/testset/ /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/classifiers/hog.rab.24x20s.xml /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/testset_100.txt gray 2
python batch_detect.py /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/testset/ /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/classifiers/lbp.gab.24x20s.xml /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/testset_100.txt gray 2
python batch_detect.py /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/testset/ /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/classifiers/lbp.rab.24x20s.xml /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/testset_100.txt gray 2

python batch_detect.py /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/testset/ /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/classifiers/lbp.gab.24x35s.xml /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/testset_100.txt gray 2
python batch_detect.py /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/testset/ /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/classifiers/lbp.rab.24x35s.xml /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/testset_100.txt gray 2


# run public domain set detection

python batch_detect.py /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/publicdomainset/ /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/classifiers/haar.gab.24x20s.xml /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/publicdomainset_25.txt gray 2
python batch_detect.py /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/publicdomainset/ /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/classifiers/haar.rab.24x20s.xml /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/publicdomainset_25.txt gray 2
python batch_detect.py /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/publicdomainset/ /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/classifiers/hog.gab.24x20s.xml /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/publicdomainset_25.txt gray 2
python batch_detect.py /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/publicdomainset/ /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/classifiers/hog.rab.24x20s.xml /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/publicdomainset_25.txt gray 2
python batch_detect.py /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/publicdomainset/ /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/classifiers/lbp.gab.24x20s.xml /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/publicdomainset_25.txt gray 2
python batch_detect.py /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/publicdomainset/ /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/classifiers/lbp.rab.24x20s.xml /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/publicdomainset_25.txt gray 2
python batch_detect.py /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/publicdomainset/ /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/classifiers/lbp.gab.24x35s.xml /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/publicdomainset_25.txt gray 2


# test noisy sets
python batch_detect.py /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/publicdomainset.noisy/ /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/classifiers/haar.rab.24x20s.xml /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/publicdomainset_25.txt gray 2
python batch_detect.py /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/publicdomainset.noisy/ /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/classifiers/hog.rab.24x20s.xml /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/publicdomainset_25.txt gray 2

python batch_detect.py /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/testset.noisy/ /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/classifiers/haar.rab.24x20s.xml /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/testset_100.txt gray 2
python batch_detect.py /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/testset.noisy/ /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/classifiers/hog.rab.24x20s.xml /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/testset_100.txt gray 2

python batch_detect.py /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/trainingset.noisy/ /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/classifiers/haar.rab.24x20s.xml /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/trainingset_100.txt gray 2
python batch_detect.py /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/trainingset.noisy/ /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/classifiers/hog.rab.24x20s.xml /Users/juliusskye/Documents/COMP.VISION/final.tests/final_testing/final.results/trainingset_100.txt gray 2
