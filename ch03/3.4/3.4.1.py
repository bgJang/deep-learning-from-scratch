# 3. 신경망
# 3.4. 3층 신경망 구현하기
# 3.4.1. 표기법 설명 (p.83)

import numpy as np

# 3.2.4에서 정의한 시그모이드
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# p.88 출력층 활성화 홤수
def identity_function(x):
    return x

# p.86 (은닉층 1층까지)
# A(1) = X*W1 + B1
X = np.array([1.0, 0.5])
W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
B1 = np.array([0.1, 0.2, 0.3])

print(W1.shape)
print(X.shape)
print(B1.shape)

# 가중치 합 a
A1 = np.dot(X, W1) + B1

# 활성화함수 h()로 출력된 결과 z
Z1 = sigmoid(A1)

print(A1)
print(Z1)

W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
B2 = np.array([0.1, 0.2])

A2 = np.dot(Z1, W2) + B2
Z2 = sigmoid(A2)

W3 = np.array([[0.1, 0.3], [0.2, 0.4]])
B3 = np.array([0.1, 0.2])

A3 = np.dot(Z2, W3) + B3
Y = identity_function(A3)

print(Y) # [0.31682708 0.69627909]

