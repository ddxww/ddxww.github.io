import numpy as np
from scipy.optimize import linprog
# c=np.array([-20,-30,-40])
# A_ub=np.array([[4,8,10],
#                [1,1,1]])
# b_ub=np.array([100,20])
# bounds=[[0,None]]*3
# result=linprog(c,A_ub=A_ub,b_ub=b_ub)
# print(result.x)
# print(-result.fun)
import numpy as np
from scipy.optimize import linprog

# 物品重量和利润
weights = np.array([6, 3, 4, 5, 1, 2, 3, 5, 4, 2])
profits = np.array([540, 200, 180, 350, 60, 150, 280, 450, 320, 120])
max_weight = 30
# 目标函数：最大化总利润 -> 最小化负利润
c = -profits  # linprog默认最小化，所以取负
# 不等式约束：总重量 <= 30
A_ub = [weights]  # 系数矩阵
b_ub = [max_weight]  # 右侧约束值
# 变量边界：0 <= x_i <= 1（松弛后的连续约束）
bounds = [(0, 1) for _ in range(len(weights))]
# 求解线性规划
res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')
# 输出结果
if res.success:
    print("线性规划松弛解：")
    selected_items = []
    total_profit = 0
    total_weight = 0
    # 检查每个变量，四舍五入为0或1
    for i in range(len(weights)):
        if res.x[i] > 0.5:  # 四舍五入
            selected_items.append(i + 1)
            total_profit += profits[i]
            total_weight += weights[i]
        print(f"物品 {i + 1}: 选择概率 = {res.x[i]:.4f}")
    print("\n四舍五入后的整数解：")
    print(f"选择物品: {selected_items}")
    print(f"总利润: {total_profit}")
    print(f"总重量: {total_weight} (限制: {max_weight})")
    if total_weight > max_weight:
        print("⚠️ 警告：四舍五入后解不可行（总重量超过限制）")
    else:
        print("✅ 解可行")
else:
    print("无解或求解失败")