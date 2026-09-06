import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
plt.rcParams["font.family"] = ["SimSun", "Microsoft YaHei", "SimHei"]
plt.rcParams["axes.unicode_minus"] = False
# 生成数据
np.random.seed(0)
a1 = np.random.normal(85, 10, 20)
s1 = pd.DataFrame(a1, columns=['X'], index=range(1, 21))  # 索引是RangeIndex
print("原始数据：")
print(s1.round(2))
# 数据预处理
X = s1[['X']]
# K-means聚类
kmeans = KMeans(n_clusters=2, random_state=0)
s1['cluster'] = kmeans.fit_predict(X)
print("\n聚类结果：")
print(s1.round(2))
# 可视化聚类结果
plt.figure(figsize=(10, 6))
# 绘制不同簇的数据点
colors = ['blue', 'red']
for cluster_id in [0, 1]:
    cluster_data = s1[s1['cluster'] == cluster_id]
    plt.scatter(
        cluster_data.index,
        cluster_data['X'],
        c=colors[cluster_id],
        label=f'簇 {cluster_id}',
        alpha=0.7,
        s=100
    )
# 绘制簇中心点（修复索引均值计算）
centers = kmeans.cluster_centers_
# 将RangeIndex转换为numpy数组后再计算均值
index_mean = s1.index.to_numpy().mean()  # 关键修复：用to_numpy()转换后计算均值
for i, center in enumerate(centers):
    plt.scatter(
        [index_mean],  # 使用转换后计算的索引均值
        center[0],
        c=colors[i],
        marker='X',
        s=200,
        edgecolors='black'
    )
# 图表美化
plt.xlabel('数据索引')
plt.ylabel('值（X）')
plt.title('K-means聚类结果（修复索引均值计算）')
plt.legend()
plt.grid(alpha=0.3)
plt.show()

