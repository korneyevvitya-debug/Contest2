n=int(input())
array=list(map(int,input().split()))
keys=[0]*10
for x in array:
    keys[x-1]+=1
for k in range(1,10):
    keys[k]+=keys[k-1]
arraySorted=[-1]*n
for i in range(n-1,-1,-1):
    pos=keys[array[i]-1]-1
    keys[array[i]-1]-=1
    arraySorted[pos]=array[i]
print(*arraySorted)
    
    
