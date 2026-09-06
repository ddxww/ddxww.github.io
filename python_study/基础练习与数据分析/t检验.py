import numpy as np
from scipy.stats import ttest_ind, levene

# ---------------------- 1. 准备数据（两组独立样本） ----------------------
# 组1：传统教学法学生成绩
group1 = np.array([78, 82, 85, 76, 80, 79, 83, 81, 77, 84])
# 组2：多媒体教学法学生成绩
group2 = np.array([85, 88, 90, 86, 89, 92, 87, 88, 91, 86])

# 先看两组数据的基本统计信息（均值、标准差），直观了解差异
print("=== 两组数据基本统计 ===")
print(f"组1（传统教学）：均值={group1.mean():.2f}，标准差={group1.std():.2f}，样本量={len(group1)}")
print(f"组2（多媒体教学）：均值={group2.mean():.2f}，标准差={group2.std():.2f}，样本量={len(group2)}")

# ---------------------- 2. （可选）方差齐性检验（独立样本t检验前提） ----------------------
# 独立样本t检验需要满足“两组方差齐性”（即两组数据的离散程度相近），用levene检验判断
stat_levene, p_levene = levene(group1, group2)
print(f"\n=== 方差齐性检验（Levene检验） ===")
print(f"p值={p_levene:.4f}")
if p_levene > 0.05:
    print("结论：两组方差齐性（p>0.05），可使用方差齐性的t检验（equal_var=True）")
else:
    print("结论：两组方差不齐（p≤0.05），需使用方差不齐的t检验（equal_var=False）")

# ---------------------- 3. 独立样本t检验 ----------------------
# 根据方差齐性结果选择equal_var参数
equal_var_flag = p_levene > 0.05  # 方差齐则为True，不齐则为False
t_stat, p_value = ttest_ind(group1, group2, equal_var=equal_var_flag)

# 计算t检验的自由度（独立样本t检验：df = n1 + n2 - 2，n1、n2为两组样本量）
df_t = len(group1) + len(group2) - 2

# ---------------------- 4. 结果解读 ----------------------
print(f"\n=== 独立样本t检验结果 ===")
print(f"t统计量：{t_stat:.4f}")
print(f"p值：{p_value:.4f}")
print(f"自由度：{df_t}")  # 本例中n1=10, n2=10 → df=10+10-2=18

# 基于95%置信水平（α=0.05）判断
alpha = 0.05
if p_value < alpha:
    print(f"结论：在95%置信水平下，拒绝原假设 → 两组教学方法的学生成绩存在显著差异")
else:
    print(f"结论：在95%置信水平下，不能拒绝原假设 → 两组教学方法的学生成绩无显著差异")