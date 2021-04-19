import math
x=int(input("Enter the value: "))
t=int(input("Enter the term: "))
temp=2
sign=1
sum=0
fact=1
for i in range(1,temp+1):
    fact=fact*temp
    temp+=2
if(t%2)==0:
    sign*=(-1)
sum=1+sum +((x**temp)/fact)*sign
#temp+=2
print("SUM = ",sum)
    
    
