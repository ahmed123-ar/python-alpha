# DECLARE TheData : ARRAY [0 : 8] OF INTEGER

TheData = [20 , 3 , 4 , 8 , 12 , 99 , 4 , 26 , 4]

def InsertionSort(Array) :
    for index in range(1 , len(Array)) :
        DataToInsert = Array[index]
        Inserted = 0
        NextValue = index - 1
        while NextValue >= 0 and Inserted != 1 :
            if DataToInsert < Array[NextValue] :
                Array[NextValue + 1] = Array[NextValue]
                NextValue = NextValue - 1
                Array[NextValue + 1] = DataToInsert
            else :
                Inserted = 1 

def Output(Array) :
    for index in range(len(Array)) :
        print(Array[index])    

print("Before sorting")                       
Output(TheData)
InsertionSort(TheData)

print("After Sorting")
Output(TheData)

def SeachArray(Array) :
    Num = int(input("Enter a number :  "))
    for index in range(len(Array)) :
        if Num == Array[index] :
            print("found")
            return True
    print("Not Found")
    return False 

SeachArray(TheData)       

