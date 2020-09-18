def insersort(l):
    for i in range(1,(len(l))):
        j=i-1
        key=a[i]
        while(j>=0 and key<a[j]):
            a[j+1]=a[j]
            j-=1
        a[j+1]=key
    return l
a=[int(i) for i in input().split(" ")]
a=insersort(a)
print(a)
