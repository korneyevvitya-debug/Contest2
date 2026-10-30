n=int(input())
matrix=[]
for i in range(0,n):
    matrix.append(list(map(int,input().split())))
for i in range(0,n):
    for j in range(0,n):
        if matrix[i][j]==1:
            print(i+1,j+1)
