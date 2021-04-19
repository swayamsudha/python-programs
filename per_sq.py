##WAP TO CHECK  A NUMBER IF A PERFECT SQUARE OR NOT
num=int(input("Enter the number: "))
root=(num**0.5)
#print("root =",root)
n=int(root+0)**2 
#print("n=",n)
if n ==num:
    print(num,"is a perfect square:")
else:
    print(num,"is not a perfect square:")
