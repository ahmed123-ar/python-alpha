# Q 17 of Booklet

class node:
    def __init__(self) :
        self.data = -1
        self.nextNode = -1

#DECLARE link list

linkedList = [node() for i in range (10)]

linkedList[0].data = 1
linkedList[0].nextNode =1
linkedList[1].data = 5
linkedList[1].nextNode =4
linkedList[2].data = 6
linkedList[2].nextNode =7
linkedList[3].data = 7
linkedList[3].nextNode =-1
linkedList[4].data = 2
linkedList[4].nextNode =2
linkedList[5].data = 0
linkedList[5].nextNode =6
linkedList[6].data = 0
linkedList[6].nextNode =8
linkedList[7].data = 56
linkedList[7].nextNode =3
linkedList[8].data = 0
linkedList[8].nextNode =9
linkedList[9].data = 0
linkedList[9].nextNode =-1

#DECLARE startPointer , emptyList : INTEGER

startPointer = 0
emptyList = 5

def outputNodes(Arr , StartPoint):
    pointer = StartPoint
    while pointer  != -1 :
        print(Arr[pointer].data)
        pointer = Arr[pointer].nextNode

outputNodes(linkedList , startPointer)    

def addNode(Arr , Start , empty) :
    if empty == -1 :
        return False

    Value = int(input("Enter value to add to list"))
    Arr[empty].data = Value
    temp = empty

    if empty ==  0 :
        Start = 0
        empty = 1
        return True
    
    empty = Arr[empty].nextNode
    pointer = Start
    prev = -1
    while pointer != -1 :
        prev = pointer
        pointer = Arr[pointer].nextNode

    Arr[prev].nextNode = temp
    Arr[temp].nextNode = -1

    return True

X = addNode(linkedList , startPointer , emptyList)   
if X == True :
    print("Data added")
else :
    print("Data not added")  



outputNodes(linkedList , startPointer)



