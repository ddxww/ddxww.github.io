from cProfile import label
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import pa1 as pd
plt.rcParams["font.family"] = ["SimSun", "Microsoft YaHei", "SimHei"]
plt.rcParams["axes.unicode_minus"] = False
# 1. 原始数据（年龄x & 运动能力y，一一对应）
x_age = np.array([17, 19, 21, 23, 25, 27, 29])  # 年龄
y_ability = np.array([22.415, 26.62, 26.225, 30.7, 26.51, 23, 20.325])  # 平均运动能力
# 2. 构造DataFrame（ statsmodels 要求用DataFrame传数据）
data = pd.DataFrame({'x': x_age, 'y': y_ability})
# 3. 拟合二次多项式回归（公式需用 I(x**2) 包裹非线性项）
model = smf.ols(formula='y ~ x + I(x**2)', data=data)  # 二次项：x + x²
results = model.fit()
# 4. 输出回归结果
print(results.summary())        # 详细统计结果
print("残差均方误差(MSE):", results.mse_resid)  # 残差MSE
# 5. 绘制拟合曲线（用更多点画平滑曲线）
x_fit = np.linspace(17, 29, 100)  # 生成17-29的连续x值
y_fit = results.predict(pd.DataFrame({'x': x_fit}))  # 预测拟合值
# 6. 可视化
plt.figure(figsize=(8,5))
plt.scatter(x_age, y_ability, color='blue', label='原始数据')  # 原始点
plt.plot(x_fit, y_fit, color='red', linewidth=2, label='二次多项式拟合')  # 拟合曲线
plt.xlabel('年龄')
plt.ylabel('运动能力（平均值）')
plt.title('年龄与运动能力的二次多项式回归分析')
plt.legend()
plt.grid(True)
plt.show()
