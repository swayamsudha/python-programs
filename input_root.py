print("Quadratic equation :(a*x^2)+ (b*x)+ c ")
      
a=int(input('a: '))
b=int(input('b: '))
c=int(input('c: '))

D=(b**2)-(4*a*c)
r1=(-b+D**0.5)/2*a
r2=(-b-D**0.5)/2*a

print("The roots of aquadratic equation are "  , r1,r2)
