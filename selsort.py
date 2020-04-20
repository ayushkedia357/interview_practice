a=[int(i) for i in input().split(" ")]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]>=a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print(a)
            
