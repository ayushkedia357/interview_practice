def subarr(a,b):
    if b>len(a):
        return "not possible"
    s=sum(a[:b])
    d=0
    for i in range(1,len(a)-b+1):
        #s1=s-a[i-1]+a[i+b-1]
        if(sum(a[i:b+i])>s):#s1>s
            s=sum(a[i:b+i])#s=s1
            d=i
    return a[d:d+b]
a=[int(i) for i in input().split(",")]
b=int(input())
print(subarr(a,b))