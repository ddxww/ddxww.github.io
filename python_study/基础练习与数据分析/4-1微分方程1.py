# from matplotlib import pyplot as plt
# from scipy.integrate import odeint
# import numpy as np
# def model(y,t):
#     k=0.3
#     dydt=-k*y
#     return dydt
# y0=5
# t=np.linspace(0,20,100)
# result=odeint(model,y0,t)
# plt.plot(t,result)
# plt.show()
# print(result)
# from scipy.integrate import solve_ivp
# import numpy as np
# import matplotlib.pyplot as plt
# plt.rcParams["font.family"] = ["SimSun", "Microsoft YaHei", "SimHei"]  # 宋体、微软雅黑、黑体
# plt.rcParams["axes.unicode_minus"] = False  # 解决负号显示问题
# # 设置图片清晰度
# plt.rcParams['figure.dpi'] = 300
#
# # 定义微分方程模型
# def model(t, y):  # 注意：solve_ivp 默认 t 是第一个参数
#     k = 0.3
#     dydt = -k * y
#     return dydt
#
# # 初始条件和时间范围
# y0 = [5]  # 初始条件
# t_span = (0, 20)  # 时间范围
#
# # 使用 solve_ivp 求解微分方程
# sol = solve_ivp(model, t_span, y0, t_eval=np.linspace(0, 20, 100))
#
# # 打印结果
# print("求解结果形状:", sol.y.shape)
# print("部分结果示例:", sol.y[0, :5])  # 显示前5个结果
#
# # 绘制结果
# plt.figure(figsize=(10, 5))
# plt.plot(sol.t, sol.y[0], 'b-', linewidth=2, label='数值解')
# plt.xlabel('时间 (t)', fontsize=12)
# plt.ylabel('y(t)', fontsize=12)
# plt.title('一阶线性微分方程的解: dy/dt = -0.3y', fontsize=14)
# plt.grid(True, linestyle='--', alpha=0.7)
# plt.legend(fontsize=12)
# plt.tight_layout()  # 调整布局，使内容完整显示
# plt.show()
from scipy.integrate import solve_ivp, odeint
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = ["SimSun", "Microsoft YaHei", "SimHei"]  # 宋体、微软雅黑、黑体
plt.rcParams["axes.unicode_minus"] = False  # 解决负号显示问题
# 设置图片清晰度
plt.rcParams['figure.dpi'] = 300
def model(P,t,r):
    dPdt=r*P
    return dPdt
P0=100
t=np.linspace(0,1000,1000)
r=0.001
P=odeint(model,P0,t,args=(r,))
plt.plot(t,P)
plt.xlabel('t')
plt.ylabel('P')
plt.show()




