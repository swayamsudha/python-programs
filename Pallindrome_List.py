#WAP TO CHECK A LIST PALLINDROME OR NOT

Arr=[]
print("How many times you want to insert:")
size=int(input())
print("Enter the values of the list ")
for i in range(size):
    print("Value in index",i)
    item=int(input())
    Arr.append(item)
print("Elements of Array =",Arr)

for i in range (len(Arr)-1,-1,-1):
    Rev=Arr
    
if(Rev==Arr):
    print("The list is pallindrome: ")
else:
    print("The list is not pallindrome: ")
