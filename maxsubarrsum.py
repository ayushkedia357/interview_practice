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

'''