# DECLARE arrayData : ARRAY [0:9] OF INTEGER

arrayData = [10 , 5 , 6 , 7 , 1 , 12 , 13 , 15 , 21 , 8]

def linearSearch(item) :
    global arrayData
    for index in range(10) :
        if item == arrayData[index] :
            return True
    return False 

def bubbleSort():
    global arrayData
    for x in range(len(arrayData) - 1) :
        for y in range(len(arrayData) - 1) :
            if arrayData[y] < arrayData[y+1] :
                temp = arrayData[y]
                arrayData[y] = arrayData[y+1]
                arrayData[y+1] = temp


Value = int(input("Enter vlaue :  "))   
Res = linearSearch(Value) 
if Res == True :
    print("the value was found")
else :
    print("vlaue not found")


