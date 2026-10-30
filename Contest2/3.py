from math import log2
def PullDown(array,root,end):
    swaps=[]
    index = root
    while index*2+1 <= end or index*2+2 <= end:
        if (index*2+2>end or array[index*2+1]<=array[index*2+2]) and array[index]>=array[index*2+1]:
            (array[index], array[index*2+1]) = (array[index*2+1], array[index])
            swaps.append((index,index*2+1))
            index = index*2+1
        elif index*2+2 <= end and array[index*2+2]<=array[index*2+1] and array[index]>=array[index*2+2]:
            (array[index], array[index*2+2]) = (array[index*2+2], array[index])
            swaps.append((index,index*2+2))
            index = index*2+2
        else:
            break
    return swaps
n=int(input())
array=list(map(int,input().split()))
allSwaps=[]
for i in range(2**int(log2(len(array)))-2,-1,-1):
    allSwaps+=PullDown(array,i,len(array)-1)
print(len(allSwaps))
for pair in allSwaps:
    print(pair[0],pair[1])
        
    
