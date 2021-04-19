##WAP to calculate factorial of a number:

num=int(input("Enter the number:"))
fact=1

if(num<0):
    print("factorial can not be calculated! please Enter a positive number")
else:
    for i in range (1,num+1):
        fact=fact*i
    
print("Factorial of ",num ,"is" ,fact)
    
