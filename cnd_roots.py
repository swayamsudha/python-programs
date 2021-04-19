##Find the roots of a quadratic eqn using conditional statement

print("Quadratic equation :(a*x^2)+ (b*x)+ c ")
      
a=int(input('a: '))
b=int(input('b: '))
c=int(input('c: '))

D=(b**2)-(4*a*c)
if D == 0:
    root = -b/(2*a)
    print("The two roots are same and root is",root)
elif D > 0:
    r1=(-b+D**0.5)/2*a
    r2=(-b-D**0.5)/2*a
    print("The two roots are:",r1,r2)
else:
    print("The roots of aquadratic equation are not real")
