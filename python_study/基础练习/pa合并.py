import pandas as pd
import numpy as np

# 生成与行数匹配的数组（5行）
data1 = pd.DataFrame({
    '姓名': ['A', 'B', 'C', 'D', 'E'],
    '学校': ['一中', '二中', '一中', '一中', '一中'],
    '数学': [np.random.randint(70,100)  for _ in range(5)],
    '政治': [np.random.randint(70,100)  for _ in range(5)]
})
data2 = pd.DataFrame({
    '姓名': ['A', 'B', 'E', 'F', 'G'],
    '学校': ['一中', '二中', '一中', '一中', '一中'],
    '语文': [np.random.randint(70,100) for _ in range(5)],
    '历史': [np.random.randint(70,100) for _ in range(5)]
})

result1 = pd.merge(data1, data2, on='姓名', how='left')
print(result1)
result1 = pd.merge(data1, data2, on=['姓名','学校'], how='left')
print(result1)
result1=pd.merge(data1,data2[['姓名','语文']],on='姓名',how='left')
print(result1)
import pandas as pd

# 创建示例数据
data = {
    '班级': ['一班', '一班', '二班', '二班', '一班', '二班'],
    '姓名': ['张三', '李四', '王五', '赵六', '孙七', '周八'],
    '科目': ['数学', '数学', '数学', '语文', '语文', '语文'],
    '分数': [85, 92, 78, 90, 88, 76]
}
df = pd.DataFrame(data)
print("原始数据：")
print(df)
# 1. 按“班级”分组，计算每个班级的平均分
class_group = df.groupby('班级')  # 按班级分组
class_mean = class_group['分数'].mean()  # 对每个组的“分数”列求均值
print("每个班级的平均分：")
print(class_mean)
# 2. 按“班级”和“科目”多列分组，计算每个组的最高分和最低分
class_subject_group = df.groupby(['班级', '科目'])  # 先按班级、再按科目分组
class_subject_stats = class_subject_group['分数'].agg(['max', 'min'])  # 同时求最大、最小值
print("每个班级各科目的最高分和最低分：")
print(class_subject_stats)
import pandas as pd

# 示例数据：班级、科目、分数
data = {
    '班级': ['一班', '一班', '二班', '二班', '一班', '二班'],
    '科目': ['数学', '数学', '数学', '语文', '语文', '语文'],
    '分数': [85, 92, 78, 90, 88, 76]
}
df = pd.DataFrame(data)
# 创建数据透视表：按班级（行）和科目（列），计算分数的平均值
pivot = pd.pivot_table(
    data=df,
    index='班级',    # 行：按班级分组
    columns='科目',  # 列：按科目分组
    values='分数',   # 计算对象：分数列
    aggfunc='mean'  # 聚合方式：求平均值
)

print("数据透视表结果：")
print(pivot)
import pandas as pd

# 销售单数据：每一行是一次销售记录
data = {
    '单品编码': [1001, 1001, 1002, 1002, 1002, 1003],  # 商品的唯一编码
    '销量(千克)': [2, 4, 1, 3, 2, 5]  # 每次销售的数量
}
df2 = pd.DataFrame(data)
print("原始销售单数据 df2：")
print(df2)
group_by = df2.groupby('单品编码')['销量(千克)'].agg('mean')
print("\n分组计算后的平均销量 group_by：")
print(group_by)
import pandas as pd

# 创建示例数据
data = {
    '销售日期': ['2021-01-01', '2021-01-01', '2021-01-02', '2021-01-02', '2021-01-01', '2021-01-02'],
    '分类名称': ['A', 'B', 'A', 'B', 'A', 'B'],
    '成本定价项': [5.0, 8.0, 6.0, 9.0, 5.5, 9.5]
}

df = pd.DataFrame(data)

# 查看原始数据
print("原始数据：")
print(df)

# 按 '销售日期' 和 '分类名称' 分组，计算 '成本定价项' 的平均值，并使用 unstack() 将 '分类名称' 转换为列
price_sum = df.groupby(['销售日期', '分类名称'])['成本定价项'].agg('mean').unstack()

# 查看结果
print("\n聚合后并转置（unstack）后的数据：")
print(price_sum)
price_sum = df.groupby(['销售日期'])['成本定价项'].agg('mean')
print(price_sum)
price_sum = df.groupby(['分类名称'])['成本定价项'].agg('mean')
print(price_sum)
