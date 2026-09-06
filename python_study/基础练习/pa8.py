import pandas as pd
import numpy as np
# 采用pandas库的DataFrame构造数据集
data = pd.DataFrame({
    '学号': [1, 2, 3, 4, 5, 6, 7, 7, 8],
    '身高': [172.0, 162.0, 175.0, 170.0, 168.0, 160.0, 164.0, 164.0, 160.0],
    '体重': [70, 62, 75, 68, 67, 58, 64, 64, 53]
})
# 查看数据集内容
print(data)
# 检测重复行，返回布尔序列标记是否重复
data.duplicated()
# 按学号作为判断是否重复的依据，重复行保留第一行，直接在原数据上删除重复行
# 'first' 表示重复的行中，除了第一行，其余删除；若为 'last' 则保留最后一行
# inplace=True 表示直接修改 data 变量，若为 False 则不修改原数据，返回删除重复后的新数据
print(data.duplicated())
data.drop_duplicates(subset=['学号'], keep='first', inplace=True)

data = pd.DataFrame({
    '学号': [1, 2, 3, 4, 5, 6, 7, 7, 8],
    '身高': [172.0, 162.0, 175.0, np.nan, 168.0, 160.0, 164.0, 164.0, 160.0],
    '体重': [70, 62, 75, 68, 67, 58, 64, 64, 53]
})
print(data)
data1=data.dropna()
print(data1)
data2=data.fillna(170.0)
print(data2)
data3=data.fillna(data.mean(),inplace=False)
print(data3.round(1))


import numpy as np
from sklearn import preprocessing

# 构造原始数据
X = np.array([[2, 2, -1],
              [1, 2, -2],
              [0, -2, 2]])
print("原始数据 X：")
print(X)

# 1. 最大值最小值归一化（Min-Max Scaling）
scaler_minmax = preprocessing.MinMaxScaler()
X_processing_minmax = scaler_minmax.fit_transform(X)
print("\n最大值最小值归一化结果：")
print(X_processing_minmax)

# 2. 均值方差归一化（标准化，Standard Scaling）
scaler_standard = preprocessing.StandardScaler()
X_processing_standard = scaler_standard.fit_transform(X)  # 正确的变量名
print("\n均值方差归一化（标准化）结果：")
print(X_processing_standard)  # 这里修正了拼写错误

# 3. 验证归一化后的数据方差（以标准化为例）
print("\n标准化后数据的方差：")
print(X_processing_standard.var(axis=0))
# 创建包含缺失值的DataFrame
data = pd.DataFrame({
    'A': [1, np.nan, 3, None],
    'B': [np.nan, 5, 6, 7],
    'C': [8, 9, 10, 11]
})
# 检测缺失值
print(data.isnull())