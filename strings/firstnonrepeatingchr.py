a=input()
a=a.lower()
k=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in a:
    #if a.count(i)==1
    k[ord(i)-97]+=1
M=-1
for i in range(26):
    if k[i]==1:
        l.append(a.index(chr(97+i)))
print(a[min(l)])
    



'''
ABBZECCA
K=[]
L=[3,4]
'''
