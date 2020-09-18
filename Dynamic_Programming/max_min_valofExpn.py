n = 2
m = 2
arr = [1,2,3,4]
tot = sum(arr)
length = n+m
memo1 = [[-1 for i in range(tot+1)] for j in range(length+1)]
memo2 = [[-1 for i in range(tot+1)] for j in range(length+1)]
'''
def minexprn(arr,length,n,tot,currtot):
    if n==0 and currtot != 0:
        return currtot * (tot - currtot)
    elif length == 0 and n!=0:
        return 2**31 - 1 
    
    return min(minexprn(arr,length-1,n-1,tot,currtot + arr[length - 1]) , minexprn(arr,length-1,n,tot,currtot))

def maxexprn(arr,length,n,tot,currtot):
    if n==0 and currtot != 0:
        return currtot * (tot - currtot)
    elif length == 0 and n!=0:
        return 0
    
    return max(maxexprn(arr,length-1,n-1,tot,currtot + arr[length - 1]) , maxexprn(arr,length-1,n,tot,currtot))

arr = [1,2,3,4]
n=2 -- n=1 -> 0
len = 4 ->3 ->2 ->1->0
currsum = 0 + 4 + 3 = 7
2ndsubset = 10 - 7 =3
return 7*3 = 21

if n==0:
    return currsum * (tot - currsum)
if len == 0 and n!=0:
    return -1





'''

def minexprn(memo1,arr,length,n,tot,currtot):
    if n==0 and currtot != 0:
        return currtot * (tot - currtot)
    elif length == 0 and n!=0:
        return 2**31 - 1

    if memo1[length][currtot] != -1:
        return memo1[length][currtot]
    
    memo1[length][currtot] = min(minexprn(memo1,arr,length-1,n-1,tot,currtot + arr[length - 1]) , minexprn(memo1,arr,length-1,n,tot,currtot))
    return memo1[length][currtot]

def maxexprn(memo2,arr,length,n,tot,currtot):
    if n==0 and currtot != 0:
        return currtot * (tot - currtot)
    elif length == 0 and n!=0:
        return 0

    if memo2[length][currtot] != -1:
        return memo2[length][currtot]

    memo2[length][currtot] = max(maxexprn(memo2,arr,length-1,n-1,tot,currtot + arr[length - 1]) , maxexprn(memo2,arr,length-1,n,tot,currtot))
    return memo2[length][currtot]

print( minexprn (memo1 , arr , length , n , tot , 0 ) , maxexprn(memo2,arr,length,n,tot,0) )
