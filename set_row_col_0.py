m,n=[int(j) for j in input().split(" ")]
a=0
l=[]
lc=[]
for i in range(m):
    ll=[int(i) for i in input().split(" ")]
    l+=ll
row=[]
col=[]
for i in range(n*m):
    if l[i]==0:
        row.append(i//n)
        col.append(i%n)
row=set(row)
col=set(col)
for i in row:
    l[i*n:i*n+n]=[0]*n
for i in col:
    l[i::n]=[0]*m
for i in range(m):
    print(l[i*n:i*n+n])
