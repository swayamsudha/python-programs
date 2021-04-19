#WAP TO SEARCH A KEY ELEMENT AND FIND IT'S FREQUENCY:

Arr=[]
count=0
print("How many times you want to insert:")
size=int(input())
print("Enter the values of the list ")
for i in range(size):
    print("Value in index",i)
    item=int(input())
    Arr.append(item)
print("Elements of Array are =",Arr)
key=int(input("Enter the element to search:"))
for i in range(size):
    if(key==Arr[i]):
        count+=1
if(count==0):
    print("Searched element is not found!! ")
print("The frequency of searched element ",count)


    

