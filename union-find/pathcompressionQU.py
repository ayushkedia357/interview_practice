def root(arr,p):
    temp=p
    temp1=p
    while(arr[p]!=p):
        p=arr[p]
    while(temp1!=arr[temp1]):
        print(arr)
        temp1=arr[temp]
        arr[temp]=p
        temp=temp1
    return p

def connected(arr,p,q):
    return root(arr,p)==root(arr,q)

def union(arr,p,q):
    temp=root(arr,p)
    temp1=root(arr,q)
    arr[temp]=temp1

N=int(input("array size: "))
arr=[1, 8, 1, 8, 3, 0, 5, 1, 8, 8]
for i in range(N):
    arr[i]=i
arr=[1, 8, 1, 8, 3, 0, 5, 1, 8, 8]
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