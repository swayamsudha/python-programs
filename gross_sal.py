##Calculate the gross salary of the Employee:

b_sal = int (input("Enter the basic salary of the Employee:"))
print("N.B - DA,HRA,conveyance,medical is given in %")

DA_amt = b_sal*(60/100)
HRA_amt = b_sal*(15/100)
con_amt = b_sal*(15/100)
med_amt = b_sal *(10/100)
                  
g_sal = b_sal + DA_amt + HRA_amt + con_amt + med_amt
print("{0} is the gross salary of the Employee..".format(g_sal))
