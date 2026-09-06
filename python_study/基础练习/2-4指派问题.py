from pulp import LpMinimize,LpProblem,LpVariable,lpSum,value
problem=LpProblem("knapsack",LpMinimize)
c=[66.8,75.6,87,58.6,57.2,66,66.4,53,75,67.8,84.6,59.4,70,74.2,69.6,57.2,67.4,71,83.8,62.4]
x=[LpVariable(f"x{i+1}",cat="Binary")for i in range(20)]
problem+=lpSum(c[i]*x[i] for i in range(20))
A=[
    [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
]
b=[1,1,1,1,1]
for i in range(len(A)):
    problem+=lpSum(A[i][j]*x[j] for j in range(20))<=b[i]
Aeq=[
    [1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0],
    [0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0],
    [0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0],
    [0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0]
]
beq=[1,1,1,1]
for i in range(len(Aeq)):
    problem+=lpSum(Aeq[i][j]*x[j] for j in range(20))==beq[i]
problem.solve()
assignments=[value(x[i])for i in range(20)]
print(assignments)
print("最小值:")
print(problem.objective.value())
import numpy as np
assignments=np.array(assignments).reshape(5,4)
assignments=assignments.astype(int)
print(assignments)