# coding: Shift_JIS

import cv2
import numpy as np

# �w�肵���摜(path)�̕��̂����o���A�O�ڋ�`�̉摜���o�͂��܂�
def detect_contour():

  # �摜��Ǎ�
  src = cv2.imread("C:/Python36/img/APC_0023.jpg")

  # �O���[�X�P�[���摜�֕ϊ�
  gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

  # 2�l��
  retval, bw = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

  # �֊s�𒊏o
  #   contours : [�̈�][Point No][0][x=0, y=1]
  #   cv2.CHAIN_APPROX_NONE: ���ԓ_���ێ�����
  #   cv2.CHAIN_APPROX_SIMPLE: ���ԓ_�͕ێ����Ȃ�
  image, contours, hierarchy = cv2.findContours(bw, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
  
  # ��`���o���ꂽ���i�f�t�H���g��0���w��j
  detect_count = 0

  # �e�֊s�ɑ΂��鏈��
  for i in range(0, len(contours)):

    # �֊s�̗̈���v�Z
    area = cv2.contourArea(contours[i])

    # �m�C�Y�i����������̈�j�ƑS�̗̂֊s�i�傫������̈�j�����O
    if area < 1e2 or 1e5 < area:
      continue

    # �O�ڋ�`
    if len(contours[i]) > 0:
      rect = contours[i]
      x, y, w, h = cv2.boundingRect(rect)
      cv2.rectangle(src, (x, y), (x + w, y + h), (0, 255, 0), 2)

      # �O�ڋ�`���ɉ摜��ۑ�
      cv2.imwrite('out' + str(detect_count) + '.jpg', src[y:y + h, x:x + w])

      detect_count = detect_count + 1

  # �O�ڋ�`���ꂽ�摜��\��
  # cv2.imshow('output', src)
  # cv2.waitKey(0)

  # �I������
  cv2.destroyAllWindows()

if __name__ == '__main__':
  detect_contour()