array = [3,34,4,12,5,2]
target = 46

def subsetsum(array,target,n):
    if target == 0:
        return True
    elif n==0 and target!=0:
        return False
    
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
        return subsetsum(array,target,n-1) or subsetsum(array,target-array[n-1],n-1)
    else:
        return subsetsum(array,target,n-1)

print(subsetsum(array,target,len(array)))