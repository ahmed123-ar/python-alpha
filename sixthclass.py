# summer 2025 p41 q1


# DECLARE Queue : ARRAY [0:19] OF STRING
# DECLARE HeadPointer , TailPointer ,NumberItems : INTEGER
Queue =["-1" for index in range(20)]
HeadPointer  = -1
TailPointer = -1
NumberItems = 0


def Enqueue(NewItem) :
    global Queue , HeadPointer , TailPointer , NumberItems
    if(NumberItems == 20 ):
        return False
    else :
        if(HeadPointer == -1 and TailPointer == -1) :
            HeadPointer = 0
            TailPointer = 0
        elif (TailPointer == 19):
            TailPointer = 0
        else :
            TailPointer = TailPointer + 1
    Queue[TailPointer] = NewItem
    NumberItems = NumberItems + 1
    return True

for index in range(1, 26) :
    Res = Enqueue(index)
    if (Res) :
        print(index , "Successful")
    else :
        print(index , "Unsuccessful")   


def Dequeue() :
    global Queue , HeadPointer , TailPointer , NumberItems
    if NumberItems == 0 :
        return -1
    else :
        dlt = Queue[HeadPointer]
        if HeadPointer == TailPointer :
            HeadPointer = -1
            TailPointer = -1
        elif HeadPointer == 19 :
            HeadPointer = 0
        else :
            HeadPointer = HeadPointer + 1  
    NumberItems = NumberItems -1 
    return dlt

print(Dequeue())
print(Dequeue())





             