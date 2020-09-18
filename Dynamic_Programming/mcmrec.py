arr = [40,20,30,10,30]

def mcm(arr,i,j,memo):
    if i>=j:
        return 0
    if memo[i][j] != -1:
        return memo[i][j]
    mini = 2**31 - 1
    print(arr[i-1:j+1])
    for k in range(i,j):
        temp = mcm(arr,i,k,memo) + mcm(arr,k+1,j,memo) + arr[i-1]*arr[k]*arr[j]

        mini = min(mini,temp)
    memo[i][j] = mini
    return mini
n = len(arr)
memo = [[-1 for i in range(n)]for j in range(n)]
print(mcm(arr,1,n-1,memo))
### memoization and dp for this qs is same.
