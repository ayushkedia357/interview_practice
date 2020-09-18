def root(arr,p):
    while(arr[p]!=p):
        p=arr[p]
    return p

def connected(arr,p,q):
    return root(arr,p)==root(arr,q)

def union(arr,p,q):
    temp=root(arr,p)
    temp1=root(arr,q)
    arr[temp]=temp1

N=int(input("array size: "))
arr=[0]*N
for i in range(N):
    arr[i]=i
while(1):
    a=int(input("1: union   2:find root    3:check for connected     3:quit:   "))
    if(a==1):
        p=int(input("1st ele: "))
        q=int(input("2nd ele: "))
        print(union(arr,p,q))
    elif(a==2):
        p=int(input("ele: "))
        print(root(arr,p))
    elif(a==3):
        p=int(input("1st ele: "))
        q=int(input("2nd ele: "))
        print(connected(arr,p,q))
    else:
        break
    print(arr)