#WAP TO GET STUDENT'S DEATAILS LIKE NAME, ROLL NO,MARK,ADDRESS AND SEARCH A STUDENT THROUGH ROLL NO:

student=[]
size=int(input("Enter how many student's detaills you want to store:"))

for i in range(size):
    print("NAME:")
    student.append(input())
    print("ROLL NO:")
    student.append(int(input()))
    print("MARK:")
    student.append(float(input()))
    print("ADDRESS:")
    student.append(input())

print("The details of students :",student)
Roll_No=int(input("Enter a student's roll no to search:"))
for i in range(len(student)):
    if Roll_No == student[i]:
        print("Name = {:s} \nRoll No = {:d} \nMark = {:f} \nAddress = {:s}".format(student[i-1],student[i],student[i+1],student[i+2]))
        break
    
