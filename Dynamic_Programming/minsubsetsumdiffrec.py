arr = [1,2,7]
totsum = sum(arr)
memo = []
def dp(memo,arr,tot,currsum,n):
    if n==0:
        memo.append(currsum)
    dp(memo,arr,tot,currsum + arr[n-1],n-1)
    dp(memo,arr,tot,currsum,n-1)
    
n=len(arr)
dp(memo,arr,totsum,0,n)
mini = -1
memo = set(memo)
for i in memo:
    mini = min(mini,abs(totsum-2*i))

print(mini)


'''
#dp = [0 0 0 0 0 0 0 0 0 0 0 0]
#dp2= [0 0 0 0 0 0 0 0 0 0 0 0]
dp = [False for i in range(totsum+1)]
dp[0] = True
for i in arr:
    dp2 = [] + dp
    for j in range(i,totsum+1):
        dp[j] = dp[j] or dp2[j-i]
    print(dp)
print(dp)
'''