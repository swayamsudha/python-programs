#Implement Queue operations using list
Queue=[]

def getChoice():
    print("1.INSERT\n2.DELETE\n3.DISPLAY\n")
    choice=int(input("Enter the choice:\n"))
    return choice

def insert(item):
    Queue.append(item)
    
def delete(item):
    global Queue
    item = Queue[0]
    del Queue[0]
    return item

def display():
        print("Elements of stack are",Queue)


print("-----Implementation of Queue-----")
choice = getChoice()

while choice != 4:
    
    if(choice==1):
        item=int(input("Enter the item to insert:"))
        insert(item)
        
    elif(choice==2):
        if(len(Queue) != 0):
            item = delete(item)
            print("Deleted item = ",item)
        else:
            print("Queue underflow!!")
            
    elif(choice==3):
        if(len(Queue) != 0):
             display()   
        else:
            print("Queue underflow!!")
            
    else:
        print("Invalid choice")
        
    choice = getChoice()
print("Queue Operations Over")
    
