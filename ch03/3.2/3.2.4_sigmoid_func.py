# 3. 신경망
# 3.2. 활성화함수
# 3.2.4. 시그모이드 함수 구현하기(p.72) 
# -> 3.2.2 계단함수 조합하여 3.2.5 스타일로 출력하도록 작성

import numpy as np
import matplotlib.pyplot as plt

def step_function(x):
    return np.array(x > 0, dtype=int)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.arange(-5.0, 5.0, 0.1)
y1 = step_function(x)
y2 = sigmoid(x)

plt.plot(x, y1, label="step", linestyle="--")
plt.plot(x, y2, label="sigmoid")

plt.ylim(-0.1, 1.1) # y축 범위
plt.show()
