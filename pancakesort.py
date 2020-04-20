a=[int(i) for i in input().split(" ")]
d=len(a)
b=a
for i in range(len(a)-1):
    c=max(b)
    c=a.index(c)
    l=a[:c+1]
    b=l[::-1]+b[c+1:]
    b=b[::-1]
    a=b+a[d-i:]
    b=a[:-i-1]
print(a)
