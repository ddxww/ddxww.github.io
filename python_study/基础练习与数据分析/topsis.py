import numpy as np
import pandas as pd

# 数据
data = np.array([
    [7, 6, 7, 8],  # A
    [8, 5, 6, 7],  # B
    [9, 7, 8, 9],  # C
    [6, 4, 7, 6]   # D
])

# 指标属性：1=效益型(越大越好)，-1=成本型(越小越好)
criteria = [1, -1, 1, 1]

# 权重
weights = np.array([0.3, 0.2, 0.3, 0.2])

# 1. 归一化
norm_data = data / np.sqrt((data**2).sum(axis=0))

# 2. 加权
weighted_data = norm_data * weights

# 3. 正理想解 & 负理想解
ideal_pos = np.max(weighted_data * criteria, axis=0)
ideal_neg = np.min(weighted_data * criteria, axis=0)

# 4. 计算距离
dist_pos = np.sqrt(((weighted_data - ideal_pos)**2).sum(axis=1))
dist_neg = np.sqrt(((weighted_data - ideal_neg)**2).sum(axis=1))

# 5. 贴近度
scores = dist_neg / (dist_pos + dist_neg)

# 输出结果
alternatives = ["A", "B", "C", "D"]
result = pd.DataFrame({"地点": alternatives, "综合得分": scores})
result["排序"] = result["综合得分"].rank(ascending=False).astype(int)

print(result.sort_values("综合得分", ascending=False))
