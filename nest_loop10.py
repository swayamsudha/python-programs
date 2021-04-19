num=int(input("Enter the number:"))
for row in range(0,num):
    for col in range(1,num-row+1):
        print(col,end=" ")
    print()
for row in range(1,num+1):
    for  col in range(1,row+1):
        print(col,end = " ")
    print()
