import pulp
import numpy as np
from pprint import pprint
def transportation_problem(costs, x_max, y_max):
    row = len(costs)
    col = len(costs[0])
    prob = pulp.LpProblem("transportation problem", pulp.LpMaximize)
    # 定义决策变量：x[i][j] 表示从工厂i运输到种植地j的数量
    var = [[pulp.LpVariable(f'x{i}{j}', lowBound=0, cat=pulp.LpInteger)
            for j in range(col)] for i in range(row)]
    # 设置目标函数：最大化总收益
    prob += pulp.lpSum(costs[i][j] * var[i][j] for i in range(row) for j in range(col))
    # 添加约束条件：每个工厂的运输量不超过其最大产量
    for i in range(row):
        prob += pulp.lpSum(var[i][j] for j in range(col)) <= x_max[i]
    # 添加约束条件：每个种植地的接收量不超过其最大需求量
    for j in range(col):
        prob += pulp.lpSum(var[i][j] for i in range(row)) <= y_max[j]
    # 求解问题
    prob.solve()
    # 提取并返回结果
    return {
        'objective': pulp.value(prob.objective),
        'var': [[pulp.value(var[i][j]) for j in range(col)] for i in range(row)]
    }
if __name__ == '__main__':
    costs = np.array([[500, 550, 630, 1000, 800, 700],
                      [800, 700, 600, 950, 900, 930],
                      [1000, 960, 840, 650, 600, 700],
                      [1200, 1040, 980, 860, 880, 780]])
    max_plant = [76, 88, 96, 40]  # 各工厂的最大产量
    max_cultivation = [42, 56, 44, 39, 60, 59]  # 各种植地的最大需求量

    res = transportation_problem(costs, max_plant, max_cultivation)
    print(f'最大值为 {res["objective"]}')
    print('各变量的取值为：')
    pprint(res['var'])