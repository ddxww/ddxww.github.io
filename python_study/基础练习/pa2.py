import numpy as np

# 创建一维数组
array1 = np.array([1, 2, 3, 4, 5])
print(array1)

# 创建二维数组
array2 = np.array([[1, 2, 3], [4, 5, 6]])
print(array2)

# 创建全零数组
zeros = np.zeros((3, 3))
print(zeros)

# 创建全一数组
ones = np.ones((3, 3))
print(ones)

# 创建随机数组
random_array = np.random.random((3, 3))
print(random_array)

# 数组切片
print(array2[:, 1])

# 数组索引
print(array2[1, 2])

# 数组加法
print(array1 + array1)

# 数组乘法
print(array1 * 2)

# 数组矩阵乘法
print(np.dot(array2, array2.T))
