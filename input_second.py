seconds=int(input('Enter the seconds to be converted:'))
min,sec=divmod(seconds,60)
hour,min=divmod(min,60)
print("Seconds into corresponding hour,minute,second is:",hour,"hrs" ,min,"min" ,sec,"secs")
