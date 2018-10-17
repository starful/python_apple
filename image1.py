# coding: Shift_JIS

from PIL import Image

# 既存ファイルを readモードで読み込み
img = Image.open('C:\Python36\img\APC_0023.jpg', 'r')

# リサイズ。サイズは幅と高さをtupleで指定
resize_img = img.resize((100, 100))

# リサイズ後の画像を保存
resize_img.save('resize_img.jpg', 'JPEG', quality=100, optimize=True)