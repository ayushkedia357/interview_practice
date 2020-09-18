s1=input()
s2=input()
d=0
if s1==s2:
    d=1
for i in range(1,len(s1)):
    if(d==1):
        break
    if(s1[i:]==s2[:-i]):
        if(s1[:i]==s2[-i:]):
            #print("YES")
            d=1
            break
if(d==1):
    print("YES")
else:
    print("NO")
        
    
