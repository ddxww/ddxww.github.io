import numpy as np

y = np.array([
    [0.1, 0.2, 0.6, 0.1],
    [0.7, 0.1, 0.1, 0.1],
    [0.2, 0.5, 0.2, 0.1]
])

t = np.array([2, 0, 1])

n = y.shape[0]
print(n)
print(y[np.arange(n),t])
# 第0个样本的正确类别是2
# 第1个样本的正确类别是0
# 第2个样本的正确类别是1