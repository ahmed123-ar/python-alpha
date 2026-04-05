# linear search 

# DECLARE StudentData :ARRAY [0 : 9] [0 : 1 ] OF INTEGER

StudentData = [[0,0] for index in range(10)]

StudentData = [[1001,65] , [1002,91] , [1003,56] , [1004,76] , [1005,91] , [1006,67] , [1007,65] , [1008,45] , [1009,90] , [1010,83]]
Search = int(input("Enter Id :  "))
flag = False
index = 0
while index < len(StudentData) :
    if Search == StudentData[index][0] :
        flag = True
        break
    else :
        index = index +1
if flag == True :
    print(Search , StudentData[index][1])
else :
    print("Marks not found")



# bubble sort

# DECLARE StudentData :ARRAY [0 : 9] [0 : 1 ] OF INTEGER

StudentData = [[0,0] for index in range(10)]
StudentData = [[1001,65] , [1002,91] , [1003,56] , [1004,76] , [1005,91] , [1006,67] , [1007,65] , [1008,45] , [1009,90] , [1010,83]]
for x in range(len(StudentData) - 1) :
    for y in range(len(StudentData) - 1) :
        if StudentData[y][1] < StudentData[y + 1][1]:
            temp = StudentData[y + 1][1]
            StudentData[y + 1][1] = StudentData[y][1]
            StudentData[y][1] = temp

            temp = StudentData[y + 1][0]
            StudentData[y + 1][0] = StudentData[y][0]
            StudentData[y][0] = temp







#binary search

# DECLARE StudentData :ARRAY [0 : 9] [0 : 1 ] OF INTEGER

StudentData = [[0,0] for index in range(10)]
StudentData = [[1001,65] , [1002,91] , [1003,56] , [1004,76] , [1005,91] , [1006,67] , [1007,65] , [1008,45] , [1009,90] , [1010,83]]
flag = False
top = 0
bottom = len(StudentData)-1
Search = int(input("Enter ID :  "))
while top <= bottom :
    middle = int((top+bottom)/2)
    if Search == StudentData[middle][0] :
        flag = True
        break
    elif Search > StudentData[middle][0] : 
        top = middle + 1
    else :
        bottom = middle - 1
if flag == True :
    print(Search , StudentData[middle][1])
else :
    print("marks not found")             

# insertion sort

# DECLARE StudentData :ARRAY [0 : 9] [0 : 1 ] OF INTEGER

StudentData = [[0,0] for index in range(10)]
StudentData = [[1001,65] , [1002,91] , [1003,56] , [1004,76] , [1005,91] , [1006,67] , [1007,65] , [1008,45] , [1009,90] , [1010,83]]

max = len(StudentData)
for index in range(1 , max) :
    ItemToBeInserted1 = StudentData[index][1]
    ItemToBeInserted2 = StudentData[index][0]
    CurrentPointer = index - 1
    while StudentData[CurrentPointer][1] < ItemToBeInserted1 and CurrentPointer >= 0:
        StudentData[CurrentPointer + 1][1] = StudentData[CurrentPointer][1]
        StudentData[CurrentPointer + 1][0] = StudentData[CurrentPointer][0]
        CurrentPointer = CurrentPointer - 1

    StudentData[CurrentPointer + 1][1] = ItemToBeInserted1
    StudentData[CurrentPointer + 1][0] = ItemToBeInserted2
print(StudentData)    
