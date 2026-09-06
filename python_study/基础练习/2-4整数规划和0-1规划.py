from pulp import LpMaximize,LpProblem,LpVariable,lpSum,value
import numpy as np
# problem=LpProblem("maximize",LpMaximize)
# x1=LpVariable("x1",lowBound=0,upBound=None,cat="Integer")
# x2=LpVariable("x2",lowBound=0,upBound=None,cat="Integer")
# x3=LpVariable("x3",lowBound=0,upBound=None,cat="Integer")
# problem+=20*x1+30*x2+40*x3#目标函数
# problem+=4*x1+8*x2+10*x3<=100
# problem+=x1+x2+x3<=20
# problem.solve()
# print("结果")
# print(value(x1),value(x2),value(x3))
# print("最终")
# print(value(problem.objective))
problem=LpProblem("knapsack",LpMaximize)
weights = np.array([6, 3, 4, 5, 1, 2, 3, 5, 4, 2])
profits = np.array([540, 200, 180, 350, 60, 150, 280, 450, 320, 120])
x=[LpVariable(f"x{i+1}",cat="Binary")for i in range(10)]
# print(x)
# print(x[0])
# print(type(x[0]))
problem+=lpSum(profits[i]*x[i] for i in range(10))
# print(problem)
problem+=lpSum(weights[i]*x[i] for i in range(10))<=30
problem.solve()
items=[value(x[i]) for i in range(10)]
print(items)
print("最大利润:")
print(value(problem.objective))