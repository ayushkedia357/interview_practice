t1 = "abcdxyz"

t2 = "xyzabcd"

def lcs(t1,t2,m,n,count,memo):

    #print(t1[:m],t2[:n],count)

    if m==0 or n==0:
        return count
    
    if memo[m][n] != -1:
        return memo[m][n]

    if t1[m-1] == t2[n-1]:
        count = lcs(t1,t2,m-1,n-1,count + 1,memo)
        memo[m][n] = count

    count = max(count , max(lcs(t1,t2,m-1,n,0,memo),lcs(t1,t2,m,n-1,0,memo))) 
    memo[m][n] = count
    return count

m = len(t1)
n = len(t2)
memo = [[-1 for i in range(n+1)]for j in range(m+1)]
print(lcs(t1,t2,m,n,0,memo))