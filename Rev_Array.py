#WAP TO REVERSE A LIST

Arr=[]
print("How many times you want to insert:")
size=int(input())
print("Enter the values of the list ")
for i in range(size):
    print("Value in index",i)
    item=int(input())
    Arr.append(item)
print("Elements of Array =",Arr)

#case - 1
print("\nReversed elements of the array :")
for i in range (len(Arr)-1,-1,-1):
    print(Arr[i])

'''#reverse by using in buit ()
Arr.reverse()
print("Reverse Array:",Arr)'''
'''#case - 3
print("\nReversed elements of the array :")
Arr[:-1]
print(Arr)'''

