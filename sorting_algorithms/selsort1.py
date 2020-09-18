a=[int(i) for i in input().split(" ")]
for i in range(len(a)):
    c=i
    for j in range(i+1,len(a)):
        if a[j]<a[c]:
            c=j
    temp=a[i]
    a[i]=a[c]
    a[c]=temp
print(a)
