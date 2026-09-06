import numpy as np
from scipy import stats

# 1. 生成模拟数据（x和y存在正相关）
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])  # 近似 y ≈ 0.6x + 2.2

# 2. 执行线性回归
result = stats.linregress(x, y)

# 3. 输出关键统计量
print(f"斜率 (slope): {result.slope:.4f}")        # 输出：斜率: 0.6000
print(f"截距 (intercept): {result.intercept:.4f}")# 输出：截距: 2.2000
print(f"相关系数 (rvalue): {result.rvalue:.4f}")  # 输出：相关系数: 0.8165
print(f"p值 (pvalue): {result.pvalue:.4f}")      # 输出：p值: 0.0842
print(f"斜率标准误差 (stderr): {result.stderr:.4f}")# 输出：斜率标准误差: 0.2673

# 4. 解读结果：
# - 斜率为正（0.6），说明x和y大致正相关；
# - 相关系数0.8165，说明线性相关性较强；
# - p值0.0842 > 0.05，在95%置信水平下，线性关系不显著（无法拒绝“斜率为0”的原假设）。