import numpy as np
import pandas as pd
def sigma_detection(ser, sigma=3):
    '''
    ser参数：被检测的数据（Series）
    sigma参数：σ的倍数（默认3，可调整为2使阈值更严格）
    返回：异常值及其索引
    '''
    mean_data = ser.mean()
    std_data = ser.std()
    # 计算上下限
    lower_bound = mean_data - sigma * std_data
    upper_bound = mean_data + sigma * std_data
    # 筛选异常值
    outliers = ser[(ser < lower_bound) | (ser > upper_bound)]
    # 打印计算过程（方便理解）
    print(f"均值: {mean_data:.2f}")
    print(f"标准差: {std_data:.2f}")
    print(f"{sigma}σ范围: [{lower_bound:.2f}, {upper_bound:.2f}]")
    return outliers
value = [86, 67, -100, 62, 79, 84, 200, 82, 80, 90, 72, 79, 79, 75, 71, 79]
ser = pd.Series(value)
# 用2σ检测（更严格，能同时识别-100和200）
print("使用2σ检测结果：")
outliers = sigma_detection(ser, sigma=2)
print("\n异常值（索引: 值）：")
print(outliers)

np.random.seed(0)
a1=np.random.normal(85,10,20)
s1=pd.DataFrame(a1,columns=['X'],index=range(1,21))
print(s1)
np.where(a1>100,np.nan,a1)
df=s1.where(s1<=100)#小等于100
print(df)
from matplotlib import pyplot as plt
plt.plot(s1.query('X<=100'),'bo')
plt.plot(s1.query('X>100'),'ro')
plt.show()
ss=s1.query('X<X.mean()+3*X.std() and X>X.mean()-3*X.std()')
print(ss)

