import torch
import numpy as np
import matplotlib.pyplot as plt
from torch import LongTensor, dtype

# def f(x):
#     return x**2+x
# X=np.array([[0,1,2],[3,4,5],[6,7,8]])
# print(f(X))

# Z = np.zeros((5,5), [('x',float),('y',float)])
# Z['x'], Z['y'] = np.meshgrid(np.linspace(0,1,5),np.linspace(0,1,5))
# print(Z)
# z=Z['x']**2+Z['y']**2
# plt.contourf(Z['x'],Z['y'],z)
# plt.show()

# x=np.arange(-10,10,0.01)
# y=np.arange(-5,5,0.01)
# X,Y = np.meshgrid(x,y)
# z = X**2 + Y**2
# plt.contourf(x,y,z)
# plt.show()
# faces = np.array([
#     [1, 2, 3],
#     [4, 5, 6]
# ])
# print(np.roll([[0],[1],[2],[3]],1,axis=0))#按列滚动
# print(np.roll([[0,1,2,3]],1,axis=1))#按行滚动
# print(np.array([[1, 2, 3, 4]]).repeat(2, axis=1))#横向重复
# print(np.array([[1, 2, 3, 4]]).repeat(2, axis=0))#纵向重复
#
# print(faces.repeat(2, axis=1))
# F = np.roll(faces.repeat(2, axis=1),0, axis=1)
# print(F)
# print(np.logspace(1, 3, 3,base=2))
# Z=np.random.randint(0,10,size=(5,5))
# print(Z)
# tensor1=torch.randn(10)
# print(tensor1)
# print(tensor1.data)
# a=(10,20)
# print(a)
# print(a[0],a[1])
# num_dict={1:"10",2:20,3:30,4:40,5:50,6:60,7:70,8:80}
# tensor=torch.Tensor([1,2,3])
# print(tensor[2].item())
# tensor=torch.IntTensor([1,2,3]).to(torch.int64)
# print(tensor)
# print(tensor[0])
# print(tensor[0].item())
# print(num_dict.items())
# print(num_dict.get(10,'hajimi'))
# print(LongTensor([[1]]))
# print(LongTensor(2,2))
# print(LongTensor(2))
# s = "  hello world \n"
# print(s)
# res = s.strip()
# print(repr(res)) # 'hello world'
# s = "  hello world \t"
# print(s)
# res = s.strip()
# print(repr(res)) # 'hello world'
# a=[[1,2],[3,4],[5,6]]
# for idx,(x,y)in enumerate(a):
#     print(idx,x,y)

