import numpy as np
import pa1 as pd
from scipy import linalg
# arr_2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(np.mean(arr_2d,axis=0))
# summ=np.cumsum(arr_2d,axis=1)
# print(summ)
# eigenvalues=np.array([3,1,4,2])
# eigenvectors=np.array([
#     [1,0,0,1],
#     [0,1,0,1],
#     [0,0,1,1],
#     [1,1,1,1]
# ])
# eigenvalues=eigenvalues[::-1]
# print(eigenvalues)
# eigenvectors=eigenvectors[:, ::-1]
# print(eigenvectors)



df=pd.read_excel('棉花产量数据.xlsx',usecols='C:F')
print(df)
x=df.to_numpy()
print(x)
X=(x-np.mean(x,axis=0))/np.std(x,ddof=1,axis=0)#标准化
R=np.cov(X.T)
eigenvalues,eigenvectors=linalg.eigh(R)#计算特征值和特征向量
eigenvalues=eigenvalues[::-1]
eigenvectors=eigenvectors[:, ::-1]
contribution_rate=eigenvalues/sum(eigenvalues)
cum_contribution_rate=contribution_rate.cumsum()
print("特征值")
print(eigenvalues)
print("贡献率为")
print(contribution_rate)
print("累计贡献率为")
print(cum_contribution_rate)
print("对应特征向量矩阵")
print(eigenvectors)