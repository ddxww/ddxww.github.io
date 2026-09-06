import numpy as np
from scipy.optimize import minimize
def fun(x):
    a=np.array([1,4,3,5,9,12,6,20,17,8])
    b=np.array([2,10,8,18,1,4,5,10,8,9])
    f=np.zeros(10)
    for i in range(10):
        f[i]=np.abs(x[0]-a[i])+np.abs(x[1]-b[i])
    return f
def overall_objective(x):
    return np.max(fun(x))
x0=np.array([6,6])
lb=np.array([3,4])
ub=np.array([8,10])
bounds=[(lb[0],ub[0]),(lb[1],ub[1])]
result=minimize(overall_objective,x0,method="SLSQP",bounds=bounds)
x=result.x
feval=fun(x)
print("坐标:")
print(x)
print(feval)
print("最小的最大距离:")
print(np.max(feval))
# 图3：加权图