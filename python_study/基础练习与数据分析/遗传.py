import numpy as np

N_COURSES = 3
TIME_SLOTS = 4
POP_SIZE = 10
N_GEN = 20
CROSS_RATE = 0.8
MUTATE_RATE = 0.2

# 适应度函数：统计时间冲突
def fitness(pop):
    scores = []
    for ind in pop:
        conflicts = len(ind) - len(set(ind))  # 时间重复的就是冲突
        score = 1 / (1 + conflicts)  # 冲突越多，分数越低
        scores.append(score)
    return np.array(scores)

# 初始化种群
pop = [np.random.randint(1, TIME_SLOTS+1, N_COURSES) for _ in range(POP_SIZE)]

for gen in range(N_GEN):
    fit = fitness(pop)
    probs = fit / fit.sum()
    idx = np.random.choice(range(POP_SIZE), size=POP_SIZE, replace=True, p=probs)
    new_pop = [pop[i].copy() for i in idx]

    # 交叉
    for i in range(0, POP_SIZE, 2):
        if np.random.rand() < CROSS_RATE:
            cut = np.random.randint(0, N_COURSES)
            new_pop[i][:cut], new_pop[i+1][:cut] = new_pop[i+1][:cut], new_pop[i][:cut]

    # 变异
    for ind in new_pop:
        if np.random.rand() < MUTATE_RATE:
            c = np.random.randint(0, N_COURSES)
            ind[c] = np.random.randint(1, TIME_SLOTS+1)

    pop = new_pop

# 输出最优解
fit = fitness(pop)
best_idx = np.argmax(fit)
print("最佳课程安排:", pop[best_idx])
