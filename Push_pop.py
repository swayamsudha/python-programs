#Implement stack operations using list
stack=[]

def getChoice():
    print("1.PUSH\n2.POP\n3.DISPLAY\n")
    choice=int(input("Enter the choice:\n"))
    return choice

def push(item):
    stack.append(item)
    
def pop(item):
    global stack
    item = stack[-1]
    del stack[-1]
    return item

def display():
        print("Elements of stack are",stack)


print("-----Implementation of stack-----")
choice = getChoice()

while choice != 4:
    
    if(choice==1):
        item=int(input("Enter the item to push:"))
        push(item)
        
    elif(choice==2):
        if(len(stack) != 0):
            item = pop(item)
            print("Poped item",item)
        else:
            print("Satck underflow!!")
            
    elif(choice==3):
        if(len(stack) != 0):
             display()   
        else:
            print("Satck underflow!!")
            
    else:
        print("Invalid choice")
        
    choice = getChoice()
print("Stack Operations Over")
    
