# coding: UTF-8

from PIL import Image
import os
import sys
import cv2
import numpy as np
from pprint import pprint
import shutil

# Set the root directory
rootdir = 'C:/Python36/workspace/image/jpg/C'
resultdir = 'C:/Python36/workspace/image/after/'
enddir = 'C:/Python36/workspace/image/end/C/'

def long_slice(image_path, out_name, outdir, file_num):

    img = Image.open(image_path)
    filename = img.filename
    
    s_path, s_file = os.path.split(filename)
    
    print(filename)
    
    imageWidth, imageHeight = img.size
    
    img.crop((300, 350, imageWidth-600, imageHeight-1450)).save(enddir + 'C.' + file_num+ '.jpg')

if __name__ == '__main__':
    # Iterate through all the files in a set of directories.
    for subdir, dirs, files in os.walk(rootdir):
        file_num = 0
        for file in files:
            long_slice(subdir + '/' + file, 'longcat', subdir, str(file_num))
            file_num = file_num + 1