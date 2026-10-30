n,m=map(int,input().split())
vertices = [(0,0)]*n
for i in range(m):
    ex,en = map(int,input().split())
    vertices[ex-1]=(vertices[ex-1][0]+1,vertices[ex-1][1])
    vertices[en-1]=(vertices[en-1][0],vertices[en-1][1]+1)
for vertex in vertices:
    print(vertex[1])
    print(vertex[0])
