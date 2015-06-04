import numpy as np
from PIL import Image

def normalize(arr):
    """
    Linear normalization
    http://en.wikipedia.org/wiki/Normalization_%28image_processing%29
    """
    arr = arr.astype('float')
    # Do not touch the alpha channel
    for i in range(3):
        minval = arr[...,i].min()
        maxval = arr[...,i].max()
        if minval != maxval:
            arr[...,i] -= minval
            arr[...,i] *= (255.0/(maxval-minval))
    return arr

def demo_normalize(FILENAME):

    img = Image.open(FILENAME).convert('L')
    arr=np.array(np.asarray(img).astype('float'))
    new_img = Image.fromarray(normalize(arr).astype('uint8'),'L')
    new_img.save('normalized.png')

FILENAME = "bananas.jpg"
demo_normalize(FILENAME)
