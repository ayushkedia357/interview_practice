a=input()
l=[]
m=1
for i in a:
    if i=='(' or i=='{' or i=='[':
        l.append(i)
    elif(i==')'):
        if l==[]:
            m=0
            break
        elif(l[-1]!='('):
            m=0
            break
        else:
            l.pop(-1)
    elif(i=='}'):
        if l==[]:
            m=0
            break
        elif(l[-1]!='{'):
            m=0
            break
        else:
            l.pop(-1)
    elif(i==']'):
        if l==[]:
            m=0
            break
        elif(l[-1]!='['):
            m=0
            break
        else:
            l.pop(-1)
if m==1 and l==[]:
    print("valid")
else:
    print("invalid")
