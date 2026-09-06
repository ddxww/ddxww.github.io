import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = ["SimSun", "Microsoft YaHei", "SimHei"]  # 宋体、微软雅黑、黑体
plt.rcParams["axes.unicode_minus"] = False  # 解决负号显示问题
# 构造数据，对应表10.10中的数据
x = np.array([1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5])
n_i = np.array([25, 32, 58, 52, 43, 39, 28, 21, 15])
m_i = np.array([8, 13, 26, 22, 20, 22, 16, 12, 10])
p_i = m_i / n_i
# 计算逻辑变换后的值 p_i* = ln(p_i / (1 - p_i))
p_i_star = np.log(p_i / (1 - p_i))
# 构建线性回归模型
X = x.reshape(-1, 1)
y = p_i_star.reshape(-1, 1)
linear_model = LinearRegression()
linear_model.fit(X, y)
# 获取线性回归的系数
beta_0 = linear_model.intercept_[0]
beta_1 = linear_model.coef_[0][0]
print(f"线性回归方程：p* = {beta_0:.4f} + {beta_1:.4f}x")
# 定义逻辑回归预测函数
def logistic_predict(x_val):
    return 1 / (1 + np.exp(beta_0 - beta_1 * x_val))

# 预测不同家庭年收入下的购房比例
x_pred = np.linspace(1, 10, 100)
p_pred = logistic_predict(x_pred)

# 绘制原始数据点和逻辑回归曲线
plt.scatter(x, p_i, color='red', label='Original Data')
plt.plot(x_pred, p_pred, color='blue', label='Logistic Regression Curve')
plt.xlabel('家庭年收入 x（万元）')
plt.ylabel('实际购房比例 p')
plt.title('Logistic 回归：家庭年收入与购房比例的关系')
plt.legend()
plt.show()