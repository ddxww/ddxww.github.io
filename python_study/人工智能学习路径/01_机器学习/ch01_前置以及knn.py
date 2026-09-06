import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.feature_selection import VarianceThreshold
from sklearn.linear_model import LinearRegression,Lasso,Ridge,LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import (confusion_matrix,accuracy_score,precision_score,recall_score,
                             f1_score,classification_report,roc_auc_score,roc_curve)

from sklearn.datasets import make_classification
from sklearn.neighbors import KNeighborsRegressor,KNeighborsClassifier
from tensorflow.python.ops.metrics_impl import precision
# 绘图全局设置
sns.set(style='whitegrid')
plt.rcParams["font.family"] = ["SimHei", "Microsoft YaHei", "Arial"]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["font.size"] = 12
# enconding = "utf-8"
# data = 2*np.random.rand(10000,2)-1
# x=data[:,0]
# y=data[:,1]
# print(x)
# print(y)
# idx = x**2 + y**2 < 1
# hole = x**2 + y**2 < 0.25
# idx = np.logical_and(idx,~hole)
# plt.plot(x[idx],y[idx],'go',markersize=1)
# plt.show()
# p = np.random.rand(10000)
# np.set_printoptions(edgeitems=10,suppress=None)
# print(p.shape)
# print(p)
# plt.hist(p,bins=10,color='g',edgecolor='k')
# plt.show()
# n=10000
# times=100
# z=np.zeros(n)
# for i in range(times):
#     z+=np.random.randn(n)
# z/=times
# plt.hist(z,bins=10,color='r',edgecolor='k')
# plt.show()
# d=np.random.rand(10)
# print(d)
# print(d<0.5)
# print(d[d<0.5])
# d[d<0.5]=0.5
# print(d)
# p=np.random.rand(3,4)
# print(p)
# print('='*50)
# data=pd.DataFrame(data=p,columns=list('abcd'))
# print(data)
# print(data['a'])
# print(data[list('a')])
# data.to_csv('data.csv',index=False,header=True)
# d=np.random.rand(100)*6-4
# print(d)
# d=np.random.rand(3,4)*6-4
# print(d)
# d=np.random.rand(100)*6-3
# plt.plot(d,'r.')
# plt.show()
# x=np.arange(0,10,0.1)
# x=np.linspace(0,10,100)
# y=x**x
# plt.plot(x,y,'r-',linewidth=2)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()

# str_numbers=["1","2","3","4","5","6","7","8","9"]
# result=map(int,str_numbers)
# num_str="".join(str(x) for x in result)
# num=int(num_str)
# print(num)
# print(type(num))
# print(num_str)
# print(type(num_str))
# a=[1,2,3,4]
# b=np.array(a)
# print(a)
# print(b)
# print(np.array([1,2,3,4]))
# 算阶乘第一个数出现概率
# def first_digital(x):
#     while x >= 10:
#         x //= 10        # 用整除保证返回整数
#     return x
# if __name__ == "__main__":
#     n = 1
#     N = 100
#     frequency = [0] * 9
#     for i in range(1,N+1):
#         n *= i
#         m = first_digital(n) - 1  # 0~8 索引
#         frequency[m] += 1
#     print(frequency)
#     plt.plot(frequency, 'r-', linewidth=2)
#     plt.plot(frequency, 'go', markersize=8)
#     plt.grid(True)
#     plt.show()

#环形堵车模型
# a=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
# b=a.astype(float)
# print(b)
# 参数
# path = 5000   # 道路长度
# n = 100       # 车辆数
# v0 = 5        # 初速度
# p = 0.1       # 减速概率
# Times = 500
#
# np.random.seed(0)
# x = np.random.rand(n) * path
# x.sort()
# v = np.tile([v0], n).astype(float)
#
# plt.figure(figsize=(10,8), facecolor='w')
#
# for t in range(Times):
#     # 绘制车辆位置
#     plt.scatter(x, [t]*n, s=1, c='k')  # 点稍微大一点
#
#     for i in range(n):
#         # 计算前车距离（环形道路）
#         if x[(i+1)%n] > x[i]:
#             d = x[(i+1)%n] - x[i]
#         else:
#             d = path - x[i] + x[(i+1)%n]
#
#         # 更新速度
#         if v[i] < d:
#             if np.random.rand() < p:  # p 概率减速
#                 v[i] -= 1
#             else:                     # 1-p 概率加速
#                 v[i] += 1
#         else:
#             v[i] = d - 1
#
#     # 限制速度
#     v = v.clip(0, 150)
#
#     # 更新位置，环形道路
#     x = (x + v) % path
# # 绘图美化
# plt.xlim(0, path)
# plt.ylim(0, Times)
# plt.xlabel('x', fontsize=16)
# plt.ylabel('t', fontsize=16)
# plt.title('Traffic Flow Simulation', fontsize=18)
# plt.tight_layout(pad=2)
# plt.show()
#蒙特卡洛算pi
# def get_pi(N=10000,method='simulation'):
#     if method == 'simulation':
#         x=np.random.rand(N)
#         y=np.random.rand(N)
#         inside=np.sum(x**2+y**2<=1)
#         return 4*inside/N
#     elif method=='strict':
#         return np.pi
# pi_sim=get_pi(N=10000,method='simulation')
# print(pi_sim)
# pi_strict=get_pi(N=10000,method='strict')
# print(pi_strict)
# def win_p(p, N, method='simulation', trials=100000):
#     k = N // 2 + 1
#     if method == 'simulation':
#         wins = 0
#         for _ in range(trials):
#             player_wins = 0
#             opponent_wins = 0
#             while player_wins < k and opponent_wins < k:
#                 if random.random() < p:
#                     player_wins += 1
#                 else:
#                     opponent_wins += 1
#             if player_wins == k:
#                 wins += 1
#         return wins / trials
#     elif method == 'strict':
#         prob = 0
#         for i in range(k, N+1):
#             prob += comb(i-1, k-1) * (p**k) * ((1-p)**(i-k))
#         return prob
# p = 0.6
# N = 5
# prob_formula = win_p(p, N, method='strict')
# prob_simulation = win_p(p, N, method='simulation', trials=100000)
# print(f"公式计算获胜概率: {prob_formula:.4f}")
# print(f"模拟计算获胜概率: {prob_simulation:.4f}")
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy import stats
# def rotate(x, y, theta_deg):
#     theta = np.radians(theta_deg)
#     cos_t = np.cos(theta)
#     sin_t = np.sin(theta)
#     xr = x * cos_t - y * sin_t
#     yr = x * sin_t + y * cos_t
#     return xr, yr
# def cal_pearson(x, y):
#     std1 = np.std(x)
#     std2 = np.std(y)
#     cov = np.cov(x, y, bias=True)[0, 1]
#     pearson = cov / (std1 * std2)
#     return pearson
# def pearson(x, y, tip):
#     clrs = list("rgbmyc")
#     plt.figure(figsize=(8, 10), facecolor='w')
#     for i, theta in enumerate(np.linspace(0, 90, 6)):
#         xr, yr = rotate(x, y, theta)
#         p = stats.pearsonr(xr, yr)[0]
#         print(f"旋转角度: {theta:.1f}°, pearsonr: {p:.3f}")
#         # 修复颜色错误：用索引 i 取色，不是用 p
#         plt.scatter(xr, yr, alpha=0.9, linewidths=0.5, s=40, color=clrs[i], label=f"{theta:.0f}°")
#     plt.legend(loc='upper left', shadow=True, fancybox=True, facecolor='w')
#     plt.xlabel("x")
#     plt.ylabel("y")
#     plt.title("Pearson系数分布: %s" % tip, fontsize=18)
#     plt.grid(True)  # 修复过时写法
#     plt.show()
# if __name__ == '__main__':
#     # 构造测试数据
#     np.random.seed(0)
#     x = np.linspace(-1, 1, 100)
#     y = x**2
#     pearson(x, y, "测试数据")
# u=np.random.uniform(0.0,1.0,10000)
# print(u)
# plt.hist(u,80,facecolor='g',alpha=0.8)
# plt.grid(True)
# plt.show()
# times=10000
# for i in range(times):
#     u+=np.random.uniform(0.0,1.0,10000)
# print(len(u))
# u/=times
# plt.hist(u,80,facecolor='g',alpha=0.8)
# plt.grid(True)
# plt.show()
#找素数
# def is_prime(x):
#     return 0 not in [x%i for i in range(2,int(math.sqrt(x))+1)]
# a=2
# b=100000
# t=time()
# p=[p for p in range(a,b) if 0 not in [p%d for d in range(2,int(math.sqrt(b))+1)]]
# print(time()-t)
# print(p)
# p=list(filter(is_prime,list(range(a,b))))
# print(p)
# b=1000
# p_list=[]
# for i in range(2,b):
#     flag=True
#     for j in range(2,int(math.sqrt(i))):
#         if i%j==0:
#             flag=False
#             break
#     if flag:
#         p_list.append(i)
# print(p_list)
#数据处理
# arr=np.array(10)#0维度
# print(arr)
# print("arr维度:",arr.ndim)
# arr=np.array([10])#一维
# print(arr)
# print("arr维度:",arr.ndim)
# arr=np.array([[1,2,3],[4,5,6]])#二维
# print(arr)
# print("arr维度:",arr.ndim)
# arr=np.array([10,"hello"])#同质化
# print(arr)
# arr=np.array([10,2.5])#同质化
# print(arr)
# np.random.seed(0)
# arr=np.array(3)
# print("数组的形状:",arr.shape)
# print("数组类型:",arr.dtype)
# arr=np.random.rand(3)
# print(arr)
# print("数组的形状:",arr.shape)
# print("元素的转置:",arr.T)
# arr=np.random.rand(3,4)
# print(arr)
# print("数组的形状:",arr.shape)
# print(arr.size)
# print(arr.dtype)
# print(arr.ndim)
# print("元素的转置:",arr.T)
#ndarray创建
# arr=np.array([1,2,3])
# print(arr)
# list1=[4,5,6]
# print(list1)
# arr=np.array(list1)
# print(arr)
# list2=[[4,5,6],[7,8,9]]
# print(list2)
# arr=np.array(list2,dtype=np.float64)
# print(arr)
# arr1=np.copy(arr)
# print(arr1)
# arr1[0][0]=8
# print(arr1)
# arr=np.zeros((2,3))
# print(arr)
# print(arr.shape)
# print(arr.dtype)
# arr=np.zeros((2,3),dtype=np.int64)
# arr=np.zeros((6,))
# print(arr)
# arr=np.ones((5,5))
# print(arr)
# arr=np.empty((2,3),dtype=np.int64)#未初始化
# print(arr)
# arr=np.full((2,3),2026)
# print(arr)
# arr1=np.zeros_like(arr)
# print(arr1)
# arr2=np.empty_like(arr)
# print(arr2)
# arr=np.arange(1,10,1)#start,end,step
# print(arr)
# arr=np.arange(2,11,2)
# print(arr)
# arr=np.linspace(1,10,10)#start,end,num
# print(arr)
# arr=np.linspace(0,10,5)
# print(arr)
# arr=np.linspace(0,100,5,dtype=int)
# print(arr)
# arr=np.arange(0,101,25)
# print(arr)
# arr=np.logspace(0,4,100,base=2)
# print(arr)
# plt.figure(figsize=(10,10))
# plt.plot(arr)
# plt.show()
# arr=np.linspace(0,4,100)
# y=2**arr
# plt.figure(figsize=(10,10))
# plt.plot(arr,y)
# plt.show()
#特殊矩阵构造
# arr=np.eye(3,dtype=int)#单位矩阵
# print(arr)
# print(arr.shape)
# arr=np.eye(3,4,dtype=int)
# print(arr)
# arr=np.diag([1,2,3])#对角矩阵
# print(arr)
# list1=[1,2,3]
# arr=np.diag(list1)
# print(arr)
# arr=np.random.rand(3,4)#0到1
# print(arr)
# arr=np.random.uniform(3,6,size=(3,4))#随机浮点数
# print(arr)
# arr=np.random.randint(3,6,size=(3,4))
# print(arr)
# arr=np.random.randn(2,3)#正态分布
# print(arr)
# #随机种子
# np.random.seed(20)
# arr=np.random.rand(2,3)
# print(arr)
# arr=np.random.randint(1,10,size=(2,5))
# print(arr)
# arr=np.random.uniform(3,6,size=(2,3))
# print(arr)
# arr=np.random.randn(2,3)
# print(arr)
# arr=np.array([1,2,0,1],dtype=bool)
# print(arr)
# arr=np.array([1,127,0,1],dtype=np.int8)
# print(arr)
# np.random.seed(0)
# arr=np.random.randint(1,100,30)
# print(arr)
# print(arr[0])
# print(arr[:10])#0到9
# print(arr[2:5])#2到4，start:end+1
# print(arr[slice(2,5)])
# print(arr[slice(2,5,1)])
# print(arr[slice(2,10,2)])
# print(arr[10:])#10到最后一个
# print(arr>40)
# print(arr[arr>40])
# print(arr[(arr>40) & (arr<80)])
# arr=np.random.randint(1,100,(4,8))
# print(arr)
# print(arr[1][2])
# print(arr[1,2])
# print(arr[1])
# print(arr[1,2:5])
# print(arr[arr>50])#返回一维
# print(arr[2])
# print(arr[2][arr[2]>50])
# print(arr[:,0])#列数据
#运算
# a=np.array([[1,2,3],[4,5,6],[7,8,9]])
# b=np.array([[4,5,6],[7,8,9],[1,2,3]])
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a+3)
# # list1=[1,2,3]
# # list2=[4,5,6]
# # print(list1+list2)#拼接操作
# # for i in range(len(list1)):
# #     list2[i]=list1[i]*list2[i]
# #     print(list2)
# # list3=[p for i,p in enumerate(list1)]
# # print(list3)
# a=np.array([1,2,3])
# b=np.array([[4],[5],[6]])
# print(a+b)
# print(a-b)
# # 1 2 3 4 4 4 广播机制
# # 1 2 3 5 5 5
# # 1 2 3 6 6 6
# a=np.array([[1,2,3],[4,5,6],[7,8,9]])
# b=np.array([[4,5,6],[7,8,9],[1,2,3]])
# print(a@b)#矩阵乘法
#常用函数
# print(np.sqrt(9))
# list1=[1,4,9]
# print(np.sqrt(list1))
# arr=np.array(list1)
# print(np.sqrt(arr))
# print(np.exp(0))
# print(np.exp(1))
# print(np.log(np.exp(2)))#lnx
# print(np.sin(np.pi/2))
# print(np.sin(1))
# print(np.sin(-1))
# arr=np.array([1,-2,-3,4,5,-6])
# print(np.abs(arr))
# print(np.power(arr,2))
# print(np.round([3.2,3.5,4.6,3.1,1.2,1.9,1.4,4.5]))
# print(np.ceil([3.2,3.5,4.6,3.1,1.2,1.9,1.4,4.5]))
# print(np.floor([3.2,3.5,4.6,3.1,1.2,1.9,1.4,4.5]))
# np.random.seed(42)
# arr=np.random.randint(1,20,9)
# print(arr)
# print(np.sum(arr))
# print(np.mean(arr))
# print(np.max(arr),np.argmax(arr))
# print(np.min(arr),np.argmin(arr))
# print(np.var(arr))#方差
# print(np.std(arr))#标准差
# print(np.std(arr)**2)
# print(np.percentile(arr,50))
# print(np.percentile(arr,25))
# print(np.median(arr))
# arr=np.array([1,2,3,4,5])
# print(arr.sum())
# print(np.sum(arr))
# print(np.cumsum(arr))
# np.random.seed(42)
# arr=np.array([3,4,5,6,7,8,9,10])
# print(arr>4)
# print(np.greater(arr,4))
# print(arr<4)
# print(np.less(arr,4))
# print(arr==4)
# print(np.equal(arr,4))
# print(np.equal([3,4,5],[4,4,4]))
# print(np.logical_and([1,1,1],[0,1,0]))
# print(np.logical_or([1,0,1],[0,0,0]))
# print(np.logical_not([1,0,1]))
# print(np.any([0,1,0]))
# print(np.any([0,0,0]))
# print(np.all([1,0,1]))
# print(np.all([1,1,1]))
# print(np.where(arr>5,arr,0))
# print(np.where(arr<5,arr,0))
# print(np.where(arr>5,arr,0))
# print(np.where(arr<5,1,0))
# print(np.where(arr==5,arr,0))
# arr=np.random.randint(50,100,10)
# print(arr)
# print(np.where(arr>60,'及格','不及格'))
# print(np.where(arr<60,'不及格',np.where(arr<80,'良好','优秀')))
# print(np.select([arr>80,(arr>=60)&(arr<=80),arr<60], ['优秀','良好','不及格'], default=''))
# np.random.seed(42)
# arr=np.random.randint(1,100,10)
# print(arr)
# print(np.unique(arr))#去重排序
# print(np.sort(arr))
# print(np.argsort(arr))#排序后的索引
# print(arr)
# arr.sort()
# print(arr)
# a=np.array([1,2,3])
# b=np.array([4,5,6])
# print(np.concatenate((a,b)))
# a=np.array([1,2,3])
# b=np.array([4,5])
# print(np.concatenate((a,b)))
# a=np.array([[1,2,3],[4,5,6]])
# b=np.array([[4,5,6],[1,2,3]])
# print(np.concatenate((a,b),axis=0))#纵向合并
# a=np.array([[1,2,3],[4,5,6]])
# b=np.array([[4,5,6],[1,2,3]])
# print(np.concatenate((a,b),axis=1))#横向合并
# print(np.split(a,2))
# print(np.split(arr,2))
# a=np.array([1,2,3,4,5,6])
# arr=np.reshape(a,(3,2))
# print(arr)
# tem=[28,30,29,31,32,30,29]
# arr=np.array(tem)
# print('平均气温','%.3f'%arr.mean())
# print(arr.max())
# print(arr.min())
# print(len(arr[arr>30]))
# print(np.count_nonzero(arr>30))
# print(np.cumsum(np.where(arr>30,1,0)))
# score=[85,90,78,92,88]
# print(score)
# arr=np.array(score)
# print(np.mean(arr))
# print(np.median(arr))
# print('%.3f'%np.std(arr))
# print(arr/10)
# A=np.array([[1,2],[3,4]])
# B=np.array([[5,6],[7,8]])
# print(A+B)
# print(A*B)
# print(A@B)
# np.random.seed(42)
# arr=np.random.randint(0,10,(3,4))
# print(arr)
# print('列最大值和最小值', np.max(arr,axis=0), np.min(arr,axis=0))
# print('行最大值和最小值',np.max(arr,axis=1),np.min(arr,axis=1))
# print(np.where(arr%2==1,-1,arr))
# arr[arr%2==1]=-1
# print(arr)
# arr=np.arange(1,13)
# print(arr)
# arr=np.reshape(arr,(3,4))
# print(arr)
# print('每行的和',np.sum(arr,axis=1))
# print('每列的和',np.mean(arr,axis=0))
# print('每列的和',np.sum(arr,axis=0))
# ar=np.reshape(arr,(1,12))
# print(ar)
# arr=np.random.randint(0,20,(5,5))
# print(arr)
# print(arr[arr>10])
# arr[arr>10]=0
# print(arr)
# print(np.where(arr>10,0,arr))
# money=np.array([120,135,110,125,130,140])
# print(np.sum(money))
# print(np.mean(money))
# print(np.var(money))
# print(np.argmax(money)+1)
# print(np.argmin(money)+1)
# A=np.array([1,2,3])
# B=np.array([4,5,6])
# C=np.concatenate((A,B))
# print(C)
# # print(np.reshape(C,(2,3)))
# arr=np.array([2,1,2,3,1,4,3])
# print(arr)
# print(np.unique(arr))
# new_arr,counts=np.unique(arr,return_counts=True)
# print(new_arr)
# print(counts)
# for i in range(len(new_arr)):
#     print(len(arr[arr==new_arr[i]]))
# money=np.array([20,25,22,30,28])
# a=np.array([15,18,16,22,20])
# print(money-a)
# b=money-a
# print(np.mean(b))
# print(np.std(b))
# print(len(b[b==np.max(b)]))
# print(np.where(b==np.max(b))[0]+1)
# b = np.array([
#     [1,9,9],
#     [4,9,9]
# ])
# print(np.where(b==9))
# print(np.where(b==9)[0])   # 行
# print(np.where(b==9)[1])   # 列
# #输出结果表示9的函数和列数
# rows, cols = np.where(b == 9)
# coords = list(zip(rows, cols))
# print(coords)
# a=[1,2,3]
# b=['x','y','z']
# c=list(zip(a,b))
# print(c)
#pandas
# s=pd.Series([1,2,3,4,5])
# print(s)
# #自定义索引
# s=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'],name='month')
# print(s)
# s=pd.Series({"a":1,"b":2,"c":3,"d":4,"e":5})
# print(s)
# d={"A":1,"B":2,"C":3,"D":4,"E":5}
# s=pd.Series(d)
# print(s)
# s1=pd.Series(s,index=["A","C"])
# print(s1)
# s=pd.Series({"A":1,"B":2,"C":3,"D":4,"E":5},name="test")
# print(s.index)
# print(s.values)
# print(s.shape,s.dtypes,s.size,s.ndim)
# print(s.name)
#显示索引不包左
# print(s.loc['A'])
# print(s.loc['B'])
# print(s.loc['C'])
# print(s.loc['A':'C'])
# print(s.at['A'])#不支持切片
#隐式索引不包右
# print(s.iloc[0])
# print(s.iloc[0:2])
# print(s.iloc[:2])
# print(s.iloc[2:])
# print(s.iat[0])
# print(s.iat[1])
# s=pd.Series({"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7})
# print(s['a'])
# print(s['b'])
# print(s[s<3])
# print(s.head(),s.tail(),s.head(2),s.tail(1),s.head(6))
# s=pd.Series([10,2,3,np.nan,None,4,5],index=['a','b','c','d','e','f','g'],name="test")
# print(s)
# print(s.head(),s.tail(),s.tail(2),s.head(7))
# print(s.describe(),s.count())#忽略缺失值
# print(s.index,s.keys())#kesy是方法,index是属性
# print(s.isna())
# print(s.isin([4]))
# print(s.isin([4,5]))
# print(s.mean(),s.sum(),s.std(),s.var(),s.max(),s.min(),s.median())
# print(s.sort_values())
# print(s.quantile(0.25),s.quantile(0.5),s.quantile(0.75),s.quantile(0.8))
# print("===============================================================")
# print(s.mode())
# s['h']=4
# print(s.mode())
# print(s.values)
# print(s.value_counts())
# print("===============================================================")
# a=s.drop_duplicates()
# print(a)
# print(s.unique(),s.nunique(),len(s.unique()))
# print(s.sort_index())#索引排序
# print(s.sort_values())
# np.random.seed(42)
# values = np.random.randint(50, 101, 10)
# index = []
# for i in range(1, 11):
#     index.append("学生" + str(i))
# scores=pd.Series(values,index)
# print(scores)
# scores=pd.Series(np.random.randint(50,101,10),index=['学生'+str(i) for i in range(1,11)])
# print(scores)
# print('平均分:',scores.mean())
# print('最高分:',scores.max())
# print('最低分:',scores.min())
# mean=scores.mean()
# print(scores>mean)
# print(scores[scores>mean])
# print(scores[scores>mean].count())
# print(scores[scores>mean].size)
# print(len(scores[scores>mean]))
# temps=pd.Series([28,31,29,32,30,27,33],index=['周一','周二','周三','周四','周五','周六','周日'])
# print(temps[temps>30])
# print(temps[temps<30].count())
# print(len(temps[temps>30]))
# print(temps[temps>30].size)
# print(temps.mean())
# print(temps.sort_values(ascending=False))
# print(temps.diff())#获取差值
# print(temps.diff().abs().sort_values(ascending=False))#获取差值
# print(temps.keys())
# print(temps.diff().abs().sort_values(ascending=False).keys()[:2])#获取差值
# print(temps.diff().abs().sort_values(ascending=False).keys()[:2].tolist())#获取差值
# date=pd.date_range(start='2018-01-01', end='2018-12-31', freq='D')
# print(date)
# date=pd.date_range("2026-04-29",periods=15)
# print(date.tolist())
# prices=pd.Series([102.3,103.5,105.1,104.8,106.2,107.0,106.5,108.1,109.3,110.2],
#                  index=pd.date_range("2023-1-1",periods=10))
# print(prices)
# print(prices.pct_change())#每日收益率
# # for i in range(len(prices)-1):
# #     print(prices.iloc[i+1]/prices.iloc[i]-1)
# # print(prices.loc['2023-1-3'])
# # print(prices.iloc[2])
# print(prices.pct_change().idxmax())
# print(prices.pct_change().idxmin())
# print(prices.pct_change().std())
# a=pd.date_range('1970-1-1',periods=12,freq='MS')
# print(a)
# sales = pd.Series(
#     [120,135,145,160,155,170,180,175,190,200,210,220],
#     index=pd.date_range('2022-1-1', periods=12, freq='MS')
# )
# print(sales)
# # Y  / YE   年末
# # YS / AS   年初
# # Q  / QE   季度末
# # QS        季度初 ✅
# # M         月末
# # MS        月初
# # W         周
# # D         日
# # B         工作日
# # H         小时
# # T/min     分钟
# #季度平均采样
# print(sales.resample('QS').mean())
# #年平均
# print(sales.resample('YS').mean())
# print(sales.mean())
# print(sales.max(),sales.idxmax())
# print(sales.pct_change())
# b=sales.pct_change()
# b[b>0]=1
# print(b.rolling(3))
# print(b.rolling(3).sum()>2)
# print(b[b.rolling(3).sum()>2].keys().tolist())
# np.random.seed(42)
# sales=pd.Series(np.random.randint(0,100,24),
#                 index=pd.date_range('2025-1-1',periods=24,freq='h'))
# print(sales)
# print(sales.resample('D').sum())
# print(sales.sum())
# print(sales.between_time('8:00','22:00'))
# print(sales.loc['2025-01-01 08:00:00':'2025-01-01 22:00:00'])
# business_sales=sales[(sales.index.hour >= 8) & (sales.index.hour <= 22)]
# print(business_sales)
# print(business_sales.sum()/(sales.sum()-business_sales.sum()))
# business_sales_bool=(sales.index.hour >= 8) & (sales.index.hour <= 22)
# print(business_sales_bool)
# unbusiness_sales=sales.drop(sales[business_sales_bool].index)
# print(unbusiness_sales)
# print(business_sales.sum()/unbusiness_sales.sum())
# print(sales[business_sales_bool],sales[~business_sales_bool])
# print(sales.nlargest(3))#最大的三个小时
# print(sales.nsmallest(3))#最小三个小时
# print(sales.nlargest(5))
# s=pd.Series([6,1,1,5,3,4,5,6],index=[str(i) for i in range(1,9)])
# print(s)
# s_dup=s.drop_duplicates()
# print(s_dup)
# print(s.sort_index())
# print(s.sort_values())
# print(s.unique(),s.nunique())
# print(s.sample())
# result=s.keys().tolist()
# print(result)
# result=list(map(int,result))
# print(result)
# print(s.values.tolist())
# s1=pd.Series([1,2,3,4,5])
# s2=pd.Series([6,7,8,9,10])
# df=pd.DataFrame({"第一列":s1,"第二列":s2})
# print(df)
# print(type(df))
# print(type(df['第一列']))
# df=pd.DataFrame({
#     "name":["a","b","c","d","e","a"],
#     "age":[13,16,18,16,19,13],
#     "scores":[50,60,70,80,90,50]
# },index=[1,2,3,4,5,6],columns=["name","scores","age"])
# print(df.index,df.columns)
# print(df.values)
# print(df.ndim)
# print(df.dtypes)
# print(df.shape)
# print(df.size)
# print(df.T)
# print(df.T.index)#交换了
# print(df.loc[4])
# print(df.iloc[3])
# print(df.loc[:,'name'])#先行后列
# print(df.iloc[:,0:2])
# print(df.iloc[:,0])
# print(df.name,df.scores)
# print(df['name'])
# print(df.name.iloc[0])
# print(df)
# print(df.at[3,'name'])
# print(df.iat[2,0])
# print(df.loc[3,'name'])
# print(df.iloc[2,0])
# print(df['name'].dtypes)
# print(df.name.dtypes)
# print(df[['name']])
# print(df[['age','scores']])#获取多列数据
# print(df.head())
# print(df.tail(3))
# print(df.scores>70)
# print(df[df.scores>70])
# print(df[(df.scores>70) & (df.age<19)])
# print(df.sample(3))#随机抽样
# s=pd.Series(np.random.randn(100),index=pd.date_range('2020-1-1', periods=100))
# print(s)
# print(df.isin(['a',13]))
# print(df.isna())
# print(df['scores'].sum(),df['age'].mean())
# print(df.scores.mean(),df.scores.median())
# print(df.age.max())
# print(df.scores.mode())
# print(df.scores.std())
# print(df.scores.var())
# print(df.scores.quantile([0.25,0.75]))
# print(df.describe())
# print(df.value_counts())
# print(df.drop_duplicates())
# print(df.duplicated(subset=['age']))
# print(df.age.replace(13,18))
# print(df.scores.cumsum())
# print(df.scores.cummax())
# print(df.scores.cummin())
# print(df.scores.sort_index(ascending=False))
# print(df.sort_values(by=['scores','age'],ascending=[False,True]))
# print(df.nlargest(2,['scores','age']))
# data=pd.DataFrame({
#     '姓名':['a','b','c','d','e'],
#     '数学':[85,92,78,88,95],
#     '英语':[90,88,85,92,80],
#     '物理':[75,80,88,85,90]
# })
# print(data[['数学','英语','物理']].sum(axis=1))
# data['总分']=data[['数学','英语','物理']].sum(axis=1)
# data['平均分']=data['总分']/3
# data['平均分2']=data[['数学','英语','物理']].mean(axis=1)
# print(data)
# print(data[(data.数学>90) | (data.英语>85)])
# print(data.sort_values(by='总分',ascending=False).head(3))
# print(data.nlargest(3,columns=['总分']))
# data={
#     '产品名称':['a','b','c','d'],
#     '单价':[100,150,200,120],
#     '销量':[50,30,20,40]
# }
# df=pd.DataFrame(data)
# print(df)
# df['总销售额']=df['单价']*df['销量']
# print(df)
# print(df.nlargest(1,['总销售额']))
# print(df.sort_values('总销售额',ascending=False))
# data = {
#     '用户ID': [101, 102, 103, 104, 105],
#     '用户名': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
#     '商品类别': ['电子产品', '服饰', '电子产品', '家居', '服饰'],
#     '商品单价': [1200, 300, 800, 150, 200],
#     '购买数量': [1, 3, 2, 5, 4]
# }
# df=pd.DataFrame(data)
# print(df)
# df['总金额']=df.商品单价*df.购买数量
# print(df)
# print(df.nlargest(1,columns=['总金额']))
# print(df.总金额.mean())
# print(df[df['商品类别']=='电子产品'].购买数量.sum())
# print(df.groupby(['商品类别'])['购买数量'].sum())
# print(df.groupby('用户名')['总金额'].sum())
# df=pd.read_csv('employees.csv')
# print(type(df))
# print(df.head())
# print(df.salary.mean())
# df=df.tail()
# df=df.to_csv('new.csv')
# data1=pd.read_json('data1.json')
# print(data1.head())
# test=pd.read_json('test.json')
# print(test.head())
# print(type(test))
# with open('test.json') as f:
#     data=json.load(f)
# print(type(data))
# data2=pd.DataFrame(data['users'])
# print(type(data2))
# print(data2)
# s=pd.Series([1,2,np.nan,None,pd.NA,3])
# print(s)
# print(s.isna(),s.isnull())
# print(s.dropna())
# print('='*50)
# data=pd.DataFrame([[1,2,np.nan],[2,3,5],[None,4,6]],columns=['A','B','C'])
# print(data)
# print('='*50)
# print(data.isna().sum())
# print(data.dropna())
# print(data)
# print("="*50)
# print(data.dropna(how='all'))
# print(data.dropna(thresh=2))#行至少有n个值不是缺失值则删除该行
# print(data.dropna(axis=1))#删除列
# print(data.dropna(subset=['A']))#某列有缺失值，则剔除有缺失值的那一行
# df=pd.read_csv('weather_withna.csv')
# print(df.tail())
# print(df.isna().sum(axis=0))
# print(df.fillna({'temp_max':20,'wind':2.5}))
# print(df.fillna(df[['temp_max','wind']].mean().tail()))
# print(df.ffill().tail())#前面的值填充
# print(df.bfill().tail())#后面的值填充
# data = {
#     "name": ['alice', 'alice', 'bob', 'alice', 'jack', 'bob'],
#     "age": [26, 25, 30, 25, 35, 30],
#     "city": ['NY', 'NY', 'LA', 'NY', 'SF', 'LA']
# }
# df=pd.DataFrame(data)
# print(df)
# print(df.duplicated())
# print(df.drop_duplicates())
# print(df.drop_duplicates(subset=['name']))#根据name去除
# print(df.drop_duplicates(subset=['name'],keep='last'))#保留最后一次
# df=pd.read_csv('sleep.csv')
# print(df.dtypes)
# df['age']=df['age'].astype('int16')
# print(df.dtypes)
# df['gender']=df['gender'].astype('category')
# print(df.dtypes)
# print(df.gender)
# df['is_male']=df['gender'].map({'female':True,'male':False})
# print(df.is_male)
# data = {
#     'ID': [1, 2],
#     'name': ['alice smith', 'bob smith'],
#     'Math': [90, 85],
#     'English': [88, 92],
#     'Science': [95, 89]
# }
# df = pd.DataFrame(data)
# print(df)
# print(df.T)# 行列转置
# df2=pd.melt(df,id_vars=['ID','name'],var_name='科目',value_name='分数')
# print(df2)
# print(df2.sort_values('name'))
# print(pd.pivot(df2,index=['ID','name'],columns='科目',values='分数'))
# print(pd.pivot(df2,index=['ID','name'],columns='分数',values='科目'))
# print(df['name'].str.split(' ',expand=True))
# df[['first','last']]=df['name'].str.split(' ',expand=True)
# print(df)
# df=pd.read_csv('sleep.csv')
# df=df[['person_id','blood_pressure']]
# print(df.head())
# print(df['blood_pressure'])
# df[['high_blood','small_blood']]=df['blood_pressure'].str.split('/',expand=True)
# print(df)
# print(df.info())
# df[['high_blood','small_blood']]=df[['high_blood','small_blood']].astype('int64')
# print(df.info())
# print(df[['high_blood','small_blood']].mean())
# data = {
#     'ID': [1, 2],
#     'name': ['alice smith', 'bob smith'],
#     'Math': [90, 85],
#     'English': [88, 92],
#     'Science': [95, 89]
# }
# df=pd.DataFrame(data)
# print(df)
# #id_vars保持列名不变,var_name原来列名字变成这一列名字,value_name原来单元格数字放到这一列
# df2=pd.melt(df,id_vars=['ID','name'],var_name='科目',value_name='分数')
# print(df2)
#pd.cut(x,bins,labels)
# df=pd.read_csv('employees.csv')
# print(df.head(10))
# df1=df.head(10)[['employee_id','salary']]
# print(df1)
# pd.cut(df1['salary'],bins=2)
# # print(pd.cut(df1['salary'],bins=2))
# print(pd.cut(df1['salary'],bins=2).value_counts())#区间计数
# print(pd.cut(df1['salary'],bins=3).value_counts())#区间计数
# print(pd.cut(df1['salary'],bins=[0,10000,20000,30000]).value_counts())#bins=list
# print(pd.cut(df1['salary'],bins=[0,10000,20000,30000],labels=['低','中','高']))
# print(pd.cut(df1['salary'],bins=[0,10000,20000,30000],labels=['低','中','高']).value_counts())
# df1['收入范围']=pd.cut(df1['salary'],bins=[0,10000,20000,30000],labels=['低','中','高'])
# print(df1)
# print(pd.qcut(df1['salary'],3).value_counts())
# df=pd.read_csv('sleep.csv')
# df1=df.head(10)[['person_id','sleep_quality']]
# print(df1)
# df['睡眠质量']=pd.cut(df['sleep_quality'],3,labels=['差','一班','好'])
# print(df)
# print(df['睡眠质量'].value_counts())
# print('='*50)
# print(df['gender'].value_counts())
# df['gender']=df['gender'].astype('category')
# print(df['gender'].value_counts())
# df=pd.DataFrame({
#     'name':['a','b','c','d'],
#     'age':[20,30,40,50],
#     'gender':['male','female','male','female'],
# })
# df.set_index('name',inplace=True)
# print(df)
# df.reset_index(inplace=True)
# print(df)
# df.rename(columns={'age':'年龄'},index={0:4})#老:新
# print(df)
# df.index=[1,2,3,4]
# df.columns=['姓名','年龄','性别']
# print(df)
#时间戳
# d=pd.Timestamp('2015-4-21 22:22')
# print(d)
# print(type(d))
# print(d.year, d.month, d.day, d.hour, d.minute, d.second)
# print(d.quarter, d.weekday, d.hour, d.minute, d.second)
# print(d.is_month_end,d.is_month_start)
# print(d.day_name())#获取星期几
# print(d.to_period('D'))#天
# print(d.to_period('Q'))#季度
# print(d.to_period('Y'),d.to_period('M'),d.to_period('W'))
# a=pd.to_datetime('2015-4-21 22:22')
# print(a)
# print(a.day_name())
# df=pd.DataFrame({
#     'sales':[100,200,300],
#     'date':['20250601','20250602','20250603']
# })
# df['daytime']=pd.to_datetime(df['date'])
# print(df.info())
# df['day']=df['daytime'].dt.day_name()
# print(df['daytime'].dt.year)
# print(df['day'].value_counts())
# df=pd.date_range('2020-1-1',periods=6)
# print(df)
# df=pd.DataFrame(df)
# print(df)
# df.columns=['date']
# print(df['date'].dt.day_name())
# df=pd.read_csv('weather.csv')
# print(df.info())
# print(df.head())
# df['daytime']=pd.to_datetime(df['date'])
# print(df.head())
# print(df.info())
# df=pd.read_csv('weather.csv',parse_dates=['date'])
# print(df['date'].dt.day_name())
# df.set_index('date',inplace=True)
# print(df.loc['2013-1':'2013-2'])
# print(df.iloc[0:61])
# d1=pd.Timestamp('2006-1-14')
# d2=pd.Timestamp('2026-5-15')
# d3=d2-d1
# print(d3)
# print(type(d3))
# df=pd.read_csv('weather.csv',parse_dates=['date'])
# df['delta']=df['date']-df['date'][0]
# print(df['delta'])
# df.set_index('delta',inplace=True)
# print(df)
# print(df.loc['10days':'20days'])
# df=pd.date_range(start='2025/7/3',end='2026/2/9',freq='W')
# print(df)
# df=pd.date_range(start='2025/7/3',periods=6,freq='Y')
# print(df)
# df=pd.read_csv('weather.csv',parse_dates=['date'])
# df.set_index('date',inplace=True)
# print(df.head())
# print(df[['temp_max','temp_min']].resample("YE").mean())
# print(df[['temp_max','temp_min']].resample("YS").mean())
#df.groupby('分组的字段')['聚合的字段'].聚合函数()
# df=pd.read_csv('employees.csv')
# print(df.head())
# print(df['department_id'].isna().sum())
# df.dropna(subset=['department_id'], inplace=True)
# print(df['department_id'].isna().sum())
# df['department_id']=df['department_id'].astype('int64')
# print(df.head())
# #计算不同部门平均薪资
# print(df.groupby('department_id').groups)
# print(df.groupby('department_id').get_group(100))
# print(df.groupby('department_id')['salary'].sum())
# print(df.groupby('department_id')['salary'].mean())
# df2=df.groupby('department_id')['salary'].mean().round(2)
# print(df2.head())
# df2=df2.reset_index()
# df2=pd.DataFrame(df2)
# print(df2)
# df2.sort_values('salary',ascending=False,inplace=True)
# print(df2)
# print(df.groupby(['department_id','job_id']).groups)
# print(df.groupby(['department_id','job_id']).get_group((30,'PU_CLERK')))
# print(df.groupby(['department_id','job_id'])['salary'].mean())
# df3=df.groupby(['department_id','job_id'])['salary'].mean()
# print(type(df3))
# print(df.groupby(['department_id','job_id'])[['salary']].mean())
# df4=df.groupby(['department_id','job_id'])[['salary']].mean()
# print(type(df4))
# df4.reset_index(inplace=True)
# df4.sort_values('salary',ascending=False,inplace=True)
# print(type(df4))
# print(df4)
# df=pd.read_csv('penguins.csv')
# print(df.head())
# print(len(df))
# print(df.isna().sum())
# df.dropna(inplace=True)
# print(df.isna().sum())
# print(len(df))
# print(df.dtypes)
# df['sex']=df['sex'].astype('category')
# print(df.info())
# df['bill_ratio']=df['bill_length_mm']/df['bill_depth_mm']
# print(df.head())
# df['mass_level']=pd.cut(df['body_mass_g'],bins=3,labels=['低','中','高级'])
# print(df.head())
# print(df['mass_level'].value_counts())
# print(df.groupby(['sex']).agg({
#     'body_mass_g':['mean','median']
# }))
# print(df.groupby(['island']).agg({
#     'body_mass_g':['mean','median']
# }))
# print(df.groupby(['species']).agg({
#     'body_mass_g':['mean','median']
# }))
# df=pd.read_csv('sleep.csv')
# print(df.head())
# print(df.describe())
# print(df.isna().sum())
# df.drop(columns=['sleep_disorder'],inplace=True)
# print(df.head())
# df['gender']=df['gender'].astype('category')
# df['occupation']=df['gender'].astype('category')
# df['bmi_category']=df['bmi_category'].astype('category')
# df[['high','low']]=df['blood_pressure'].str.split('/',expand=True)
# labels=['差','中','优']
# df['sleep_level']=pd.cut(df['sleep_quality'],bins=3,labels=labels)
# labels=['青少年','中年人','老年']
# df['age_level']=pd.cut(df['age'],bins=3,labels=labels)
# print(df.head())
# print(df['bmi_category'].value_counts())
# print(df.groupby(['age_level','bmi_category']).agg({
#     'sleep_duration':'mean',
#     'sleep_quality':'mean',
#     'stress_level':'mean'
# }))
# np.random.seed(42)
# plt.figure(figsize=(10,5))
# month=pd.date_range(start='2018-01-01', periods=8)
# sales=np.random.randint(0,200,8)
# plt.plot(month,sales,label='产品A',color='orange',
#          linewidth='2',linestyle='--',marker='o')#(x,y)
# plt.title('销售趋势',color='r',fontsize=20)
# plt.xlabel('月份',fontsize=10)
# plt.ylabel('销售额（万）',fontsize=10)
# plt.legend(loc='upper left')
# # plt.grid(axis='y')#只有y
# # plt.grid(axis='x')#只有x
# #设置刻度字体大小
# plt.axvline(x=month[2], color='red', linewidth=3, linestyle='-', alpha=0.7)
# plt.xticks(rotation=10,fontsize=12)#rotation旋转
# plt.yticks(rotation=0,fontsize=20)
# plt.ylim(0,250)#y的范围
# for x,y in zip(month,sales):
#     print(x,y)
#     plt.text(x,y+4,str(y),ha='center',va='bottom')#ha水平,va垂直
# plt.grid(True,alpha=0.1,color='blue',linestyle='--')#都有
# plt.show()
# subject=['语文','数学','英语','科学']
# scores=[85,92,78,88]
#柱状图
# plt.bar(subject,scores,label='a',color='orange',width=0.5)
# plt.title('成绩分布',fontsize=20,color='red')
# plt.grid(axis='y',alpha=0.75,linestyle='--',color='black')
# plt.yticks(fontsize=20)
# plt.xticks(fontsize=20)
# for x,y in zip(subject,scores):
#     plt.text(x,y,str(y),ha='center',va='bottom',fontsize=12)
# plt.legend(loc='upper right',fontsize=8)
# plt.tight_layout()
# plt.show()
#条形图
# countries=['US','Chinese','Japan','germany','India']
# gdp=[85,92,12,38,14]
# plt.barh(countries,gdp,color=['red','blue','green','yellow','magenta'],
#          label=countries,height=0.5)
# plt.legend(loc='upper right')
# plt.title('GDP')
# plt.xlabel('GDP per capita')
# plt.ylabel('Countries')
# plt.tight_layout()
# plt.show()
#饼图
# things=['学习','娱乐','运动','睡觉','其他']
# times=[6,4,1,8,5]
# colors=['#66b3ff','#99ff99','#ffcc99','#ff9999','#ff4499']
# plt.pie(times,labels=things,
#         autopct='%.2f%%',
#         startangle=90,#调整初始化图角度
#         colors=colors,#颜色
#         )
# plt.title('时间分布',fontsize=20,color='red')
# plt.tight_layout()
# plt.show()
# #环形图
# things=['学习','娱乐','运动','睡觉','其他']
# times=[6,4,1,8,5]
# colors=['#66b3ff','#99ff99','#ffcc99','#ff9999','#ff4499']
# plt.pie(times,labels=things,
#         autopct='%.2f%%',#数据显示占比
#         startangle=90,#调整初始化图角度
#         colors=colors,#颜色
#         wedgeprops={'width':0.5},#圆环设置
#         pctdistance=0.8,#圆心距离
#     shadow=True,#阴影
#         )
# plt.title('时间分布',fontsize=20,color='red')
# plt.tight_layout()
# plt.text(0,0,'总计:\n%100',ha='center',va='bottom',fontsize=15)
# plt.show()
# #爆炸饼图
# things=['学习','娱乐','运动','睡觉','其他']
# times=[6,4,1,8,5]
# colors=['#66b3ff','#99ff99','#ffcc99','#ff9999','#ff4499']
# explode=[0.2,0,0,0,0]#离圆心距离
# plt.pie(times,labels=things,
#         autopct='%.2f%%',#数据显示占比
#         startangle=90,#调整初始化图角度
#         colors=colors,#颜色
#         explode=explode,#突出地方
#         shadow=True,#阴影
#         )
# plt.title('时间分布',fontsize=20,color='red')
# plt.tight_layout()
# plt.text(0,0,'总计:\n%100',ha='center',va='bottom',fontsize=15)
# plt.show()
#散点图
# scores=np.arange(50,85,5)
# hours=np.linspace(1,7,7)
# print(hours)
# plt.figure(figsize = (10,5))
# plt.scatter(hours,scores)
# plt.show()
# x=[]
# y=[]
# for i in range(1000):
#     tmp=random.uniform(0,10)
#     x.append(tmp)
#     y.append(tmp*2+random.gauss(0,1))
# plt.figure(figsize=(10,8))
# plt.scatter(x,y,color="blue",alpha=0.5,
#             s=20,#圆点大小
#             )
# plt.title('x与y的关系图')
# plt.ylim(0,25)
# plt.ylabel('y')
# plt.xlabel('x')
# plt.show()
# 箱线图
# data = {
#     '语文': [82, 85, 88, 70, 90, 76, 84, 83, 95],
#     '数学': [75, 80, 79, 93, 88, 82, 87, 89, 92],
#     '英语': [70, 72, 68, 65, 78, 80, 85, 90, 95]
# }
# print(data.keys())
# plt.figure(figsize=(8, 6))
# plt.boxplot(data.values(), tick_labels=data.keys())
# plt.title("各科成绩分布（箱线图）")
# plt.ylabel("分数")
# plt.grid(True, axis='y', linestyle='--', alpha=0.5)
# plt.show()
# month=[1,2,3,4]
# sales=[100,80,150,130]
# f1=plt.subplot(2,2,1)
# f1.plot(month,sales)
# f2=plt.subplot(2,2,2)
# f2.bar(month,sales)
# f3=plt.subplot(2,2,3)
# f3.pie(sales,colors=['r','g','b','orange'],
#        autopct='%.2f%%',
#        explode=(0.1,0,0,0),
#        shadow=True,
#        )
# f3.set_title('月度销量占比',fontsize=10,y=-0.1,color='#ff2299')
# f4=plt.subplot(2,2,4)
# f4.barh(month,sales)
# plt.show()
#merge
#水平
# left = pd.DataFrame({
#     'key1': ['K0', 'K0', 'K1', 'K2'],
#     'key2': ['K0', 'K1', 'K0', 'K1'],
#     'A': ['A0', 'A1', 'A2', 'A3'],
#     'B': ['B0', 'B1', 'B2', 'B3']
# })
#
# right = pd.DataFrame({
#     'key1': ['K0', 'K1', 'K1', 'K2'],
#     'key2': ['K0', 'K0', 'K0', 'K0'],
#     'C': ['C0', 'C1', 'C2', 'C3'],
#     'D': ['D0', 'D1', 'D2', 'D3']
# })
# result = pd.merge(left, right, how='inner', on=['key1', 'key2'])
# # 打印看看
# print("\ninner join 结果表：")
# print(result)
# result = pd.merge(left, right, how='outer', on=['key1', 'key2'])
# print("\nouter join 结果表：")
# print(result)
# result = pd.merge(left, right, how='left', on=['key1', 'key2'])#保证左边都留下来
# print("\nleft join 结果表：")
# print(result)
# result = pd.merge(left, right, how='right', on=['key1', 'key2'])#保证右边都留下来
# print("\nright join 结果表：")
# print(result)
# movies = pd.DataFrame({
#     'movie_id': [1, 2, 3, 5, 7],
#     'title': ['t1', 't2', 't3', 't5', 't7'],
#     'description': ['d1', 'd2', 'd3', 'd5', 'd7']
# })
# ratings = pd.DataFrame({
#     'user_id': [1, 2, 7, 9, 11, 15],
#     'movie_id': [1, 2, 4, 5, 6, 7],
#     'title': ['t1', 't2', 't3', 't4', 't5', 't6'],
#     'rating': [5, 4, 3, 2, 3, 1],
#     'time': ['t1', 't2', 't4', 't4', 't1', 't3']
# })
# print(pd.merge(movies, ratings))#等价下一行
# print(pd.merge(ratings, movies,on=['movie_id','title']))
# print(pd.merge(ratings, movies,on=['movie_id']))#只基于movie_id合并
# print(pd.merge(movies, ratings,left_on='movie_id',right_on='user_id'))
# print(pd.merge(movies, ratings,left_index=True,right_index=True))#基于索引拼在一起，行数取最小的是吗
# print(pd.merge(ratings, movies, on=['movie_id'], suffixes=['_left','_right']))#只基于movie_id合并
# print(pd.merge(ratings, movies,on=['movie_id','title'],how='inner'))#只join都有的
# print(pd.merge(ratings, movies,on=['movie_id','title'],how='outer'))#所有都join起来
# print(pd.merge(ratings, movies,on=['movie_id','title'],how='left'))#保留左边
# print(pd.merge(ratings, movies,on=['movie_id','title'],how='right',indicator='indicator_col'))#保留左边

# plt.figure(figsize=(10,10))
# plt.plot(df['date'],df['temp_max'],label='最高气温')
# plt.plot(df['date'],df['temp_min'],label='最低气温')
# plt.title('2015气温趋势变化图')
# plt.xlabel('date')
# plt.ylabel('temp')
# plt.legend()
# plt.show()
# df=pd.read_csv('weather.csv')
# print(df.head())
# df['date']=pd.to_datetime(df['date'])
# df['temp_mean']=(df['temp_min']+df['temp_max'])/2
# df=df[df['date'].dt.year==2015]
# plt.figure(figsize=(10,10))
# plt.plot(df['date'],df['temp_mean'],label='平均气温')
# plt.title('2015气温趋势变化图')
# plt.xlabel('date')
# plt.ylabel('temp')
# plt.legend()
# plt.show()
# plt.hist(df['precipitation'],bins=5)
# plt.show()
# df=pd.read_csv('penguins.csv')
# df.dropna(inplace=True)
# sns.histplot(df,x='species')
# plt.title('Penguins种类分布图')
# plt.show()
# #密度图
# sns.kdeplot(df,x='bill_length_mm')
# sns.histplot(df,x='bill_length_mm',kde=True,color='red')
# plt.show()
# #计数图
# sns.countplot(df,x='island')
# plt.show()
# #散点图
# sns.scatterplot(df,x='body_mass_g',y='flipper_length_mm',hue='sex')#hue分组
# plt.show()
#二位核密度
# sns.kdeplot(
#     df,
#     x='body_mass_g',        # 分类：企鹅种类
#     y='flipper_length_mm', # 数值：喙长度
#     estimator='mean',   # 计算平均值
#     errorbar=None       # 不显示误差线
# )
# plt.show()
# text = "第1次"
# result = text.replace("第", "").replace("次", "")
# # print(result)
# #分析
# df=pd.read_csv('house_sales.csv')
# print(len(df))
# print(len(df.columns))
# print(df.head().to_string())
# print(df.info())
# df.drop(columns=['origin_url'], inplace=True)
# print(df.head())
# print(df.isna().sum())
# df.dropna(inplace=True)
# print(df.duplicated().sum())
# df.drop_duplicates(inplace=True)#删除重复
# print(len(df))
# print(df['area'].dtypes)
# #面积数据类型转换
# df['area']=df['area'].str.replace('㎡','').astype(float)
# print(df['area'].head())
# df['price']=df['price'].str.replace('万','').astype(float)
# df['unit']=df['unit'].str.replace('元/㎡','').astype(float)
# df['year']=df['year'].str.replace('年建','').astype(int)
# print(df['price'].head())
# print(df['toward'].value_counts())
# df['toward']=df['toward'].astype('category')
# df=df[(df['area']<600) & (df['area']>20)]
# Q1=df['price'].quantile(0.25)
# Q3=df['price'].quantile(0.75)
# IQR = Q3 - Q1
# low_price=Q1 - 1.5*IQR
# high_price=Q3 + 1.5*IQR
# print(df[df['price']<low_price].count())
# print(df[df['price']>high_price].count())
# df=df[(df['price']>low_price) & (df['price']<high_price)]
# print(len(df))
# df['district']=df['address'].str.split('-').str[0]
# print(df['floor'].str.split('（').str[0][0])#"高楼层（共30层）" → 切成 ["高楼层", "共30层）"]
# df['floor']=df['floor'].str.split('（').str[0]
# def fun1(str1):
#     if pd.isnull(str1):
#         return '位置'
#     elif '低' in str1:
#         return '低楼层'
#     elif '中' in str1:
#         return '中楼层'
#     elif '高' in str1:
#         return '高楼层'
#     else:
#         return '未知'
# df['floor_type2']=df['floor'].apply(fun1).astype('category')#把 floor 列的每一个值，都丢进 fun1 函数里处理一遍
# print(df.head())
# # df['zxs']=df['city'].apply(lambda x: True if x in ['北京','上海','天津','重庆'] else False)
# df['zxs']=df['province'].isin(['北京','上海','天津','重庆'])
# print(df['zxs'].head())
# df['bedrooms']=df['rooms'].str.split('室').str[0].astype('int')
# # df['livingrooms']=df['rooms'].str.split('室').str[1].str.replace('厅','')
# df['livingrooms']=df['rooms'].str.extract(r'(\d+)厅').astype('int')#捕获厅前面的数字
# print(df['livingrooms'].head())
# df['building_age']=2026-df['year']
# df['price_labels']=pd.cut(df['price'],bins=4,labels=['低','中','高','豪华'])
# print(df.head().to_string())
# a=df[['price','area','unit','building_age']].corr()
# print(a['price'].sort_values(ascending=False)[1:])
# plt.figure(figsize=(10,10))
# plt.title('热力图相关特征')
# sns.heatmap(a,cmap='YlGnBu',annot=True)
# plt.tight_layout()
# plt.show()
# print(df.describe())
# plt.subplots(figsize=(10,10))
# plt.hist(df['price'],bins=10)
# plt.show()
# sns.histplot(data=df,x='price',bins=10,kde=True)
# plt.show()
# print(df['toward'].value_counts())
# print(df.groupby('toward').agg({
#     'price':['mean','median'],
#     'unit':['median'],
#     'building_age':['mean','median'],
# }))
# plt.figure(figsize=(10,10))
# sns.boxplot(data=df,x='toward',y='price')
# plt.tight_layout()
# plt.show()
# x=np.arange(-2,2,0.1)
# y=x**2
# y1=x
# fig, axe = plt.subplots()
# axe.plot(x, y)
# axe.plot(x, y1)
# plt.show()
# fig=plt.figure()
# plot=fig.add_subplot(1,2,1)
# plt.plot(x, y)
# plot=fig.add_subplot(1,2,2)
# plt.plot(x, y1)
# plt.show()
# plt.savefig('2-1.png')#保存图片
# x=np.linspace(-2,2,100)
# y1=x
# y2=x**2
# plt.figure(figsize=(8,8))
# plt.plot(x,y1)
# plt.plot(x,y2)
# plt.xlim(-3,3)
# plt.xticks([2,0,-2],['x1', 'x2', 'x3'])
# plt.yticks([-2,-1,0,1,2],['y1', 'y2', 'y3', 'y4','y5'])
# plt.show()
# fig,axe=plt.subplots()
# axe.set_xlim(-3,3)
# axe.set_xticks(np.linspace(-3,3,6))
# axe.plot(x,y1,label='line1')
# axe.plot(x,y2,label='line2')
# axe.tick_params(direction='in',length=6,width=3,labelsize=12)
# axe.spines['left'].set_position(('axes',0.5))#左边移到中间
# axe.spines['bottom'].set_position('zero')#下边移到中间
# axe.spines['right'].set_color('none')#右边隐藏
# axe.spines['top'].set_color('none')#顶部隐藏
# axe.legend(loc=0,title='legend title',shadow=True,facecolor='white',ncol=2)
# axe.annotate('y=x',
#              xy=(1.5,1.5),
#              xytext=(2,0),
#              arrowprops=dict(arrowstyle='->',
#                              color='red',
#                              connectionstyle='arc3,rad=-0.5',#arc3弯曲程度，rad代表箭头弯曲程度
#                              ),#箭头款式
#              bbox=dict(boxstyle='round',fc='none',ec='gray'),#ec是边框, boxstyle='round'给文字加【圆角矩形框】
#              )
# plt.show()
# fig,axe=plt.subplots()
# x=np.arange(-3.0,3.0,0.1)
# y=x**2
# axe.fill_between(x,y,color='blue',alpha=0.5)
# plt.show()
# y1=x**2
# y2=x**2-10
# axe.fill_between(x,y1,y2,color='b',alpha=0.5)
# plt.show()
# fig,axe=plt.subplots()
# x=np.arange(0,5,0.01)
# y=np.sin(x*np.pi)
# axe.fill_between(x,y,where=y>0,color='b',alpha=0.5)
# axe.fill_between(x,y,where=y<0,color='g',alpha=0.5)
# plt.show()
# #snsborn
# plt.figure(figsize=(5,3))
# plt.text(0.5,0.5,'seaborn已就绪',ha='center',fontsize=20)
# plt.axis('off')
# plt.show()
# df=pd.DataFrame({
#     '类别':['A','A','B','B','C','C'],
#     '数值':[12,3,15,16,28,98]
# })
# sns.set_theme(
#     style="whitegrid",#风格
#     palette="colorblind",#配色方案
#     font='SimHei',#字体
# )
# print(df)
# plt.figure(figsize=(8,8))
# sns.barplot(df,x='类别',y='数值')#计算平均值高度
# plt.title('seaborn 一键分类绘图')
# plt.figure(figsize=(8,8))
# plt.plot([2,3,7],[5,7,5])
# plt.show()
# plt.show()
# y=np.random.randint(50,100,20)
# x=range(20)
# sns.set_style("darkgrid")
# plt.subplot(2,3,1)#两行三列第一个
# plt.plot(x,y)
# plt.subplot(2,3,2)
# sns.set_style("white")
# plt.plot(x,y)
# plt.subplot(2,3,3)
# sns.set_style("whitegrid")
# plt.plot(x,y)
# plt.subplot(2,3,4)
# sns.set_style("ticks")
# plt.plot(x,y)
# plt.subplot(2,3,5)
# sns.set_style("dark")
# plt.plot(x,y)
# plt.subplot(2,3,6)
# with sns.axes_style("dark"):#临时风格with sns.axes_style()
#     plt.plot(x,y)
# plt.show()
#sns.set(style='whitegrid')默认是darkgrid
# sns.set(style='whitegrid')
# plt.subplot(2,2,1)
# sns.set_style("whitegrid")
# plt.plot(x,y)
# sns.despine()#要放在后面
# plt.subplot(2,2,2)
# sns.set_style("white")
# plt.plot(x,y)
# plt.show()
# y = np.random.randint(10,100,10)
# x = range(10)
# #['papar','notebook','talk','poster']
# #set_context设置比例
# sns.set(style='whitegrid',context='paper',rc={'lines.linewidth':1,'xtick.minor.width':3})
# plt.plot(x,y)
# plt.show()
#
# sns.set_context(context="poster",)
# plt.plot(x,y)
# plt.show()
#
# sns.set_context(context="paper",)
# plt.plot(x,y)
# plt.show()
#color_palette()调色板
# sns.palplot(sns.color_palette())
# sns.palplot(sns.color_palette('Reds'))#深到浅
# sns.palplot(sns.color_palette('Reds_r'))#浅到深
# sns.palplot(sns.color_palette('Blues'))
# sns.palplot(sns.color_palette('Blues_r'))
# sns.palplot(sns.color_palette('colorblind'))
# sns.palplot(sns.color_palette('pastel'))
# sns.palplot(sns.color_palette(['#34495e','#2ecc71','#e4733c']))
# sns.palplot(sns.light_palette("red"))#白到黑
# sns.palplot(sns.light_palette("green"))#白到黑
# sns.palplot(sns.light_palette("blue"))#白到黑
# sns.palplot(sns.dark_palette("red"))#黑到白
# sns.palplot(sns.color_palette("Reds"))
# sns.palplot(sns.color_palette('Spectral',n_colors=15))
# plt.show()
# x=range(10)
# y=np.random.randint(50,100,10)
# plt.subplot(2,1,1)
# sns.set_style("darkgrid")
# plt.plot(x,y)
# sns.despine()
# plt.subplot(2,1,2)
# sns.set_style("dark")
# plt.plot(x,y)
# sns.despine()
# plt.show()
# x=range(10,15)
# plt.plot([1,2],[3,4],sns.xkcd_rgb['apple green'],lw=4)#lw线条宽度
# plt.show()
# plt.subplot(2,2,1)
# plt.bar(x,x,color=sns.color_palette('Greens'))
# plt.subplot(2,2,2)
# plt.bar(x,x,color=sns.light_palette('blue'))
# plt.subplot(2,2,3)
# plt.bar(x,x,color=sns.color_palette(['#95d0fc','#033500','#c7fdb5','#95d0fc','#033500']))
# plt.show()
# data=np.random.normal(size=(20,8))+np.arange(8)/2
# sns.barplot(data=data,palette=sns.color_palette("hls",8))
# plt.show()
# sns.set(style='white')
# x = np.random.normal(size=100)
# sns.histplot(x, bins=20,kde=True)
# plt.show()
# plt.subplot(2,2,3))
# sleep=pd.read_csv('sleep.csv')
# sns.barplot(
#     x='bmi_category',       # X轴：BMI分类
#     y='sleep_duration',     # Y轴：睡眠时间（必须是数字！）
#     hue='gender',           # 分组：男 / 女 → 一眼看出差距
#     data=sleep,
#     palette=sns.light_palette('blue')     # 蓝色系，干净好看
# )
# plt.title('不同BMI下男女睡眠时长对比')
# plt.xlabel('BMI分类')
# plt.ylabel('平均睡眠时间')
# plt.legend(title='性别')    # 自动显示男女图例
# plt.tight_layout()
# plt.show()
# titanic=pd.read_csv('train.csv')
# sns.barplot(x='Sex', y='Survived',
#             data=titanic,
#             hue='Pclass',palette=sns.light_palette('blue',n_colors=3)
#             )#hue是分类
# plt.show()
# tips=pd.read_csv('tips.csv')
# sns.boxplot(
#     x="day",
#     y="total_bill",
#     data=tips,
#     palette=sns.light_palette('blue',n_colors=2),
#     hue='time',
#     legend=False,
# )
# plt.show()
# N=9
# x=np.linspace(0,6,N)+np.random.randn(N)
# x=np.sort(x)
# y=x**2+4*x-3+np.random.randn(N)
# x.shape=-1,1#-1：占位符，NumPy 自动根据元素总数算出对应行数
#矩阵向量化
# A=np.array([[1,2],[3,4]])
# B=np.array([[5,6],[7,8]])
# print(A.dot(B))
# print(A.flatten())#行向量化
# print(B.flatten())
# print("<A,B>=",np.dot(A.flatten(),B.flatten()))
#低方差过滤法
# np.random.seed(42)
# a=np.random.randn(100)
# b=np.random.randn(100)*0.1
# c=np.random.normal(5,0.1,100)#均值，标准差
# print(a.var())
# print(b.var())
# print(c.var())
# X=np.vstack((a,b))
# print(X.shape)
# print(X.T)
# X=X.T
# var_threshold=VarianceThreshold(0.01)
# X_filtered=var_threshold.fit_transform(X)
# print(X_filtered.shape)
# print(X_filtered)
#皮尔逊系数
# data=pd.read_csv('advertising.csv')
# data.drop(data.columns[0],axis=1,inplace=True)#每一行的第一列删掉
# data.dropna(inplace=True)
# X=data.drop('Sales',axis=1)
# print(X.head())
# y=data['Sales']
# print(data.corr(method="pearson"))
# print(X.corrwith(y,method='pearson'))#subset：限定只检查哪些列的空值,corrwith(y)：表内每一列 单独 和 y 求相关系数
# sns.heatmap(data.corr(method="pearson"),
#             annot=True,#annot=True在热力图每个格子里，显示具体相关系数数值。
#             cmap="coolwarm",#配色方案：冷色（蓝）代表负相关，暖色（红）代表正相关。
#             fmt='.2f')#数值格式：保留2 位小数。
# plt.title("correlation heatmap")
# plt.show()
# print(y.head())
# print(data.head())
# print(data.describe())
# print(data.shape)
#斯皮尔曼系数
# X=[[5],[8],[10],[12],[15],[3],[7],[9],[14],[6]]
# y=[55,65,70,75,85,50,60,72,80,58]
# X=pd.DataFrame(X)
# y=pd.DataFrame(y)
# print(X.corrwith(y,method='spearman'))
# print(X)
# print(y)
# df=pd.DataFrame({'A':[1,2], 'B':[3,4]})
# df.columns=['列1', '列2']
# print(df)
# df=df.rename(columns={'列1':'新列名1'})
# df=df.rename(columns={'列1':'name', '列2':'value'})
# print(df)
#主成分分析(PCA)from sklearn.decomposition import PCA
# np.random.seed(42)
# X=np.random.randn(1000,3)
# print(X)
#使用PCA将三维数据变为二维
# pca=PCA(n_components=2)
# X_pca=pca.fit_transform(X)
# print(X_pca.shape)
# fig=plt.figure(figsize=(12,4))
# ax1=fig.add_subplot(121,projection='3d')
# ax1.scatter(X[:,0],X[:,1],X[:,2],c="g")
# ax1.set_title("Before_PCA")
# ax1.set_xlabel("Feature1")
# ax1.set_ylabel("Feature2")
# ax1.set_zlabel("Feature3")
# ax2=fig.add_subplot(122)
# ax2.scatter(X_pca[:,0],X_pca[:,1],c="g")
# ax2.set_title("After_PCA")
# ax2.set_xlabel("Principal component1")
# ax2.set_ylabel("Principal component2")
# plt.show()
# n = 1000
# pc1 = np.random.normal(0, 1, n)
# pc2 = np.random.normal(0, 0.2, n)
# noise = np.random.normal(0, 0.05, n)
#
# # 修正：np.vstack 传入数组列表，再转置
# X = np.vstack([pc1 + pc2, pc1 - pc2, pc2 + noise]).T
#
# pca = PCA(n_components=2)
# X_pca = pca.fit_transform(X)
#
# fig = plt.figure(figsize=(12, 4))
# # 3D 散点图：降维前原始3维特征
# ax1 = fig.add_subplot(121, projection='3d')
# ax1.scatter(X[:, 0], X[:, 1], X[:, 2], c="g")
# ax1.set_title("Before_PCA")
# ax1.set_xlabel("Feature1")
# ax1.set_ylabel("Feature2")
# ax1.set_zlabel("Feature3")
#
# # 2D 散点图：PCA降维后2维主成分
# ax2 = fig.add_subplot(122)
# ax2.scatter(X_pca[:, 0], X_pca[:, 1], c="g")
# ax2.set_title("After_PCA")
# ax2.set_xlabel("Principal component1")
# ax2.set_ylabel("Principal component2")
#
# plt.show()
#拟合案例
# 构造数据，X直接转为二维特征
# X = np.linspace(-3, 3, 300).reshape(-1, 1)
# Y = np.sin(X) + np.random.uniform(-0.5, 0.5, 300).reshape(-1, 1)
# print(X.shape)
# print(Y.shape)
# fig, ax = plt.subplots(1, 3, figsize=(15, 4))
# ax[0].scatter(X, Y, color='y')
# ax[1].scatter(X, Y, color='y')
# ax[2].scatter(X, Y, color='y')
# # 划分数据集
# trainX, testX, trainY, testY = train_test_split(X, Y, test_size=0.2, random_state=42)
# # 训练线性回归，欠拟合
# model = LinearRegression()
# model.fit(trainX, trainY)  # X已是二维，直接训练
# print(model.coef_)
# print(model.intercept_)
# x_train1=trainX
# x_test1=testX
# y_pred1 = model.predict(x_test1)
# train_pred = model.predict(x_train1)
# test_loss1 = mean_squared_error(testY, y_pred1)
# train_loss1 = mean_squared_error(trainY, train_pred)
# ax[0].plot(X, model.predict(X), color='r')
# ax[0].text(-2.8, 1.0, f"test loss: {test_loss1:.4f}")
# ax[0].text(-2.8, 1.3, f"train loss: {train_loss1:.4f}")
# #恰好拟合五次多项式
# poly5=PolynomialFeatures(degree=5)
# x_train2=poly5.fit_transform(trainX)
# x_test2=poly5.fit_transform(testX)
# print(x_train2.shape)
# print(x_test2.shape)
# model.fit(x_train2, trainY)
# y_pred2 = model.predict(x_test2)
# train_pred = model.predict(x_train2)
# test_loss2 = mean_squared_error(testY, y_pred2)
# train_loss2 = mean_squared_error(trainY, train_pred)
# ax[1].plot(X, model.predict(poly5.fit_transform(X)), color='r')
# ax[1].text(-2.8, 1.0, f"test loss: {test_loss2:.4f}")
# ax[1].text(-2.8, 1.3, f"train loss: {train_loss2:.4f}")
# #过拟合
# poly20=PolynomialFeatures(degree=20)
# x_train3=poly20.fit_transform(trainX)
# x_test3=poly20.fit_transform(testX)
# print(x_train3.shape)
# print(x_test3.shape)
# model.fit(x_train3, trainY)
# y_pred3 = model.predict(x_test3)
# train_pred3 = model.predict(x_train3)
# test_loss3 = mean_squared_error(testY, y_pred3)
# train_loss3 = mean_squared_error(trainY, train_pred3)
# ax[2].plot(X, model.predict(poly20.fit_transform(X)), color='r')
# ax[2].text(-2.8, 1.0, f"test loss: {test_loss3:.4f}")
# ax[2].text(-2.8, 1.3, f"train loss: {train_loss3:.4f}")
# plt.tight_layout()
# plt.show()
#正则化

#无正则化
# X = np.linspace(-3, 3, 300).reshape(-1, 1)
# Y = np.sin(X) + np.random.uniform(-0.5, 0.5, 300).reshape(-1, 1)
# print(X.shape)
# print(Y.shape)
# fig, ax = plt.subplots(2, 3, figsize=(15, 8))
# ax[0,0].scatter(X, Y, color='y')
# ax[0,1].scatter(X, Y, color='y')
# ax[0,2].scatter(X, Y, color='y')
# poly20=PolynomialFeatures(degree=20)
# trainX,testX,trainY,testY = train_test_split(X,Y,test_size=0.2,random_state=42)
# x_train=poly20.fit_transform(trainX)
# x_test=poly20.transform(testX)
# model = LinearRegression()
# model.fit(x_train, trainY)
# y_pred1=model.predict(x_test)
# test_loss1 = mean_squared_error(testY,y_pred1)
# ax[0,0].plot(X, model.predict(poly20.transform(X)), color='r')
# ax[0,0].text(-2.8, 1.0, f"test loss: {test_loss1:.4f}")
# ax[1,0].bar(np.arange(21), model.coef_.reshape(-1))
# #L1正则化（lasso回归）
# lasso=Lasso(alpha=0.01)
# lasso.fit(x_train,trainY)
# y_pred2=lasso.predict(x_test)
# test_loss2 = mean_squared_error(testY,y_pred2)
# ax[0,1].plot(X, lasso.predict(poly20.transform(X)), color='r')
# ax[0,1].text(-2.8, 1.0, f"test loss: {test_loss2:.4f}")
# ax[1,1].bar(np.arange(21), lasso.coef_.reshape(-1))
# #L2正则化（岭回归）
# ridge=Ridge(alpha=0.01)
# ridge.fit(x_train,trainY)
# y_pred3=ridge.predict(x_test)
# test_loss3 = mean_squared_error(testY,y_pred3)
# ax[0,2].plot(X, ridge.predict(poly20.transform(X)), color='r')
# ax[0,2].text(-2.8, 1.0, f"test loss: {test_loss3:.4f}")
# ax[1,2].bar(np.arange(21), ridge.coef_.reshape(-1))
# plt.show()
#梯度下降法
#定义目标函数
# def f(x):
# #     return x**2
#     return (x+3)**2-5
# #定义梯度函数
# def gradient(x):
#     return 2*(x+3)
# #用列表保存点的变化轨迹
# x_list=[]
# y_list=[]
# #定义超参数和x初始值
# alpha=0.1
# x=1
# #重复迭代一百次
# for i in range(100):
#     y=f(x)
#     x_list.append(x)
#     y_list.append(y)
#     print(f"x={x}, y={y}")
#     grad=gradient(x)
#     #update
#     x=x-alpha*grad
# #画图
# x=np.arange(-5,1,0.01)
# plt.plot(x,f(x))
# plt.plot(x_list,y_list,color='red')
# plt.scatter(x_list,y_list,color='red')
# plt.show()
# def J(x):
#     return (x**2-2)**2
# def gradient(x):
#     return 4*x**3-8*x
# x=1
# alpha=0.1
# x_list=[]
# y_list=[]
# while np.abs(grad:=gradient(x))> 1e-10:#先执行gradient(x)算出梯度，把结果赋值给变量grad，同时把这个值作为表达式本身参与判断。
#     y=J(x)
#     x_list.append(x)
#     y_list.append(y)
#     print(f"x:{x},y:{y}")
#     x=x-alpha*grad
# print(len(x_list))
# x=np.linspace(0.9,1.6)
# plt.figure()
# plt.plot(x,J(x),"y")
# plt.plot(x_list,y_list,color="r")
# plt.scatter(x_list,y_list,color="r")
# plt.tight_layout()
# plt.show()
# fig,ax=plt.subplots(1,2,figsize=(10,5))
# ax[0].plot(x,J(x))
# ax[0].plot(x_list,y_list,color="r")
# ax[0].scatter(x_list,y_list,color="r")
# x_list2=x_list[1:]
# y_list2=y_list[1:]
# x=np.arange(1.399,1.425,0.001)
# ax[1].plot(x,J(x))
# ax[1].plot(x_list2,y_list2,color="r")
# ax[1].scatter(x_list2,y_list2,color="r")
# plt.tight_layout()
# plt.show()

# #性能指标
# labels=['猫','狗']
# #定义数据（预测值和真实值）
# y_true=['猫','猫','猫','猫','猫','猫','狗','狗','狗','狗']
# y_pred=['猫','猫','狗','猫','猫','猫','猫','猫','狗','狗']
# martix=confusion_matrix(y_true,y_pred,labels=labels)
# # print(martix)
# # print(pd.DataFrame(martix,columns=labels,index=labels))
# # sns.heatmap(martix,annot=True,fmt='d',cmap='Greens')
# # plt.xlabel('预测标签')
# # plt.ylabel('真是标签')
# # plt.title('混淆矩阵')
# # plt.show()
# #准确率
# # accuracy=accuracy_score(y_true,y_pred)
# # print(accuracy)
# #查准率
# precision_cat=precision_score(y_true,y_pred,pos_label='猫')
# print(precision_cat)
# precision_dog=precision_score(y_true,y_pred,pos_label='狗')
# print(precision_dog)
# #召回率
# recall_cat=recall_score(y_true,y_pred,pos_label='猫')
# recall_dog=recall_score(y_true,y_pred,pos_label='狗')
# print(recall_cat)
# print(recall_dog)
# #F1 Score
# f1_cat=f1_score(y_true,y_pred,pos_label='猫')
# f1_dog=f1_score(y_true,y_pred,pos_label='狗')
# print(f1_cat)
# print(f1_dog)
#
# report = classification_report(y_true,y_pred,labels=labels,target_names=None)
# print(report)
#ROC和AUC
#生成数据
# X,y=make_classification(n_samples=1000,n_features=20,n_classes=2,random_state=42)
# print(X.shape)
# print(y.shape)
# X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=42)
# model=LogisticRegression()
# model.fit(X_train,y_train)
# y_pred=model.predict(X_test)
# report = classification_report(y_test,y_pred)
# print(report)
# #获取预测正类的概率值
# y_pred_proba=model.predict_proba(X_test)[:,1]
# print(y_pred_proba)
# roc_auc=roc_auc_score(y_test,y_pred_proba)
# print(roc_auc)
# # 绘制 ROC 曲线
# fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)
#
# plt.figure(figsize=(6, 5))
# plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (AUC = {roc_auc:.2f})')
# # 对角线（随机猜测基准）
# plt.plot([0, 1], [0, 1], color='navy',lw=2,)
#
# plt.xlim([0.0, 1.0])
# plt.ylim([0.0, 1.05])
# plt.xlabel('False Positive Rate (FPR)')
# plt.ylabel('True Positive Rate (TPR)')
# plt.title('ROC Curve')
# plt.legend(loc="lower right")
# plt.show()
#KNN算法
#分类
# X=np.array([[2,1],[3,1],[1,4],[2,6]])
# y=np.array([0,1,0,1])
# knn=KNeighborsClassifier(n_neighbors=2,weights='distance')
# knn.fit(X,y)
# x=np.array([[4,9]])
# x_class=knn.predict(x)
# print(x_class)
# X1=X[y==0]
# X2=X[y==1]
# colors=['C0','C1']
# plt.figure(figsize=[8,8])
# plt.scatter(X1[:,0],X1[:,1],c=colors[0])
# plt.scatter(X2[:,0],X2[:,1],c=colors[1])
# x_color=colors[0] if x_class==0 else colors[1]
# plt.scatter(x[:,0],x[:,1],c=x_color)
# plt.axis('equal')#横纵坐标一样长
# plt.title('KNN')
# plt.show()
#回归
# X=np.array([[2,1],[3,1],[1,4],[2,6]])
# y=np.array([0.5,0.33,4,3])
# knn=KNeighborsRegressor(n_neighbors=2,weights='distance')
# knn.fit(X,y)
# x=np.array([[4,9]])
# x_class=knn.predict(x)
# print(x_class)
#归一化
# from sklearn.preprocessing import MinMaxScaler
# X=np.array([[2,1],[3,1],[1,4],[2,6]])
# X=MinMaxScaler(feature_range=(-1,1)).fit_transform(X)
# print(X)#一列一个特征
#标准化
# from sklearn.preprocessing import StandardScaler
# X=np.array([[2,1],[3,1],[1,4],[2,6]])
# X_scaled=StandardScaler().fit_transform(X)
# print(X_scaled)
# print(X.mean(axis=0),X.std(axis=0))
# print(X_scaled.mean(axis=0),X_scaled.std(axis=0))


















