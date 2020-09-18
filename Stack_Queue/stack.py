def push(stack,top,x):
    stack.append(x)
    top+=1
    return

def pop(stack,top):
    if(isEmpty(stack)):
        print("STACK IS EMPTY")
        return
    stack.pop()
    if(isEmpty(stack)):
        top=-1
        return
    top-=1
    return

def isEmpty(stack):
    if stack==[]:
        return bool(1)
    return bool(0)

stack=[]
top=-1
while(1):
    choice=int(input("Enter - 1:PUSH  2:POP  3:PEEK  4:PRINT  5:END-->"))
    if(choice==1):
        x=int(input("ENTER THE ELEMENT:  "))
        push(stack,top,x)
    elif(choice==2):
        pop(stack,top)
    elif(choice==3):
        print(stack[-1])
    elif(choice==4):
        print(stack)
    else:
        break