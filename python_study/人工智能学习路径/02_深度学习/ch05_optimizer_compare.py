import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict
from ch05_optimizer import *

#定义函数
def f(x,y):
    return x**2/20+y**2

#定义梯度计算方法，得到长度为2的向量
def f_grad(x,y):
    return x/10,2*y

#定义初始点位置
init_pos=(-7.0,2.0)
params={}
grads={}

#定义优化器,指定学习率
optimizers=OrderedDict()
optimizers["SGD"]=SGD(lr=0.9)
optimizers["Momentum"]=Momentum(lr=0.1, momentum=0.85)
optimizers["AdaGrad"]=AdaGrad(lr=1.5)
optimizers["Adam"]=Adam(lr=0.5,alpha1=0.5)

idx=1 #子图序号

#遍历优化器，更新参数，求最小值点
for key in optimizers:
    optimizer=optimizers[key]
    #记录参数点更新的历史
    x_history=[]
    y_history=[]
    #参数初始化
    params['x'],params['y']=init_pos[0],init_pos[1]
    #指定迭代次数
    for i in range(30):
        #保存当前点坐标
        x_history.append(params['x'])
        y_history.append(params['y'])
        #1.计算梯度
        grads['x'],grads['y']=f_grad(params['x'],params['y'])

        #2.更新参数
        optimizer.update(params,grads)

    x=np.arange(-10,10,0.01)
    y=np.arange(-5,5,0.01)
    X,Y=np.meshgrid(x,y)
    Z=f(X,Y)
    Z = np.ma.masked_where(Z > 7, Z)
    #定义子图
    plt.subplot(2,2,idx)
    idx+=1
    #画出等高线
    plt.contour(X,Y,Z,levels=np.arange(0, 7, 0.5),colors="black",linewidths=0.5)
    #单独画出最小值点
    plt.plot(0,0,'+')
    #画出点轨迹
    plt.plot(x_history,y_history,'ro-',markersize=2,label=key)
    plt.xlim(-10,10)
    plt.ylim(-5,5)
    plt.legend(loc='best')

plt.show()

