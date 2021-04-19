##WAP TO PRINT THE VALUE OF X TO THE POWER Y
print("Find the value of x to the power y")
x=int(input("X: "))
y=int(input("Y: "))
val =1
for i in range(y):
    val = val * y
print("value of {0} to the power {1} is = ".format(x,y),val)
