def push(st,x):

    st.append(x)
    return

def pop(st):

    if(isEmpty(st)):
        print("STACK IS EMPTY")
        return None
    return st.pop()

def isEmpty(st):

    if st==[]:
        return bool(1)
    return bool(0)

def enqueue(stack,x):

    push(stack,x)

def dequeue(stack,stack2):

    if(isEmpty(stack2)==False):
        return pop(stack2)

    while(isEmpty(stack)==False):
        push(stack2,pop(stack))

    return pop(stack2)

def peek(stack,stack2):

    if(isEmpty(stack2)==False):
        return stack2[-1]

    while(isEmpty(stack)==False):
        push(stack2,pop(stack))

    return stack2[-1]


stack=[]
stack2=[]

while(1):

    choice=int(input("Enter - 1:ENQUEUE  2:DEQUEUE  3:PEEK  4:PRINT  5:END-->"))

    if(choice==1):
        x=int(input("ENTER THE ELEMENT:  "))
        enqueue(stack,x)

    elif(choice==2):
        print(dequeue(stack,stack2))

    elif(choice==3):
        print(peek(stack,stack2))

    elif(choice==4):
        l=stack2[::-1] + stack
        print(l)

    else:
        break