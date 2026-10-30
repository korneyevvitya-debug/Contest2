from math import log2
def PullDown(array,root,end):
    index = root
    while index*2+1 <= end or index*2+2 <= end:
        if (index*2+2>end or array[index*2+1]>=array[index*2+2]) and array[index]<=array[index*2+1]:
            (array[index], array[index*2+1]) = (array[index*2+1], array[index])
            index = index*2+1
        elif index*2+2 <= end and array[index*2+2]>=array[index*2+1] and array[index]<=array[index*2+2]:
            (array[index], array[index*2+2]) = (array[index*2+2], array[index])
            index = index*2+2
        else:
            break
    return
def HeapSort(array):
    for i in range(2**int(log2(len(array)))-2,-1,-1):
        PullDown(array,i,len(array)-1)
    for i in range(len(array)-1,0,-1):
        (array[0],array[i]) = (array[i],array[0])
        PullDown(array,0,i-1)
    return array
print(HeapSort([3,2,5,100,0,12,5,104,16,-3,-8,1,-1,1,1]))
#print(HeapSort([15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]))
