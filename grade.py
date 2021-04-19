##to calculate the grade of a student

P_mark = float(input("Enter the Phy mark of the student:"))
M_mark = float(input("Enter the math mark of the student:"))
C_mark = float(input("Enter the chem mark of the student:"))
B_mark = float(input("Enter the bio mark of the student:"))
E_mark = float(input("Enter the evs mark of the student:"))

avg = (P_mark+M_mark+C_mark+B_mark+E_mark)/5

print("Average =",avg)

if avg>=90:
    print("O grade")
elif avg >= 80 and avg < 90:
    print("E grade")
elif avg >= 70 and avg < 80:
    print("A grade")
elif avg >= 60 and avg < 70:
    print("B grade")
else:
    print("C grade")


    

