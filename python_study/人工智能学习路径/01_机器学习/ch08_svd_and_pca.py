import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

A=np.array([[1,1],[2,2],[0,0]])
S,V,D=np.linalg.svd(A)
print(S,V,D)

from sklearn.utils.extmath import randomized_svd
S,V,D=randomized_svd(A, n_components=2)
print(S,V,D)

from sklearn.decomposition import PCA

X=np.random.rand(100,3)
pca=PCA(n_components=2)
X_pca=pca.fit_transform(X)
print(X_pca)

import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

np.random.seed(42)

# 100个样本，每个样本3个特征
X = np.random.rand(100, 3)

# PCA：3维降到2维
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

fig = plt.figure(figsize=(12, 5))

# 左图：降维前的三维数据
ax1 = fig.add_subplot(1, 2, 1, projection="3d")

ax1.scatter(
    X[:, 0],
    X[:, 1],
    X[:, 2],
    c=X[:, 2],
    cmap="viridis"
)

ax1.set_xlabel("Feature 1")
ax1.set_ylabel("Feature 2")
ax1.set_zlabel("Feature 3")
ax1.set_title("Before PCA: 3D")

# 右图：PCA降维后的二维数据
ax2 = fig.add_subplot(1, 2, 2)

scatter = ax2.scatter(
    X_pca[:, 0],
    X_pca[:, 1],
    c=X[:, 2],
    cmap="viridis"
)

ax2.set_xlabel("Principal Component 1")
ax2.set_ylabel("Principal Component 2")
ax2.set_title("After PCA: 2D")
ax2.grid(alpha=0.3)

fig.colorbar(scatter, ax=ax2, label="Original Feature 3")

plt.tight_layout()
plt.show()
