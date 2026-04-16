class SaleData :
    # DECLARE Id : STRING
    # DECLARE Quantity : INTEGER
    def __init__(self , id , no):
        self.Id = id 
        self.Quantity = no


# DECLARE CircularQueue : ARRAY [0:4] OF SaleData
# DECLARE Head , Tail , NumberItems : INTEGER

CircularQueue = [SaleData("" , -1)for index in range(5)]
Head = 0
Tail = 0
NumberItems = 0

def Enqueue(record) :
    global CircularQueue , Head , Tail , NumberItems
    if NumberItems == 5 :
        return -1
    else :
        CircularQueue[Tail] = record
        NumberItems = NumberItems + 1
        if Tail == 4 :
            Tail = 0
        else :
            Tail = Tail + 1    
        return 1
    
def Dequeue () :   
    global CircularQueue , Head , Tail , NumberItems 
    if NumberItems == 0 :
        return CircularQueue[Head]
    else :
        removed = CircularQueue[Head]
        NumberItems = NumberItems - 1
        if Head == 4 :
            Head = 0
        else :
            Head = Head + 1  
        return removed     

def EnterRecord() :
    global CircularQueue , Head , Tail , NumberItems 
    id = input("Enter Id  :  ") 
    Quantity = int(input("Enter quantity :  ")) 
    data = SaleData(id , Quantity)
    res = Enqueue(data)
    if res == -1 :
        print("Full")
    else :
        print("Stored") 

EnterRecord()
EnterRecord()
EnterRecord()
EnterRecord()
EnterRecord()
EnterRecord()
Res = Dequeue()
if Res.Id == "" :
    print("Queue is Empty")
else :
    print(Res.Id , Res.Quantity)    
EnterRecord()
for index in range(NumberItems) :
    print(CircularQueue[index].Id , CircularQueue[index].Quantity)
