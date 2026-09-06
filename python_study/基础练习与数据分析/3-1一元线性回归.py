import numpy as np

# 数据
x = np.array([143, 145, 146, 147, 149, 150, 153, 154, 155, 156, 157, 158, 159, 160, 162, 164])  # 身高
y = np.array([88, 85, 88, 91, 92, 93, 93, 95, 96, 98, 97, 96, 98, 99, 100, 102])  # 腿长

# 计算均值
x_mean = np.mean(x)
y_mean = np.mean(y)

# 计算斜率 (β₁)
numerator = np.sum((x - x_mean) * (y - y_mean))
denominator = np.sum((x - x_mean) ** 2)
slope = numerator / denominator
# 计算截距 (β₀)
intercept = y_mean - slope * x_mean
y_pred = slope * x + intercept
print(f"斜率 β₁ = {slope:.4f}")  # 应接近 0.7194
print(f"截距 β₀ = {intercept:.4f}")  # 应接近 -16.08
print(f"回归方程: ŷ = {slope:.4f}x{intercept:.4f}")
tss = np.sum((y - y_mean) ** 2)
ess = np.sum((y_pred - y_mean) ** 2)
rss = np.sum((y - y_pred) ** 2)
print(tss, ess, rss)
# 计算 R²
r_squared = ess / tss
print(f"R² = {r_squared:.4f}")