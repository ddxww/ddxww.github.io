import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.tree import plot_tree
import matplotlib.font_manager as fm

# 1. 自动检测系统中可用的中文字体
available_fonts = [f for f in fm.findSystemFonts() if any(['simhei' in f.lower(), 'microsoftyahei' in f.lower(),
                                                           'heiti' in f.lower(), 'pingfang' in f.lower()])]

# 2. 设置可用的中文字体（优先选择系统中已安装的）
if available_fonts:
    # 提取字体名称
    font_name = fm.FontProperties(fname=available_fonts[0]).get_name()
    plt.rcParams["font.family"] = font_name
else:
    # 如果没有检测到中文字体，使用默认字体（可能显示方块，但避免报错）
    print("警告：未检测到中文字体，可能无法正常显示中文")

plt.rcParams["axes.unicode_minus"] = False  # 解决负号显示问题

# 3. 加载数据集
iris = load_iris()
X = iris.data  # 特征：花萼长度、花萼宽度、花瓣长度、花瓣宽度
y = iris.target  # 标签：0-山鸢尾，1-变色鸢尾，2-维吉尼亚鸢尾

# 中文特征名称和类别名称
特征名称 = ["花萼长度（cm）", "花萼宽度（cm）", "花瓣长度（cm）", "花瓣宽度（cm）"]
类别名称 = ["山鸢尾", "变色鸢尾", "维吉尼亚鸢尾"]

# 将数据转换为DataFrame以便查看
df = pd.DataFrame(X, columns=特征名称)
df['种类'] = [类别名称[i] for i in y]
print("数据集前5行：")
print(df.head())
print("\n数据集基本信息：")
print(f"特征数量：{X.shape[1]}")
print(f"样本数量：{X.shape[0]}")
print(f"类别：{类别名称}")

# 4. 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42  # 30%作为测试集
)

# 5. 创建并训练决策树模型
clf = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=42)
clf.fit(X_train, y_train)

# 6. 模型预测与评估
y_pred = clf.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"\n模型准确率：{accuracy:.2f}")

print("\n分类报告：")
print(classification_report(y_test, y_pred, target_names=类别名称))

print("混淆矩阵：")
print(confusion_matrix(y_test, y_pred))

# 7. 可视化决策树
plt.figure(figsize=(15, 10))
plot_tree(
    clf,
    feature_names=特征名称,
    class_names=类别名称,
    filled=True,
    rounded=True,
    proportion=True
)
plt.title("鸢尾花分类决策树")
plt.show()

# 8. 特征重要性分析
feature_importance = pd.DataFrame({
    '特征': 特征名称,
    '重要性': clf.feature_importances_
}).sort_values(by='重要性', ascending=False)

print("\n特征重要性：")
print(feature_importance)
# 新样本特征（可以是单个样本，也可以是多个样本组成的列表）
new_samples = [
    [5.1, 3.5, 1.4, 0.2],  # 样本1
    [6.7, 3.0, 5.2, 2.3],  # 样本2
    [5.9, 3.0, 4.2, 1.5]   # 样本3
]

# 预测类别（返回的是类别索引，对应0-山鸢尾，1-变色鸢尾，2-维吉尼亚鸢尾）
pred_indices = clf.predict(new_samples)

# 将索引转换为中文类别名称
pred_names = [类别名称[i] for i in pred_indices]

# 打印结果
for i, (sample, name) in enumerate(zip(new_samples, pred_names)):
    print(f"样本{i+1}特征：{sample} → 预测种类：{name}")
