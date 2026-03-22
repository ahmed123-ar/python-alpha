# Queue

# declare myList : ARRAY [0:4] OF STRING
myList =["" for index in range(5)]

head = -1
tail=-1


def display() :
    global myList , head , tail
    for index in range(5) :
        print(index , myList[index])
    print("head" ,head , "tail" , tail)


def enqueue(newItem) :
    global myList , head , tail
    if (head == 0 and tail == 4 )or (head == tail + 1) :
        print("full")
    else :
        if head == -1 and tail == -1:
            head = 0
            tail = 0
        elif tail == 4 :
            tail = 0
        else :
            tail = tail + 1

        myList[tail] = newItem
        print("enqueue")    


def dequeue() :
    global myList , head , tail
    if head == -1 and tail == -1 :
        print("empty")
    else :
        print(myList[head])
        myList[head] = ""
        if head == tail :
            head = -1
            tail = -1
        elif head == 4 :
            head = 0
        else :
            head = head + 1 
        print("dequeue")



                   
#run display and enqueue and dequeue
enqueue("A")
enqueue("B")
enqueue("C")
enqueue("D")
dequeue()
enqueue("D")
enqueue("X")
enqueue("M")
dequeue()
dequeue()
display()
