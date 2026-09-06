import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram
from scipy.spatial.distance import squareform
plt.rcParams["font.family"] = ["SimSun", "Microsoft YaHei", "SimHei"]  # 宋体、微软雅黑、黑体
plt.rcParams["axes.unicode_minus"] = False  # 解决负号显示问题

# 模拟生成玻璃化学成分数据集
data = {
    '玻璃样本编号': [1, 2, 3, 4, 5],
    '二氧化硅(SiO₂)': [70, 72, 68, 15, 13],
    '氧化钠(Na₂O)': [10, 11, 9, 5, 6],
    '氧化钾(K₂O)': [5, 4, 6, 60, 58],
    '氧化钙(CaO)': [15, 13, 17, 20, 23]
}
df = pd.DataFrame(data)

# 提取化学成分列
chemical_columns = ['二氧化硅(SiO₂)', '氧化钠(Na₂O)', '氧化钾(K₂O)', '氧化钙(CaO)']
chemical_data = df[chemical_columns]

# 计算相关系数矩阵
corr_matrix = chemical_data.corr()
print("相关系数矩阵：")
print(corr_matrix)

# 将相关系数矩阵转换为距离矩阵
distance_matrix = 1 - np.abs(corr_matrix)
print("距离矩阵：")
print(distance_matrix)

# 转换为压缩向量
condensed_distance = squareform(distance_matrix, checks=False)

# 进行R型聚类分析
Z = linkage(condensed_distance, method='ward')

# 绘制聚类树状图
plt.figure(figsize=(10, 6))
dendrogram(Z, labels=chemical_columns)
plt.title('R型聚类分析树状图')
plt.xlabel('化学成分')
plt.xticks(rotation=45)
plt.ylabel('距离')
plt.show()
