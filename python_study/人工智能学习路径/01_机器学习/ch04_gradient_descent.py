import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

plt.rcParams["font.family"] = ["SimHei", "Microsoft YaHei", "Arial"]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["font.size"] = 12

def J(beta):
    return np.sum((X@beta-y)**2)/n

def gradient(beta):
    return 2*X.T@(X@beta-y)/n

X=np.array([[5],[8],[10],[12],[15],[3],[7],[9],[14],[6]])
y=np.array([55,65,70,75,85,50,60,72,80,58]).reshape(-1,1)
n=X.shape[0]
X=np.hstack((np.ones((n,1)),X))
#定义列表保存参数变化

beta0=[]
beta1=[]
#初始化参数以及超参数
alpha=0.01
iterations=10000
cnt=0
beta=np.array([[1],[1]])
#迭代
for i in range(iterations):
    grad=gradient(beta)
    beta=beta-alpha*grad
    beta0.append(beta[0,0])
    beta1.append(beta[1,0])
    if (np.abs(grad) < 1e-10).any():
        break
    cnt+=1
    if i%10==0:
        print(f"beta:{beta.reshape(-1)}\tJ:{J(beta)}")
print(cnt)

plt.plot(beta0,beta1,'r-')
plt.xlabel('beta0')
plt.ylabel('beta1')
plt.show()
