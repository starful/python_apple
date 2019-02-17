# coding: Shift_JIS

import cv2
import numpy as np


def main():

    # 入力画像の読み込み
    img = cv2.imread("/Users/s-han/git/python_apple/dataset/training_set/cccc.jpg")

    if not img is None:
        imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY);
        ret,thresh = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY);
        image, contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        #draw a three pixel wide outline 
        cv2.drawContours(img,contours,-1,(0,255,0),3);
        
        

    cv2.imwrite("/Users/s-han/git/python_apple/dataset/training_set/A_16_end.jpg", img)
if __name__ == "__main__":
    main()