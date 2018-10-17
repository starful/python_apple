# coding: UTF-8

import os
import cv2
import sys
import numpy as np
from PIL import Image
import rawpy
import imageio

# Set the root directory
dngdir = 'C:/Python36/workspace/image/dng'
jpgdir = 'C:/Python36/workspace/image/jpg/'

def long_slice(image_path, out_name, outdir):

    img = Image.open(image_path)
    
    filename = img.filename
    s_path, s_file = os.path.split(filename)
    name, ext = os.path.splitext(s_file)

    raw = rawpy.imread(filename)
    rgb = raw.postprocess()
    imageio.imsave(jpgdir + name + '.jpg', rgb)
    
if __name__ == '__main__':
    # Iterate through all the files in a set of directories.
    for subdir, dirs, files in os.walk(dngdir):
        for file in files:
            long_slice(subdir + '/' + file, 'longcat', subdir)