# 3. 신경망
# 3.2. 활성화함수
# 3.2.7. ReLU 함수(p.76) 

import numpy as np
import matplotlib.pyplot as plt

def relu(x):
    return np.maximum(0, x)

x = np.arange(-5.0, 5.0, 0.1)
y = relu(x)

plt.plot(x, y)
plt.show()