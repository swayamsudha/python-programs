##WAP TO TO PRINT A DECIMAL NUMBER TO ITS BINARY FORM

n = int(input("Enter the decimal Value:"))
bin = 0
i = 1

while(n!=0):
    rem = n % 2
    bin = bin + (i * rem)
    n = n//2
    i = i * 10
print("Converted Binary form of {0} is =  {1}".format(n,bin))
