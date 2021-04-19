#WAP TO IMPLEMENT ALL SORTING MECHANISM:
#Using quicksort mechanism
def QuickSort(Arr,start,last):
    if(start<last):
        pos=Partition(Arr,start,last)
        QuickSort(Arr,start,pos-1)
        QuickSort(Arr,pos+1,last)
def Partition(Arr,start,last):
    j=start
    i=j-1
    pivot=Arr[last]
    while(j<last):
        if(Arr[j]<=pivot):
            i+=1
            temp=Arr[i]
            Arr[i]=Arr[j]
            Arr[j]=temp
        j+=1
    temp=Arr[i+1]
    Arr[i+1]=Arr[last]
    Arr[last]=temp
    return (i+1)

'''def MergeSort(Arr,start,last):
    if start < last:
        mid = (start + last)//2
        MergeSort(Arr,start,mid)
        MergeSort(Arr,mid+1,last)
        Merge(Arr,start,mid,last)
        
def Merge(Arr,start,mid,last):
    temp = []
    i = start
    j = mid
    k = start
    last1 = mid
    last2 = last
    while(i <= last1 and j <= last2):
        if Arr[i] <= Arr[j]:
            temp[k] = Arr[i]
            k+=1
            i+=1
        else:
            temp[k] = Arr[j]
            k+=1
            j+=1
    while i <= last1 :
            temp[k] = Arr[i]
            k+=1
            i+=1
    while j <= last2:   
            temp[k] = Arr[j]
            k+=1
            j+=1
    for i in range(0,last+1):
        Arr[i] = temp[i]'''
        
        
Arr=[]

print("How many times you want to insert:")
size=int(input())
print("Enter the values of the list ")

for i in range(size):
    print("Value in index",i)
    item=int(input())
    Arr.append(item)
print("Elements of Array before sorting =",Arr)

QuickSort(Arr,0,size-1)
print("\nBy using Quicksort mechanism \nThe elements of Array after sorting =")
for i in range(size):
    print(Arr[i],end=' ')
print()

'''MergeSort(Arr,0,size-1)
print("\nBy using mergesort mechanism \nThe elements of Array after sorting =")
for i in range(size):
    print(Arr[i],end=' ')
print()'''

for i in range(size-1):
    for j in range(size-1-i):
        if(Arr[j]>Arr[j+1]):
            temp = Arr[j]
            Arr[j] = Arr[j+1]
            Arr[j+1] = temp
print("\nBy using Bubble sort mechanism \nThe elements of Array  after sorting =",Arr)
