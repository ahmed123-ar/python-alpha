class node :

    def __init__(self , data , pointer):
        self.data = data
        self.nextNode = pointer

# DECLARE linkedList : ARRAY [0:9] OF INTEGER
# DECALRE startPointer , emptyList : INTEGER

linkedList = [node(0 , -1) for index in range(10)]  

linkedList[0] = node(1 , 1)
linkedList[1] = node(5 , 4)
linkedList[2] = node(6 , 7)
linkedList[3] = node(7 , -1)
linkedList[4] = node(2 , 2)
linkedList[5] = node(0 , 6)
linkedList[6] = node(0 , 8)
linkedList[7] = node(56 , 3)
linkedList[8] = node(0 , 9)
linkedList[9] = node(0 , -1)

startPointer = 0
emptyList = 5

def outputNodes(arr , start) :
    CurrentPointer = start
    while CurrentPointer != -1 :
        print(arr[CurrentPointer].data)
        CurrentPointer = arr[CurrentPointer].nextNode

def addNode(arr , start , free) :
    global startPointer , emptyList
    if free == -1 :
        return True
    else :
        item = int(input("enter data :  "))
        temp = free
        free  =arr[free].nextNode
        arr[temp].data = item
        if start == -1 :
            arr[temp].nextNode = start
            start = temp
        else :
            CurrentPointer = start
            while CurrentPointer != -1 :
                PreviousPointer = CurrentPointer
                CurrentPointer = arr[CurrentPointer].nextNode
            arr[temp].nextNode = CurrentPointer
            arr[PreviousPointer].nextNode = temp   
        startPointer = startPointer
        emptyList = free  
        return True  


print("before")
outputNodes(linkedList , startPointer) 

Res = addNode(linkedList , startPointer , emptyList)
if Res == True :
    print("Success")
else :
    print("unsuccess")  

print("after")
outputNodes(linkedList , startPointer)

