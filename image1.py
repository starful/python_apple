# coding: Shift_JIS

from PIL import Image

# �����t�@�C���� read���[�h�œǂݍ���
img = Image.open('C:\Python36\img\APC_0023.jpg', 'r')

# ���T�C�Y�B�T�C�Y�͕��ƍ�����tuple�Ŏw��
resize_img = img.resize((100, 100))

# ���T�C�Y��̉摜��ۑ�
resize_img.save('resize_img.jpg', 'JPEG', quality=100, optimize=True)