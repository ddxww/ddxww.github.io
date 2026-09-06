import numpy as np
from ch02_functions import softmax,sigmoid,cross_entropy
from ch03_gradient import numerical_gradient

class TwoLayerNet:
    def __init__(self, input_size, hidden_size, output_size,weight_init_std=0.01):
        self.params = {}
        self.params['W1'] = weight_init_std * np.random.randn(input_size, hidden_size)
        self.params['b1'] = np.zeros(hidden_size)
        self.params['W2'] = weight_init_std * np.random.randn(hidden_size, output_size)
        self.params['b2'] = np.zeros(output_size)
    #前向传播
    def forward(self, x):
        W1,W2 = self.params['W1'],self.params['W2']
        b1,b2 = self.params['b1'],self.params['b2']
        a1=np.dot(x,W1)+b1
        z1=sigmoid(a1)
        a2=np.dot(z1,W2)+b2
        y=softmax(a2)
        return y
    #计算损失
    def loss(self, x, t):
        y = self.forward(x)
        loss = cross_entropy(y, t)
        return loss
    #计算准确度
    def accuracy(self, x, t):
        y_proba = self.forward(x)
        #根据最大概率得到分类号
        y=np.argmax(y_proba,axis=1)
        #与正确解标签得到准确率
        accuracy = np.sum(y==t) / float(x.shape[0])
        return accuracy
    #计算梯度
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


