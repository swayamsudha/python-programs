#Delete duplicacy  of each element in the array:
Arr=[]
size=int(input("Enter the size of Array:"))

for i in range(size):
    print("Value in index",i)
    item=int(input())
    Arr.append(item)
    
print("The Array is",Arr)
'''New_Arr=[]
for i in Arr:
        if i not in New_Arr:         
           New_Arr.append(i)
print("The new Array is",New_Arr)'''
'''[New_Arr.append(i) for i in Arr if i not in New_Arr]'''
'''print("The new Array is",New_Arr)'''
'''New_Arr=[i for size,i in enumerate(Arr) if i not in Arr[:size] ]
print("The new Array is",New_Arr)'''
Arr=list(set(Arr))
print("The new Array is",Arr)     
