import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
plt.rcParams["font.family"] = ["SimSun", "Microsoft YaHei", "SimHei"]  # 宋体、微软雅黑、黑体
plt.rcParams["axes.unicode_minus"] = False  # 解决负号显示问题
# 生成数据
np.random.seed(42)  # 设置随机种子，保证结果可复现
data_array = np.random.randint(0, 101, size=(150, 4))
data_df = pd.DataFrame(data_array, columns=["A", "B", "C", "D"])
# 标准化处理
x1 = pd.DataFrame(
    StandardScaler().fit_transform(data_array),
    columns=['A', 'B', 'C', 'D']
)
# 设置画布
plt.figure(figsize=(16, 10))
# 为每个特征绘制折线图
for i, col in enumerate(['A', 'B', 'C', 'D'], 1):
    plt.subplot(2, 2, i)  # 2行2列布局
    # 绘制原始数据折线
    plt.plot(data_df.index, data_df[col], label='原始数据', color='blue', alpha=0.6, linewidth=1.5)
    # 绘制标准化数据折线
    plt.plot(x1.index, x1[col], label='标准化数据', color='red', alpha=0.6, linestyle='--', linewidth=1.5)
    plt.title(f'特征{col}：标准化前后对比', fontsize=12)
    plt.xlabel('样本索引', fontsize=10)
    plt.ylabel('值', fontsize=10)
    plt.legend()
    plt.grid(alpha=0.3)
# 调整布局
plt.tight_layout()
plt.show()
