##WAP TO TO DISPLAY FIBBONACI NUMBERS UPTO NTH TERM
n = int(input("Enter the Nth term:"))
f=0
print("Fibbonaci numbers up to {0}th term = ".format(n))
for i in range (1,n+1):
    f=f+i
    print(f)
