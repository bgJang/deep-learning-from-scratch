# 3. 신경망
# 3.5. 출력층 설계하기
# 3.5.1. 항등 함수와 소프트맥스 함수 구현하기 (p.91)
# 2 - 코드 구현

import numpy as np

def softmax(a):
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y

