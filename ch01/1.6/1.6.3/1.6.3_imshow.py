# p.44
import os

os.chdir(os.getcwd())
print(os.getcwd())

import matplotlib.pyplot as plt
from matplotlib.image import imread

# 이미지 읽어오기
# FileNotFoundError: [Errno 2] No such file or directory
# vscode explore root dir 기준으로 상대경로 입력
img = imread('ch01\\1.6\\1.6.3\\lena.png') 

plt.imshow(img)
plt.show()
