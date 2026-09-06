import numpy as np
import matplotlib.pyplot as plt
from ch04_backward import *
from ch03_load_data import get_data

x_train,x_test,t_train,t_test=get_data()
network=TwoLayerNet(input_size=784,hidden_size=50,output_size=10)
# 超参数
learning_rate=0.1
batch_size=100
num_epochs=10
train_size=x_train.shape[0]
iter_pre_epoch=np.ceil(train_size/batch_size)
iters_num=int(iter_pre_epoch*num_epochs)

train_loss_list=[]
train_acc_list=[]
test_acc_list=[]
for i in range(iters_num):
    # 随机选取批量数据
    batch_mask=np.random.choice(train_size,batch_size)
    x_batch=x_train[batch_mask]
    t_batch=t_train[batch_mask]
    # 计算梯度
    grad=network.gradient(x_batch,t_batch)
    # print("grad:======",i)
    for key in ('W1','b1','W2','b2'):
        network.params[key]-=learning_rate*grad[key]
    # 计算并且保存训练损失
    loss=network.loss(x_train,t_train)
    train_loss_list.append(loss)
    # 每完成一个epoch的迭代，就计算并保存训练准确率
    if i%iter_pre_epoch==0:
        train_acc=network.accuracy(x_train,t_train)
        test_acc=network.accuracy(x_test,t_test)
        train_acc_list.append(train_acc)
        test_acc_list.append(test_acc)
        print('Epoch:{},Loss:{},Accuracy:{},Test_acc:{}'.format(i//iter_pre_epoch+1,loss,train_acc,test_acc))

x=np.arange(len(train_acc_list))
plt.plot(x,train_acc_list,label='train')
plt.plot(x,test_acc_list,label='test',linestyle='--')
plt.xlabel('epoch')
plt.ylabel('accuracy')
plt.legend(loc='best')
plt.show()

