import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram
from scipy.spatial.distance import pdist
plt.rcParams["font.family"] = ["SimSun", "Microsoft YaHei", "SimHei"]  # 宋体、微软雅黑、黑体
plt.rcParams["axes.unicode_minus"] = False  # 解决负号显示问题
# 设置图片清晰度
plt.rcParams['figure.dpi'] = 300
# 设置中文字体
plt.rcParams['font.sans-serif'] = ['WenQuanYi Zen Hei']
plt.rcParams['axes.unicode_minus'] = False

# 定义数据
data = {
    '城市': ['城市 A', '城市 B', '城市 C', '城市 D', '城市 E'],
    '经济发展得分': [85, 90, 60, 70, 95],
    '教育水平得分': [80, 85, 65, 75, 90],
    '医疗水平得分': [75, 80, 60, 70, 85]
}
df = pd.DataFrame(data)

# 提取样本特征数据
X = df[['经济发展得分', '教育水平得分', '医疗水平得分']].values

# 计算样本间的欧氏距离
condensed_distance = pdist(X)

# 进行层次聚类
Z = linkage(condensed_distance)

# 绘制聚类树状图
plt.figure(figsize=(10, 6))
dendrogram(Z, labels=df['城市'].tolist())
plt.title('城市综合发展水平 Q 型聚类树状图')
plt.xlabel('城市')
plt.xticks(rotation=45)
plt.ylabel('距离')
plt.show()