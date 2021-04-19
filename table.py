##WAP TO PRINT MULTIPLICATION TABLE OF A GIVEN NUMBER

n=int(input("Enter the number whose multiplication table will be formed: "))
print("Form a multiplication table of ",n)
for i in range(1,11):
    m = n*i
    print("{0} * {1} = ".format(n,i),m)
