import pandas as pd
import numpy as np
# 创建Series（带索引说明）
data_series = [1, 2, 3, 4, 5]
series = pd.Series(data_series, name="数值序列")  # 给Series命名，方便识别
print("=== 示例Series ===")
print(series)
print()  # 空行分隔输出，更清晰
# 创建DataFrame（人员信息表）
data_frame = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data_frame)
print("=== 示例DataFrame ===")
print(df)
print()
# 选择列（获取姓名列）
print("=== 选择'Name'列 ===")
print(df['Name'])
print()
# 选择行（获取索引为1的行，即第二行数据）
print("=== 选择索引为1的行 ===")
print(df.iloc[1])
print()
# 过滤数据（年龄大于25岁的人员）
print("=== 年龄大于25岁的人员 ===")
print(df[df['Age'] > 25])
print()
# 排序数据（按年龄升序排列）
print("=== 按年龄升序排序 ===")
print(df.sort_values(by='Age'))
print()
# 分组数据（按城市分组，计算年龄的平均值）
# 添加numeric_only=True确保只对数值列（Age）计算均值，避免字符串列报错
print("=== 按城市分组的平均年龄 ===")
print(df.groupby('City')['Age'].mean())  # 更精确：只对Age列计算均值
# 创建带有缺失值的DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, None, 22, 32],
    'City': ['New York', 'Los Angeles', None, 'Houston']
}
df = pd.DataFrame(data)
# 删除包含缺失值的行
df.dropna(inplace=True)
print(df)
# 创建带有缺失值的DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, None, 22, 32],
    'City': ['New York', 'Los Angeles', None, 'Houston']
}
df = pd.DataFrame(data)

# 填充缺失值
df.fillna({'Age': df['Age'].mean(), 'City': 'Unknown'}, inplace=True)
print(df)
# 创建带有重复值的DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Alice'],
    'Age': [24, 27, 22, 32, 24],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'New York']
}
df = pd.DataFrame(data)

# 删除重复值
df.drop_duplicates(inplace=True)
print(df)
# 创建带有不一致格式的DataFrame
data = {
    'Name': ['Alice', 'BOB', 'Charlie', 'david'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data)
print(df)
# 将姓名转换为一致的格式,str.capitalize() 是 Python 中字符串的一个方法，作用是：
# 将字符串的第一个字符转为大写，其余字符转为小写，并返回处理后的新字符串（原字符串不会被修改）。
df['Name'] = df['Name'].str.capitalize()
print(df)
# 创建带有日期的DataFrame
data = {
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03'],
    'Value': [100, 200, 150]
}
df = pd.DataFrame(data)
# 提取日期特征,这句话的作用很简单：把 DataFrame 里名为 'Date' 的列，从原本的字符串（或其他格式）转换成 pandas 能直接处理的 “日期时间类型”
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
print(df)
# 创建DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'Salary': [50000, 60000, 55000, 65000]
}
df = pd.DataFrame(data)

# 计算均值
print(df['Age'].mean())

# 计算中位数
print(df['Salary'].median())

# 计算方差
print(df['Age'].var())
from scipy import stats

# 创建样本数据
sample1 = [24, 27, 22, 32, 28]
sample2 = [25, 29, 21, 30, 26]

# 进行独立样本t检验
t_stat, p_value = stats.ttest_ind(sample1, sample2)
print(f"T-statistic: {t_stat}, P-value: {p_value}")

import matplotlib.pyplot as plt

# 创建数据
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
values = [100, 120, 150, 130, 170]

# 绘制折线图
plt.plot(months, values)
plt.title('Monthly Values')
plt.xlabel('Month')
plt.ylabel('Value')
plt.show()

# 绘制柱状图
plt.bar(months, values)
plt.title('Monthly Values')
plt.xlabel('Month')
plt.ylabel('Value')
plt.show()
# 例：
# train.shape     # 原始数据, 891行, 12列
#
# # 方式1: 删除缺失值
# # 删除缺失值会损失信息，并不推荐删除，当缺失数据占比较低的时候，可以尝试使用删除缺失值
# # 按行删除: 删除包含缺失值的记录
# # train.dropna().shape        # 默认按行删(该行只要有空值, 就删除该行), 结果为: 183行, 12列
# train.loc[:10].dropna()       # 获取前11行数据, 删除包含空值的行. 
#
# # any: 只要有空值就删除该行|列, all: 该行|列 全为空才删除  subset: 参考哪些列的空值.  inplace=True 在原表修改
# train.dropna(subset=['Age'], how='any')
#
# # 该列值只要有空, 就删除该列值.
# train.dropna(how='any', axis=1)  # 0(默认): 行,  1: 列
#
# train.isnull().sum() # 快速计算是否包含缺失值
