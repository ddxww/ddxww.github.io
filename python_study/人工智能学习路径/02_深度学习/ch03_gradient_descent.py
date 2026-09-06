import numpy as np
import matplotlib.pyplot as plt
from ch03_gradient import numerical_gradient

#定义梯度下降法函数
def gradient_descent(f,init_x,lr=0.1,num_iter=100):
    x=init_x
    x_history=[]
    for i in range(num_iter):
        x_history.append(x.copy())
        #梯度下降
        grad=numerical_gradient(f,x)
        #更新参数
        x-=lr*grad
    return x,np.array(x_history)

#定义目标函数
def f(x):
    return x[0]**2+x[1]**2

if __name__=='__main__':
    # 初始值
    x = np.array([-3.0, 4.0])
    lr = 0.2
    num_iter = 20
    x, x_history = gradient_descent(f, x, lr, num_iter)
    print("最小值点：", x)
    # 创建曲面的x[0]和x[1]
    x0 = np.linspace(-5, 5, 100)
    x1 = np.linspace(-5, 5, 100)
    X0, X1 = np.meshgrid(x0, x1)
    # 计算曲面高度
    Z = X0 ** 2 + X1 ** 2
    # 计算梯度下降过程中每一个点的函数值
    Z_history = (x_history[:, 0] ** 2+ x_history[:, 1] ** 2)
    fig = plt.figure()
    ax = fig.add_subplot(111,projection="3d")
    ax.view_init(elev=30, azim=45)
    # 绘制函数曲面
    ax.plot_surface(X0,X1,Z,cmap="viridis",alpha=0.6)
    # 绘制梯度下降轨迹
    ax.plot(x_history[:, 0],x_history[:, 1],Z_history,"o-r")
    ax.set_xlabel("x[0]")
    ax.set_ylabel("x[1]")
    ax.set_zlabel("f(x)")
    plt.show()


