import numpy as np

#定义转换函数：
def f_1(A):#极小型->极大型
    x = np.max(A)
    for i in range(0,A.shape[0]):
        A[i] = x-A[i]
    return A

def f_2(A,a):#中间型->极大型
    x = np.max(np.abs(A-a))
    for i in range(0,A.shape[0]):
        A[i] = 1-np.abs(A[i]-a)/x
    return A

def f_3(A,a,b):#区间型->极大型
    u = a-np.min(A)
    v = np.max(A)-b
    M = v
    if u>=v:
        M=u
    for i in range(0,A.shape[0]):
        if A[i]<=a:
            A[i] = 1-(a-A[i])/M
        elif A[i]>=b:
            A[i] = 1-(A[i]-b)/M
        else:
            A[i] = 1
    return A

#定义标准化函数：
def standardize(A):
    for j in range(0,A.shape[1]):
        sum = 0
        for i in range(0,A.shape[0]):
            sum = sum+A[i][j]**2
        for i in range(0,A.shape[0]):
            A[i][j] = A[i][j]/np.sqrt(sum)
    return A

#定义打分函数：
def score(Z):
    Z = np.transpose(Z)
    Z_max = []
    Z_min = []
    for j in range(0,Z.shape[0]):
        Z_max.append(np.max(Z[j]))
        Z_min.append(np.min(Z[j]))
    S = []
    for i in range(0,Z.shape[1]):
        sum1 = 0
        for j in range(0,Z.shape[0]):
            sum1 = sum1+(Z[j][i]-Z_max[j])**2
        D1 = np.sqrt(sum1)
        sum2 = 0
        for j in range(0,Z.shape[0]):
            sum2 = sum2+(Z[j][i]-Z_min[j])**2
        D2 = np.sqrt(sum2)
        S.append(D2/(D1+D2))
    return S

#归一化函数：
def g(S):
    S = np.array(S)
    sum = 0
    for i in range(0,S.shape[0]):
        sum = sum+S[i]
    for i in range(0,S.shape[0]):
        S[i] = S[i]/sum
    return S

def main():
    A = np.array([[28,19,3,5,3,3,8],
                  [1806,3180,3080,2560,3551,3309,3139],
                  [11.2,7.98,8.12,5.29,4.3,5.68,6.58],
                  [0.67,0.71,0.75,0.76,0.874,0.92,0.708],
                  [17413,11770,9081,11566,8295,9143,9556],
                  [0.823,0.741,0.804,0.7947,0.851,0.754,0.8676],
                  [0.112,0.111,0.1,0.091,0.071,0.058,0.067]])
    A[1] = f_2(A[1],2500)
    A[3] = f_2(A[3],0.74)
    A[6] = f_2(A[6],0.105)
    B = np.transpose(A)
    Z = standardize(B)
    S = score(Z)
    S1 = g(S)
    print(S1)

main()

