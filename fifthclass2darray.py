# # declaration

myList = [[0,0] for index in range(5)]

# #input names and marks of 5 students and output

for index in range(5):
    Id = input("Enter student ID : ")
    marks = int(input("Enter student marks : "))

    myList[index][0] = Id
    myList[index][1] = marks

print(myList)

#linear search program make function and call it

myList = [[1001,75] , [1002,90] , [1003,45] , [1004,89] , [1005,60]]

def linearsearch(Id) :
    global myList
    index = 0
    while index < 5 :
        if Id == myList[index][0] :
            return myList[index][1]
        else :
            index = index + 1
    return -1        

StudentId = int(input("enter Student Id : ")) 
X = linearsearch(StudentId)
if X == -1 :
    print("Id not found...  ")    
else : 
    print("marks are" , X)           


#bubble sort 2d array
myList = [[1001,75] , [1002,90] , [1003,45] , [1004,89] , [1005,60]]

def bubblesort():
    global myList
    for X in range(0,len(myList)-1):
        for Y in range(0,len(myList)-1):
            if myList[Y][1] > myList[Y+1][1] :
                
                temp = myList[Y][0]
                myList[Y][0] = myList[Y+1][0]
                myList[Y+1][0] = temp

                temp = myList[Y][1]
                myList[Y][1] = myList[Y+1][1]
                myList[Y+1][1] = temp


#display 

def display():
    global myList
    for index in range(5):
        print(myList[index][0] , myList[index][1])


#call bubble sort and display
bubblesort()
display()


# practice question page 1 q1

#DECLARE arrayData : ARRAY [0:9] OF INTEGER

arrayData = [10,5,6,7,1,12,13,15,21,8]

def linearSearch(num) :
    global arrayData
    index=0
    while index < 10 :
        if (num == arrayData[index]) :
            return True
        else :
            index = index + 1
    return False        

num = int(input("Enter a value : "))
x = linearSearch(num)
if x == True :
    print("value found")
else :
    print("Value not found")

    
def bubbleSort() :
    global arrayData
    for x in range(0,len(arrayData)-1) :
        for y in range(0,len(arrayData)-1) :
            if arrayData[y] < arrayData[y+1] :
                temp = arrayData[y]
                arrayData[y] = arrayData[y+1]
                arrayData[y+1] =temp


