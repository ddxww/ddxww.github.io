import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# 设置中文显示
plt.rcParams["font.family"] = ["SimSun", "Microsoft YaHei", "SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# 1. 数据准备
x = np.array([0.9, 1.1, 1.8, 2.3, 3.0, 3.3, 4.0])
p = np.array([0.37, 0.31, 0.44, 0.60, 0.67, 0.81, 0.79])

# 2. 计算逻辑变换 z = ln(p / (1 - p))
z = np.log(p / (1 - p))

# 3. 拟合Logistic回归的线性部分
x_with_const = sm.add_constant(x)
logistic_linear_model = sm.OLS(z, x_with_const).fit()
beta0, beta1 = logistic_linear_model.params  # 获取截距和斜率

# 4. 生成预测数据（用于绘制平滑曲线）
x_pred = np.linspace(min(x) - 0.5, max(x) + 0.5, 100)  # 扩展x范围，使曲线更完整
x_pred_with_const = sm.add_constant(x_pred)  # 添加常数项

# 5. 计算Logistic回归预测值
z_pred = logistic_linear_model.predict(x_pred_with_const)  # 预测z值
p_pred = 1 / (1 + np.exp(-z_pred))  # 将z转换回p（Logistic变换的逆过程）

# 6. 绘制图形
plt.figure(figsize=(10, 6))
# 绘制原始数据点
plt.scatter(x, p, color='red', label='原始数据', s=60, alpha=0.8)
# 绘制Logistic回归曲线
plt.plot(x_pred, p_pred, color='blue', linewidth=2, label='Logistic回归曲线')
# 标记半数效应剂量点（p=0.5时的x）
dose_half = -beta0 / beta1
plt.scatter(dose_half, 0.5, color='green', s=100, marker='*', label=f'半数效应剂量: {dose_half:.4f}')
plt.axhline(y=0.5, color='gray', linestyle='--', alpha=0.5)  # 水平线p=0.5
plt.axvline(x=dose_half, color='gray', linestyle='--', alpha=0.5)  # 垂直线x=半数剂量

# 添加标签和标题
plt.xlabel('剂量 x', fontsize=12)
plt.ylabel('副作用比例 p', fontsize=12)
plt.title('剂量与副作用比例的Logistic回归曲线', fontsize=14)
plt.legend(fontsize=10)
plt.grid(alpha=0.3)
plt.show()
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 手动构造简单数据：二维特征，二分类标签
X = np.array([
    [1, 2],
    [2, 3],
    [3, 1],
    [4, 2],
    [5, 6],
    [6, 5],
    [7, 7],
    [8, 6]
])
y = np.array([0, 0, 0, 0, 1, 1, 1, 1])

# 创建并训练逻辑回归模型
model = LogisticRegression()
model.fit(X, y)

# 预测与评估
y_pred = model.predict(X)
accuracy = accuracy_score(y, y_pred)
print(f"模型准确率：{accuracy:.2f}")
print("模型系数：", model.coef_)
print("模型截距：", model.intercept_)

# 绘制图形
plt.figure(figsize=(10, 6))

# 1. 绘制原始数据点
# 类别0用蓝色圆圈，类别1用红色叉号
plt.scatter(X[y == 0, 0], X[y == 0, 1], color='blue', marker='o', label='类别0')
plt.scatter(X[y == 1, 0], X[y == 1, 1], color='red', marker='x', label='类别1')
# 3. 标记新样本预测结果
new_sample = np.array([[3, 4]])
new_pred = model.predict(new_sample)
plt.scatter(new_sample[0, 0], new_sample[0, 1],
            color='green', s=150, marker='*',
            label=f'新样本(预测：{new_pred[0]})')

# 添加标签和标题
plt.xlabel('特征1')
plt.ylabel('特征2')
plt.title('逻辑回归分类结果与决策边界')
plt.legend()
plt.grid(alpha=0.3)
plt.show()
