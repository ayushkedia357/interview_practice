array = [1,2,5]
target = 5
n=len(array)
memo = [[-1 for i in range(target+1)] for j in range(n+1)]

def subsetsum(memo,array,n,target):
    if target == 0:
        return 1
    elif n==0 and target!=0:
        return 0
    
    if memo[n][target] != -1:
        return memo[n][target]
    if array[n-1] <= target:
        print(n,target)
        memo[n][target] = subsetsum(memo,array,n-1,target) + subsetsum(memo,array,n,target - array[n-1])
    else:
        memo[n][target] = subsetsum(memo,array,n-1,target)
    return memo[n][target]

print(subsetsum(memo,array,n,target))