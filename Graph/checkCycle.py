graph={0:[1,2,3],1:[0,2],2:[0,1,3],3:[0,2]}

vertices=len(graph)
marked=[False]*vertices
recArray=[-1]*vertices
def iscycle(graph,marked,recArray,v):
    marked[v]=True
    recArray[v]=1
    #res=True
    for adj in graph[v]:
        print(recArray,marked)
        if recArray[adj]==1:
            return False
        if marked[adj]==False:
            res=iscycle(graph,marked,recArray,adj)
            if res==False:
                return False
    recArray[v]=0
    return True

a=0
for vert in range(vertices):
    result=iscycle(graph,marked,recArray,vert)
    if result==False:
        a=1
        break

if a==1:
    print("Cyclic")
else:
    print("Acyclic")
