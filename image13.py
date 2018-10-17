# coding: UTF-8

from PIL import Image
import os
import sys
import cv2
import numpy as np
from pprint import pprint
import shutil

# Set the root directory
rootdir = 'C:/Python36/workspace/image/jpg'
resultdir = 'C:/Python36/workspace/image/after/'
enddir = 'C:/Python36/workspace/image/end/'

def long_slice(image_path, out_name, outdir):

    img = Image.open(image_path)
    filename = img.filename
    
    s_path, s_file = os.path.split(filename)
    
    os.mkdir(resultdir)
    
    imageWidth, imageHeight = img.size
    img.crop((300, 700, imageWidth-700, imageHeight-950)).save(resultdir + 'cut_result_'+ s_file)
    
    cut_image = cv2.imread(resultdir + 'cut_result_'+ s_file)
    cut_image = cv2.cvtColor(cut_image, cv2.COLOR_BGR2HSV) 

    # 白抽出：凄く明るい場所
    threashhold_min = np.array([0,0,180], np.uint8)
    threashhold_max = np.array([255,255,255], np.uint8)
    cut_image = cv2.inRange(cut_image, threashhold_min, threashhold_max)
    cv2.imwrite(enddir + 'threashhold_result_'+ s_file, cut_image)

    # ノイズ除去
    kernel = np.ones((9,9), np.uint8)
    cut_image   = cv2.morphologyEx(cut_image, cv2.MORPH_OPEN, kernel)
    cut_image   = cv2.morphologyEx(cut_image, cv2.MORPH_CLOSE, kernel)
    
    # 画像の読み込み
    img_src =  cv2.imread(resultdir + 'cut_result_'+ s_file, 1)
    img_maskn = cv2.bitwise_not(cut_image)
    img_masked = cv2.bitwise_and(img_src, img_src, mask=img_maskn )
    cv2.imwrite(enddir + 'end_result_'+ s_file, img_masked)
    
    shutil.rmtree(resultdir)
    
if __name__ == '__main__':
    # Iterate through all the files in a set of directories.
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            long_slice(subdir + '/' + file, 'longcat', subdir)