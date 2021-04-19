##Input three numbers and arrange in descending order

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))


if(a>b and a>c):
    if(b>c):
        big = a
        mid = b
        small = c
    else:
        big = a
        mid = c
        small = b
elif(b>a and b>c):
    if(c>a):
        big = b
        mid = c
        small = a
    else:
        big = b
        mid = a
        small = c
elif(c>a and c>b):
    if(a>b):
        big = c
        mid = a
        small = b
    else:
        big = c
        mid = b
        small = a
    

print("The no in descending order:",big,mid,small)
    
        
    
    
    
