import numpy as np
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,MinMaxScaler
from ch02_functions import sigmoid,softmax

def get_data():
    data=pd.read_csv('train1.csv')
    X=data.drop(columns=['label'])
    y=data['label']
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=42)
    scaler=MinMaxScaler()
    scaler.fit(X_train)
    X_train=scaler.transform(X_train)
    X_test=scaler.transform(X_test)
    return X_test,y_test

def inti_network():
    network=joblib.load('nn_sample')
    return network
def forward(network,x):
    w1, w2, w3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']
    a1 = np.dot(x, w1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, w2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, w3) + b3
    y = softmax(a3)
    return y

x,y=get_data()
network=inti_network()
# print(network['W1'].shape)
# print(network['W2'].shape)
# print(network['W3'].shape)
# print(network['b1'].shape)
# print(network['b2'].shape)
# print(network['b3'].shape)

#前向传播
y_proba=forward(network,x)

#转化为标签
y_pred=np.argmax(y_proba,axis=1)

#计算准确率
accuracy_sum=np.sum(y_pred==y)
n=x.shape[0]
print('accuracy:',accuracy_sum/n)


