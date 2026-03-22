#stack

# declare myList : ARRAY [0:4] OF STRING
myList =["" for index in range(5)]

tos = -1

def Push(NewItem) :
    global myList , tos
    if tos == 4 :
        print("full")
    else :
        tos = tos + 1
        myList[tos] = NewItem
        print("pushed")

def display():
    global myList , tos
    for index in range(5) :
        print(index , myList[index])  
    print("top of stack" , tos)  

def pop() :
    global myList , tos 
    if tos == -1 :
        print("empty")
    else :
        myList[tos] = ""
        tos = tos - 1
        print("pop")


#run push function and display and 
Push("A")
Push("B")
Push("C")
Push("D")
Push("E")
Push("F")
pop()
pop()
pop()
Push("Y")
Push("Z")
pop()
pop()
Push("X")
Push("F")
display()






            

