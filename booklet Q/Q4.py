# DECLARE TheData : ARRAY [0 : 9] [0 : 9] OF INTEGER
import random
TheData = [ [0,0,0,0,0,0,0,0,0,0] for index in range(10)]
for x in range(10) :
    for y in range(10) :
        TheData[x][y] = random.randint(1 , 100)

def output(arr) :
    for x in range(10) :
        print(arr[x][0] , "" , arr[x][1] , "" , arr[x][2] , "" , arr[x][3] , "" , arr[x][4] , "" , arr[x][5] , "" , arr[x][6] , "" , arr[x][7] , "" , arr[x][8] , "" , arr[x][9]  )
print("before")
output(TheData)

ArrayLength = 10
for x in range(ArrayLength) :
    for y in range(ArrayLength - 1) :
        for z in range(ArrayLength - y - 1) :
            if TheData[x][z] > TheData[x][ z+ 1] :
                TempValue = TheData[x] [z]
                TheData[x][z] = TheData[x] [z + 1]
                TheData[x] [z + 1] = TempValue

print("after")
output(TheData)


def BinarySearch (Arr , lower , upper , SearchItem) :
    if upper >=  0 :
        Mid =int((lower + ( upper - 1)) / 2)
        if Arr[0][Mid] == SearchItem :
            return Mid
        else :
            if Arr[0][Mid] > SearchItem : 
                return BinarySearch(Arr , lower , Mid - 1 , SearchItem)
            else :
                return BinarySearch(Arr , Mid + 1 , upper , SearchItem)
    return -1        

num1 = int(input("Enter the number : "))
num2 = int(input("Enter the number : "))
Res1 = BinarySearch(TheData , 0 , len(TheData) - 1 ,num1)      
Res2 = BinarySearch(TheData , 0 , len(TheData) - 1 ,num2)      
print(Res1)
print(Res2)
