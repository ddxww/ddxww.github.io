# 1. 导入所需库
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = ["SimSun", "Microsoft YaHei", "SimHei"]  # 宋体、微软雅黑、黑体
plt.rcParams["axes.unicode_minus"] = False  # 解决负号显示问题
# 2. 生成模拟数据（核心：用4个班级的成绩代表4组数据）
# 用正态分布模拟成绩：loc=均值, scale=标准差, size=数据个数
np.random.seed(42)  # 固定随机种子，让结果可重复
class1_scores = np.random.normal(loc=75, scale=8, size=50)  # 1班：均值75，标准差8，50个学生
class2_scores = np.random.normal(loc=82, scale=6, size=50)  # 2班：均值82，标准差6（成绩更集中）
class3_scores = np.random.normal(loc=68, scale=10, size=50) # 3班：均值68，标准差10（成绩差异大）
class4_scores = np.random.normal(loc=78, scale=7, size=50)  # 4班：均值78，标准差7
data = [class1_scores, class2_scores, class3_scores, class4_scores]
class_names = ["1班", "2班", "3班", "4班"]  # 每组数据的标签
plt.figure()  # 设置画布大小（宽10，高6）
box_plot = plt.boxplot(
    data,
    tick_labels=class_names,  # x轴标签（班级名）
    patch_artist=True,   # 允许给箱体填充颜色
    boxprops=dict(facecolor='lightblue'),  # 箱体填充色
    medianprops=dict(color='red', linewidth=2)  # 中位数线（红色粗线，更醒目）
)
plt.title('4个班级数学考试成绩分布箱线图', fontsize=14, pad=20)  # 标题
plt.xlabel('班级', fontsize=12)  # x轴名称
plt.ylabel('考试分数', fontsize=12)  # y轴名称
plt.ylim(40, 110)  # y轴范围（避免异常值让图变形）
plt.grid(axis='y', linestyle='--', alpha=0.7)  # 添加y轴网格线（虚线，透明度0.7）
plt.show()
class5_scores=np.random.normal(73,2,50);
data=[class5_scores]
plt.figure()
plt.boxplot(
    data,  # 假设 data 是一个单一数据集（如 [五班成绩数据]）
    tick_labels=['五班'],  # 用列表包裹单个标签
)
plt.show()
