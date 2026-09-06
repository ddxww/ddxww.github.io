import pa1 as pd
import numpy as np
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------- 修正字体配置（关键部分） --------------------------
# 使用系统通用中文字体（Windows默认有，避免找不到）
plt.rcParams["font.family"] = ["SimSun", "Microsoft YaHei", "SimHei"]  # 宋体、微软雅黑、黑体（系统通常预装）
plt.rcParams["axes.unicode_minus"] = False  # 解决负号显示问题
# ------------------------------------------------------------------------------

# 数据
data = {
    'x1': [7, 1, 11, 11, 7, 11, 3, 1, 2, 21, 1, 11, 10],
    'x2': [26, 29, 56, 31, 52, 55, 71, 31, 54, 47, 40, 66, 68],
    'x3': [6, 15, 8, 8, 6, 9, 17, 22, 18, 4, 23, 9, 8],
    'x4': [60, 52, 20, 47, 33, 22, 6, 44, 22, 26, 34, 12, 12],
    'y': [78.5, 74.3, 104.3, 87.6, 95.9, 109.2, 102.7, 72.5, 93.1, 115.9, 83.8, 113.3, 109.4]
}
df = pd.DataFrame(data)
X = df[['x1', 'x2', 'x3', 'x4']]
y = df['y']


# 向前选择逐步回归（记录变量进入顺序）
def forward_selection_with_order(X, y, criterion='aic'):
    included = []
    order = []
    history = []
    while True:
        excluded = list(set(X.columns) - set(included))
        if not excluded:
            break
        best_criterion = float('inf')
        best_var = None
        for var in excluded:
            model = sm.OLS(y, sm.add_constant(X[included + [var]])).fit()
            current_criterion = getattr(model, criterion)
            if current_criterion < best_criterion:
                best_criterion = current_criterion
                best_var = var
        if best_var and best_criterion < float('inf'):
            included.append(best_var)
            order.append(best_var)
            model = sm.OLS(y, sm.add_constant(X[included])).fit()
            history.append({
                'variables': included.copy(),
                'criterion': best_criterion,
                'rsquared': model.rsquared,
                'adj_rsquared': model.rsquared_adj
            })
        else:
            break
    return order, history


# 计算重要性指标
def calculate_importance_metrics(X, y, order):
    metrics = {}
    order_score = {var: len(order) - i for i, var in enumerate(order)}

    final_model = sm.OLS(y, sm.add_constant(X[order])).fit()
    pvalue_score = {var: 1 / final_model.pvalues[var] for var in order}

    X_std = pd.DataFrame(StandardScaler().fit_transform(X[order]), columns=order)
    std_model = sm.OLS(y, sm.add_constant(X_std)).fit()
    coef_score = {var: abs(std_model.params[var]) for var in order}

    base_r2 = 0
    r2_score = {}
    for var in order:
        model = sm.OLS(y, sm.add_constant(X[order[:order.index(var) + 1]])).fit()
        delta_r2 = model.rsquared - base_r2
        r2_score[var] = delta_r2
        base_r2 = model.rsquared

    importance = {var: (order_score[var] + pvalue_score[var] + coef_score[var] + r2_score[var]) for var in order}
    metrics['order'] = order_score
    metrics['pvalue'] = pvalue_score
    metrics['coef'] = coef_score
    metrics['delta_r2'] = r2_score
    metrics['importance'] = importance
    return metrics, final_model, std_model


# 执行分析
order, history = forward_selection_with_order(X, y, criterion='aic')
metrics, final_model, std_model = calculate_importance_metrics(X, y, order)

# 输出结果
print("\n=== 逐步回归变量选择过程 ===")
for i, step in enumerate(history):
    print(f"步骤 {i + 1}: 添加变量 {step['variables'][-1]}")
    print(f"  - AIC: {step['criterion']:.4f}, R²: {step['rsquared']:.4f}, 调整R²: {step['adj_rsquared']:.4f}")

print("\n=== 变量重要性评估 ===")
for metric_name, metric_values in metrics.items():
    if metric_name != 'importance':
        print(f"\n{metric_name} 排名:")
        print(pd.Series(metric_values).sort_values(ascending=False))

print("\n=== 综合变量重要性排名 ===")
importance = pd.Series(metrics['importance']).sort_values(ascending=False)
print(importance)

# 可视化
plt.figure(figsize=(14, 10))

plt.subplot(2, 2, 1)
steps = list(range(1, len(history) + 1))
plt.plot(steps, [h['criterion'] for h in history], 'o-', label='AIC')
plt.xlabel('步骤')
plt.ylabel('AIC')
plt.title('模型AIC随变量添加的变化')
plt.xticks(steps)
plt.grid(True)

plt.subplot(2, 2, 2)
sns.barplot(x=importance.index, y=importance.values)
plt.title('综合变量重要性')
plt.xlabel('变量')
plt.ylabel('重要性得分')

plt.subplot(2, 2, 3)
coef = std_model.params.drop('const')
coef_sorted = coef.sort_values(ascending=False)
colors = ['green' if c > 0 else 'red' for c in coef_sorted]
plt.bar(coef_sorted.index, coef_sorted.values, color=colors)
plt.title('标准化系数（影响方向和强度）')
plt.xlabel('变量')
plt.ylabel('标准化系数')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.subplot(2, 2, 4)
delta_r2 = pd.Series(metrics['delta_r2'])[order]
plt.bar(delta_r2.index, delta_r2.values)
plt.title('变量的边际R²贡献')
plt.xlabel('变量')
plt.ylabel('ΔR²')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()

print("\n=== 最终模型摘要 ===")
print(final_model.summary())
plt.figure(figsize=(15, 4))
plt.subplot(1, 3, 1)
plt.scatter(df['x1'], df['y'])
plt.xlabel('x1（推销开支）')
plt.ylabel('y（销量）')
plt.title('x1与y的关系')

plt.subplot(1, 3, 2)
plt.scatter(df['x2'], df['y'])
plt.xlabel('x2（实际账目数）')
plt.ylabel('y（销量）')
plt.title('x2与y的关系')

plt.subplot(1, 3, 3)
plt.scatter(df['x4'], df['y'])
plt.xlabel('x4（销售潜力）')
plt.ylabel('y（销量）')
plt.title('x4与y的关系')

plt.tight_layout()
plt.show()