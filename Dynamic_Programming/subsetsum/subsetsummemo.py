array = [3,34,4,12,5,2]
target = 41
n=len(array)
memo = [[-1 for i in range(target+1)] for j in range(n+1)]

def subsetsum(memo,array,target,n):
    if target == 0:
        return True
    elif n==0 and target!=0:
        return False
    
    if memo[n][target]!=-1:
        return memo[n][target]

    if array[n-1] <= target:
        '''
        if subsetsum(array,target-array[n-1],n-1):
            return True
        if subsetsum(array,target,n-1):
            return True
        else:
            return False
        '''
        print(n,target)
        memo[n][target] = subsetsum(memo,array,target,n-1) or subsetsum(memo,array,target-array[n-1],n-1)
        return memo[n][target]
    else:
        memo[n][target] = subsetsum(memo,array,target,n-1)
        return memo[n][target]

print(subsetsum(memo,array,target,len(array)))