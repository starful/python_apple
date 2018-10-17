# coding: Shift_JIS

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('001.jpg' ,0)
plt.imshow(img)
plt.colorbar()
plt.show()