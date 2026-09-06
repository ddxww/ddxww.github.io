import numpy as np
from matplotlib import rcParams
from scipy.optimize import linprog
from matplotlib import pyplot as plt
weights=[
    (0.4,0.6),
    (0.5,0.5),
    (0.3,0.7)
]
A=[[-1,-1]]
b=[-7]
lb=[0,0]
ub=[5,6]
bounds=((lb[0],ub[0]),(lb[1],ub[1]))
for w1,w2 in weights:
    c=[w1/30*2+w2/2*0.4,w1/30*5+w2/2*0.3]
    result = linprog(c, A, b, bounds=bounds,method='highs')
    x=result.x
    fval=result.fun
    f1=2*x[0]+5*x[1]
    f2=0.4*x[0]+0.3*x[1]
    print(f"\n权重组合:w1={w1},w2={w2}")
    print(f"目标函数:f1={f1:.2f},f2={f2:.2f},综合指标={fval:.2f}")
W1=np.arange(0.1,0.501,0.001)
W2=1-W1
n=len(W1)
F1=np.zeros(n)
F2=np.zeros(n)
X1=np.zeros(n)
X2=np.zeros(n)
FVAL=np.zeros(n)
for i in range(n):
    w1=W1[i]
    w2=W2[i]
    c = [w1 / 30 * 2 + w2 / 2 * 0.4, w1 / 30 * 5 + w2 / 2 * 0.3]
    result = linprog(c, A, b, bounds=bounds,method='highs')
    x=result.x
    F1[i]=2*x[0]+5*x[1]
    F2[i]=0.4*x[0]+0.3*x[1]
    X1[i]=x[0]
    X2[i]=x[1]
    FVAL[i]=result.fun
rcParams['font.sans-serif'] = ['SimHei']
rcParams['axes.unicode_minus'] = False
plt.figure()
plt.plot(W1, F1,label="f1")
plt.plot(W2, F2,label="f2")
plt.xlabel("f1权重(w1)")
plt.ylabel("目标函数值")
plt.legend()
plt.title("目标函数权重变化的关系")
plt.grid()

plt.figure()
plt.plot(W1, X1,label="x1")
plt.plot(W2, X2,label="x2")
plt.xlabel("f1权重(w1)")
plt.xlabel("f1权重(w1)")
plt.ylabel("决策变量值")
plt.title("决策变量权重变化的关系")
plt.grid()

plt.figure()#打开白布
plt.plot(W1, FVAL)
plt.xlabel("f1的权重")
plt.ylabel("综合指标值")
plt.title("综合指标值权重变化关系")
plt.grid()

plt.show()

