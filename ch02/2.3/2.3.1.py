# 2.3 퍼셉트론 구현하기
# 2.3.1 간단한 구현 (p.51)

# AND 함수
def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1 * w1 + x2 * w2
    if tmp <= theta:
        print(0)
        return 0
    elif tmp > theta:
        print(1)
        return 1

# 출력
AND(0, 0)
AND(0, 1)
AND(1, 0)
AND(1, 1)