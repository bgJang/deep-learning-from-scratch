# 2.3 
# 2.5.2 XOR 게이트 구현하기 (p.59)

import numpy as np

# AND 함수
def AND(x1, x2):
    x = np.array([x1, x2]) # 입력
    w = np.array([0.5, 0.5]) # 가중치
    b = -0.7 # 편향
    tmp = np.sum(w * x) + b
    
    if tmp <= 0:
        return 0
    elif tmp > 0:
        return 1

# NAND 함수
def NAND(x1, x2):
    x = np.array([x1, x2]) # 입력
    w = np.array([-0.5, -0.5]) # 가중치와 편향만 다름
    b = 0.7 # 편향
    tmp = np.sum(w * x) + b
    
    if tmp <= 0:
        return 0
    elif tmp > 0:
        return 1

# OR 함수
def OR(x1, x2):
    x = np.array([x1, x2]) # 입력
    w = np.array([0.5, 0.5]) # 가중치와 편향만 다름
    b = -0.2 # 편향
    tmp = np.sum(w * x) + b
    
    if tmp <= 0:
        return 0
    elif tmp > 0:
        return 1

# XOR 함수
def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y

# 출력
print(XOR(0, 0))
print(XOR(0, 1))
print(XOR(1, 0))
print(XOR(1, 1))