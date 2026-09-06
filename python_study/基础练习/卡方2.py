import numpy as np
from scipy.stats import norm, chi2
import pandas as pd

# 滚珠直径样本数据（假设有50个数据）
# 根据题目分组信息还原的近似数据分布
data = np.array([
    14.3, 14.4, 14.4, 14.5, 14.5, 14.5,  # 第一组 (14.2,14.6]，6个数据
    14.7, 14.7, 14.8, 14.8, 14.8, 14.8, 14.9, 14.9, 14.9, 14.9, 14.9,  # 第二组 (14.6,15.0]，10个数据
    15.1, 15.1, 15.1, 15.1, 15.1, 15.1, 15.2, 15.2, 15.2, 15.2, 15.2,  # 第三组 (15.0,15.4]，19个数据
    15.2, 15.3, 15.3, 15.3, 15.3, 15.3, 15.3, 15.3, 15.4, 15.4,
    15.5, 15.5, 15.5, 15.6, 15.6, 15.6, 15.7, 15.7, 15.7,  # 第四组 (15.4,15.8]，9个数据
    15.9, 15.9, 16.0, 16.0, 16.1, 16.2  # 第五组 (15.8, +∞)，6个数据
])

# 已知的正态分布参数
mu = 15.0780
sigma = 0.4325

# 1. 定义分组区间
bins = [14.2, 14.6, 15.0, 15.4, 15.8, np.inf]

# 2. 计算实际频数
observed, _ = np.histogram(data, bins=bins)

# 3. 计算理论概率和理论频数
n = len(data)
theoretical_prob = []
for i in range(len(bins)-1):
    # 计算每个区间的理论概率
    lower = bins[i]
    upper = bins[i+1]
    p = norm.cdf(upper, loc=mu, scale=sigma) - norm.cdf(lower, loc=mu, scale=sigma)
    theoretical_prob.append(p)

theoretical = np.array(theoretical_prob) * n  # 理论频数 = 总样本数 × 理论概率

# 4. 合并理论频数小于5的组（最后一组理论频数较小）
# 合并第四组和第五组
observed_merged = np.array([observed[0], observed[1], observed[2], observed[3]+observed[4]])
theoretical_merged = np.array([theoretical[0], theoretical[1], theoretical[2], theoretical[3]+theoretical[4]])

# 5. 计算χ²统计量
chi2_stat = np.sum((observed_merged - theoretical_merged)**2 / theoretical_merged)

# 6. 确定自由度和临界值
k = len(observed_merged)  # 合并后的组数
r = 0  # 已知总体均值和标准差，无需估计参数
df = k - r - 1  # 自由度
alpha = 0.05
critical_value = chi2.ppf(1-alpha, df)

# 7. 计算p值
p_value = 1 - chi2.cdf(chi2_stat, df)

# 输出结果
print("滚珠直径正态分布检验结果：")
print(f"样本量: {n}")
print("\n分组区间及频数：")
groups = [f"({bins[i]}, {bins[i+1]}]" for i in range(len(bins)-1)]
df_result = pd.DataFrame({
    "分组区间": groups,
    "实际频数": observed,
    "理论频数": theoretical.round(3)
})
print(df_result)

print("\n合并小理论频数后的结果：")
merged_groups = ["(14.2, 14.6]", "(14.6, 15.0]", "(15.0, 15.4]", "(15.4, +∞)"]
df_merged = pd.DataFrame({
    "分组区间": merged_groups,
    "实际频数": observed_merged,
    "理论频数": theoretical_merged.round(3)
})
print(df_merged)

print(f"\nχ²统计量: {chi2_stat:.4f}")
print(f"自由度: {df}")
print(f"α={alpha}的临界值: {critical_value:.4f}")
print(f"p值: {p_value:.4f}")

# 结论
if chi2_stat < critical_value and p_value > alpha:
    print("\n结论：不拒绝原假设，认为滚珠直径服从正态分布N(15.0780, 0.4325²)")
else:
    print("\n结论：拒绝原假设，认为滚珠直径不服从正态分布N(15.0780, 0.4325²)")
