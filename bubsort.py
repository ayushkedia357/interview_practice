a=[int(i) for i in input().split(" ")]
for i in range(len(a)):
    for j in range(len(a)-i-1):
        b=a[j]
        if b>=a[j+1]:
            a[j]=a[j+1]
            a[j+1]=b
print(a)
            
