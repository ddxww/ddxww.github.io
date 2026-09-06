import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import f_oneway

data = {
    'Lab1': [4.07, 4.04, 4.07, 4.05, 4.04, 4.02, 4.06, 4.10, 4.04],
    'Lab2': [3.85, 4.08, 4.11, 4.08, 4.01, 4.02, 4.04, 3.97, 3.95],
    'Lab3': [4.02, 4.01, 4.01, 4.04, 3.99, 4.03, 3.97, 3.98, 3.98],
    'Lab4': [3.88, 3.91, 3.95, 3.92, 3.97, 3.92, 3.90, 3.97, 3.90],
    'Lab5': [3.95, 4.02, 3.89, 3.91, 4.01, 3.89, 3.89, 3.99, 4.00],
    'Lab6': [3.86, 3.96, 3.97, 4.00, 3.82, 3.98, 3.99, 4.02, 3.93],
    'Lab7': [4.02, 4.03, 4.04, 4.10, 3.81, 3.91, 3.96, 4.05, 4.06]
}
data = pd.DataFrame(data)
df = data
df.boxplot()
plt.show()

lab1 = df['Lab1'].values
lab2 = df['Lab2'].values
lab3 = df['Lab3'].values
lab4 = df['Lab4'].values
lab5 = df['Lab5'].values
lab6 = df['Lab6'].values
lab7 = df['Lab7'].values

# 单因素方差分析
f_stat, p_value = f_oneway(lab1, lab2, lab3, lab4, lab5, lab6, lab7)

# 计算自由度
k = len(df.columns)  # 组数，即实验室数量
N = df.size  # 总样本量

df_between = k - 1
df_within = N - k
df_total = N - 1

# 输出结果
print(f"方差分析统计量 F = {f_stat:.4f}")
print(f"P 值 = {p_value:.4e}")
print(f"组间自由度 df_between = {df_between}")
print(f"组内自由度 df_within = {df_within}")
print(f"总自由度 df_total = {df_total}")

# 判断是否拒绝原假设（显著水平 α=0.05）
alpha = 0.05
if p_value < alpha:
    print("P 值 < 0.05，拒绝原假设，认为各实验室测量均值有显著差异。")
else:
    print("P 值 ≥ 0.05，不拒绝原假设，认为各实验室测量均值无显著差异。")