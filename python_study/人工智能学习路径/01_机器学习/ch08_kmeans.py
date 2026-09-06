import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
plt.rcParams["font.family"] = ["SimHei", "Microsoft YaHei", "Arial"]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["font.size"] = 12

X, y = make_blobs(n_samples=150, cluster_std=2 , centers=3, random_state=42)

fig,ax=plt.subplots(2,figsize=(8,8))
ax[0].scatter(X[:, 0], X[:, 1], c='gray',s=50,label="原始数据")
ax[0].set_title('原始数据')
ax[0].legend()

kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)

centers = kmeans.cluster_centers_
y_kmeans = kmeans.predict(X)
ax[1].scatter(X[:, 0], X[:, 1], c=y_kmeans)
ax[1].scatter(centers[:, 0], centers[:, 1], c='red', marker='x',label='簇中心',s=200)
ax[1].set_title('KMeans聚类结果')
ax[1].legend()
plt.show()


