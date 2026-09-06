import numpy as np
from ch02_functions import softmax,cross_entropy
from ch03_gradient import numerical_gradient

#定义一个简单神经网络类
class SimpleNet:
    #初始化
    def __init__(self):
        self.W = np.random.randn(2,3)
    #前向传播
    def forward(self,X):
        a=X@self.W
        y=softmax(a)
        return y
    #计算损失
    def loss(self,x,t):
        y=self.forward(x)
        return cross_entropy(y,t)#计算交叉熵

if __name__=='__main__':
    x=np.array([0.6,0.9])
    t=np.array([0,0,1])
    net=SimpleNet()
    f=lambda _: net.loss(x,t)
    gradw=numerical_gradient(f,net.W)
    print(gradw)
    #如果梯度是＞0，如w00>0，w00增大，则f损失函数也会增大；如果小于0w00增大损失函数减小


#使用说明
# x = np.array([0.6, 0.9])
# 特征1 = 0.6
# 特征2 = 0.9
# t = np.array([0, 0, 1])
# 第1类：0
# 第2类：0
# 第3类：1
# W = [
#     [w00, w01, w02],
#     [w10, w11, w12]
# ]
# score0 = 0.6*w00 + 0.9*w10
# score1 = 0.6*w01 + 0.9*w11
# score2 = 0.6*w02 + 0.9*w12
# y = softmax(scores)
# 得到三个类别的概率，例如：y = [0.2, 0.3, 0.5]
# y = np.array([0.2, 0.3, 0.5])
# t = np.array([0, 0, 1])
# # 将单个样本变成二维数组
# y = y.reshape(1, -1)
# t = t.reshape(1, -1)
# 正确答案是第3类，因此交叉熵主要使用：y[2],loss = -log(y[2])
# f = lambda _: net.loss(x, t)
# 以 W[0, 0] 为例。
# gradW[0,0]=(loss_plus - loss_minus)/(2 * 0.0001)#依次计算每个梯度
# gradW = [
#     [损失对w00的梯度, 损失对w01的梯度, 损失对w02的梯度],
#     [损失对w10的梯度, 损失对w11的梯度, 损失对w12的梯度]
# ]
