# coding: Shift_JIS

import cv2
import numpy as np
from matplotlib import pyplot as plt

def main():
    # 臒l
    t = 127

    # ���͉摜�̓ǂݍ���
    img = cv2.imread("/Users/s-han/git/python_apple/dataset/training_set/A_16.jpg")

    # �O���[�X�P�[���ϊ�
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    
    # ���@2 �iOpenCV�Ŏ����j      
    ret, th2 = cv2.threshold(gray, t, 255, cv2.THRESH_BINARY)
    
    dst = cv2.fastNlMeansDenoisingColored(th2,None,10,10,7,21)
    
    # ���ʂ��o��
    cv2.imwrite("/Users/s-han/git/python_apple/dataset/training_set/end.jpg", th2)

if __name__ == "__main__":
    main()