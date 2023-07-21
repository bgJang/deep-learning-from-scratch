# 3. 신경망
# 3.5. 출력층 설계하기
# 3.5.2. 소프트맥스 구현 시 주의점 (p.93)
# 2 - 코드 구현

import numpy as np

def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c) # 오버플로우 대책
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y

