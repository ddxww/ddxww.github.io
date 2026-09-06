import random
a=12
print(a)
print(f"hello{a}")
print("abcd",end="")#输出不换行
b=str(a)
c=float(a)
print(b)
print(c)
d=random.randint(1,100)#整数
print(d)
d=random.uniform(1,100)#小数
print(d)
d=random.random()#0到1的小数
print(d)
a="my name is xxx"
a=a[:5]
print(a)
a=a[1:5]
print(a)
a=a[1:5:2]
print(a)
a="my name is xxx"
print(a)
arr=a.split(" ")
print(arr)
string="-".join(arr)
print(string)
print(int(3.14159)==float(3))
print(float(3))