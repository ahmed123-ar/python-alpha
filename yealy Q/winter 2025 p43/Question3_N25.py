def RecursiveCount(ArrayCopy , NumberElements , DataToFind) :
    if NumberElements == 0:
        return 0
    if ArrayCopy[0] == DataToFind :
        return 1 + RecursiveCount(ArrayCopy[1:] , NumberElements - 1 , DataToFind)
    else :
        return RecursiveCount(ArrayCopy[1:] , NumberElements - 1 , DataToFind)


MyArray = [0,5,1,2,5,9,9,6,5,0]     
print(RecursiveCount(MyArray , 10 , 5))

MyString = "x=0;y=1;x=x+y;y++;"

def SplitData(string) :
    index = 0
    while index < len(string):
        line = ""
        while index < len(string) and string[index] != ";" :
            line = line  + string[index]
            index = index + 1
        
        print(line)
        index = index + 1
        

SplitData(MyString)     
print(MyString[3])           
