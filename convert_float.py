##Round a floating point number to an integer
a = float(input("a: "))
b=int(a)

c = a-b

if(c>=0.5):
    print("Rounded value of a is {0}".format(b+1))
else:
    print("Rounded value of a is {0}".format(b))
