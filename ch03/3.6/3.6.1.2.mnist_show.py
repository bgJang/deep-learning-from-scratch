# 3. 신경망
# 3.6. 손글씨 숫자 인식
# 3.6.1. MNIST 데이터셋 - 2. 화면에 출력(p.99)

import sys, os
sys.path.append(os.pardir)

import numpy as np
from dataset.mnist import load_mnist
from PIL import Image

def img_show(img):
    pil_img = Image.fromarray(np.uint8(img)) # numpy로 저장된 이미지를 PIL용 데이터 객체로 변환.
    pil_img.show()

(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize = False)

img = x_train[0]
label = t_train[0]
print(label) 

print(img.shape)
img = img.reshape(28, 28) # flatten으로 1차원 배열로 만들었기 때문에 원본 형상으로 변형해야 함.
print(img.shape)

img_show(img)
