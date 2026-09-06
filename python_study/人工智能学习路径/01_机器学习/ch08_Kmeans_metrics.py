import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score,calinski_harabasz_score
plt.rcParams["font.family"] = ["SimHei", "Microsoft YaHei", "Arial"]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["font.size"] = 12

X, y = make_blobs(n_samples=150, cluster_std=2 , centers=3, random_state=42)
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)
centers = kmeans.cluster_centers_
y_kmeans = kmeans.predict(X)

#评价指标
print(kmeans.inertia_)
print(silhouette_score(X, y_kmeans))
print(calinski_harabasz_score(X, y_kmeans))