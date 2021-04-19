##WAP to find sum of the natural numbers;

num=int(input("Enter the number:"))
sum=0
temp=num
if(num<0):
    print("Not a valid input!!")
else:
    while(num!=0):
        sum+=num
        num-=1
    print("The sum of " ,temp, "natural number is" ,sum)
