import numpy as np
import matplotlib.pyplot as plt
from ch03_gradient import numerical_diff

def f(x):
    return 0.01*x**2+0.1*x

#返回切线方程函数
def tangent_line(f,x):
    y=f(x)
    #计算x处倒数（数值微分）
    a=numerical_diff(f,x)
    print("斜率为：",a)
    b=y-a*x
    return lambda x:a*x+b

x=np.arange(0.0,20.0,0.1)
y=f(x)
#计算x等于5处的切线方程
f_line=tangent_line(f,x=5)
y_line=f_line(x)
plt.plot(x,y)
plt.plot(x,f_line(x))
plt.show()
