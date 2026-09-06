import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

# 设置中文字体
plt.rcParams["font.family"] = ["SimSun", "Microsoft YaHei", "SimHei"]  # 宋体、微软雅黑、黑体
plt.rcParams["axes.unicode_minus"] = False  # 解决负号显示问题

# 定义系统参数
w_value = 1.0  # 角频率

# 数值求解微分方程
def func(t, x):
    dx1_dt = x[1]
    dx2_dt = -w_value**2 * x[0]
    return [dx1_dt, dx2_dt]

t = np.linspace(0, 10, 100)
x0 = [1, 0]  # 初始条件：x(0)=1, v(0)=0
result_num = odeint(func, x0, t, tfirst=True)

# 符号求解微分方程
x = sp.Symbol('x')
y = sp.Function('y')(x)
w = sp.Symbol('w')
eq = sp.Eq(y.diff(x, 2) + w**2 * y, 0)
sol = sp.dsolve(eq, y)

# 应用初始条件
C1, C2 = sp.symbols('C1 C2')
constants = sp.solve([sol.rhs.subs(x, 0) - 1,  # x(0) = 1
                      sol.rhs.diff(x).subs(x, 0) - 0],  # v(0) = 0
                     [C1, C2])
sol_with_constants = sol.rhs.subs(constants)

# 将符号解转换为数值函数以便绘图
sol_numerical = sp.lambdify(x, sol_with_constants.subs(w, w_value), 'numpy')
t_sym = np.linspace(0, 10, 100)
result_sym = sol_numerical(t_sym)

# 绘制结果
plt.figure(figsize=(10, 6))
plt.plot(t, result_num[:, 0], 'b-', label='数值解')
plt.plot(t_sym, result_sym, 'r--', label='解析解')
plt.xlabel('时间 (t)')
plt.ylabel('位移 (A)')
plt.title('简谐振动的解')
plt.legend()
plt.grid(True)
plt.show()

# 打印解析解
print("微分方程:", eq)
print("通解:", sol)
print("特解:", sol_with_constants)