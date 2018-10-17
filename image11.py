# coding: Shift_JIS
 
import cv2
import numpy as np
 
if __name__ == '__main__':
 
    # �摜�̓ǂݍ���
    img_src = cv2.imread("kura.jpg", 1)
 
    # �}�X�N�摜�̓ǂݍ���
    img_mask = cv2.imread("heart.jpg", 0)
 
    img_masked = cv2.bitwise_and(img_src, img_src, mask=img_mask )
 
 
    # �\��
    cv2.imshow("Show MASK Image", img_masked)
    cv2.waitKey(0)
    cv2.destroyAllWindows()