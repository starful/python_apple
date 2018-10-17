# coding: Shift_JIS

import cv2
import matplotlib.pyplot as plt
import numpy as np
import sys, os
from PIL import Image

#���̓t�@�C���̃p�X���w��
in_jpg = "C:/Python36/img/in/"
out_jpg = "C:/Python36/img/out/"
 
#���X�g�Ō��ʂ�Ԃ��֐�
def get_file(dir_path):
    filenames = os.listdir(dir_path)
    return filenames
 
pic = get_file(in_jpg)
 
for i in pic:
    # �摜�̓ǂݍ��� 
    image_gs = cv2.imread(in_jpg + i)
 
    # ��F���p�����ʃt�@�C����ǂݍ��� --- �i�J�X�P�[�h�t�@�C���̃p�X���w��j
    cascade = cv2.CascadeClassifier("C:/Python36/Lib/site-packages/cv2/data/haarcascade_frontalface_alt.xml")
    
    # ��F���̎��s
    face_list = cascade.detectMultiScale(image_gs,scaleFactor=1.1,minNeighbors=1,minSize=(1,1))
    
    # �炾���؂�o���ĕۑ�
    no = 1;
    for rect in face_list:
        x = rect[0]
        y = rect[1]
        width = rect[2]
        height = rect[3]
        dst = image_gs[y:y + height, x:x + width]
        save_path = out_jpg + '/' + 'out_('  + str(i) +')' + str(no) + '.jpg'
        
        #�F�����ʂ̕ۑ�
        a = cv2.imwrite(save_path, dst)
        plt.show(plt.imshow(np.asarray(Image.open(save_path))))
        print(no)
        no += 1