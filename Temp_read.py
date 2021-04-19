##Temperature of the oven according to reading:

temp_read = int(input("Enter the reading of the oven:"))
default = 300

if(temp_read == 2 or temp_read == 3):
    print("Temperature should be set to 500 degree..")
elif(temp_read == 4):
    print("Temperature should be set to 600 degree..")
elif(temp_read == 5 or temp_read == 6 or temp_read == 7 ):
    print("Temperature should be set to 600 degree..")
else:
    print("The temperature should be set to default = {0} degree".format(default))


    

