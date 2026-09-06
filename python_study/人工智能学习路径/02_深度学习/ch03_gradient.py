import numpy as np


def function_test(x):
    return np.sum(x**2+x)

# 数值微分求导
def numerical_diff(f,x):
    h=1e-4
    return (f(x+h)-f(x-h))/(2*h)


# 数值微分求梯度，传入x是向量
def _numerical_gradient(f,x):
    h=1e-4
    grad=np.zeros(x.shape)

    for i in range(x.size):
        tmp=x[i]
        x[i]=tmp+h
        fxh1=f(x)
        x[i]=tmp-h
        fxh2=f(x)
        grad[i]=(fxh1-fxh2)/(2*h)
        x[i]=tmp

    return grad


# 传入X是一个矩阵
def numerical_gradient(f,X):
    if X.ndim==1:
        return _numerical_gradient(f,X)
    else:
        grad=np.zeros(X.shape)
        for i,x in enumerate(X):
            grad[i]=_numerical_gradient(f,x)
    return grad


if __name__=="__main__":
    x=np.array([1,2,3,4],dtype=float)

    X=np.array([
        [1,2,3,4],
        [5,6,7,8]
    ],dtype=float)

    print(numerical_gradient(function_test,x))
    print(numerical_gradient(function_test,X))

