ss=input()
ss=ss.lower()
d=""
f=""
ch=0
for i in ss:
    b=ord(i)
    b-=97
    k=1<<b
    if k&ch:
        if(len(f)>len(d)):
            d=f
        #print(f,i)
        t=f.index(i)
        for k in f[:t]:
            bb=ord(k)
            bb-=97
            ch=(~(1<<bb))&ch
        f=f[t+1:]
        f+=i
    else:
        ch=k|ch
        f+=i
if(len(f)>len(d)):
    d=f
print(d)

