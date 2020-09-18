a=[i for i in input().split(",")]
b=[int(i) for i in input().split(",")]
j=0
for i in range(len(a)):
    if(a[i]!='*'):
        a[i]=int(a[i])
        a[j]=a[i]
        j+=1
j-=1
i=len(b)-1
k=len(a)-1
while(i>-1 and j>-1):
    if(b[i]<a[j]):
        a[k]=a[j]
        k-=1
        j-=1
    else:
        a[k]=b[i]
        k-=1
        i-=1
while(i>-1):
    a[k]=b[i]
    k-=1
    i-=1
print(a)