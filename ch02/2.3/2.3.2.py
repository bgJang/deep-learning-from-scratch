# 2.3 퍼셉트론 구현하기
# 2.3.2 가중치와 편향 도입 (p.52)

import numpy as np

x = np.array([0, 1]) # 입력
w = np.array([0.5, 0.5]) # 가중치
b = -0.7 # 편향

print(w * x)

print(np.sum(w * x))

print(np.sum(w * x) + b) # 부동소수점에 의한 연산 오차 발생
