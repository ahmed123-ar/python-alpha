# DECLARE DataArray : [0:24] OF INTEGER

DataArray = [-1 for index in range(25)]
myfile = open("Data.txt" , "r")
for index in range(25) :
    DataArray[index] = int(myfile.readline().strip())


def PrintArray(Arr) :
    Out = ""
    for index in range(len(Arr)) :
        Out = Out + "  " + str(Arr[index])
    print(Out)

PrintArray(DataArray)

def LinearSearch(Arr , Value) :
    Repeat = 0
    for index in range(len(Arr)) :
        if Arr[index] == Value :
            Repeat = Repeat + 1
    return Repeat        

Num = int(input("Enter a number between 0 and 100 inclusive  :  "))
while Num < 0 or Num > 100 :
    print("Enter again ")
    Num = int(input("Enter a number between 0 and 100 inclusive  :  "))
print("Number validated")
Res = LinearSearch(DataArray , Num)
print("The number " , Num , "is found" , Res , "times")    
