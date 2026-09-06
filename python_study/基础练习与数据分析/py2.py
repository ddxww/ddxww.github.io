import numpy as np
arr=np.arange(1,11)
print(arr)
print(arr[::-1])
arr=np.ones(20)
print(arr)
arr=arr.reshape(4,5)
print(arr)
random_array = np.random.random((3, 3, 3))
print(random_array)
arr = np.random.randint(1, 11, 10)
print(arr)
print(np.max(arr))
print(np.min(arr))
print(np.sum(arr))
print(np.average(arr))
print(np.std(arr))
print(np.var(arr))
print(arr[arr%2==1])
arr=np.arange(1,101,5)
print(arr)
arr=arr.astype(int)
print(arr)
arr=np.random.randint(1,11,10)
print(arr[(arr > 3) & (arr < 8)])
mask = (arr > 3) & (arr < 8)  # 生成布尔掩码
arr[mask] = -arr[mask]
print(arr[mask])
arr = np.array([1, 2, 3, 4, 5])
n=len(arr)
new_len=2*n-1
new_arr=np.zeros(new_len,dtype=int)
new_arr[0:new_len:2] = arr
print(new_arr)
arr=np.random.random((5,5))
print(arr)
arr[[0, 1]] = arr[[1, 0]]
print(arr)

arr=np.ones(10,dtype=int)*2
print(arr)
arr[4]=1
print(arr)

arr=np.random.random(10)
print(arr)
print(np.sum(arr))

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
arr[arr%2==1]=-1
print(arr)

a=np.arange(12).reshape(4,3)
b=np.arange(12,24).reshape(4,3)
c=np.hstack((a, b))
d=np.vstack((a,b))
print(c)
print(d)

a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
print(a[a==b])

#%% md
a=np.array([7,2,10,2,7,4,9,4,9,8])
mask=(a>=5)&(a<=10)
print(mask)
print(a[mask])
