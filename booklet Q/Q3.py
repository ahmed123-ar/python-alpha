# DECLARE TheData : ARRAY [0:8] OF INTEGER

TheData = [20 , 3 , 4 , 8 , 12 , 99 , 4 ,26 , 4]

# def InsertionSort(Arr) : 
#     Max = len(Arr)
#     for index in range(1 , Max) :
#         ItemToBeInserted = Arr[index]
#         CurrentItem = index -1
#         while ItemToBeInserted < Arr[CurrentItem]  and CurrentItem >= 0 :
#             Arr[CurrentItem + 1] = Arr[CurrentItem]
#             CurrentItem = CurrentItem  -1
#         Arr[CurrentItem + 1] = ItemToBeInserted     

#     print(Arr)

   

def InsertionSort(TheData) : 
    for index in range(1 , len(TheData)) :
        DataToInsert = TheData[index]
        inserted = 0
        NextValue = index - 1
        while NextValue >= 0 and inserted != 1 :
            if DataToInsert < TheData[NextValue] :
                TheData[NextValue + 1] = TheData[NextValue]
                NextValue = NextValue - 1
                TheData[NextValue  + 1] = DataToInsert
            else :
                inserted =  1    

def output(Arr) :
    for index in range(len(Arr)) :
        print(Arr[index])                           




# print("the data before sort")
# output(TheData)

# print("the data after sort")
# InsertionSort(TheData) 
# output(TheData)

def Search(TheData) :
    Num = int(input("Enter  Number to search"))
    for index in range(len(TheData)) :
        if Num == TheData[index] :
            print("found")
            return True
        
    print("not found")
    return False    

Search(TheData)
    
