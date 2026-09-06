# import numpy as np
# from scipy.optimize import minimize
# def fun1(x):
#     return x[0]**2+x[1]**2-x[0]*x[1]-2*x[0]-5*x[1]
# def nonlcon1(x):
#     return -(x[0]-1)**2+x[1]
# def nonlcon2(x):
#     return 2*x[0]-3*x[1]+6
# x0=np.array([0,0])
# res=minimize(fun1,x0,constraints=({'type':'ineq','fun':nonlcon1},
#                                     {'type':'ineq','fun':nonlcon2}),
#              bounds=None,tol=None,options=None,args=())
# print("最优解",res.x)
# print("最优值",res.fun)
# #蒙特卡洛
# n=10000000
# x1=np.random.uniform(-100,100,size=n)
# x2=np.random.uniform(-100,100,size=n)
# fmin=10000000
# for i in range(n):
#     x=np.array([x1[i],x2[i]])
#     if nonlcon1(x)>=0 and nonlcon2(x)>=0:
#         result=fun1(x)
#         if result<fmin:
#             fmin=result
#             x0=x;
# print("选取的初始值",x0)
# res_final=minimize(fun1,x0,constraints=({'type':'ineq','fun':nonlcon1},
#                                     {'type':'ineq','fun':nonlcon2}),
#              bounds=None,tol=None,options=None,args=())
# print("最优解",res_final.x)
# print("最优解的值",res_final.fun)
import numpy as np
from scipy.optimize import minimize, linprog

a = np.array([1.25, 8.75, 0.5, 5.75, 3, 7.25])
b = np.array([1.25, 0.75, 4.75, 5, 6.5, 7.75])
d = np.array([3, 5, 4, 7, 6, 11])

# 计算到初始点的距离
x1_coord, y1_coord = 5, 1
x2_coord, y2_coord = 2, 7

distances_to_x1 = np.sqrt((x1_coord - a) ** 2 + (y1_coord - b) ** 2)
distances_to_x2 = np.sqrt((x2_coord - a) ** 2 + (y2_coord - b) ** 2)

# 第一阶段：线性规划
f = np.hstack([distances_to_x2, distances_to_x1])
A = np.array([
    [1] * 6 + [0] * 6,  # 第一个仓库容量约束
    [0] * 6 + [1] * 6  # 第二个仓库容量约束
])
b_constraints = np.array([20, 20])

eye_matrix = np.eye(6)
A_eq = np.hstack([eye_matrix, eye_matrix])  # 每个客户需求必须满足
b_eq = d

bounds = [(0, None)] * 12  # 每个变量非负约束

result = linprog(f, A_ub=A, b_ub=b_constraints, A_eq=A_eq, b_eq=b_eq, bounds=bounds)
x1, fval1 = result.x, result.fun
print("线性规划最优解:", x1)
print("线性规划最优值:", fval1)


# 第二阶段：非线性规划
def objective(x):
    # 前12个变量是分配量，后4个变量是仓库坐标
    allocations = x[:12]
    warehouse1_x, warehouse1_y = x[12], x[13]
    warehouse2_x, warehouse2_y = x[14], x[15]

    # 计算从两个仓库到各客户的距离
    dist1 = np.sqrt((warehouse1_x - a) ** 2 + (warehouse1_y - b) ** 2)
    dist2 = np.sqrt((warehouse2_x - a) ** 2 + (warehouse2_y - b) ** 2)

    # 目标函数：总运输距离
    return np.sum(dist1 * allocations[:6]) + np.sum(dist2 * allocations[6:])


def ineq_constraint1(x):
    # 第一个仓库容量约束
    return 20 - np.sum(x[:6])


def ineq_constraint2(x):
    # 第二个仓库容量约束
    return 20 - np.sum(x[6:12])


def eq_constraint(x):
    # 每个客户的需求必须满足
    return np.array([
        x[0] + x[6] - d[0],
        x[1] + x[7] - d[1],
        x[2] + x[8] - d[2],
        x[3] + x[9] - d[3],
        x[4] + x[10] - d[4],
        x[5] + x[11] - d[5]
    ])


# 正确定义约束：分为不等式约束和等式约束
cons = [
    {'type': 'ineq', 'fun': ineq_constraint1},
    {'type': 'ineq', 'fun': ineq_constraint2},
    {'type': 'eq', 'fun': eq_constraint}
]

# 变量边界：前12个是分配量(非负)，后4个是仓库坐标(无限制)
bounds = [(0, None)] * 12 + [(-np.inf, np.inf)] * 4

# 构造初始点：使用线性规划结果和初始坐标
x0_lp = np.hstack([x1, [x1_coord, y1_coord, x2_coord, y2_coord]])
print("非线性优化初始点:", x0_lp)

# 使用SLSQP方法求解非线性规划问题
result_2 = minimize(fun=objective, x0=x0_lp, constraints=cons, bounds=bounds, method='SLSQP')
x2_lp, fval2 = result_2.x, result_2.fun

print("非线性规划解:", x2_lp)
print("非线性规划值:", fval2)

# 提取最优仓库坐标
warehouse1_optimal_x, warehouse1_optimal_y = x2_lp[12], x2_lp[13]
warehouse2_optimal_x, warehouse2_optimal_y = x2_lp[14], x2_lp[15]

print(f"最优仓库1坐标: ({warehouse1_optimal_x:.4f}, {warehouse1_optimal_y:.4f})")
print(f"最优仓库2坐标: ({warehouse2_optimal_x:.4f}, {warehouse2_optimal_y:.4f})")