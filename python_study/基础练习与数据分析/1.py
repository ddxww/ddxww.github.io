# #file_sample=open(file="sample.txt",mode="r",encoding="utf-8")
# #content=file_sample.readlines()
# #for line in content:
# #    print(line)
# #file_sample.close()
# with open(file="sample.txt",mode="w",encoding="utf-8") as file_sample:
#       file_sample.write("hello world")
# #with open(file="sample.txt",mode="a",encoding="utf-8") as file_sample:
# #   file_sample.write("大家好!\n")
# from os import write
# #pip install numpy,pip install matplotlib,install pandas,unstall 卸载
# import numpy as np
# import  pandas as pd
# import matplotlib.pyplot as plt
# arr=np.array([1,2,4,3,5])
# print(arr[0])
# print(arr[0:3])
# print(arr[1:3])
# print(arr,type(arr))
# arr=np.array([[1,2,4,3,5],[2,3,4,5,6]])
# print(arr,type(arr),arr.shape)
# print(arr[1][1:4])
# print(np.array([1,2,3])+np.array([4,5,6])+np.array([7,8,9]))
# arr=np.array([[1,2,3],[2,3,4],[3,4,5],[4,5,6]])
# print(arr,arr.shape)
# arr=arr.reshape(2,6)
# print(arr,arr.shape)
# new_arr=arr.transpose()
# print(new_arr,new_arr.shape)
# arr1=np.array([1,2,3])
# arr2=np.array([4,5,6])
# print(np.dot(arr1,arr2))
# print(np.mean(arr1))
# print(arr)
# print(arr.mean())
# print(np.max(arr))
# print(np.min(arr))
# print(arr.sum)
# import numpy as np
# arr=np.array([2,3,1,4,5])
# print(arr.min(),arr.max(),arr.std())
# print(np.min(arr),np.max(arr),np.std(arr))
# print(np.sort(arr))
# arr=np.array([[1,2,4],[2,4,5],[5,6,1],[99,15,3]])
# print(np.sort(arr.reshape(-1)))
# print(arr[(arr>5) & (arr<20)])
# print(arr[(arr>5) | (arr<20)])
# import numpy as np
# arr=np.load("arr.npy")
# print(arr)
# import numpy as np
# #np.random.seed(1) #固定随机种子
# print(np.random.randint(1,100))
# arr=np.random.randint(1,100,16).reshape(4,4)
# print(np.sum(arr[arr<10]))
# import numpy as np
# arr=np.random.randint(1,100,16).reshape(4,4)
# print(arr,arr.sum())
# print(arr.reshape(8,2))


# import pandas as pd
# df=pd.read_excel("111111.xlsx","铜盘校区-非数学A类",engine="openpyxl")
# print(df.head(10))
# print(type(df))
# data={"样本号":[1,2,3],"参赛编号":[4,5,6],"姓名":[7,8,9]}
# datadf=pd.DataFrame(data)
# print(datadf)
# print(df.head())
# print(df.info())
# import pandas as pd
# df=pd.read_excel("训练数据.xlsx","Sheet1",engine="openpyxl")
# import pandas as pd
# df=pd.read_excel("训练数据.xlsx","Sheet1",engine="openpyxl")
# print(df.head(10))
# data={"样本号":[1,2,3],"萼片长":[4,5,6],"萼片宽":[7,8,9]}
# datadf=pd.DataFrame(data)
# print(datadf.head())
# df=df.dropna()
# print(df.head(10))
# print(df[df["类型_num"]==1])
# print(df.head(10))
# print(df.info())
# df=df.dropna()
# print(df.head(10))
# df["类型_num"]=df["类型_num"].astype(float)
# print(df.info())
# print(df["类型_num"]==1)
# print(df[df["类型_num"]==1])
# df_1=df[df["类型_num"]==1]
# print(df_1.head())
# print(df_1.info())
# lb=df["花瓣宽"].mean()-3 * df["花瓣宽"].std()
# ub=df["花瓣宽"].mean()+3 * df["花瓣宽"].std()
# print((df["花瓣宽"]>=lb) & (df["花瓣宽"]<=ub))
# print(df[(df["花瓣宽"]>=lb) & (df["花瓣宽"]<=ub)&df["类型_num"]==1])
# selected_df=df[(df["花瓣宽"]>=lb) & (df["花瓣宽"]<=ub)]
# print(selected_df.info())
# import pandas as pd
# import numpy as np
# data={"姓名": ["张三", "李四", "王五", "老六", "赵七"],
#      "身高": [175 for i in range(5)],
#      "体重": [50 for j in range(5)],
#      "成绩": np.random.randint(40, 100, 5)}
# df = pd.DataFrame(data)
# print(df)
# print(df[(df["成绩"] == max(df["成绩"]))])
# name=df[df["成绩"]<=60]
# print("平均分",np.mean(df["成绩"]))
# print(name["姓名"])
# print(df[df["成绩"]<=60]["姓名"])
# arr=np.array([1,2,3,4,5,6])
# print(arr.reshape(2,3))
# for i in range(3):
#       print(arr[i])
# for i in range(6):
#       print(random.randint(10,100))
# for i in range(6):
#       print(np.random.randint(10,100,5))
# import random
# import numpy as np
# arr=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
# for i in range(2):
#       arr[i]=np.random.randint(10,100,5)
# print(arr)
import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib.pylab import mpl
# mpl.rcParams['font.sans-serif'] = ['SimHei']
# mpl.rcParams['axes.unicode_minus'] = False
# x=np.linspace(0,10,10)
# print(x)
# y=np.sin(x)
# plt.plot(x,y)
# plt.title("sin(x)")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.show()
# plt.scatter(x, y,marker='*',color='red',label="数据点")
# plt.plot(x,y,linestyle='--',label="折线")
# plt.legend()
# plt.show()
# fig,axes=plt.subplots(1,2)
# axes[0].scatter(x,y,linestyle="--",c='r',label="拟合结果")
# axes[0].set_xlabel("X1")
# axes[0].set_ylabel("Y1")
# axes[0].set_title("数据点")
# axes[1].plot(x,y,marker='*',label="数据点")
# axes[1].set_xlabel("X2")
# axes[1].set_ylabel("Y2")
# axes[1].set_title("拟合结果")
# fig.legend()
# fig.show()
# import matplotlib.pyplot as plt
# import numpy as np
# # 生成示例数据
# x = np.linspace(0, 10, 100)
# y1 = np.sin(x)
# y2 = np.cos(x)
# # 绘制两条曲线，并分别设置标签
# plt.plot(x, y1, label='sin(x)',c='blue')  # 通过 label 参数指定图例标签
# plt.plot(x, y2, label='cos(x)')
# # 显示图例
# plt.legend()  # 自动获取各数据系列的标签并生成图例
# # 添加其他元素（可选）
# plt.title('Sin and Cos Functions')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.show()
# import matplotlib.pyplot as plt
# import numpy as np
#
# # 修正1: 使用正确的 linspace 函数
# # 修正2: 将 x 的范围改为 [-1,1]，这是 arcsin 的有效定义域
# x = np.linspace(-1, 1, 100)
# y = np.arcsin(x)  # 使用 numpy 内置的 arcsin 函数
#
# plt.plot(x, y, label='arcsin(x)')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend()
# plt.title('Arcsine Function')
# plt.grid(True)  # 添加网格线便于查看
# plt.show()
# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.linspace(0, 1, 100)
# y = np.sin(10*x) * np.cos(10*x)  # 实际函数：sin(10x)·cos(10x)
#
# # 修正图例标签，使用LaTeX格式让表达式更准确
# plt.plot(x, y, label=r'$\sin(10x) \cdot \cos(10x)$')
#
# plt.legend()
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Product of Sine and Cosine Functions')  # 添加标题
# plt.grid()  # 添加网格线便于查看
#
# plt.show()
# import numpy as np
# x=np.linspace(0,10,1000)
# y=np.sin(x)
# plt.bar(x,y)
# plt.show()
# plt.title('sin(x)')
# import numpy as np
# def f(x):
#     return np.exp(x)-np.pi
# resolution=0.00000001
# def search(x1,x2):
#     x0=(x1+x2)/2
#     if np.abs(f(x0)) < resolution:
#         return x0
#     elif f(x1)*f(x0)<0:
#         return search(x1,x0)
#     elif f(x2)*f(x0)<0:
#         return search(x0,x2)
# print("方程的根",np.log(np.pi))
# print("二分方程的根",search(0,10))
# import matplotlib.pyplot as plt
# import numpy as np
# from numpy import polyfit
# time=[0.25,0.45,0.5,0.75,1,1.25,1.5,1.75,2,3,4,6,7,8,9,12,13,14,15,16,17,18,19,20]
# alcohol=[30,45,68,75,82,82,77,68,68,58,51,50,41,38,35,28,25,18,15,12,10,7,7,4]
# y=[np.log(a) for a in alcohol]
# y1=[np.log(a) for a in alcohol]
# alcohol_tup1=alcohol[0:alcohol.index(max(alcohol))]
# time_tup1=time[0:alcohol.index(max(alcohol))]
# y_tup1=y[0:alcohol.index(max(alcohol))]
# k1,b1=polyfit(time_tup1,y_tup1,1)
# print(k1,b1)
# alcohol_tup=alcohol[alcohol.index(max(alcohol)):]
# time_tup=time[alcohol.index(max(alcohol)):]
# y_tup=y[alcohol.index(max(alcohol)):]
# k,b=polyfit(time_tup,y_tup,1)
# # plt.scatter(time,y)
# # plt.title("Alcohol Change With Time")
# # plt.xlabel("Time[h]")
# # plt.ylabel("Alcohol[mg/100ml]")
# # plt.show()
# print(k,b)
# def model(t):
#     a=np.exp(-0.11906643*t+4.37680097)
#     return a
# time0=np.linspace(time_tup[0],20,1000)
# time1=np.linspace(0,time_tup[0],1000)
# predy=model(time0)
# predy1=model(time1)
# plt.scatter(time,alcohol,label="sample")
# plt.plot(time0,predy,label="fitting result",c='red')
# plt.plot(time1,predy,c='red')
# plt.title("Alcohol Change With Time")
# plt.xlabel("Time[h]")
# plt.ylabel("Alcohol[mg/100ml]")
# plt.legend()
# plt.show()



# import matplotlib.pyplot as plt
# import numpy as np
# from numpy import polyfit
# from matplotlib.pylab import mpl
# mpl.rcParams['font.sans-serif'] = ['SimHei']
# mpl.rcParams['axes.unicode_minus'] = False
# # 原始数据
# time = [0.25,0.45,0.5,0.75,1,1.25,1.5,1.75,2,3,4,6,7,8,9,12,13,14,15,16,17,18,19,20]
# alcohol = [30,45,68,75,82,82,77,68,68,58,51,50,41,38,35,28,25,18,15,12,10,7,7,4]
#
# # 对数转换
# y = [np.log(a) for a in alcohol]
#
# # 分割数据为上升和下降阶段
# max_idx = alcohol.index(max(alcohol))
# time_tup1, alcohol_tup1, y_tup1 = time[:max_idx], alcohol[:max_idx], y[:max_idx]
# time_tup2, alcohol_tup2, y_tup2 = time[max_idx:], alcohol[max_idx:], y[max_idx:]
#
# # 拟合上升阶段 (注意：可能需要非线性拟合)
# k1, b1 = polyfit(time_tup1, y_tup1, 1)
# print(f"上升阶段参数: k={k1:.4f}, b={b1:.4f}")
#
# # 拟合下降阶段 (酒精消除通常是指数衰减)
# k2, b2 = polyfit(time_tup2, y_tup2, 1)
# print(f"下降阶段参数: k={k2:.4f}, b={b2:.4f}")
#
# # 定义分段模型函数
# def model(t):
#     if isinstance(t, np.ndarray):
#         return np.array([np.exp(k1*ti + b1) if ti < time[max_idx] else np.exp(k2*ti + b2) for ti in t])
#     else:
#         return np.exp(k1*t + b1) if t < time[max_idx] else np.exp(k2*t + b2)
#
# # 生成预测数据
# time_fit = np.linspace(0, 20, 1000)
# predicted = model(time_fit)
#
# # 可视化
# plt.figure(figsize=(10, 6))
# plt.scatter(time, alcohol, label="观测数据", color='blue')
# plt.plot(time_fit, predicted, label="分段指数模型", color='red', linestyle='-')
# plt.axvline(x=time[max_idx], color='gray', linestyle='--', label="峰值时间")
#
# plt.title("酒精浓度随时间变化模型")
# plt.xlabel("时间 [小时]")
# plt.ylabel("酒精浓度 [mg/100ml]")
# plt.grid(True, linestyle='--', alpha=0.7)
# plt.legend()
# plt.tight_layout()
# plt.show()
# import numpy as np
# A=np.array([[1,2,3,5],[1/2,1,1/2,2],[1/3,2,1,2],[1/5,1/2,1/2,1]])
# n=A.shape[0]
# eig_val,eig_vec=np.linalg.eig(A)
# max_eig_val=np.max(eig_val)
# CI=(max_eig_val-n)/(n-1)
# RI=[0,0.0001,0.52,0.89,1.12,1.26,1.36,1.41,1.46,1.49,1.52,1.54,1.56,1.58,1.59]
# CR=CI/RI[n-1]
# print("一致化指标CI=",CI)
# print("一致化比例CR=",CR)
# if CR<0.1:
#     print("可以接受")
# else:
#     print("需要修改")
# Asum=np.sum(A,axis=0)#0是按列求和，1是按行求和
# print("Asum=",Asum)
# n=A.shape[0]
# stand_A=A/Asum
# Asumr=np.sum(stand_A,axis=1)
# weights=Asumr/n
# print("weights=",weights)
# prod_A=np.prod(A,axis=1)
# prod_n_A=np.power(prod_A,1/n)
# re_prod_A=prod_n_A/np.sum(prod_n_A)
# print("re_prod_A=",re_prod_A)
# eig_values,eig_vectors=np.linalg.eig(A)
# max_index=np.argmax(eig_values)
# max_vector=eig_vectors[:,max_index]
# weights=max_vector/np.sum(max_vector)
# print("weights=",weights)
# import numpy as np
# A=np.array([[1,3,0.5],[1/3,1,1/7],[2,7,1]])
# n=A.shape[0]
# eig_val,eig_vec=np.linalg.eig(A)#特征值，特征向量
# max_eig_val=np.max(eig_val)
# RI=[0,0.0001,0.52,0.89,1.12,1.26,1.36,1.41,1.46,1.49,1.52,1.54,1.56,1.58,1.59]
# CI=(max_eig_val-n)/(n-1)
# CR = CI / RI[n - 1]
# print(CI)
# print(CR)
# if CR<=0.1:
#     print("可以接受")
# else:
#     print("修改")
# max_index=np.argmax(eig_val)
# max_vector=eig_vec[:,max_index]
# print(max_vector)
# weights=max_vector/np.sum(max_vector)
# print(weights)
# Asum=np.sum(A,axis=0)
# Astand=A/Asum
# Asumr=np.sum(Astand,axis=1)
# weights=Asumr/n
# print(weights)
# 生成0到20小时的拟合曲线
# kind=input().split(" ")
# print(kind)
# import numpy as np
# A=np.zeros((2,3))
# print(A)
# a=[1,2,3,4,5,6,7,8,9,10]
# for i in a:
#     print(i)
# sum=0
# for i in range(2,10,2):
#     sum=sum+i
#     print(i)
# print(sum)
# A=['1','2','3','4','5','6','7','8','9']
# print(A)
# sum=str(0)
# for i in A:
#     print(i)
#     sum=sum+i
# print(sum)
# A=list(map(int,A))
# print(A)
# A=['1.0','2.0','3.0','4.0','5.0','6.0']
# print(A)
# A=list(map(float,A))
# print(A)
# x=[1,2,3]
# maxx=5
# ans=[[maxx-e] for e in x]
# print(ans)
# list0=[1,2,3]
# list0.append(4)
# print(list0)
# list0=['1','2','3']
# list0.append('4')
# print(list0)
# A=list(map(float,list0))
# print(A)
# import numpy as np
# arr1=np.array([[4],[5],[6],[7],[8]])
# arr2=np.array([[1],[2],[3],[4],[5]])
# sta_arr=np.hstack((arr1,arr2))
# print(arr1)
# print(sta_arr)
# import numpy as np
# A=np.array([[1,2],[3,4],[5,6]])
# x_max=np.array([10,20])
# Amax=A-np.tile(x_max,(3,1))
# print(Amax)
# import numpy as np
# n = int(input())  # 行数
# m = int(input())  # 列数
# A = np.zeros(shape=(n, m))  # 创建全零数组
# kind=input().split(" ")
# for i in range(n):
#     A[i]=input().split(" ")
#     A[i]=list(map(float,A[i]))  # 直接赋值 map 对象
# print(A)
# def minTomax(maxx,x):
#     x=list(x)
#     ans=[(maxx-e) for e in x]
#     return np.array(ans)
# def midTomax(bestx,x):
#     x=list(x)
#     h=[(bestx-e) for e in x]
#     M=max(h)
#     if M==0:
#         M=1
#     ans=[(1-e/M) for e in h]
#     return np.array(ans)
# def regTomax(lowx,highx,x):
#     x=list(x)
#     M=max(lowx-min(x),max(x)-highx)
#     if M==0:
#         M=1
#     ans=[]
#     for i in range(len(x)):
#         if x[i]<lowx:
#             ans.append([(1-(lowx-x[i])/M),(1+(lowx-x[i])/M)])
#         elif x[i]>highx:
#             ans.append([(1-(highx-x[i])/M)])
#         else:
#             ans.append([1])
#     return np.array(ans)
# X=np.zeros(shape=(n,1))
# for i in range(n):
#     if kind[i]=="1":
#         v=np.array(A[:,i])
#     elif kind[i]=="2":
#         maxA=max(A[:,i])
#         v=minTomax(maxA,A[:,i])
#     elif kind[i]=="3":
#         bestA=eval(input())
#         v=midTomax(bestA,A[:,i])
#     elif kind[i]=="4":
#         lowA=eval(input())
#         highA=eval(input())
#         v=regTomax(lowA,highA,A[:,i])
#     if i==0:
#         X=v.reshape(1,-1)
#     else:
#         X=np.hstack((X,v.reshape(1,-1)))
# print("统一指标后,:\n{}".format(X))
# X=X.astype('float')
# for j in range(m):
#     X[:,j]=X[:,j]/np.sqrt(sum(X[:,j])**2)
# print("标准化后,:\n{}".format(X))
# x_max=np.max(X,axis=0)
# x_min=np.min(X,axis=0)
# d_z=np.sqrt(np.sum(np.square(X-np.tile(x_max,(n,1))),axis=1))
# d_f=np.sqrt(np.sum(np.square(X-np.tile(x_min,(n,1))),axis=1))
# s=d_f/(d_z+d_f)
# score=100*s/sum(s)
# for i in range(len(score)):
#     print(i)
# import numpy as np
# def mylog(p):
#     n=len(p)
#     lnp=np.zeros(n)
#     for i in range(n):
#         if p[i]==0:
#             lnp[i]=0
#         else:
#             lnp[i]=np.log(p[i])
#     return lnp
# X=np.array([[9,0,0,0],[8,3,0.9,0.5],[6,7,0.2,1]])
# Z=X/np.sqrt(np.sum(X*X,axis=0))
# print("标准化:Z=")
# print(Z)
# n,m=Z.shape
# D=np.zeros(m)
# for i in range(m):
#     x=Z[:,i]
#     p=x/np.sum(x)
#     e=-np.sum(p*mylog(p))/np.log(n)
#     D[i]=1-e
# W=D/np.sum(D)
# print("W=")
# print(W)
# import numpy as np
# R23=np.array([
#     [0.18,0.14,0.18,0.14],
#     [0.15,0.20,0.15,0.25],
#     [0.25,0.12,0.13,0.12],
#     [0.25,0.14,0.14,0.14]
# ])
# A23=np.array([0.2,0.15,0.10,0.55])
# B23=np.dot(A23,R23)
# print(B23)
# import numpy as np
#
# # 输入初始矩阵，例如 [[1,2],[3,4]]
# A = np.array(eval(input("输入初始矩阵（例如 [[1,2],[3,4]]）：")))
#
# # 数据标准化（均值归一化）
# Mean = np.mean(A, axis=0)
# A_norm = A / Mean
# print("标准化后的矩阵:\n", A_norm)
#
# # 提取参考序列和比较序列
# Y = A_norm[:, 0]  # 第一列作为参考序列
# X = A_norm[:, 1:]  # 其余列作为比较序列
#
# # 计算绝对差值矩阵
# absX0_X1 = np.abs(X - Y.reshape(-1, 1))  # 自动广播
# print("绝对差值矩阵:\n", absX0_X1)
#
# # 计算灰色关联系数
# a = np.min(absX0_X1)  # 全局最小差值
# b = np.max(absX0_X1)  # 全局最大差值
# rho = 0.5  # 分辨系数
# gamma = (a + rho * b) / (absX0_X1 + rho * b)  # 逐元素计算
#
# # 计算灰色关联度（每列的平均值）
# result = np.mean(gamma, axis=0)
# print("灰色关联度:", result)


# import numpy as np
# arr_2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
# summ=np.cumsum(arr_2d,axis=1)
# print(summ)
# eigenvalues=np.array([3,1,4,2])
# eigenvectors=np.array([
#     [1,0,0,1],
#     [0,1,0,1],
#     [0,0,1,1],
#     [1,1,1,1]
# ])
# eigenvalues=eigenvalues[::-1]
# print(eigenvalues)
# eigenvectors=eigenvectors[:, ::-1]
# print(eigenvectors)
# 生成区间 [-2,2] 的网格
# import numpy as np
# import matplotlib.pyplot as plt
# x = np.linspace(-2,2,100)
# y = np.linspace(-2,2,100)
# X,Y = np.meshgrid(x,y)
# Z = X**2 + Y**2   # 计算每个网格点函数值
# plt.contourf(X,Y,Z)
# plt.show()
import pandas as pd

df=pd.DataFrame({
    'department':['A','A','B','B','B'],
    'employee':['张三','李四','王五','赵六','王五'],
    'sales':[100,200,300,150,250]
})

print(df)
res=df.groupby('department').size()
print(res)
res=df.groupby('department').size().reset_index(name='count')
print(res)
res=df.groupby('department')['sales'].sum().reset_index()
print(res)
res=df.groupby('department')['sales'].mean().reset_index()
print(res)
res=(
    df.groupby('department')['sales']
    .agg(['sum','mean','max'])
    .reset_index()
)
print(res)
res=(
    df.groupby('department')
    .agg(
        total_sales=('sales','sum'),
        average_sales=('sales','mean'),
        max_sales=('sales','max')
    )
    .reset_index()
)
print(res)
res=(
    df.groupby(['department','employee'])['sales']
    .sum()
    .reset_index()
)
print(res)