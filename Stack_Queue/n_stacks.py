def push(stackdata,topofStack,nextavailableindex,nextindex,x,stackNum,n):
    if(stackNum<1 or stackNum>n):
        print("Incorrect stack number")
        return

    if(nextavailableindex==-1):
        print("stack overflow")
        return

    tempindex = nextavailableindex
    nextavailableindex = nextindex[tempindex]
    nextindex[tempindex] = topofStack[stackNum-1]
    topofStack[stackNum-1] = tempindex
    stackdata[tempindex] = x
    return nextavailableindex

def pop(stackdata,topofStacks,nextavailableindex,nextindex,stackNum,n):
    if(stackNum<1 or stackNum>n):
        print("Incorrect stack number")
        return

    if(topofStacks[stackNum-1] == -1):
        print("stack underflow")
        return

    temptop = topofStacks[stackNum-1]
    topofStacks[stackNum-1] = nextindex[temptop]
    nextindex[temptop] = nextavailableindex
    nextavailableindex = temptop
    return stackdata[temptop],nextavailableindex

def printstack(stackdata,topofStacks,nextavailableindex,nextindex,stackNum,n):
    if(stackNum<1 or stackNum>n):
        print("Incorrect stack number")
        return

    j=topofStacks[stackNum-1]
    tempstack=[]
    while(j!=-1):
        tempstack.append(stackdata[j])
        j=nextindex[j]
    print(tempstack)
    return 


n=int(input("Enter N. of stacks: "))
size=int(input("Enter the capacity of the array:  "))
topofStacks=[-1]*n
nextavailableindex=0
nextindex=[]

for i in range(size-1):
    nextindex.append(i+1)
nextindex.append(-1)

stackdata=[0]*size
print(nextindex)

while(1):
    choice=int(input("Enter - 1:PUSH  2:POP  3:PEEK  4:PRINT  5:END-->"))

    if(choice==1):
        x=int(input("ENTER THE ELEMENT:  "))
        stackNum=int(input("Enter the stack No.:  "))
        nextavailableindex = push(stackdata,topofStacks,nextavailableindex,nextindex,x,stackNum,n)

    elif(choice==2):
        stackNum=int(input("Enter the stack No.:  "))
        a,nextavailableindex = pop(stackdata,topofStacks,nextavailableindex,nextindex,stackNum,n)
        print("Element popped = ",a)
        
    elif(choice==3):
        stackNum=int(input("Enter the stack No.:  "))
        print(stackdata[topofStacks[stackNum]])

    elif(choice==4):
        stackNum=int(input("Enter the stack No.:  "))
        printstack(stackdata,topofStacks,nextavailableindex,nextindex,stackNum,n)

    else:
        break

    print(stackdata)
    print(topofStacks)
    print(nextindex)
    print(nextavailableindex)
