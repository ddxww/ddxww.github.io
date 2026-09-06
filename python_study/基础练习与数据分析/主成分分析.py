import numpy as np
import pandas as pd
from sklearn.decomposition import PCA

# 1. 整理Hald水泥数据
data = {
    'x1': [7, 1, 11, 11, 7, 11, 3, 1, 2, 21, 1, 11, 10],
    'x2': [26, 29, 56, 31, 52, 55, 71, 31, 54, 47, 40, 66, 68],
    'x3': [6, 15, 8, 8, 6, 9, 17, 22, 18, 4, 23, 9, 8],
    'x4': [60, 52, 20, 47, 33, 22, 6, 44, 22, 26, 34, 12, 12]
}
df = pd.DataFrame(data)
X = df.values

# 2. PCA 不标准化
pca = PCA(n_components=4)
pca.fit(X)

# 输出特征值
print("特征值：", np.round(pca.explained_variance_, 4))

# 输出每个主成分的贡献率（百分比）
explained_ratio = pca.explained_variance_ratio_ * 100
for i, ratio in enumerate(explained_ratio):
    print(f"PC{i+1} 贡献率: {ratio:.2f}%")

# 输出累计贡献率
cumulative_ratio = np.cumsum(explained_ratio)
for i, cum_ratio in enumerate(cumulative_ratio):
    print(f"PC1~PC{i+1} 累计贡献率: {cum_ratio:.2f}%")

# 输出主成分载荷（原始变量形式）
loadings = pca.components_
variables = ['x1', 'x2', 'x3', 'x4']

for i in range(3):
    comp = loadings[i]
    expr_terms = []
    for j in range(4):
        var = variables[j]
        w = comp[j]
        sign = "+" if w >= 0 else "-"
        term = f"{sign} {abs(w):.4f}·{var}"
        expr_terms.append(term)
    expr_terms[0] = expr_terms[0].lstrip("+ ").strip()
    pc_expr = " ".join(expr_terms)
    print(f"\nPC{i+1} = {pc_expr}")
