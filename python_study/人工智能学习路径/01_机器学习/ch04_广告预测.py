import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression,SGDRegressor,Ridge,Lasso
from sklearn.metrics import mean_squared_error

dataset=pd.read_csv('advertising.csv')
dataset.dropna(inplace=True)
dataset.drop(dataset.columns[0], axis=1, inplace=True)

X=dataset.iloc[:,:-1]
#或 X=dataset.drop(columns='Sales', axis=1)
y=dataset.iloc[:,-1]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=42)

scaler=StandardScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)
#线性回归
model_lr = LinearRegression()
model_lr.fit(X_train,y_train)
print("LR Coefficients:",model_lr.coef_)
print("LR Coefficients:",model_lr.intercept_)
#随机梯度下降
model_sgd = SGDRegressor()
model_sgd.fit(X_train,y_train)
print("SGD Coefficients:",model_sgd.coef_)
print("SGD Coefficients:",model_sgd.intercept_)
#Lasso回归
model_lasso=Lasso()
model_lasso.fit(X_train,y_train)
print("Lasso Coefficients:",model_lasso.coef_)
print("Lasso Coefficients:",model_lasso.intercept_)
#岭回归
model_ridge=Ridge()
model_ridge.fit(X_train,y_train)
print("Ridge Coefficients:",model_ridge.coef_)
print("Ridge Coefficients:",model_ridge.intercept_)
#预测
y_pred1=model_lr.predict(X_test)
y_pred2=model_sgd.predict(X_test)
#均方误差评价
print("LR mean_squared_error",mean_squared_error(y_test,y_pred1))
print("SGD mean_squared_error",mean_squared_error(y_test,y_pred2))
print("Lasso mean_squared_error",mean_squared_error(y_test,y_pred2))
print("Ridge mean_squared_error",mean_squared_error(y_test,y_pred1))