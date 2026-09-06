import pa1 as pd
from matplotlib.pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False
data = {
    'state': ['a', 'b', 'c', 'd'],
    'year': [1991, 1992, 1993, 1994],
    'pop': [6, 7, 8, 9]
}
df = pd.DataFrame(data)
df.index = ['A', 'B', 'C', 'D']
df.index.name = '索引'
print(pd.DataFrame(data))
print(df.to_csv(sep='\t', na_rep='nan'))  # 使用制表符对齐列
df.loc['E'] = ['e', 1995, 10]
print(df)
df=df.drop('E')
print(df)
df['port'] = 1
# 正确写法：使用括号明确分组，并使用布尔索引
filtered_df = df[(df['year'] == 1991) | (df['year'] == 1994)]
print(filtered_df)
subset=df[['state','pop']]
print(subset)
df['pop']=df['pop']*2
print(df)

# 前面的数据处理步骤不变...
pd.set_option('display.max_columns', None)  # 显示所有列，不省略
pd.set_option('max_colwidth', 100)  # 列宽足够显示长名称（可根据需要调大）
pd.set_option('display.width', 3000)  # 表格总宽度足够宽，避免换行
hotel = pd.read_excel("香港酒店数据.xlsx", header=0, skiprows=[1])
hotel = hotel.drop(columns=hotel.columns[0])
hotel.columns = ['名字', '类型', '城市', '地区', '地点', '评分', '价格', '评分人数']
hotel = hotel.dropna(how='all').reset_index(drop=True)
print(hotel)
print(hotel[(hotel['类型'] == '浪漫情侣') & ( hotel['地区'] =='湾仔')] )
print(hotel[((hotel['地区'] == '观塘') | (hotel['地区'] == '油尖旺')) & (hotel['评分'] > 4)] )
missing_data = hotel[hotel.isna().any(axis=1)]
print(missing_data)
hotel['类型'] = hotel['类型'].fillna('其他')
hotel['地区'] = hotel['地区'].fillna('其他')

hotel.dropna()
hotel['评分']=hotel['评分'].fillna(hotel['评分'].mean())
hotel=hotel.dropna(subset=['价格', '评分人数'])
hotel.to_excel("酒店数据1.xlsx", index=False)




