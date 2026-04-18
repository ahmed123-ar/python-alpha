class node :

    # DECLARE data : INTEGER
    # DECLARE nextNode : INTEGER

    def __init__(self , data , next):
        self.data = data
        self.nextnode = next


# DECLARE linkedlist : ARRAY [0:9] OF node
# DECLARE startPointer , emptyList : INTEGER

startPointer = 0
emptyList = 5

linkedList = [node(0 , -1) for index in range(10)] 
linkedList[0].data = 1
linkedList[0].nextnode = 1  
linkedList[1].data = 5
linkedList[1].nextnode = 4
linkedList[2].data = 6
linkedList[2].nextnode = 7
linkedList[3].data = 7
linkedList[3].nextnode = -1
linkedList[4].data = 2
linkedList[4].nextnode = 2
linkedList[5].data = 0
linkedList[5].nextnode = 6
linkedList[6].data = 0
linkedList[6].nextnode = 8
linkedList[7].data = 56
linkedList[7].nextnode = 3
linkedList[8].data = 0
linkedList[8].nextnode = 9
linkedList[9].data = 0
linkedList[9].nextnode = -1

def outputNodes (List , SPointer) :
    CurrentPtr = SPointer
    while CurrentPtr != -1:
        print(List[CurrentPtr].data)
        CurrentPtr = List[CurrentPtr].nextnode


def addNode(list , Spointer , Fpointer) :
    global startPointer, emptyList

    item = int(input("Enter data to add :  "))
    if Fpointer == -1  :
        return False
    else :
        temp = Fpointer
        Fpointer = list[Fpointer].nextnode
        list[temp].data = item
        if Spointer == -1 :
            list[temp].nextnode = Spointer
            Spointer = temp
        else :
            CurrentPointer = Spointer
            while CurrentPointer != -1 :
                PreviousPointer = CurrentPointer
                CurrentPointer = list[CurrentPointer].nextnode
            list[temp].nextnode = CurrentPointer
            list[PreviousPointer].nextnode = temp  
    startPointer = Spointer
    emptyList = Fpointer               
    return True

# outputNodes(linkedList , startPointer)
res = addNode(linkedList , startPointer , emptyList)
if res == True :
    print("the item ios added")
else :
    print("Item not added")    
outputNodes(linkedList , startPointer)




