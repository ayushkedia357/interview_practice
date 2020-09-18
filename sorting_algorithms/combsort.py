a=[int(i) for i in input().split(" ")]
c=len(a)
b=c
while(b//1.3>=1):
    b=int(b//1.3)
    for i in range(c-b):
        if(a[i]>a[i+b]):
            temp=a[i]
            a[i]=a[i+b]
            a[i+b]=temp
print(a)
