from scipy.integrate import solve_ivp, odeint
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = ["SimSun", "Microsoft YaHei", "SimHei"]  # 宋体、微软雅黑、黑体
plt.rcParams["axes.unicode_minus"] = False  # 解决负号显示问题
def model(P,t,r,K):
    dPdt=r*P*(1-P/K)
    return dPdt
P0=100
t=np.linspace(0,1000,1000)
r=0.04
K=1000
P=odeint(model,P0,t,args=(r,K))
plt.plot(t,P)
plt.xlabel('t')
plt.ylabel('P')
plt.show()