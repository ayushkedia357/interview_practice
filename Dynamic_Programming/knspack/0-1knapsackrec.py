wt = [10,20,30]
val = [60,100,120]
W = 45
profit = 0
def knapsack(wt,val,n,W):
    if n == len(wt) or W <= 0:
        return W
    
    if W >= wt[n]:
        return max( val[n] + knapsack(wt,val,n+1,W-wt[n]) , knapsack(wt,val,n+1,W) )
    else:
        return knapsack(wt,val,n+1,W)

print(knapsack(wt,val,0,50))     