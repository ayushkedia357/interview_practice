def fib(c,a):
    if a==0:
        return 0
    d=sum(c)
    c[0]=c[1]
    c[1]=d
    a=a-1
    fib(c,a)
    return sum(c)
   
a=int(input())
c=[0,1]
if(a<2):
    print(c[a])
else:
    a=a-2
    print(fib(c,a))
