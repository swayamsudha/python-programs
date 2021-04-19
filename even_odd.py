##WAP TO CHECK HOW MANY NUMBERS ARE ODD AND EVEN AMONG TEN RANDOM NUMBERS
o=0
e=o
print("Enter 10 random numbers:")
for i in range (1,11):
    n = int (input())
    if(n%2==0):
        print("{0} is an even number..".format(n))
        e+=1
    else:
        print("{0} is an odd number..".format(n))
        o+=1
        
print("The total no of odd number is " , o, "even number is ",e)
        
