from scipy.optimize import minimize
import numpy as np
# def fun(x):
#     return x[0]+1/x[0]
# x0=[2]
# cons={"type":"ineq","fun":lambda x:x[0]}
# result=minimize(fun, x0, method='SLSQP', constraints=cons)
# print(result.x)
# print(result.fun)
def fun(x):
    return (2+x[0])/(1+x[1])-3*x[0]+4*x[2]
x0=[0.5,0.5,0.5]
bounds=[(0.1, 0.9) for _ in range(3)]
result=minimize(fun, x0, bounds=bounds)
print(result.x)
print(result.fun)
