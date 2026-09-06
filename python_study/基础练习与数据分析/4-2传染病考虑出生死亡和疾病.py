import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# 解决中文显示
plt.rcParams["font.family"] = ["SimSun", "Microsoft YaHei", "SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# 微分方程模型（S:易感者, I:感染者, ND:自然死亡, ID:因病死亡）
def disease_model(y, t, mu, beta, nu, d):
    S, I, ND, ID = y
    N_prime = S + I  # 存活总人口 N' = S + I
    # 按状态转移写方程
    dSdt = mu * N_prime - beta * S * I / N_prime - nu * S   # 新增-感染-自然死亡
    dIdt = beta * S * I / N_prime - nu * I - d * I         # 感染-自然死亡-因病死亡
    dNDdt = nu * (S + I)                                    # 自然死亡总和
    dIDdt = d * I                                          # 因病死亡
    return [dSdt, dIdt, dNDdt, dIDdt]

# 参数与初始条件
mu = 0.01    # 自然出生率（新增人口系数）
beta = 0.2   # 传播系数
nu = 0.005   # 自然死亡率
d = 0.1      # 疾病死亡率

S0 = 900     # 初始易感者
I0 = 100     # 初始感染者
ND0 = 0      # 初始自然死亡
ID0 = 0      # 初始因病死亡
y0 = [S0, I0, ND0, ID0]
t = np.linspace(0, 200, 1000)  # 0-200天，1000个时间点

# 求解
sol = odeint(disease_model, y0, t, args=(mu, beta, nu, d))
S, I, ND, ID = sol[:,0], sol[:,1], sol[:,2], sol[:,3]

# 可视化
plt.figure(figsize=(10,6))
plt.plot(t, S, 'g-', label='易感者(S)')
plt.plot(t, I, 'r-', label='感染者(I)')
plt.plot(t, ND, 'gray', label='自然死亡(ND)')
plt.plot(t, ID, 'black', label='因病死亡(ID)')

plt.xlabel('时间（天）')
plt.ylabel('人数')
plt.title('传染病模型（含自然出生/死亡 + 疾病死亡）')
plt.legend()
plt.grid()
plt.show()