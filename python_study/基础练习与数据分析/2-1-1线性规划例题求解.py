import numpy as np
from scipy.optimize import linprog


# 目标函数系数（最小化 2x1 + 3x2 - 5x3）
c = np.array([2, 3, -5])

# 不等式约束：A*x <= b
A = np.array([
    [-2, 5, -1],  # -2x1 + 5x2 - x3 <= -10
    [1, 3, 1]     # x1 + 3x2 + x3 <= -12
])
b = np.array([-10, 12])

# 等式约束：Aeq*x = beq
Aeq = np.array([[1, 1, 1]])  # 修正：转为二维数组（1个约束，3个变量）
beq = np.array([7])         # x1 + x2 + x3 = 7
# 变量边界（修正：补全3个变量的边界）
bounds = [(0, None), (0, None), (0, None)]  # 所有变量 >= 0
# 求解线性规划问题
res = linprog(c, A_ub=A, b_ub=b, A_eq=Aeq, b_eq=beq, bounds=bounds)
print(-res.fun)
print(res.x)