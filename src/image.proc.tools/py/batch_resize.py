#!/usr/bin/python
from PIL import Image
import os, sys
import glob


# dirPath = sys.argv[2]


# path = "/root/Desktop/python/images/"
# dirs = os.listdir( path )

# def resize():
#     for item in dirs:
#         if os.path.isfile(path+item):
#             im = Image.open(path+item)
#             f, e = os.path.splitext(path+item)
#             imResize = im.resize((300,175), Image.ANTIALIAS)
#             imResize.save(f + ' resized.jpg', 'JPEG', quality=90)
#
# resize()


files=glob.glob("*.jpg")
for file in files:
    f=open(file)
    filename=f.name
    image = Image.open(file)
    imResized = image.resize((128,128), Image.ANTIALIAS)
    imResized.save(filename + ' resized.jpg', 'JPEG', quality=100)
    # image.save(filename+".jpg")
    f.close()
