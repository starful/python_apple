# coding: Shift_JIS

import cv2
import numpy as np


def main():

    # ���͉摜�̓ǂݍ���
    img = cv2.imread("C:/Python36/img/APC_0023.jpg")

    if not img is None:
        imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY);
        ret,thresh = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY);
        image, contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        #draw a three pixel wide outline 
        cv2.drawContours(img,contours,-1,(0,255,0),3);
        
        

    cv2.imwrite("C:/Python36/img/th8.jpg", img)
if __name__ == "__main__":
    main()