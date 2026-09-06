import numpy as np
import pandas as pd
from sklearn.datasets import load_wine
# 导入 sklearn 自带的红酒数据集
X, y = load_wine(return_X_y=True, as_frame=True)
# 展示数据集
print(X)
# 计算方差
print(X.var())
# 方差选择法
from sklearn.feature_selection import VarianceThreshold
# 设置方差阈值为5
ts = 5
# 筛选后只剩下4列了，这里我只输出前五行
print(VarianceThreshold(threshold=5).fit_transform(X)[:5])
var=X.var();
col=var[var>ts].index
print(X[col])
corr=X.corr()
print(corr)
import seaborn as sns
import matplotlib.pyplot as plt
corr = X.corr()  # 计算列之间的 Pearson 相关系数
ts=0.7
mask=corr<ts
# 2. 绘制热力图
sns.heatmap(
    corr,           # 输入：相关系数矩阵（DataFrame 或 numpy 数组）
    annot=True,     # 显示每个格子的数值
    cmap="coolwarm",# 颜色映射（红-蓝对比，也可试 'viridis' 'RdBu' 等）
    mask=mask,
)
# 3. 美化与展示
plt.title("Feature Correlation Heatmap")  # 添加标题
plt.show()  # 显示图形
from sklearn.feature_selection import chi2  # 从sklearn导入卡方检验函数
#卡方
for col in X.columns:  # 遍历数据集中的每一个特征列
    score = chi2(X[[col]], y)  # 对当前特征列与标签y执行卡方检验，返回检验结果(卡方值和p值)
    # 打印特征名、卡方值(保留3位小数)和p值(保留3位小数)，用制表符对齐
    print(f'{col}:\t chi2: {round(score[0][0], 3)}\t p-value: {round(score[1][0], 3)}')
