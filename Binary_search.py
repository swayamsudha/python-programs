#Binary search in python
def binary_search(Arr,item,start,end):
    if start > end:
        return -1
    mid = (start+end)//2
    if item == Arr[mid]:
        return mid

    elif item < Arr[mid]:
        return binary_search(Arr,item,start,mid-1)

    else:
        return binary_search(Arr,item,mid+1,end)
Arr=[]
size=int(input("Enter the size of Array:"))

for i in range(size):
    print("Value in index",i)
    item=int(input())
    Arr.append(item)
    
print("The Array is",Arr)
item=int(input("Enter the item to be searched -:"))
print("Index of {0} =".format(item),binary_search(Arr,item,0,len(Arr)))        
