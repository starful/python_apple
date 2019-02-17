# coding: Shift_JIS

import cv2
import numpy as np
from matplotlib import pyplot as plt

def main():
    # 閾値
    t = 127

    # 入力画像の読み込み
    img = cv2.imread("/Users/s-han/git/python_apple/dataset/training_set/A_16.jpg")

    # グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    
    # 方法2 （OpenCVで実装）      
    ret, th2 = cv2.threshold(gray, t, 255, cv2.THRESH_BINARY)
    
    dst = cv2.fastNlMeansDenoisingColored(th2,None,10,10,7,21)
    
    # 結果を出力
    cv2.imwrite("/Users/s-han/git/python_apple/dataset/training_set/end.jpg", th2)

if __name__ == "__main__":
    main()