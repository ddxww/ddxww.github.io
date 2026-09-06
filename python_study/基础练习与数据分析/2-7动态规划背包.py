def knapsack(weights,values,capacity):
    n=len(weights)
    dp=[[0 for j in range(capacity+1)] for i in range(n+1)]#创建动态数组
    for i in range(1,n+1):
        for j in range(1,capacity+1):
            if j<=weights[i-1]:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i-1][j-weights[i-1]]+values[i-1])
    return dp[n][capacity]
w=input("输入重量列表:")
v=input("输入价值列表:")
c=int(input("输入容量"))
weights=[int(x) for x in w.split(',')]
value=[int(x) for x in v.split(',')]
res=knapsack(weights,value,c)
print("最大值:",res)