# DECLARE Queue : ARRAY[0:99] OF STRING
# DECLARE QueueHead , QueueTail , NumberItems : INTEGER
Queue = ["" for index in range(100)]
QueueHead = -1
QueueTail = -1
NumberItems = 0 

def Enqueue(item) :
    global Queue , QueueHead , QueueTail , NumberItems
    if NumberItems == 100 :
        return False
    else :
        if QueueHead == -1 and QueueTail == -1 :
           QueueHead= 0
           QueueTail = 0
        elif QueueTail == 99 :
           QueueTail = 0
        else :
           QueueTail = QueueTail+1
    Queue[QueueTail] = item 
    NumberItems = NumberItems + 1          
           
def Dequeue() :
    global Queue , QueueHead , QueueTail , NumberItems
    if NumberItems == 0 :
        return False
    else :
        removed = Queue[QueueHead]
        if QueueHead == QueueTail :
            QueueHead = -1
            QueueTail = -1
        elif QueueHead == 99 :
             QueueHead = 0
        else :
            QueueHead = QueueHead + 1
        NumberItems = NumberItems - 1
        return removed    
    
def ReadData() :
    myfile = open("BinaryData.txt" , "r")
    data = myfile.readline().strip()
    while data != "" :
        Enqueue(data)
        data = myfile.readline().strip()
    myfile.close()   

NewString = ""

def Compress() :
    global Queue, NewString  , NumberItems
    first = Dequeue()
    while NumberItems > 0 and first != False :
        next = Dequeue()
        count = 1
        while next == first :
            count = count + 1
            first = next
            next = Dequeue()  
        NewString = NewString + first + str(count)
        first = next    



ReadData()
Compress()     
print(NewString)    



