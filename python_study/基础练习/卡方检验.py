import numpy as np
from scipy.stats import chi2_contingency

# 定义2×3的频数矩阵（按行输入数据）
observed = np.array([
    [1, 1, 10],   # 第一行数据
    [2, 15, 13]   # 第二行数据
])

# 进行卡方检验
chi2, p, dof, expected = chi2_contingency(observed)

# 输出结果
print("卡方检验结果：")
print(f"观测频数矩阵：\n{observed}")
print(f"\n卡方值：{chi2:.4f}")
print(f"自由度：{dof}")  # 自由度=(行数-1)×(列数-1)=(2-1)×(3-1)=2
print(f"p值：{p:.4f}")
print(f"期望频数矩阵：\n{expected.round(2)}")  # 保留2位小数

# 基于95%置信区间（α=0.05）的判断
alpha = 0.05
if p < alpha:
    print(f"\n结论：在95%置信水平下，两个分类变量存在显著关联（p={p:.4f} < {alpha}）")
else:
    print(f"\n结论：在95%置信水平下，两个分类变量无显著关联（p={p:.4f} ≥ {alpha}）")

import numpy as np
import scipy.stats as stats

# 观察频数
observed = np.array([[60, 140], [10, 190]])

# 计算期望频数
row_totals = observed.sum(axis=1)
col_totals = observed.sum(axis=0)
total = observed.sum()
expected = np.outer(row_totals, col_totals) / total

# 计算卡方值和p值
chi2, p, dof, expected_freq = stats.chi2_contingency(observed)

# 计算标准化残差
residuals = (observed - expected) / np.sqrt(expected)

# 结果
print("观察频数:")
print(observed)
print("\n期望频数:")
print(expected)
print(f"\n卡方值: {chi2:.2f}")
print(f"p值: {p:.4f}")
print(f"自由度: {dof}")
print("\n标准化残差:")
print(residuals)

# 残差分析
print("\n残差分析:")
for i in range(residuals.shape[0]):
    for j in range(residuals.shape[1]):
        if abs(residuals[i, j]) > 1.96:
            print(f"单元格({i + 1}, {j + 1})的标准化残差为{residuals[i, j]:.2f},超过1.96,有显著差异。")
        else:
            print(f"单元格({i + 1}, {j + 1})的标准化残差为{residuals[i, j]:.2f},未超过1.96,无显著差异。")