##to test a no divisble by both 11 and 13 or by both 5 and 7
##print("Enter the number:")
num = int(input("Enter the number: "))
print("Number :",num)
if (num % 11 == 0 and num % 13 == 0):  
    print("The number is divisible by 11 and 13")
elif(num % 5 == 0 and num % 7 == 0):
    print("The number is divisible by 5 and 7")
else:
    print("The number is not divisible by 11 and 13 or 5 and 7")
