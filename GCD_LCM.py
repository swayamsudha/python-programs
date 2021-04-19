##WAP to find the GCD and LCM of two number;

print("Enter two numbers whose gcd and lcm to be calculated:")
num1 = int(input("num1 = "))
num2 = int(input("num2 = "))
temp1 = num1
temp2 = num2
while(num1!=num2):
    if(num1 > num2):
        num1-=num2
    else:
        num2-=num1
gcd = num1

lcm = (temp1*temp2)//num1

print("GCD & LCM of ",temp1,"and" ,temp2, "is" ,gcd,"and",lcm, "respectively" )
