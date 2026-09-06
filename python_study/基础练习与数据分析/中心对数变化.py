import numpy as np

# 风化后的成分比例（总和=1）
weathered = np.array([
    [0.6, 0.3, 0.1],  # 样本1
    [0.4, 0.5, 0.1]  # 样本2
])

# 假设参数
conservative_idx = 0  # 第0列作为保守成分（如SiO₂）
retention_rate = 0.5  # 非保守成分的保留率


# 定义函数：计算风化前含量
def estimate_original(weathered_data, conservative_idx, retention_rate):
    n_samples, n_components = weathered_data.shape
    original = np.zeros_like(weathered_data, dtype=float)

    for i in range(n_samples):
        # 保守成分绝对量（风化前后不变）
        conservative_absolute = weathered_data[i, conservative_idx]

        # 计算各成分风化前的绝对量
        for j in range(n_components):
            if j == conservative_idx:
                original[i, j] = conservative_absolute  # 保守成分不变
            else:
                original[i, j] = weathered_data[i, j] / retention_rate  # 反推非保守成分

    # 计算风化前的总质量和比例
    original_total = original.sum(axis=1, keepdims=True)
    original_ratio = original / original_total

    # 关键：确保return在函数内部（有正确缩进）
    return original, original_ratio  # 这行必须缩进，属于函数的一部分


# 调用函数
original_absolute, original_ratio = estimate_original(
    weathered,
    conservative_idx,
    retention_rate
)

# 输出结果
print("风化后成分比例：")
print(weathered)
print("\n风化前成分比例：")
print(original_ratio)
import numpy as np
from skbio.stats.composition import clr
x = np.array([1, 3, 4, 2])

print(clr(x))