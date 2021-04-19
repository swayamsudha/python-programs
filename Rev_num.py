##WAP to find the reverse of a number

num = int(input("Enter the number whose reverse is to be calculated:"))
rev=0
while(num!=0):
    dg = num % 10
    rev=rev*10+dg
    num//=10

print("The reverse of the number is = ",rev)
