import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
plt.rcParams["font.family"] = ["SimSun", "Microsoft YaHei", "SimHei"]  # 宋体、微软雅黑、黑体
plt.rcParams["axes.unicode_minus"] = False  # 解决负号显示问题
# 1. 数据准备（假设数据格式：行=蔬菜类别，列=特征，如销量、价格、增长率等）
# 示例数据（请替换为你的实际数据）
data = {
    '蔬菜类别': ['水生根茎类', '花叶类', '花菜类', '茄类', '辣椒类', '食用菌'],
    '平均销量(千克)': [120, 350, 180, 220, 280, 150],
    '价格波动(%)': [5.2, 3.8, 4.5, 6.1, 7.3, 4.0],
    '季度增长率(%)': [2.1, 5.3, 3.2, 4.8, 6.5, 2.8],
    '库存周转率': [3.2, 4.5, 3.8, 4.2, 5.1, 3.5]
}
df = pd.DataFrame(data)

# 2. 数据预处理
# 提取特征列（排除类别名称）
features = df.drop('蔬菜类别', axis=1)

# 数据标准化（K-means对尺度敏感，需标准化特征）
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# 3. K-means聚类（假设聚为2类，可根据实际需求调整n_clusters）
k = 2  # 聚类数量，可尝试2-4类观察结果
kmeans = KMeans(n_clusters=k, random_state=42)
df['聚类标签'] = kmeans.fit_predict(scaled_features)

# 4. 结果分析
print("聚类结果：")
print(df[['蔬菜类别', '聚类标签']])

# 计算每个聚类的特征均值（分析聚类特征）
cluster_analysis = df.groupby('聚类标签').mean(numeric_only=True)
print("\n各聚类特征均值：")
print(cluster_analysis)

# 5. 可视化聚类结果（使用PCA降维到2D）
pca = PCA(n_components=2)  # 降为2个主成分
pca_features = pca.fit_transform(scaled_features)
df['PCA1'] = pca_features[:, 0]
df['PCA2'] = pca_features[:, 1]

# 绘制聚类散点图
plt.figure(figsize=(10, 6))
sns.scatterplot(
    x='PCA1', y='PCA2',
    hue='聚类标签',
    style='蔬菜类别',
    s=100,  # 点大小
    data=df,
    palette='Set1'  # 颜色方案
)

# 添加聚类中心（需将中心转换回PCA空间）
centers = kmeans.cluster_centers_
pca_centers = pca.transform(centers)
plt.scatter(
    pca_centers[:, 0], pca_centers[:, 1],
    marker='X', s=200, linewidths=3,
    color='black', label='聚类中心'
)

# 添加标签和标题
plt.title(f'蔬菜类别K-means聚类结果 (K={k})', fontsize=14)
plt.xlabel(f'主成分1 (解释方差: {pca.explained_variance_ratio_[0]:.2f})')
plt.ylabel(f'主成分2 (解释方差: {pca.explained_variance_ratio_[1]:.2f})')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')  # 图例放在右侧
plt.tight_layout()
plt.show()

# 6. 可选：确定最佳K值（肘部法）
inertia = []
k_range = range(1, 6)  # 测试1-5类
for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_features)
    inertia.append(kmeans.inertia_)

# 绘制肘部图
plt.figure(figsize=(8, 4))
plt.plot(k_range, inertia, 'bo-')
plt.xlabel('聚类数量K')
plt.ylabel('惯性值(Inertia)')
plt.title('肘部法确定最佳K值', fontsize=12)
plt.grid(alpha=0.3)
plt.show()
