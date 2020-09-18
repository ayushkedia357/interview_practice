array = [3,34,4,12,5,2]
target = 46
n = len(array)

dp = [[0 for i in range(target+1)] for j in range(n+1)]

for i in range(n+1):
    dp[i][0] = True
for i in range(1,target+1):
    dp[0][i] = False

for i in range(1,n+1):
    for j in range(1,target+1):
        if array[i-1] > j:
            dp[i][j] = dp[i-1][j]
        else:
            ret = dp[i-1][j] or dp[i-1][j-array[i-1]]
            dp[i][j] = ret
#print(dp)
print(dp[n][target])
