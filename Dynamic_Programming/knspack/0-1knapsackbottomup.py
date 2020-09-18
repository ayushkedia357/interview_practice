wt = [1,2,3]
val = [6,10,12]
W = 5
n=len(wt)
memo = [[0 for i in range(W+1)] for j in range(n+1)]

for i in range(1,n+1):
    for j in range(1,W+1):
        if wt[i-1] <= j:
            memo[i][j] = max(val[i-1] + memo[i-1][j-wt[i-1]],memo[i-1][j])
        else:
            memo[i][j] = memo[i-1][j]
            
print(memo[n][W])
