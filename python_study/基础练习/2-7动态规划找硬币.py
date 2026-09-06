def f(x):
    if(x==0):
        return 0
    res=float('inf')
    if x>=2:
        res=min(f(x-2)+1,res)
    if x>=5:
        res=min(f(x-5)+1,res)
    if x>=7:
        res=min(f(x-7)+1,res)
    return res
n=int(input("输入金额"))
print(f(n))
#动态规划
# def coinchange(n):
#     dp=[float('inf')]*(n+1)
#     dp[0]=0
#     for i in range(1,n+1):#左闭右开
#         if i>=2:
#             dp[i] = min(dp[i], dp[i - 2] + 1)
#         if i>=5:
#             dp[i] = min(dp[i], dp[i - 5] + 1)
#         if i>=7:
#             dp[i] = min(dp[i], dp[i - 7] + 1)
#     if dp[i]!=float('inf'):
#         return dp[n]
#     else:
#         return -1
# n=int(input("输入金额"))
# res=coinchange(n)
# print(res)