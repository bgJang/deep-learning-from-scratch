# 3. 신경망
# 3.6. 손글씨 숫자 인식
# 3.6.1. MNIST 데이터셋 - 1 (p.96)

sys.path.append(os.pardir) # 부모 디렉토리 파일을 가져오도록 설정
from dataset.mnist import load_mnist


# (훈련 이미지, 훈련이미지 레이블), (시험 이미지, 시험 이미지 레이블)
# normalize : 0~255의 픽셀 값을 0.0~1.0 사이의 값으로 정규화 할 것인지
# flatten : 입력 이미지를 평탄하게 (1차원 배열로) 만들 것인지. False = 1*28*28 (3차원), True = 784 (1차원)
# ont_hot_label : 레이블을 원-핫 인코딩 형태로 저장할 것인지.
(x_train, t_train), (x_test, t_test) = load_mnist(flatten = True, normalize = False)

# 각 데이터의 형상 출력
print(x_train.shape)
print(t_train.shape)
print(x_test.shape)
print(t_test.shape)