g={1:[2],2:[1,3],3:{2,4},4:[4]}
marked=[False,False,False,False,False]
def dfs(g,marked):
    stack=[]
    stack.append(1)
    #marked[v]=True
    while(stack):
        #print(g)
        v=stack.pop()
        marked[v]=True
        for i in g[v]:
            if marked[i]==False:
                print(v,i)
                stack.append(i)

dfs(g,marked)
