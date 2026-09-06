from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams["font.family"] = ["SimSun", "Microsoft YaHei", "SimHei"]  # 宋体、微软雅黑、黑体
plt.rcParams["axes.unicode_minus"] = False  # 解决负号显示问题
# 1. 加载数据
iris = load_iris()
X = iris.data  # 特征
y = iris.target  # 真实类别 (只是用来对比，不参与聚类)

# 2. KMeans 聚类
kmeans = KMeans(n_clusters=3, random_state=0)
y_kmeans = kmeans.fit_predict(X)

# 3. 聚类结果 vs 真实标签
df = pd.DataFrame({"真实类别": y, "聚类结果": y_kmeans})
print(df.head(10))

# 4. 可视化（只画前两个特征）
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, cmap="viridis", marker="o")
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],
            s=200, c="red", marker="X", label="Cluster Centers")
plt.xlabel("Sepal length")
plt.ylabel("Sepal width")
plt.title("K-Means 聚类鸢尾花")
plt.legend()
plt.show()
