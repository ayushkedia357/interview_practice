def union(arr,p,q):
    temp=arr[p]
    for i in range(len(arr)):
        if arr[i]==temp:
            arr[i]=arr[q]

def connected(arr,p,q):
    if arr[p]==arr[q]:
        return True
    return False


N=int(input("array size: "))
arr=[0]*N
for i in range(N):
    arr[i]=i
while(1):
    a=int(input("1: union   2:connected     3:quit"))
    if(a==1):
        p=int(input("1st ele: "))
        q=int(input("2nd ele: "))
        print(union(arr,p,q))
    elif(a==2):
        p=int(input("1st ele: "))
        q=int(input("2nd ele: "))
        print(connected(arr,p,q))
    else:
        break
    print(arr)