import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# 解决中文显示问题
plt.rcParams["font.family"] = ["SimSun", "Microsoft YaHei", "SimHei"]
plt.rcParams["axes.unicode_minus"] = False
def model(y,t,beta,u,v):
    S,I,ND=y;
    N_prime=S+I
    dSdt=-beta*S*I/N_prime+u*N_prime-v*S
    dIdt=beta*S*I/N_prime-v*I
    dNDdt=v*S+v*I
    return [dSdt, dIdt, dNDdt]
beta=0.1
u=0.002
v=0.001
S0=990
I0=10
ND0=0
y0=[S0,I0,ND0]
t=np.linspace(0,200,1000)
y=odeint(model,y0,t,args=(beta,u,v))
S=y[:,0]
I=y[:,1]
ND=y[:,2]
plt.figure(figsize=(10, 6))
plt.plot(t, S, label='易感者(S)', color='green')
plt.plot(t, I, label='感染者(I)', color='red')
plt.plot(t, ND, label='自然死亡(DND)', color='gray')

plt.xlabel('时间（天）')
plt.ylabel('人数')
plt.title('传染病模型（含自然新增+自然死亡）')
plt.legend()
plt.grid(True)
plt.show()