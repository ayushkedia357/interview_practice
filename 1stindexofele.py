a=[int(i) for i in input().split(",")]
ele=int(input())
s=0
t=0
e=len(a)-1
while(e>=s):
    m=(e+s)//2
    if(a[m]==ele):
        t=1
        break
    elif(a[m]>ele):
        e=m-1
    else:
        s=m+1
i=m
while(a[i]==a[m]):
    i-=1
print(i+1)