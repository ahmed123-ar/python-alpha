# link list by 2 1D arrays

ListData = ["" for index in range(10)]
ListPtr = [-1 for index in range(10)]
for index in range(9) :
    ListPtr[index] = index + 1
ListPtr[9] = -1
StartPtr = -1
FreePtr = 0

def delete(item) :
    global ListData , ListPtr , StartPtr , FreePtr
    CurrentPtr = StartPtr
    Found = False
    while CurrentPtr != - 1 and Found == False :
        if ListData[CurrentPtr] == item :
            Found = True
        else :
            PreviousPointer = CurrentPtr
            CurrentPtr = ListPtr[CurrentPtr] 
    if CurrentPtr != -1 :
        if CurrentPtr == StartPtr :
            StartPtr = ListPtr[CurrentPtr]
        else :
            ListPtr[PreviousPointer] = ListPtr[CurrentPtr]
        ListPtr[CurrentPtr] = FreePtr
        FreePtr = CurrentPtr

def insert(item) :
    global ListData , ListPtr , StartPtr , FreePtr
    if FreePtr == -1 :
        print("No space in list")
    else :
        temp = FreePtr
        FreePtr = ListPtr[FreePtr]
        ListData[temp] = item 
        if StartPtr == -1 or item < ListData[StartPtr] :
            ListPtr[temp] = StartPtr
            StartPtr = temp
        else :
            CurrentPointer = StartPtr
            while CurrentPointer != -1 and item > ListData[CurrentPointer] :
                PreviousPtr =  CurrentPointer
                CurrentPointer = ListPtr[CurrentPointer]
            ListPtr[temp] = CurrentPointer
            ListPtr[PreviousPtr] = temp  

insert("m")
insert("x")
insert("f")
insert("r")
insert("d")
insert("p")
insert("k")
delete("d")
print(ListData)
print(ListPtr)
print(StartPtr)
print(FreePtr)

        




