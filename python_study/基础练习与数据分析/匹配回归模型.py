import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols
import pandas as pd
plt.rcParams["font.family"] = ["SimSun", "Microsoft YaHei", "SimHei"]  # 宋体、微软雅黑、黑体
plt.rcParams["axes.unicode_minus"] = False  # 解决负号显示问题
x = np.array([2, 3, 4, 5, 7, 8, 10, 11, 14, 15, 16, 18, 19])
y = np.array([106.42, 109.20, 109.58, 109.50, 110.00, 109.93, 110.49,
              110.59, 110.60, 110.90, 110.76, 111.00, 111.20])
data = pd.DataFrame({'x': x, 'y': y, 'x_squared': x**2, '1/x': 1/x, 'ln_x': np.log(x)})
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', label='观测数据')
plt.xlabel('距离 x')
plt.ylabel('金属含量 y')
plt.title('距离与金属含量的散点图')
plt.legend()
plt.grid(True)
plt.show()
# 3. 二次曲线模型：y ~ x + x^2
model_quad = ols('y ~ x + x_squared', data).fit()
print("二次曲线模型 summary:")
print(model_quad.summary())
y_pred_quad = model_quad.predict(data)

# 4. 双曲线模型：1/y ~ 1/x（这里选择1/y对1/x线性回归）
data['1/y'] = 1 / y
model_hyper = ols('I(1/y) ~ Q("1/x")', data).fit()
print("\n双曲线模型 summary:")
print(model_hyper.summary())
# 还原预测值（从1/y的预测转换为y的预测）
y_pred_hyper = 1 / model_hyper.predict(data)

# 5. 对数曲线模型：y ~ ln_x
model_log = ols('y ~ ln_x', data).fit()
print("\n对数曲线模型 summary:")
print(model_log.summary())
y_pred_log = model_log.predict(data)
# 6. 绘制各模型拟合曲线
plt.figure(figsize=(12, 8))
plt.scatter(x, y, color='blue', label='观测数据')
# 二次曲线
plt.plot(x, y_pred_quad, color='red', label=f'二次曲线: R²={model_quad.rsquared:.4f}')
# 双曲线
plt.plot(x, y_pred_hyper, color='green', label=f'双曲线: R²（基于1/y）={model_hyper.rsquared:.4f}')
# 对数曲线
plt.plot(x, y_pred_log, color='purple', label=f'对数曲线: R²={model_log.rsquared:.4f}')
plt.xlabel('距离 x')
plt.ylabel('金属含量 y')
plt.title('不同回归模型拟合结果对比')
plt.legend()
plt.grid(True)
plt.show()