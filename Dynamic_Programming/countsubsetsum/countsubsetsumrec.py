array = [1,2,5]
target = 5

def subsetsum(array,n,target):
    if target == 0:
        return 1
    elif n==0 and target!=0:
        return 0
    
    if array[n-1] <= target:
        '''
        print(n,target)
        if subsetsum(array,target-array[n-1],n-1):
            return True
        if subsetsum(array,target,n-1):
            return True
        else:
            return False
        '''
        print(n,target)
        return subsetsum(array,n-1,target) + subsetsum(array,n,target - array[n-1])
    else:
        return subsetsum(array,n-1,target)
n=len(array)
print(subsetsum(array,n,target))