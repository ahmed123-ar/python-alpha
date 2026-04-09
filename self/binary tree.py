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


