# car-classifier-research

This repo combines research documentation, source files and results from two final year university research subjects
 1. COMP4110 Computer Vision 
     - Authors: myself and [Dylan Barnett](https://github.com/DBarnett73):
     - This course tasked us to conduct some computer vision based research within a group, for which we chose to focus on training object detectors using feature extraction
 2. COMP4120 Directed Studies
     - Author: myself  
     - This course allowed for any directed study for which i chose to extend the previous car detection research.


# Project Goals:<br>
<b>Train object detector to -</b> <br>
* detect cars ahead, from road view <br>
<b>Train with -</b> <br>
* Cascaded Haar-features
* Cascaded Haar-features & Viola Jones Framework
* Cascaded Local Binary Patterns (LBP)<br>
<b>Test with -</b> <br>
* color (normal) vs grayscale
* clean (normal) vs noisy
* light (normal) vs dark (night, tunnels) images
* (normal) vs low powered (raspPi)

The research is currently underway.

# Setup:<br>
The process of setting up openCV on Windows machine is found [here](http://docs.opencv.org/doc/tutorials/introduction/windows_install/windows_install.html)

We started with a clone of https://github.com/mrnugget/opencv-haar-classifier-training
And followed the following method: 

Create list of samples from images:
 
```find ./negative_images -iname "*.jpg" > negatives.txt```

```find ./positive_images -iname "*.jpg" > positives.txt```

create many positive samples from provided ones

```$ perl src/createsamples.pl positives.txt negatives.txt samples 1500 "opencv_createsamples -bgcolor 0 -bgthresh 0 -maxxangle 0.01 -maxyangle 0.01 maxzangle 0.01 -maxidev 40 -w 20 -h 20"```

nb. warnings may come up when running the perl script, since i had to change some files from png to jpg. 
This is because of [stricter libpng rules] (http://tex.stackexchange.com/questions/125612/warning-pdflatex-libpng-warning-iccp-known-incorrect-srgb-profile)
but it still works with them. 


go to samples dir and run merge script

```python mergevec.py -v ../samples -o samples.vec```

run training

```opencv_traincascade -data classifier -vec samples/samples.vec -bg negatives.txt -numStages 20 -minHitRate 0.999 -maxFalseAlarmRate 0.5 -numPos 1000 -numNeg 13 -w 300 -h 175 -mode BASIC -precalcValBufSize 512```

nb. [numPos needs to be somewhat less than the number of postive samples, based on background similarity, numStages, minHitRate]
(http://stackoverflow.com/questions/10863560/haar-training-opencv-assertion-failed)

[General rule is: (numPos = 0.9 * total samples) will work most of the time.](http://answers.opencv.org/question/7141/about-traincascade-paremeters-samples-and-other/)
Or 0.8 x numberOfElements in vec file to not risk failing.
