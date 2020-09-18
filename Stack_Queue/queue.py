def enqueue(q,x,front,rear):
    q.append(x)
    rear+=1
    front+=1

def dequeue(q,front,rear):
    if(isEmpty(q)):
        print("QUEUE IS EMPTY")
        return
    q.pop(0)
    if(isEmpty(q)):
        front=-1
        rear=-1
        return
    front=0
    return

def isEmpty(q):
    if q==[]:
        return bool(1)
    return bool(0)

q=[]
front=-1
rear=-1
while(1):
    choice=int(input("Enter - 1:ENQUEUE  2:DEQUEUE  3:PEEK  4:PRINT  5:END-->"))
    if(choice==1):
        x=int(input("ENTER THE ELEMENT:  "))
        enqueue(q,x,front,rear)
    elif(choice==2):
        dequeue(q,front,rear)
    elif(choice==3):
        print(q[0])
    elif(choice==4):
        print(q)
    else:
        break