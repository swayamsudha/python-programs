##WAP to test a number is  pallindrom or not; 

num = int(input("Enter the number to be tested:"))
temp = num
rev=0
while(num!=0):
    dg = num % 10
    rev=rev*10+dg
    num//=10
if(temp==rev):
    print("{0} is a pallindrom number".format(temp))
else:
    print("{0} is not a pallindrom number".format(temp))

