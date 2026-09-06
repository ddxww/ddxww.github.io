# 阶跃函数
def step_function0(x):
    if x > 0:
        return 1
    else:
        return 0

import numpy as np

def step_function(x):
    return np.array(x > 0, dtype=int)

#Sigmoid函数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

#ReLU函数
def ReLU(x):
    return np.maximum(0, x)

#softmax函数
def softmax0(x):
    return np.exp(x) / np.sum(np.exp(x))

#输入可能是矩阵的情况
def softmax(x):
    if(x.ndim == 2):
        x=x.T
        x=x-np.max(x, axis=0)
        return (np.exp(x) / np.sum(np.exp(x),axis=0)).T
    x-=np.max(x)
    return np.exp(x) / np.sum(np.exp(x),axis=0)

#恒等函数
def identity(x):
    return x

#损失函数
#MSE
def mean_squared_error(y, t):
    return 0.5 * np.sum((y - t)**2)

#交叉熵损失函数
def cross_entropy(y, t):
    # 单个样本变成二维
    if y.ndim == 1:
        y = y.reshape(1, y.size)
    # 如果t是one-hot标签，转换成数字标签
    if t.size == y.size:
        t = t.reshape(y.shape)
        t = np.argmax(t, axis=1)
    # 保证数字标签是一维数组
    t = t.reshape(-1)
    n = y.shape[0]
    return np.sum(-np.log(y[np.arange(n), t] + 1e-10)) / n

if __name__ == '__main__':
    x = np.array([0, 1, 2, 3, 4, 5, -1, -2, -3, -4, -5])
    print(step_function(x))
    print(sigmoid(x))
    print(np.tanh(x))
    print(ReLU(x))
    print(softmax(x))
    X=np.array([[0,1,2],[3,4,5],[6,7,8],[-1,-2,-3]])
    print(softmax(X))