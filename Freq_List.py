#Frequency of each element in the array:
Arr=[]
Freq=[]
size=int(input("Enter the size of Array:"))

for i in range(size):
    print("Value in index",i)
    item=int(input())
    Arr.append(item)
    Freq.append(-1)
    
print("The Array is",Arr)

for i in range(size):
    count=1
    for j in range(i+1,size):
        if(Arr[i]==Arr[j]):
            count+=1
            Freq[j]=0
    if(Freq[i]!=0):
        Freq[i]=count

print("Frequency of each Elements in the list is as follows: ")

for i in range(size):
    if(Freq[i] != 0):
        print("{0} occures {1} time(s) is the list.".format(Arr[i],Freq[i]))
    
        
