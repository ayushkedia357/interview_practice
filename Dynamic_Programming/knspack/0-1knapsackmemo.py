wt = [10,20,30]
val = [60,100,120]
W = 45
n=len(wt)
memo = [[-1]*(W+1)]*(n+1)

def knapsack(memo,wt,val,n,W):
    if n == 0 or W = 0:
        return 0
    if memo[n][W]!=-1:
        return memo[n][W]
    if W >= wt[n-1]:
        memo[n][W] = max( val[n-1] + knapsack(memo,wt,val,n-1,W-wt[n-1]) , knapsack(memo,wt,val,n-1,W) )
        return memo[n][W]
    else:
        memo[n][W] = knapsack(memo,wt,val,n-1,W)
        return memo[n][W]

print(knapsack(memo,wt,val,n,50))     