# coding: UTF-8

import sys
import cv2
import numpy as np
from pprint import pprint

def main():
    image = cv2.imread("/Users/s-han/git/python_apple/dataset/training_set/A_16.jpg")
   
    # HSVへ変換
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) 

    # 白抽出：凄く明るい場所
    threashhold_min = np.array([0,0,180], np.uint8)
    threashhold_max = np.array([255,255,255], np.uint8)
    image = cv2.inRange(image, threashhold_min, threashhold_max)

    # ノイズ除去
    kernel = np.ones((9,9), np.uint8)
    image   = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    image   = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    
    # 画像の読み込み
    img_src =  cv2.imread("/Users/s-han/git/python_apple/dataset/training_set/end.jpg", 1)
    img_maskn = cv2.bitwise_not(image)
    img_masked = cv2.bitwise_and(img_src, img_src, mask=img_maskn )
    cv2.imwrite('result.jpg', img_masked)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return 0

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass