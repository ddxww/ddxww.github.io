import numpy as np
print(np.random.randint(1,6,(5,8)))#1到5打出5*8的矩阵
print(np.random.randint(1,6,))#打出1到5随机数
n=100000
a=0
b=0
for i in range(n):
    x=np.random.randint(1,4)#随机生成1到3之间的整数x表示汽车出现在门后
    y=np.random.randint(1,4)#1到3表示自己选的门
    if x==y:
        a=a+1
    else:
        b=b+1
print("不改变注意",a/n)
print("改变",b/n)