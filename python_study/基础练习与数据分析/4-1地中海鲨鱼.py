from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams["font.family"] = ["SimSun", "Microsoft YaHei", "SimHei"]
plt.rcParams["axes.unicode_minus"] = False  # 解决负号显示问题

# 定义微分方程模型
def model(X, t, alpha, beta, delta, gamma, c):
    P, V = X
    dPdt = alpha * P - beta * P * V - c * P
    dVdt = delta * P * V - gamma * V
    return [dPdt, dVdt]

# 初始条件和参数
P0 = 100  # 捕食者初始数量
V0 = 20   # 猎物初始数量
t = np.linspace(0, 10, 100)  # 时间点

# 参数值
alpha = 1     # 捕食者自然增长率
beta = 0.1    # 捕食效率
delta = 0.1   # 猎物转化为捕食者的效率
gamma = 0.1   # 捕食者死亡率
c = 0.05      # 捕食者种内竞争系数

# 正确调用odeint求解
X0 = [P0, V0]  # 初始条件数组
sol = odeint(model, X0, t, args=(alpha, beta, delta, gamma, c))

# 提取结果
P, V = sol[:, 0], sol[:, 1]

# 绘制结果
plt.figure(figsize=(10, 6))
plt.plot(t, P, 'r-', label='捕食者数量 (P)')
plt.plot(t, V, 'b-', label='猎物数量 (V)')
plt.xlabel('时间', fontsize=12)
plt.ylabel('种群数量', fontsize=12)
plt.title('捕食者-猎物模型动态变化', fontsize=14)
plt.legend()
plt.grid(True)
plt.show()