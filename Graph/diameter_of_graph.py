g={1:[2],2:[1,3],3:{2,4},4:[3]}

marked=[False,False,False,False,False]
def bfs(g,marked,v):
    q=[]
    q.append(v)
    #longestShortedPath=0
    #marked[v]=True
    while(q):
        #print(g)
        v=q.pop(0)
        marked[v]=True
        for i in g[v]:
            if marked[i]==False:
                print(v,i)
                q.append(i)
        #longestShortedPath+=1
    return v

longestShortestNode = bfs(g,marked,1)
marked=[False,False,False,False,False]
print(bfs(g,marked,longestShortestNode),longestShortestNode)