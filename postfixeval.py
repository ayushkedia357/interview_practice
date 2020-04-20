a=input()
l=[]
d=0
for i in a:
    if i.isalnum():
        l.append(i)
        d+=1
    elif i.isspace():
        #print(l,d)
        k=""
        for j in range(d):
            l[-1]+=k
            k=l[-1]
            l.pop(-1)
        #k=k[::-1]
        l.append(k)
        d=0
    else:
        if a[0].isalpha():
            b=l[-2]+i+l[-1]
            l.pop(-1)
            l.pop(-1)
            l.append(b)
        else:
            b=l[-1]
            c=l[-2]
            l.pop(-1)
            l.pop(-1)
            l.append(str(eval(c+i+b)))
        d=len(l)
print(l[0])
