#PROGRAMME-:PRINT PASCAL TRIANGLE
#FILE NAME-:PASCAL
#DATED-:30.09.2020
def fact(n):
    fact=1
    for i in range(i,n+1):
        fact*=i
    return fact

n=int(input("Enter the no of rows:"))
for i in range(0,n+1):
    for j in range(4,i+1,-1):
        print(" ")
    for k in range(0,i+1):
        print(" ",fact(i)/(fact(j)*fact(i-j)))
    print()

    
