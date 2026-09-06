import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression

dataset = pd.read_csv("train1.csv")

# 划分特征与标签
X = dataset.drop(dataset.columns[0], axis=1)
y = dataset[dataset.columns[0]]

#展示图像
# digit=dataset.iloc[187,1:].values
# plt.imshow(digit.reshape(28,28),cmap='gray')
# plt.show()

# 划分训练集、测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 归一化
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 修复收敛警告：增大迭代次数 + 适配求解器
model = LogisticRegression(max_iter=500)
model.fit(X_train, y_train)

# 模型准确率
score = model.score(X_test, y_test)
print("测试集准确率：", score)

# 单样本预测
digit = X_test[123].reshape(1, -1)
print("预测类别：", model.predict(digit))
print("各类别概率：", model.predict_proba(digit))
print("真实类别：", y_test.iloc[123])

for i in range(2,10):
    print("预测类别：", model.predict(X_test[i].reshape(1, -1)))
    plt.imshow(X_test[i].reshape(28, 28), cmap='gray')
    plt.show()
#画出图像
plt.imshow(X_test[123].reshape(28, 28), cmap='gray')
plt.show()