##Conver seconds to corresponding hours minutes and seconds:

seconds=int(input('Enter the seconds to be converted:'))

if seconds>0:
    min,sec=divmod(seconds,60)
    hour,min=divmod(min,60)
else :
    print("Enter input is not valid!!!")
    
print("Seconds into corresponding hour,minute,second is:",hour,"Hr:",min,"Min:",sec,"sec")
