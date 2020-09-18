a=[int(i) for i in input().split(" ")]
currsum=a[0]
maxsum=currsum
for i in range(1,len(a)):
    #if currsum+a[i]>a[i]:
    currsum+=a[i]
    #else:
    if(currsum<a[i]):
        currsum=a[i]
    if currsum>maxsum:
        maxsum=currsum
print(maxsum)
'''
a=2 -9 5 1 -4 6 0 -7 8
currsum=2=maxsum

c=2
m=2

i=1
c=-7  m=2
i=2  c=-2 --> c=5   m=2 --> m=5
i=3   c=6  m=6
i=4  c=2  m=6
i=5  c=8 m=8
i=6  c=8 m=8
i=7  c=1 m=8
i=8 c=9 m=9
'''