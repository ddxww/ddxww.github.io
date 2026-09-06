import numpy as np
# f=[2,3,5,1,4,2,3,6,5]
# g=[1/3,1/3,1/3]
# print(f)
# print(g)
# print(np.convolve(f,g))
# print(np.convolve(f,g,mode='vaild'))

import torch
import matplotlib.pyplot as plt
# 卷积层的定义和应用测试
# 1.读取图片
img=plt.imread('duck.jpg')
print(img.shape)

# 2.将图片数据调整为卷积层输入特征图对应的形状
input=torch.tensor(img).permute(2,0,1).float()
print("输入特征的形状：",input.shape)

# 3.定义卷积层
conv=torch.nn.Conv2d(in_channels=3,out_channels=3,kernel_size=9,stride=3,padding=0,bias=False)

# 4.前向传播，将卷积层运用到输入特征图上
output=conv(input)
print("输出特征的形状：",output.shape)

# 5.将输出特征图转换为图片数据
output=torch.clamp(output.int(),0,255)
output=output.permute(1,2,0).detach().numpy()
print(output.shape)

# 显示图片进行对比
fig,ax=plt.subplots(1,2,figsize=(10,5))
ax[0].imshow(img)
ax[1].imshow(output)
plt.show()