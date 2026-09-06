import numpy as np
# 输入初始矩阵，例如 [[1,2],[3,4]]
A = np.array(eval(input("输入初始矩阵（例如 [[1,2],[3,4]]）：")))

# 数据标准化（均值归一化）
Mean = np.mean(A, axis=0)
A_norm = A / Mean
print("标准化后的矩阵:\n", A_norm)

# 提取参考序列和比较序列
Y = A_norm[:, 0]  # 第一列作为参考序列
X = A_norm[:, 1:]  # 其余列作为比较序列

# 计算绝对差值矩阵
absX0_X1 = np.abs(X - Y.reshape(-1, 1))  # 自动广播
print("绝对差值矩阵:\n", absX0_X1)

# 计算灰色关联系数
a = np.min(absX0_X1)  # 全局最小差值
b = np.max(absX0_X1)  # 全局最大差值
rho = 0.5  # 分辨系数
gamma = (a + rho * b) / (absX0_X1 + rho * b)  # 逐元素计算

# 计算灰色关联度（每列的平均值）
result = np.mean(gamma, axis=0)
print("灰色关联度:", result)