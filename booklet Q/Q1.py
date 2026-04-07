# DECLARE arrayData : ARRAY [0:9] OF INTEGER

arrayData = [ 10 , 5 ,6 , 7 , 1 ,12 ,13 , 15 , 21 ,8]

def linearSearch(integer) :
    global arrayData
    for index in range(10) :
        if arrayData[index] == integer :
            return True
    return False
Num = int(input("Enter number to search  "))
Ans = linearSearch(Num)
if Ans == True :
    print("Value have been found")
else :
    print("value not found")    

  
def bubbleSort() :
    global arrayData
    for x in range(len(arrayData) - 1):
        for y in range(len(arrayData) - 1) :
            if arrayData[y] < arrayData[y+1] :
                temp = arrayData[y]
                arrayData[y] = arrayData[y+1]
                arrayData[y+1]  =temp
    print(arrayData)

bubbleSort()                

   

    