import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
plt.rcParams["font.family"] = ["SimSun", "Microsoft YaHei", "SimHei"]  # 宋体、微软雅黑、黑体
plt.rcParams["axes.unicode_minus"] = False  # 解决负号显示问题
data = pd.DataFrame({
    'T': [50, 60, 60, 70, 70, 80, 80, 90, 90, 90, 95, 100, 100, 100, 105,
          105, 110, 110, 110, 115, 115, 115, 120, 120, 120, 125, 130, 130,
          135, 135, 140, 140, 145, 150, 150, 155, 155, 160, 160, 160, 165, 170, 180],
    'A': [19, 20, 21, 17, 22, 25, 28, 21, 25, 31, 25, 30, 29, 33, 35,
          32, 30, 28, 30, 31, 36, 30, 36, 25, 28, 28, 31, 32, 34, 35, 26,
          33, 31, 36, 33, 41, 33, 40, 30, 37, 32, 35, 38]
})
t0 = data['T'].values
x0 = data['A'].values
plt.scatter(t0, x0)
plt.xlabel('时间 T (s)')
plt.ylabel('晶体生长轴向长度 A (μm)')
plt.title('时间与晶体生长轴向长度的关系')
plt.grid(True, linestyle='--', alpha=0.7)
d = {'t': t0, 'x': x0}
model = sm.formula.ols('x ~ t', d).fit()
y_pred = model.predict(d)  # 用模型预测的y值（回归线的y坐标
print("回归分析结果:")
print(model.summary())
print('残差的方差:', model.mse_resid)
plt.plot(t0, y_pred, color='b',
         label=f'回归线: A = {model.params[0]:.4f} + {model.params[1]:.4f}T')
plt.show()
