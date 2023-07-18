# 2.3 퍼셉트론 구현하기
# 2.3.3 (p.52)

import numpy as np


# AND 함수
def AND(x1, x2):
    x = np.array([x1, x2]) # 입력
    w = np.array([0.5, 0.5]) # 가중치
    b = -0.7 # 편향
    tmp = np.sum(w * x) + b
    
    if tmp <= 0:
        print('[AND] 0')
        return 0
    elif tmp > 0:
        print('[AND] 1')
        return 1

# NAND 함수
def NAND(x1, x2):
    x = np.array([x1, x2]) # 입력
    w = np.array([-0.5, -0.5]) # 가중치와 편향만 다름
    b = 0.7 # 편향
    tmp = np.sum(w * x) + b
    
    if tmp <= 0:
        print('[NAND] 0')
        return 0
    elif tmp > 0:
        print('[NAND] 1')
        return 1

# OR 함수
def OR(x1, x2):
    x = np.array([x1, x2]) # 입력
    w = np.array([0.5, 0.5]) # 가중치와 편향만 다름
    b = -0.2 # 편향
    tmp = np.sum(w * x) + b
    
    if tmp <= 0:
        print('[OR] 0')
        return 0
    elif tmp > 0:
        print('[OR] 1')
        return 1

# 출력
AND(0, 0)
AND(0, 1)
AND(1, 0)
AND(1, 1)

NAND(0, 0)
NAND(0, 1)
NAND(1, 0)
NAND(1, 1)

OR(0, 0)
OR(0, 1)
OR(1, 0)
OR(1, 1)