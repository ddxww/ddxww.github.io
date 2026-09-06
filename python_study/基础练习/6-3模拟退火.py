import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = ["SimSun", "Microsoft YaHei", "SimHei"]
plt.rcParams["axes.unicode_minus"] = False
# 1. 定义目标函数（求最小值）
def objective_function(x):
    return x * np.sin(10 * np.pi * x) + 2.0  # 带多个局部极值的函数
# 2. 生成初始解（在定义域内随机选择）
def initial_solution(low, high):
    return np.random.uniform(low, high)  # 定义域[-1, 3]
# 3. 生成邻域解（在当前解附近添加随机扰动）
def generate_neighbor(x, step=0.1):
    # 扰动范围：当前解±step，超出定义域则截断
    neighbor = x + np.random.uniform(-step, step)
    return np.clip(neighbor, -1, 3)  # 确保在[-1, 3]内
# 4. 模拟退火算法主函数
def simulated_annealing(low, high, initial_temp=100.0, cooling_rate=0.95, max_iter=1000):
    # 初始化
    current_x = initial_solution(low, high)  # 当前解
    current_energy = objective_function(current_x)  # 当前能量（目标函数值）
    best_x = current_x  # 最优解
    best_energy = current_energy  # 最优能量
    temp = initial_temp  # 当前温度
    # 记录优化过程（用于可视化）
    history = []
    for i in range(max_iter):
        # 生成邻域解
        neighbor_x = generate_neighbor(current_x)
        neighbor_energy = objective_function(neighbor_x)
        # 计算能量差（新解 - 当前解，求最小值时，负值表示新解更优）
        energy_diff = neighbor_energy - current_energy
        # Metropolis准则：接受新解
        if energy_diff < 0:
            # 新解更优，直接接受
            current_x = neighbor_x
            current_energy = neighbor_energy
        else:
            # 新解较差，以概率exp(-energy_diff/temp)接受
            acceptance_prob = np.exp(-energy_diff / temp)
            if np.random.random() < acceptance_prob:
                current_x = neighbor_x
                current_energy = neighbor_energy
        # 更新最优解
        if current_energy < best_energy:
            best_x = current_x
            best_energy = current_energy
        # 记录历史
        history.append((current_x, current_energy))
        # 降温（指数冷却）
        temp *= cooling_rate
        # 打印迭代信息（每100次）
        if i % 100 == 0:
            print(f"迭代{i}次：温度={temp:.2f}，当前解={current_x:.4f}，当前能量={current_energy:.4f}")
    return best_x, best_energy, history
# 5. 运行算法并可视化结果
if __name__ == "__main__":
    # 定义参数
    low, high = -1, 3  # 定义域
    initial_temp = 100.0  # 初始温度
    cooling_rate = 0.95  # 冷却率（越接近1，降温越慢）
    max_iter = 1000  # 迭代次数
    # 运行模拟退火
    best_x, best_energy, history = simulated_annealing(low, high, initial_temp, cooling_rate, max_iter)
    # 输出结果
    print(f"\n最优解：x={best_x:.4f}，目标函数值={best_energy:.4f}")
    # 可视化：函数图像 + 优化轨迹
    x = np.linspace(low, high, 1000)
    y = objective_function(x)
    plt.figure(figsize=(10, 6))
    # 绘制目标函数
    plt.plot(x, y, 'b-', label='目标函数 f(x) = x·sin(10πx) + 2.0')
    # 绘制优化轨迹
    history_x = [h[0] for h in history]
    history_y = [h[1] for h in history]
    plt.scatter(history_x, history_y, c='r', s=5, alpha=0.5, label='优化轨迹')
    # 标记最优解
    plt.scatter(best_x, best_energy, c='green', s=100, marker='*', label=f'最优解：{best_energy:.4f}')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('模拟退火算法优化过程')
    plt.legend()
    plt.grid(True)
    plt.show()