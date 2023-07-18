# 3. 신경망
# 3.2. 활성화함수
# 3.2.2. 계단함수 구현하기(p.69)

import numpy as np
import matplotlib.pyplot as plt

# 실수(부동소수점)만 인자로 받을 수 있는 계단 함수
# numpy 배열을 받을 수 없다
# def step_function(x):
#     if x > 0:
#         return 1
#     else:
#         return 0


# numpy 부등호 연산 결과를 int로 리턴
# def step_function(x):
#     y = x > 0
#     return y.astype(np.int) # bool to int


def step_function(x):
    return np.array(x > 0, dtype=int) # np.int deprecated.

x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)

plt.plot(x, y)
plt.ylim(-0.1, 1.1) # y축 범위
plt.show()
