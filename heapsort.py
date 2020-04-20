def swap(x,y):
    temp=x
    x=y
    y=temp
    return x,y
a=[int(i) for i in input().split(" ")]
for i in range(len(a)):
    if (2*i+1)>=len(a):
        break
    if(a[i]<a[2*i+1] and a[2*i+1]<a[2*i+2]):
        a[i],a[2*i+2]=swap(a[i],a[2*i+2])
    elif(a[i]<a[2*i+1]):
        a[i],a[2*i+1]=swap(a[i],a[2*i+1])
print(a)