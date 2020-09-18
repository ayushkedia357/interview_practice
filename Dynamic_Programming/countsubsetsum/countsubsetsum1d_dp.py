array = [1,2,3,4,5]
target = 5
n=len(array)
memo = [0 for i in range(target+1)]

memo[0] = 1

for i in array:
    dp = [] + memo
    for j in range(i,target+1):
        memo[j] = memo[j] + dp[j-i]
print(memo[target])