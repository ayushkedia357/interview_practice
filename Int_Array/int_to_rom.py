'''
num=1994
l=[]
i=1
while(num//10**i):
    l.append(num%(10**i))
    i+=1
l.append(num%(10**i))
l=l[::-1]
l1=[1,5,10,50,100,500,1000]
d1={1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:''}
i=0
f=""
while(i<len(l)):
    j=0
    while(l1[j]<l[i]):
        print(j)
        j+=1
        if(j==len(l1)):
            j-=1
            break
    a=str(l1[j]-l[i])
    print(a)
    if((a[0])=='1'):
        f=f+d1[int(a)]+d1[l1[j]]
        i+=1
    elif((a[0])=='0'):
        f+=d1[l1[j]]
        i+=1
    else:
        while(l[i]!=0):
            f+=d1[l1[j-1]]
            #print(f)
            l[i]-=l1[j-1]
        i+=1
'''
num=10
#e=num
l=[]
i=1
while((num//10**i)>=1):
    print(num)
    if(num%(10**i)):
        l.append(num%(10**i))
        num-=l[-1]
    i+=1
l.append(num%(10**i))
print(l)
l=l[::-1]
l1=[1000,900,500,400,100,90,50,40,10,9,5,4,1,0]
l2=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I",""]
i=0
f=""
while(i<len(l)):
    j=0
    while((l[i]//l1[j])<1):
        j+=1
    m=l[i]//l1[j]
    k=0
    while(k<m):
        f+=l2[j]
        l[i]-=l1[j]
        k+=1
    if(l[i]==0):
        i+=1
print(f)
