# DECLARE StackData : ARRAY [0:9] OF INTEGER
# DECLARE StackPointer : INTEGER

StackPointer = 0 
StackData = [0 for index in range(10)]

def Display() :
    global StackPointer , StackData
    for index in range(10) :
        print(StackData[index])
    print(StackPointer) 

def push(item) :
    global StackPointer , StackData
    if StackPointer <= 9 :
        StackData[StackPointer] = item
        StackPointer = StackPointer + 1
        return True
    else:
        return False 


def pop() :
    global StackPointer , StackData
    if StackPointer == 0:
        return -1
    else :
        StackPointer = StackPointer - 1
        rem = StackData[StackPointer]
        return rem


for index in range(11) :
    Num = input("Enter the no : ")
    Res = push(Num)
    if Res ==True :
        print("The number is added to stack")
    else :
        print("Not Added . The satck is full") 

pop()
pop()        
           
Display()        

