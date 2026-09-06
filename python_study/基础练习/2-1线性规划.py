# 整数线性规划
# import numpy as np
# from scipy.optimize import linprog
# c=[-20,-30,-45]
# A_ub=([
#     [4,8,15],
#     [1,1,1]
# ])
# b_ub=[100,20]
# bounds=[[0,None],[0,None],[0,None]]
# result=linprog(c,A_ub=A_ub,b_ub=b_ub,bounds=bounds)
# print(result)
# print("A,B,C三图通关次数分别为")
# print(result.x)
# y=-result.fun
# print(y)
# array_ones=np.ones((3,4))
# print(array_ones)
# diag0=np.diag([1,2,3])#对角
# print(diag0)
# array1=np.array([
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ])
# diag1=np.diag(array1)#提取对角元素
# print(diag1)
# arr1=np.array([1,2,3])
# newarr=np.append(arr1,4)
# print(newarr)
from matplotlib.pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import linprog

# 目标函数系数（最大化转为最小化）
c = [-0.05, -0.27, -0.19, -0.185, -0.185]
# 关键修复：禁用 LaTeX（因为你的电脑没有安装）
plt.rc('text', usetex=False)  # 关闭 LaTeX 渲染
plt.rc('font', size=16)  # 保持字体大小设置
# 构造约束矩阵 A（5x5，每个变量对应一个风险约束）
risk_factors = [0, 0.025, 0.015, 0.055, 0.026]
A = np.diag(risk_factors)
# 等式约束
Aeq = np.array([[1, 1.01, 1.02, 1.045, 1.065]])
beq = np.array([1])
# 存储结果
a_values = []
Q_values = []
# 遍历风险系数 a
for a in np.linspace(0, 0.05, 50):
    b = np.ones(5) * a  # 风险约束向量（长度5，与变量数匹配）
    # 求解线性规划
    res = linprog(c,A,b,Aeq,beq,bounds=[(0, None)] * 5,)
    # 处理结果
    if res.success:
        a_values.append(a)
        Q_values.append(-res.fun)  # 转换为最大化收益
plt.figure(figsize=(10, 6))
plt.plot(a_values, Q_values, marker='*', markersize=6)
plt.xlabel('风险系数 a')  # 不使用 LaTeX 语法
plt.ylabel('最大收益 Q', rotation=90)
plt.title('风险-收益权衡曲线')
plt.grid(True)
plt.show()