import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

plt.rcParams["font.family"] = ["SimHei", "Microsoft YaHei", "Arial"]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["font.size"] = 12
X=np.array([[5],[8],[10],[12],[15],[3],[7],[9],[14],[6]])
y=np.array([55,65,70,75,85,50,60,72,80,58])
#创建模型
model = LinearRegression()
model.fit(X,y)
print(model.coef_)
print(model.intercept_)
X_new=np.array([[11]])
y_pred=model.predict(X_new)
print(y_pred)
#画图
# plt.figure(figsize=[8,6])
# plt.scatter(X,y,marker='o',color='b',label='data')
# plt.plot(X,model.predict(X),color='red',label="拟合直线")
# plt.legend(loc="upper left")
# plt.grid(visible=True,alpha=0.3)
# plt.tight_layout()
# plt.show()
x_line=np.linspace(min(X),max(X),100).reshape(-1,1)
y_line=model.predict(x_line)
plt.scatter(X,y,color='g')
plt.plot(x_line,y_line,color='r')
plt.show()
x=X.reshape(-1)
cov=np.cov(x,y)
beta1=cov[0,1]/cov[0,0]
print(beta1)
model=LinearRegression(fit_intercept=False)
model.fit(X,y)
print(model.coef_)
print(model.intercept_)
x_new=[[11]]
y_pred=model.predict(x_new)
print(y_pred)


