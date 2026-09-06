# import numpy as np
# import matplotlib.pyplot as plt
# x=np.arange(-10,10,0.1)#-10到10每隔0.1一个点
# y1=x
# y2=x**2
# plt.figure()
# plt.title("1")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.plot(x,y1,label="y=x")
# # plt.legend()#加标签
# # plt.show()
# # plt.title("2")
# # plt.xlabel("x")
# # plt.ylabel("y")
# plt.plot(x,y2,label="y=x^2")
# plt.legend()
# plt.show()
import numpy as np
import matplotlib.pyplot as plt
p=10000#总共投放的点数
r=1
x0,y0=1,1
n=0
plt.figure()
plt.title("for pi")
plt.xlabel("x")
plt.ylabel("y")
for i in range(p):
    px=np.random.rand()*2#np.random.rand()随机生成0到1的数字
    py=np.random.rand()*2
    if(px-x0)**2+(py-y0)**2<r**2:
        plt.plot(px,py,marker='.',color='b')
        n=n+1
    else:
        plt.plot(px,py,marker='.',color='r')
plt.axis('equal')#横纵坐标单位相同便于观察
plt.show()
s=(n/p)*4
print(s)
