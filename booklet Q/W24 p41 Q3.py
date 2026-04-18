# DECLARE LinkedList : ARRAY [0:19] [0:1] OF INTEGER
# DECLARE FirstNode , FirstEmpty : INTEGER

FirstNode = -1
FirstEmpty = 0
LinkedList = [[-1 , -1] for index in range(20)]

for index in range(19) :
    LinkedList[index][1] = index + 1
LinkedList[19][1] = -1


def InsertData() :
    global FirstNode , FirstEmpty , LinkedList
    for index in range(5) :
        item = int(input("Enter number : "))

        if FirstEmpty != -1 :
            temp = FirstEmpty
            FirstEmpty = LinkedList[FirstEmpty][1]
            LinkedList[temp][0] = item
            LinkedList[temp][1] = FirstNode
            FirstNode = temp


def OutputLinkedList() :
    global FirstNode , FirstEmpty , LinkedList
    current = FirstNode
    while current != -1 :
        print(LinkedList[current][0])
        current = LinkedList[current][1]


def RemoveData(item) :
    global FirstNode , FirstEmpty , LinkedList
    current = FirstNode
    found = False
    while found == False and current != -1 :
        if LinkedList[current][0] == item :
            found  = True
        else :
            previous = current
            current = LinkedList[current][1]
    if current != -1 :
        if FirstNode == current :
            FirstNode = LinkedList[current][1]
        else :
            LinkedList[previous][1] = LinkedList[current][1]

        LinkedList[current][1] = FirstEmpty
        FirstEmpty = current      



InsertData()
OutputLinkedList()
RemoveData(5)
print("after")
OutputLinkedList()  
     








