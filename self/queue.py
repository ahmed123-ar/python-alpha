# DECLARE Queue : ARRAY [0:3] OF STRING

Queue = ["" for index in range(4)]
Head = -1
Tail = -1

def Enqueue(item) :
    global Queue , Head , Tail
    if (Head == 0 and Tail == 3) or (Head == Tail + 1) :
        print("Queue is full")
    else :
        if Head == -1 and Tail == -1:
            Head = 0
            Tail = 0
        elif Tail == 3:
            Tail = 0
        else :
            Tail = Tail + 1
        Queue[Tail] = item 
        print("item pushed ")

def Dequeue():
    global Queue , Head , Tail
    if Head == -1 and Tail == -1 :
        print("Queue is empty") 
    else :
        Queue[Head] = ""
        if Head == Tail  :
            Head = -1 
            Tail = -1
        elif Head == 3 :
            Head= 0
        else :
            Head = Head + 1
        print("item removed ")  

def display() :
    global Queue , Head , Tail
    for index in range(4) :
        print(Queue[index]) 
    print("head :" , Head , "tail" , Tail)  

Enqueue("pen") 
Enqueue("pencil") 
Enqueue("toy") 
Enqueue("kiwi") 
Enqueue("mobile")
display()
Dequeue()                                              