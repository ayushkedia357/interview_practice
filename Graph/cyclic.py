graph={0:[1],1:[0,2],2:[1,3],3:[2]}

vertices=len(graph)
marked=[False]*vertices
def iscycle(graph,marked,v,src):
    marked[v]=True
    #res=True
    for adj in graph[v]:
        print(marked)
        if marked[adj]==False:
            res=iscycle(graph,marked,adj,v)
            if res==True:
                return True
        elif marked[adj]==True and adj!=src:
            return True
    return False

a=0
for vert in range(vertices):
    if marked[vert]==False:
        result=iscycle(graph,marked,vert,vert)
        if result==True:
            a=1
            break

if a==1:
    print("Cyclic")
else:
    print("Acyclic")
