import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler  # 导入最大最小归一化工具

plt.rcParams["font.family"] = ["SimSun", "Microsoft YaHei", "SimHei"]  # 支持中文显示
plt.rcParams["axes.unicode_minus"] = False  # 解决负号显示问题

# 生成原始数据
np.random.seed(42)  # 固定随机种子，结果可复现
data_array = np.random.randint(0, 101, size=(150, 4))
data_df = pd.DataFrame(data_array, columns=["A", "B", "C", "D"])
print("原始数据前5行：")
print(data_df.head(), "\n")

# 最大最小归一化处理（缩放到[0, 1]区间）
minmax_scaler = MinMaxScaler()  # 实例化归一化器
data_minmax = minmax_scaler.fit_transform(data_array)  # 拟合并转换数据
data_minmax_df = pd.DataFrame(data_minmax, columns=["A", "B", "C", "D"])  # 转为DataFrame

print("最大最小归一化后的数据前5行：")
print(data_minmax_df.head())
print("\n归一化后数据统计描述（确保在[0,1]区间）：")
print(data_minmax_df.describe().round(4))

# 可视化：对比归一化前后的数据分布
plt.figure(figsize=(16, 10))

# 为每个特征绘制折线图
for i, col in enumerate(["A", "B", "C", "D"], 1):
    plt.subplot(2, 2, i)  # 2行2列布局

    # 原始数据折线
    plt.plot(data_df.index, data_df[col], label="原始数据", color="blue", alpha=0.6, linewidth=1.5)

    # 归一化后数据折线
    plt.plot(data_minmax_df.index, data_minmax_df[col], label="归一化后数据", color="green", alpha=0.6, linestyle="--",
             linewidth=1.5)

    plt.title(f"特征{col}：最大最小归一化前后对比", fontsize=12)
    plt.xlabel("样本索引", fontsize=10)
    plt.ylabel("数值", fontsize=10)
    plt.legend()
    plt.grid(alpha=0.3)

plt.tight_layout()  # 自动调整布局
plt.show()
