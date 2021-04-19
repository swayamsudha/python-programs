##WAP TO PRINT A NUMBER IN WORDS
print("To print a number in word:")
n=int(input("Enter the number:"))
print("{0} in word -:".format(n))
rev=0
while(n!=0):
    dg=n%10
    rev=rev*10+dg
    n//=10
while(rev!=0):
    d=rev%10
    if(d==1):
        print("ONE",end=' ')
    elif(d==2):
        print("TWO",end=' ')
    elif(d==3):
        print("THREE",end=' ')
    elif(d==4):
        print("FOUR",end=' ')
    elif(d==5):
        print("FIVE",end=' ')
    elif(d==6):
        print("SIX",end=' ')
    elif(d==7):
        print("SEVEN",end=' ')
    elif(d==8):
        print("EIGHT",end=' ')
    elif(d==9):
        print("NINE",end=' ')
    rev//=10
    
