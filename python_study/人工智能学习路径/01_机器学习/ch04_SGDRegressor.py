import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import SGDRegressor

plt.rcParams["font.family"] = ["SimHei", "Microsoft YaHei", "Arial"]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["font.size"] = 12

X=np.array([[5],[8],[10],[12],[15],[3],[7],[9],[14],[6]])
y=np.array([55,65,70,75,85,50,60,72,80,58]).reshape(-1,1)

model = SGDRegressor(
    penalty=None,#正则化
    loss="squared_error",#损失函数
    max_iter=10**6,#最大迭代次数
    eta0=1e-5,#学习率
    learning_rate="constant",#常数学习率
    tol=1e-8,#停止迭代策略
)

model.fit(X, y)
print(model.intercept_, model.coef_)