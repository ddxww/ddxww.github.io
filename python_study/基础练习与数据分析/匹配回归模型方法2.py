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
p1 = np.polyfit(x, y, 1)  # 对x和y进行一次多项式拟合，得到系数数组p1（形式为[p1_slope, p1_intercept]）
p2 = np.polyfit(x, y, 2)
x_log = np.log(x)
p3 = np.polyfit(x_log, y, 1)  # 返回 [b, a]（斜率b和截距a）
x_log = np.log(x)
b, a = p3
plt.plot(x,y,'o')
plt.plot(x, p1[0] * x + p1[1])
plt.plot(x, p2[0] * x*x + p2[1]*x+p2[2])
plt.plot(x, a + b*x_log)
plt.show()
