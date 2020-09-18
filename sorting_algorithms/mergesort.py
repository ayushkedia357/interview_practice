def divide(a):
    if len(a)>1:
        m=len(a)//2
        l=a[:m]
        r=a[m:]
        divide(l)
        divide(r)
        merge(a,l,r)
        #print(a,l,r)
def merge(a,l,r):
    i=0
    j=0
    k=0
    while(i<len(l) and j<len(r)):
        print(l,r)
        if(l[i]>r[j]):
            a[k]=r[j]
            k+=1
            j+=1
        else:
            a[k]=l[i]
            i+=1
            k+=1
    for t in range(i,len(l)):
        a[k]=l[t]
        k+=1
    for t in range(j,len(r)):
        a[k]=r[j]
        k+=1
a=[4,3,2,1]
divide(a)
print(a)
