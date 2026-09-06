import pa1 as pd
import numpy as np
from matplotlib.pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False
hotel=pd.read_excel('酒店数据1.xlsx')
print(hotel)
hotelup=hotel.sort_values('评分',ascending=True)
print(hotelup)
hotellow=hotel.sort_values('评分',ascending=False)
print(hotellow)
hotel_price=hotel.sort_values('价格')
print(hotel_price)
print(hotel[hotel['地区'] == '油尖旺']['价格'].mean())
price_mean = hotel['价格'].mean()
price_var = hotel['价格'].var()
price_max = hotel['价格'].max()
price_min = hotel['价格'].min()
price_median = hotel['价格'].median()

print("\n价格列的统计指标：")
print(f"均值：{price_mean:.2f}")
print(f"方差：{price_var:.2f}")
print(f"最大值：{price_max:.2f}")
print(f"最小值：{price_min:.2f}")
print(f"中值：{price_median:.2f}")
# 计算相关系数（保留两位小数）
correlation = hotel['评分'].corr(hotel['价格']).round(2)
# 计算协方差（保留两位小数）
covariance = hotel['评分'].cov(hotel['价格']).round(2)
print(correlation)
print(covariance)
# 多条件排序（评分降序，价格升序）
hotel_sorted = hotel.sort_values(by=['评分', '价格'], ascending=[False, True])
print(hotel_sorted)
low_rating_hotels = hotel[hotel['评分'] < 3]
# 计算数量和占比（保留两位小数）
total_hotels = len(hotel)
low_rating_count = len(low_rating_hotels)
low_rating_percentage = (low_rating_count / total_hotels) * 100
print(f"{low_rating_count}家")
print(f"{low_rating_percentage:.2f}%")
high_rating_hotels = hotel[hotel['评分'] >= 4]
avg_price=high_rating_hotels['价格'].mean().round(2)
print(avg_price)
# 计算每个地区的酒店数量
region_counts = hotel['地区'].value_counts()
total_counts=len(hotel)
region_percentages=(region_counts / total_counts) * 100
print("各地区酒店占比：")
print(region_percentages)
top20_by_rating_count=hotel.sort_values('评分人数', ascending=False).head(20)
avg_price_top20=top20_by_rating_count['价格'].mean().round(2)
print(avg_price_top20)
# 统计类型数量和地区数量
type_count = hotel['类型'].nunique()
region_count = hotel['地区'].nunique()
print(type_count)
print(region_count)
# 统计各个类型包含的酒店数量
hotels_by_type = hotel['类型'].value_counts()

# 统计各个地区包含的酒店数量
hotels_by_region = hotel['地区'].value_counts()
print(hotels_by_type)
print(hotels_by_region)
# 用一行代码计算每个类型的酒店的评分人数总数量
print(hotel.pivot_table(index='类型', values='评分人数', aggfunc='sum').reset_index().rename(columns={'评分人数':'评分人数总和'}))
# （14）用数据透视表计算每个地区酒店价格和评分的最大值和最小值
print(hotel.pivot_table(index='地区', values=['价格', '评分'], aggfunc=['max', 'min']).reset_index().rename(columns={'max':'最大值','min':'最小值'}))