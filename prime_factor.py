##WAP TO FIND ALL THE PRIME FACTORS OF A NUMBER
num=int(input("Enter the number:"))
count = 0

print("Prime factors of {0} = ".format(num))
for i in range(2,num):
    if(num%i==0):
        for j in range(2,i):
            if(i%j==0):
                count+=1
        if(count == 0):
            print(i)
        count=0
        
        
    
    
            
    
