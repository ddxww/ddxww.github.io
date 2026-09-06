import numpy as np
from ch02_functions import softmax,sigmoid,cross_entropy
from ch03_gradient import numerical_gradient
from ch04_layers import *
from collections import OrderedDict

class TwoLayerNet:
    def __init__(self, input_size, hidden_size, output_size,weight_init_std=0.01):
        self.params = {}
        self.params['W1'] = weight_init_std * np.random.randn(input_size, hidden_size)
        self.params['b1'] = np.zeros(hidden_size)
        self.params['W2'] = weight_init_std * np.random.randn(hidden_size, output_size)
        self.params['b2'] = np.zeros(output_size)
        #定义层
        self.layers = OrderedDict()
        self.layers['Affine1'] = Affine(self.params['W1'], self.params['b1'])
        self.layers['Relu1'] = Relu()
        self.layers['Affine2'] = Affine(self.params['W2'], self.params['b2'])
        #单独定义最后一层，SoftmaxWithLoss
        self.lastLayer = SoftmaxWithLoss()
    #前向传播
    def forward(self, X):
        #对于每一层依次调用forward方法
        for layer in self.layers.values():
            X = layer.forward(X)
        return X
    #计算损失
    def loss(self, x, t):
        y = self.forward(x)
        loss_values=self.lastLayer.forward(y, t)
        return loss_values
    #计算准确度
    def accuracy(self, x, t):
        y_pred = self.forward(x)
        #根据最大概率得到分类号
        y=np.argmax(y_pred,axis=1)
        #与正确解标签得到准确率
        accuracy = np.sum(y==t) / float(x.shape[0])
        return accuracy
    #计算梯度,数值微分方法
    def numerical_gradient(self, x, t):
        #定义目标函数
        loss_f=lambda _:self.loss(x,t)
        #对每个参数，使用数值微分计算梯度
        grads={}
        grads['W1']=numerical_gradient(loss_f,self.params['W1'])
        grads['b1']=numerical_gradient(loss_f,self.params['b1'])
        grads['W2']=numerical_gradient(loss_f,self.params['W2'])
        grads['b2']=numerical_gradient(loss_f,self.params['b2'])
        return grads
    #计算梯度，使用反向传播方法
    def gradient(self, x, t):
        # 必须先进行一次前向传播
        self.loss(x, t)

        # 从输出层开始反向传播
        dy = 1
        dy = self.lastLayer.backward(dy)

        # 将网络层倒序
        layers = list(self.layers.values())
        layers.reverse()

        # 逐层反向传播
        for layer in layers:
            dy = layer.backward(dy)
        # 此时Affine层中的dW和db才已经计算完成
        grads = {}
        grads["W1"] = self.layers["Affine1"].dW
        grads["b1"] = self.layers["Affine1"].db
        grads["W2"] = self.layers["Affine2"].dW
        grads["b2"] = self.layers["Affine2"].db
        return grads
