##WAP to find the sum of digits of a no.

num=int(input("Enter the number whose sum to e calculated:"))
sum =0
while(num!=0):
    dg = num % 10
    sum+=dg
    num //= 10

print("Sum of the digits of the number is = ",sum)
