# 1. 导入必备库（新增scipy用于卡方检验）
import pandas as pd
from scipy.stats import chi2_contingency  # 卡方检验工具

# 2. 构造原始数据（模拟文物调查数据）
raw_data = {
    "材质": ["陶", "陶", "陶", "瓷", "瓷", "瓷", "瓷", "青铜", "青铜", "青铜"],
    "表面风化": ["有", "有", "无", "有", "无", "无", "无", "有", "有", "无"],
    "年代": ["唐代", "宋代", "唐代", "宋代", "明代", "明代", "清代", "汉代", "汉代", "唐代"]
}
df = pd.DataFrame(raw_data)
print("=== 1. 原始文物数据 ===")
print(df)
print("\n")


# 3. 按「材质」和「表面风化」分组计数
var_name = "材质"
count_df = df.groupby([var_name, "表面风化"]).size().reset_index(name="数量")
print("=== 2. 分组计数后的结果（count_df） ===")
print(count_df)
print("\n")


# 4. 提取唯一类别
var_categories = count_df[var_name].unique()
weathering_categories = count_df["表面风化"].unique()
print("=== 3. 提取的唯一类别 ===")
print(f"{var_name}的所有类别：", var_categories)
print("表面风化的所有类别：", weathering_categories)
print("\n")


# 5. 计算每种材质的风化率
print("=== 4. 基于唯一类别的后续分析（材质风化率） ===")
for material in var_categories:
    material_data = count_df[count_df[var_name] == material]
    total = material_data["数量"].sum()
    weathered = material_data[material_data["表面风化"] == "有"]["数量"].sum() if "有" in weathering_categories else 0
    weathering_rate = round(weathered / total * 100, 2)
    print(f"{material}材质的总数量：{total}件，风化率：{weathering_rate}%")
print("\n")


# 6. 卡方检验：判断材质与表面风化是否存在显著关联
print("=== 5. 卡方检验结果（材质 vs 表面风化） ===")

# 步骤1：将count_df转换为卡方检验所需的交叉频数表（行：材质，列：表面风化）
cross_table = count_df.pivot(
    index=var_name,       # 行索引为材质
    columns="表面风化",    # 列索引为表面风化
    values="数量"         # 填充值为数量
).fillna(0)  # 若某组合无数据，用0填充

print("用于检验的交叉频数表：")
print(cross_table)
print("\n")

# 步骤2：执行卡方检验
# 返回值：卡方统计量、p值、自由度、理论频数
chi2, p_value, dof, expected = chi2_contingency(cross_table)

# 步骤3：输出检验结果
print(f"卡方统计量（chi2）：{chi2:.4f}")
print(f"P值（p-value）：{p_value:.4f}")
print(f"自由度（dof）：{dof}")
print("理论频数表（无关联假设下的预期数量）：")
print(pd.DataFrame(expected, index=cross_table.index, columns=cross_table.columns).round(2))
print("\n")

# 步骤4：结果解读（显著性水平α=0.05）
alpha = 0.05
if p_value < alpha:
    print(f"结论：P值（{p_value:.4f}）< {alpha}，拒绝原假设，认为{var_name}与表面风化存在显著关联。")
else:
    print(f"结论：P值（{p_value:.4f}）≥ {alpha}，无法拒绝原假设，未发现{var_name}与表面风化存在显著关联。")
