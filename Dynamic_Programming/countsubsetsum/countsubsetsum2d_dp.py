array = [1,2,5]
target = 5
n=len(array)
memo = [[0 for i in range(target+1)] for j in range(n+1)]

for i in range(n+1):
    memo[i][0] = 1

for i in range(1,n+1):
    for j in range(1,target+1):
        if array[i-1] <= j:
            memo[i][j] = memo[i-1][j] + memo[i-1][j-array[i-1]]
        else:
            memo[i][j] = memo[i-1][j]
print(memo[n][target])