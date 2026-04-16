# DECLARE QueueArray : ARRAY [0:9] OF STRING
# DECLARE HeadPointer : INTEGER
# DECLARE TailPointer : INTEGER
# DECLARE NumberOfItems : INTEGER

QueueArray = ["" for index in range(10)]
HeadPointer = 0
TailPointer = 0
NumberOfItems = 0

def Enqueue(data)  :
    global HeadPointer , TailPointer , NumberOfItems
    if NumberOfItems == 10 :
        return False
    QueueArray[TailPointer] = data
    if TailPointer >= 9 :
        TailPointer = 0
    else :   
        TailPointer = TailPointer + 1
    NumberOfItems = NumberOfItems + 1
    return True

def Dequeue()  :
    global HeadPointer , TailPointer , NumberOfItems
    if NumberOfItems == 0:
        return False
    else :
        removed = QueueArray[HeadPointer]
        NumberOfItems = NumberOfItems - 1
        if HeadPointer >= 9 :
            HeadPointer = 0
        else :
            HeadPointer = HeadPointer + 1
        return removed

for index in range(11) :
    string = input("Enter value :  ")
    Res = Enqueue(string)
    if Res == True :
        print("Data added ")
    else :
        print("failed ! data not added : ")    

for index in range(2) :
    res = Dequeue( )
    print(res)        


