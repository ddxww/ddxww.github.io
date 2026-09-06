import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# 解决中文显示问题
plt.rcParams["font.family"] = ["SimSun", "Microsoft YaHei", "SimHei"]
plt.rcParams["axes.unicode_minus"] = False
def model(y,t,beta,d):
    S,I,ID=y;
    N_prime=S+I
    dSdt=-beta*S*I/N_prime
    dIdt=beta*S*I/N_prime-d*I
    dIDdt=d*I
    return [dSdt, dIdt, dIDdt]
beta=0.1
d=0.01
S0 = 990      # 初始易感者数量
I0 = 10       # 初始感染者数量
ID0 = 0       # 初始因病死亡者数量
y0=[S0,I0,ID0]
t=np.linspace(0,500,1000)
y=odeint(model,y0,t,args=(beta,d))
plt.figure(figsize=(10, 6))
S=y[:,0]
I=y[:,1]
ID=y[:,2]
plt.plot(t, S, label='易感者(S)', color='green')
plt.plot(t, I, label='感染者(I)', color='red')
plt.plot(t, ID, label='因病死亡者(ID)', color='black')

plt.xlabel('时间（天）')
plt.ylabel('人数')
plt.title('传染病模型（仅考虑疾病死亡率，无自然出生/死亡）')
plt.legend()
plt.grid(True)
plt.show()

