##Denominator test using an equation
a=int(input("Enter the value of a:"));
b=int(input("Enter the value of b:"));
c=int(input("Enter the value of c:"));
d=int(input("Enter the value of d:"));

x = (a-b)/(c-d)

if x == 0:
    print("The denominator is 0 and value of x is undefined")
else:
    print("The value of x is ",x)
