# #-*- coding: utf-8 -*-
# import sys
# import io
# sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
# sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import numpy as np
import matplotlib.pyplot as plt

# ������ �غ�
x = np.arange(0, 6, 0.1) # 0���� 6���� 0.1 �������� ����
y = np.sin(x)

# �׷��� �׸���
plt.plot(x, y)
plt.show()