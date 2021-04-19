#SUM OF SINE SERIES
def sine(num,n):
    sum=0
    m=1
    sign=1
    for i in range(0,num+1):
        temp=m
        fact=1
        while(temp != 0):
            fact*=temp
            temp-=1
    sum=sum+((num**m)/fact)*sign
    sign*=(-1)
    m+=2
    return sum
x=int(input("enter the value : "))
t=int(input("Enter the term: "))
res=sine(x,t)
print("The sum of sine series of {0}th term of the value {1} = ".format(t,x),res)
