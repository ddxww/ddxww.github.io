from scipy.optimize import minimize
import numpy as np
def objective(x):
    return -(x[0]*x[1]+2*x[1]*x[2]+3*x[0]*x[2])
def eq1(x):
    return x[0]+x[1]+x[2]-1
x0=np.array([0,0,1])
cons={"type":"eq","fun":eq1}
result = minimize(objective,x0,constraints=cons,method='SLSQP')
print(-result.fun)