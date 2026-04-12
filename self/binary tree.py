# tree through 3 1D arrays

# DECLARE Tree : ARRAY[0:9] OF STRING
# DECLARE Left : ARRAY[0:9] OF INTEGER
# DECLARE Right : ARRAY[0:9] OF INTEGER

Data = ["" for index in range(10)]
Left = [-1] * 10
Right = [1,2,3,4,5,6,7,8,9,-1]
RootPtr = -1
FreePtr = 0

def SearchTree (item) :
    global Data , Left , Right , RootPtr , FreePtr
    currentPtr = RootPtr
    while currentPtr !=  -1 :
        if Data[currentPtr] == item :
            return currentPtr
        elif Data[currentPtr] > item :
            currentPtr = Left[currentPtr]
        else :
            currentPtr = Right[currentPtr] 
    return -1



def insert(item) :
    global Data , Left , Right , RootPtr , FreePtr
    if FreePtr == -1 :
        print("Tree is full")
    else :
        temp = FreePtr
        FreePtr = Right[FreePtr]
        Data[temp] = item
        Left[temp] = -1
        Right[temp] = -1
        if RootPtr == -1 :
            RootPtr = temp
        else :
            CurrentPtr = RootPtr
            while CurrentPtr != -1  :
                PrevPtr = CurrentPtr
                if item > Data[CurrentPtr] :
                    Flag = True
                    CurrentPtr = Right[CurrentPtr]
                else :
                    Flag = False
                    CurrentPtr = Left[CurrentPtr]
            if Flag == True :
                Right[PrevPtr] =  temp
            else :
                Left[PrevPtr] = temp


insert("m")
insert("r")
insert("b")
insert("f")
insert("a")
insert("x")
insert("y")
insert("p")
print(Data)
print(Left)
print(Right)
print(RootPtr)
print(FreePtr)
x= SearchTree("y")
print(x)






# Tree by record data type

class Tree :

    def __init__(self):
        self.LeftPtr = -1
        self.Data = ""
        self.RightPtr = -1

# DECLARE BinaryTree : ARRAY [0:9] [0:2] OF Tree
# DECLARE RootPtr : INTEGER
# DECLARE FreePtr : INTEGER

BinaryTree = [Tree() for index in range(10)]
for index in range(9) :
    BinaryTree[index].RightPtr = index + 1
BinaryTree[9].RightPtr = -1

RootPtr = -1
FreePtr = 0

def SearchTree (item) :
    global RootPtr , FreePtr , BinaryTree
    CurrentPtr = RootPtr
    while CurrentPtr != -1 :
        if BinaryTree[CurrentPtr].Data == item :
            return CurrentPtr
        elif BinaryTree[CurrentPtr].Data < item :
            CurrentPtr = BinaryTree[CurrentPtr].RightPtr
        else :
            CurrentPtr = BinaryTree[CurrentPtr].LeftPtr
    return False

def insert(item) :
    global RootPtr , FreePtr , BinaryTree
    if FreePtr == -1 :
        return False
    else :
        Temp = FreePtr
        FreePtr = BinaryTree[FreePtr].RightPtr
        BinaryTree[Temp].Data = item
        BinaryTree[Temp].LeftPtr = -1
        BinaryTree[Temp].RightPtr = -1
        if RootPtr == -1 :
            RootPtr = Temp
        else :
            CurrentPtr = RootPtr
            while CurrentPtr != -1 :
                PreviousPtr = CurrentPtr
                if BinaryTree[CurrentPtr].Data < item :
                    Flag = True
                    CurrentPtr = BinaryTree[CurrentPtr].RightPtr
                else :
                    Flag = False   
                    CurrentPtr = BinaryTree[CurrentPtr].LeftPtr
            if Flag == True :
                BinaryTree[PreviousPtr].RightPtr = Temp
            else :
                BinaryTree[PreviousPtr].LeftPtr = Temp                 


insert("m")
insert("r")
insert("b")
insert("f")
insert("a")
insert("x")
insert("y")
insert("p")
for index in range(10) :
    print(BinaryTree[index].LeftPtr , BinaryTree[index].Data ,BinaryTree[index].RightPtr )

print(RootPtr)
print(FreePtr)
x= SearchTree("y")
print(x)