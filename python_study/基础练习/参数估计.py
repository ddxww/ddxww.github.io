import numpy as np
from scipy.stats import t,sem
d=np.array([506,508,449,503,504,510,497,512,514,505,493,496,506,502,509,496])
d=d.flatten()#转为一维数组
n=len(d)
xb=d.mean()
s=d.std()
sm=sem(d)
a=0.05
ta=t.ppf(1-a/2,n-1)
L=[xb-sm*ta,xb+sm*ta]
print(np.round(L,4))
import numpy as np
from scipy.stats import ttest_1samp
from scipy.stats import norm

alpha = 0.05; sigma = 4.2
a = np.array([26.01, 26.00, 25.98, 25.86, 26.32, 25.58, 25.32, 25.89, 26.32, 26.18])
t, p = ttest_1samp(a, 26)
xb = a.mean(); s = a.std(ddof=1)
z = t * s / sigma  # 转换为 z 统计量
za = norm.ppf(1-alpha/2, 0, 1)  # 求上 alpha/2 分位数
print('Z 统计量值：', z)
print('p 值：', p)
print('分位数：', za)

import numpy as np
from scipy.stats import t
from scipy.stats import ttest_1samp

# 直接用 np.array 传入数据
a = np.array([159, 280, 101, 212, 224, 379, 179, 264, 222, 362, 168, 250, 149, 260, 485, 170])
x=a.mean()
s=a.std(ddof=1)
n=len(a)
ta=t.ppf(0.95,n-1)
za = norm.ppf(1-alpha/2, 0, 1)
ts, p = ttest_1samp(a, 225, alternative='greater')  # 进行单侧 t 检验
print('t 统计量值:', ts)

import numpy as np
from scipy.stats import t
from scipy.stats import ttest_ind

# 方法A的数据
a = np.array([79.98, 80.04, 80.02, 80.03, 80.03, 80.04, 80.03, 80.04, 80.03, 80.02, 80.00, 80.02])
# 方法B的数据
b = np.array([80.02, 79.94, 79.98, 79.97, 79.97, 80.03, 79.95, 79.97])

# 调用库函数进行两独立样本t检验（单侧，alternative='greater'表示检验a的均值是否大于b的均值）
tstat, p = ttest_ind(a, b, alternative='greater')
print('检验统计量为:', tstat)
print('p值为:', p)

# 下面是编程计算部分
n1 = len(a)
n2 = len(b)
xa = a.mean()
sa2 = a.var(ddof=1)  # 计算样本方差（无偏，除以n-1）
xb = b.mean()
sb2 = b.var(ddof=1)
ta = t.ppf(0.95, n1 + n2 - 2)  # 计算t分布的分位数，对应置信水平0.95，自由度n1+n2-2
ts = (xa - xb) / (np.sqrt(((n1 - 1) * sa2 + (n2 - 1) * sb2) / (n1 + n2 - 2)) * np.sqrt(1 / n1 + 1 / n2))
print('检验统计量为:', ts)

import numpy as np
from scipy.stats import t

# 样本数据（灯泡寿命，单位：h）
data = np.array([1050, 1100, 1120, 1250, 1280])

# 计算基本统计量
n = len(data)  # 样本量
x_bar = np.mean(data)  # 样本均值
s = np.std(data, ddof=1)  # 样本标准差（ddof=1表示无偏估计）
df = n - 1  # 自由度
sm=sem(data)
# 置信水平90%，计算t临界值
confidence_level = 0.90
alpha = 1 - confidence_level
t_critical = t.ppf(1 - alpha/2, df)  # 双侧检验的t临界值

# 计算边际误差
margin_error = t_critical * sm

# 计算置信区间
lower_bound = x_bar - margin_error
upper_bound = x_bar + margin_error

# 输出结果
print(f"样本数据: {data}")
print(f"样本均值: {x_bar:.2f}")
print(f"样本标准差: {s:.2f}")
print(f"自由度: {df}")
print(f"90%置信水平对应的t临界值: {t_critical:.4f}")
print(f"边际误差: {margin_error:.2f}")
print(f"90%置信区间: ({lower_bound:.0f}, {upper_bound:.0f})")