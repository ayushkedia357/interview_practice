import time
start_time = time.time()
def anagram(s1,s2):
    if(len(s1)!=len(s2)):
        return 0
    k=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    l=k
    for i in range(len(s1)):
        m=ord(s1[i])
        m-=97
        k[m]+=1
        mm=ord(s2[i])
        mm-=97
        k[mm]-=1
    if(k==l):
        return 1
    return 0
    '''
    if(sorted(s1)==sorted(s2)):
        return 1
    return 0
    '''
a=input().split(" ")
ll=[]
while(a!=[]):
    t=a[0]
    a.pop(0)
    ll.append(t)
    for i in a[1:]:
        if anagram(t,i):
            ll.append(i)
            a.remove(i)
print(ll)
print("%s seconds" % (time.time() - start_time))
