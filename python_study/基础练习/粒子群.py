import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp, odeint
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = ["SimSun", "Microsoft YaHei", "SimHei"]  # 宋体、微软雅黑、黑体
plt.rcParams["axes.unicode_minus"] = False  # 解决负号显示问题
# =============================
#  粒子群算法求解配送中心选址
# =============================

# 客户点（坐标 + 需求量）
customers = np.array([
    [2, 3, 10],   # (x, y, demand)
    [5, 8, 20],
    [1, 7, 15],
    [6, 2, 25],
    [8, 6, 30]
])

# 目标函数：加权距离和
def objective(position):
    x, y = position
    total = 0
    for cx, cy, demand in customers:
        total += demand * np.sqrt((x - cx)**2 + (y - cy)**2)
    return total

# 粒子群算法参数
num_particles = 30
num_iterations = 100
w = 0.7    # 惯性权重
c1 = 1.5   # 认知学习因子
c2 = 1.5   # 社会学习因子

# 初始化粒子（随机生成坐标）
particles = np.random.rand(num_particles, 2) * 10  # 搜索范围 [0,10]
velocities = np.zeros((num_particles, 2))

# 个体极值 & 全局极值
pbest = particles.copy()
pbest_values = np.array([objective(p) for p in particles])
gbest = pbest[np.argmin(pbest_values)]
gbest_value = min(pbest_values)

# 迭代
history = []
for it in range(num_iterations):
    for i in range(num_particles):
        # 更新速度
        r1, r2 = np.random.rand(), np.random.rand()
        velocities[i] = (
            w * velocities[i]
            + c1 * r1 * (pbest[i] - particles[i])
            + c2 * r2 * (gbest - particles[i])
        )
        # 更新位置
        particles[i] += velocities[i]
        # 边界限制
        particles[i] = np.clip(particles[i], 0, 10)

        # 更新个体极值
        value = objective(particles[i])
        if value < pbest_values[i]:
            pbest[i] = particles[i]
            pbest_values[i] = value

    # 更新全局极值
    best_idx = np.argmin(pbest_values)
    if pbest_values[best_idx] < gbest_value:
        gbest = pbest[best_idx]
        gbest_value = pbest_values[best_idx]

    history.append(gbest_value)

    if it % 10 == 0:
        print(f"迭代 {it}: 最优目标值 = {gbest_value:.4f}")

print("\n最终最优配送中心坐标：", gbest)
print("最小加权距离和：", gbest_value)

# =============================
#  可视化
# =============================
plt.figure(figsize=(6,5))

# 客户点
plt.scatter(customers[:,0], customers[:,1], s=customers[:,2], c='blue', label="客户点 (需求量大小)")

# 最优解
plt.scatter(gbest[0], gbest[1], c='red', marker='*', s=200, label="最优配送中心")

plt.title("粒子群算法求解配送中心选址")
plt.xlabel("X 坐标")
plt.ylabel("Y 坐标")
plt.legend()
plt.grid(True)
plt.show()

# 收敛曲线
plt.figure()
plt.plot(history, marker='o')
plt.title("PSO 收敛曲线")
plt.xlabel("迭代次数")
plt.ylabel("目标函数值")
plt.grid(True)
plt.show()
