graph={0:[1,2,3],1:[0,2],2:[0,1,3],3:[0,2]}

def isbipartite(g,s,colour):
    colour[s]=1
    q=[]
    q.append(s)

    while(q):
        vertex=q.pop(0)
        for adj in graph[vertex]:
            if colour[adj]==-1:
                if colour[vertex]==1:
                    colour[adj]=0
                else:
                    colour[adj]=1
                    q.append(adj)
            elif colour[vertex]==colour[adj]:
                return False
    #print(colour)    
    return True



vertices=len(graph)
colour=[-1]*vertices
a=1


for src in range(vertices):
    if colour[src]==-1:
        if isbipartite(graph,src,colour)==False:
            a=1

if a==1:    
    print(False)
else:
    print(True)
        