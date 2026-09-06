# 导入库
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = ["SimSun", "Microsoft YaHei", "SimHei"]  # 宋体、微软雅黑、黑体
plt.rcParams["axes.unicode_minus"] = False  # 解决负号显示问题
# -------------------------------
# 1. 加载鸢尾花数据集
# -------------------------------
iris = load_iris()
X = iris.data
y = iris.target
feat_labels = iris.feature_names

# -------------------------------
# 2. 划分训练集和测试集
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# -------------------------------
# 3. 随机森林训练
# -------------------------------
forest = RandomForestClassifier(n_estimators=500, random_state=42, n_jobs=-1)
forest.fit(X_train, y_train)

# -------------------------------
# 4. 特征重要性评估
# -------------------------------
importances = forest.feature_importances_
indices = np.argsort(importances)[::-1]

print("特征重要性排序：")
for i, idx in enumerate(indices):
    print(f"{i+1:2d}) {feat_labels[idx]:20s} {importances[idx]:.6f}")

# -------------------------------
# 5. 可视化特征重要性
# -------------------------------
plt.figure(figsize=(8, 5))
colors = ['red' if importances[i] > 0.2 else 'orange' for i in indices]
plt.bar(range(X.shape[1]), importances[indices], color=colors, align='center')
plt.xticks(range(X.shape[1]), [feat_labels[i] for i in indices], rotation=45)
plt.ylabel("Feature Importance")
plt.title("Iris 数据集特征重要性")
plt.show()

# -------------------------------
# 6. 模型评估
# -------------------------------
y_pred = forest.predict(X_test)
print("\n测试集准确率：", accuracy_score(y_test, y_pred))
print("\n分类报告：\n", classification_report(y_test, y_pred, target_names=iris.target_names))
