import pandas as pd

df = pd.DataFrame({
    "姓名":["张三","张三","李四","李四"],
    "科目":["语文","数学","语文","数学"],
    "分数":[85,92,78,88]
})
print(df)
# 行=姓名，列=科目，值=分数
res = df.pivot(index="姓名", columns="科目", values="分数")
print(res)
df = pd.DataFrame({
    "部门":["技术","技术","运营","运营"],
    "姓名":["A","B","C","D"],
    "薪资":[8000,9000,7000,7500]
})
print(df)
print(df.groupby(["部门"])["薪资"].sum())
# 规则名	作用
# count	统计非空元素总行数
# size	统计分组总行数（包含空值）
# sum	求和（多用于数值列）
# mean	平均值
# max	最大值
# min	最小值
# median	中位数
# std	标准差
# var	方差
# first	取分组第一条数据
# last	取分组最后一条数据
# nunique	统计不重复值个数（你现在用的）
# unique	返回分组所有不重复值数组
lst=['C','B','A','A']
print(','.join(lst))
print(set(lst))
print(','.join(set(lst)))
print(sorted(lst))
print(sorted(set(lst)))
print(','.join(sorted(set(lst))))

# 创建原始数据
df = pd.DataFrame({
    'user_id': [1, 1, 2, 2, 3],
    'amount': [10, 20, 30, 50, 100]
})

print("原始数据：")
print(df)

# 按 user_id 分组，计算每个用户的平均 amount
# as_index=False 让 user_id 保持为普通列
result = df.groupby(
    'user_id',
    as_index=False
).agg(
    average_amount=('amount', 'mean')
)

print("\n分组结果：")
print(result)
