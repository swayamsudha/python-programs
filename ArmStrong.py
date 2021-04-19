##Wap to test a no is armstrong or not;

num=int(input("Enter the number to be tested: "))
sum = 0
temp = num
while(num!=0):
    dg=num%10
    sum+=dg**3
    num//=10
if(temp==sum):
    print("{0} is an Armstrong number".format(temp) )
else:
    print("{0} is not an Armstrong number".format(temp) )
