t1 = "abcdxyz"
t2 = "xyzabcd"


m = len(t1)
n = len(t2)
memo = [[0 for i in range(n+1)]for j in range(m+1)]

res = 0

for i in range(1,m+1):
    for j in range(1,n+1):
        if t1[i-1] == t2[j-1]:
            memo[i][j] = 1 + memo[i-1][j-1]
            res = max(res,memo[i][j])
        else:
            memo[i][j] = 0

print(res)