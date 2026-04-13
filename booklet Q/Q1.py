# DECLARE ArrayData : ARRAY [0:9] OF INTEGER

ArrayData = [10 , 5 , 6 , 7 , 1 , 12 , 13 , 15 , 21 , 8]

def linearSearch (item) :
    global ArrayData
    for index in range(10) :
        if ArrayData[index] == item :
            return True
    return False

Num = int(input("Enter a number : "))
Res = linearSearch(Num)
if Res == True :
    print("The number was found")
else :
    print("The number was not found")


def bubbleSort() :
    global ArrayData
    for x in range(len(ArrayData) - 1):
         for y in range(len(ArrayData) - 1):
             if ArrayData[y] < ArrayData[y+1] :
                 temp = ArrayData[y]
                 ArrayData[y] = ArrayData[y+1]
                 ArrayData[y+1] = temp


bubbleSort()
print(ArrayData)
