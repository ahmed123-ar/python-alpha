#DECLARE MyList  : ARRAY [0:4] oF STRING

# initilaze with empty string
MyList = ["" for index in range(4)]


# put 5 names in it

MyList = [ "Ahmed" , "Minhas" , "Ali" , "Ayan"]

#print list items

MyList = [ "Ahmed" , "Minhas" , "Ali" , "Ayan"]
for index in range(4) :
    print(MyList[index])


#linear search . searching ID im MyList . Do declare and inintialize

# DECLARE MyList : ARRAY [0 : 9] OF STRING

MyList = ["" for index in range(10)] 

MyList = ["MR1001" , "MR1002" , "MR1003" , "MR1004" , "MR1005" , "MR1006" , "MR1007" , "MR1008" , "MR1009" , "MR1010"]

Search = input("Enter ID to search : ").upper()

index = 0

found = False

while index < len(MyList) :
    if Search == MyList[index] :
        found = True
        break
    else :
        index = index +1
if found == True :
    print(Search , " found at position" , index)
else:
    print("ID not found ")    


# bubble sort marks array . Do declaration and initialization

# DECLARE Marks : ARRAY [0 : 9] OF INTEGER

Marks = [-1 for index in range(10)]

Marks = [56 , 67 , 45 , 89 , 45 , 90 , 23 , 75 , 55 , 91]

for x in range(len(Marks) - 1):
    for y in range(len(Marks) - 1):
        if Marks[y] < Marks[y+1] :
            temp = Marks[y+1]
            Marks[y+1] = Marks[y]
            Marks[y] = temp
  


#binary search

# DECLARE Marks : ARRAY [0 : 9] OF INTEGER

Marks = [-1 for index in range(10)]

Marks = [23, 35, 45, 55, 56, 67, 75, 89, 90, 91]
flag = False
top = 0
bottom = len(Marks) - 1 
Search = int(input("Enter Marks to Search "))
while top <= bottom :
    middle = int((top+bottom) / 2)
    if Marks[middle] == Search :
        flag = True
        break
    elif Search > Marks[middle] :
        top = middle + 1
    else :
        bottom = middle - 1

if flag == True :
    print(Search , "found at position" , middle)
else:
    print("Marks not found")

# insertion sort   

# DECLARE Marks : ARRAY [0 : 9] OF INTEGER

Marks = [-1 for index in range(10)]
Marks = [56 , 67 , 35 , 89 , 45 , 90 , 23 , 75 , 55 , 91]

Max = len(Marks)
for index in range(1,Max) :
    ItemToBeInserted = Marks[index]
    CurrentItem = index - 1
    while Marks[CurrentItem] > ItemToBeInserted and CurrentItem >= 0 :
        Marks[CurrentItem + 1] = Marks[CurrentItem]
        CurrentItem = CurrentItem - 1
    Marks[CurrentItem + 1] = ItemToBeInserted
    

 




