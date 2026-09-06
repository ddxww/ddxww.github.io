from ch02_functions import *

#激活函数
#ReLU
class Relu:
    def __call__(self):
        #内部属性，记录哪些x等于0
        self.mask=None
    #前向传播代码
    def forward(self, x):
        self.mask = (x<=0)
        y=x.copy()
        # 将x<=0的值都赋为0
        y[self.mask]=0
        return y
    #反向传播代码
    def backward(self, dy):
        dx = dy.copy()
        #将x<=0的值都赋为0
        dx[self.mask] = 0
        return dx

#Sigmoid
class Sigmoid:
    def init(self):
        #定义内部属性，记录输出y，用于反向传播时计算梯度
        self.y=None
    #前向传播
    def forward(self,x):
        y=sigmoid(x)
        self.y=y
        return y
    #反向传播
    def backward(self,dy):
        dx=dy*self.y*(1.0-self.y)
        return dx

# Affine仿射层
class Affine:
    def __init__(self, W, b):
        self.W=W
        self.b=b
        #对输入数据x做保存，方便反向传播计算梯度
        self.X=None
        self.original_x_shape=None
        #将权重和偏置参数的梯度保存成属性，方便梯度下降法计算
        self.dW=None
        self.db=None
    #前向传播
    def forward(self,X):
        self.original_x_shape=X.shape
        self.X=X.reshape(X.shape[0],-1)
        Y=np.dot(self.X,self.W)+self.b
        return Y
    #反向传播
    def backward(self,dy):
        dX=np.dot(dy,self.W.T)
        dX=dX.reshape(*self.original_x_shape)
        self.dW=np.dot(self.X.T,dy)
        self.db=np.sum(dy,axis=0)
        return dX
#输出层
class SoftmaxWithLoss:
    def __init__(self):
        self.loss=None
        self.y=None
        self.t=None
    #前向传播
    def forward(self,X,t):
        self.t=t
        self.y=softmax(X)
        self.loss=cross_entropy(self.y,t)
        return self.loss
    #反向传播
    def backward(self,dy=1):
        n=self.y.shape[0]
        #如果是独热编码的形式，就代入公式直接计算
        if self.t.size==self.y.size:
            dx=self.y-self.t
            #如果是顺序编码的标签
        else:
            dx=self.y.copy()
            dx[np.arange(n),self.t]-=1
        return dx/n











# import numpy as np
#
# # 模拟ReLU forward输入
# x = np.array([-2, 3, -1, 5])
#
# # ========== 错误写法：y = x ==========
# y = x
# mask = (x <= 0)
# y[mask] = 0
#
# print("错误写法，原始x被篡改：")
# print("x =", x)   # [0 3 0 5] 原始数据没了！
# print("y =", y)
#
# # 重置数据
# x = np.array([-2, 3, -1, 5])
#
# # ========== 正确写法：y = x.copy() ==========
# y = x.copy()
# mask = (x <= 0)
# y[mask] = 0
#
# print("\n正确写法，原始x保留：")
# print("x =", x)   # [-2  3 -1  5] 原始数据完好
# print("y =", y)   # [0 3 0 5]