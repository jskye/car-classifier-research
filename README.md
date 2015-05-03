# car-classifier-research

This repo is for a final year University of Newcastle Computer Vision research assignment conducted by 
myself and [Dylan Barnett](https://github.com/DBarnett73).<br>
We were tasked with conducting some research into training object detectors using feature extraction.<br>
We decided to look at training car detection using OpenCV's cascaded training on Haar-like features 
as well as utilise an old implementation of Viola Jones framework (JViolaJones).

We decided the main goals of the project were:<br>
*Train object detector to -<br>
* recognise cars ahead, from road view <br>
Train with - <br>
* Cascaded Haar-features
* Cascaded Haar-features & Viola Jones Framework
* Cascaded Local Binary Patterns (LBP)<br>
Test with - <br>
* color (normal) vs grayscale
* clean (normal) vs noisy
*light (normal) vs dark (night, tunnels) images
* (normal) vs low powered (raspPi)

The research is currently underway.

We started with a clone of https://github.com/mrnugget/opencv-haar-classifier-training
And followed the following method: 

Create list of samples from images:
 
```find ./negative_images -iname "*.jpg" > negatives.txt```

```find ./positive_images -iname "*.jpg" > positives.txt```

create many positive samples from provided ones

```perl bin/createsamples.pl positives.txt negatives.txt samples 1500
"opencv_createsamples -bgcolor 0 -bgthresh 0 -maxxangle 1.1
-maxyangle 1.1 maxzangle 0.5 -maxidev 40 -w 300 -h 175"```

nb. warnings may come up when running the perl script, since i had to change some files from png to jpg. 
This is because of [stricter libpng rules] (http://tex.stackexchange.com/questions/125612/warning-pdflatex-libpng-warning-iccp-known-incorrect-srgb-profile)
but it still works with them. 


go to samples dir and run merge script

```python mergevec.py -v ../samples -o samples.vec```

run training

```opencv_traincascade -data classifier -vec samples/samples.vec -bg negatives.txt -numStages 20 -minHitRate 0.999 -maxFalseAlarmRate 0.5 -numPos 1000 -numNeg 13 -w 300 -h 175 -mode BASIC -precalcValBufSize 512```

nb. [numPos needs to be somewhat less than the number of postive samples, based on background similarity, numStages, minHitRate]
(http://stackoverflow.com/questions/10863560/haar-training-opencv-assertion-failed)
