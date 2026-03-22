# array - list is made into array - list traeted as array

#declare myList : ARRAY [0:4] OF STRING

#initialise with string
myList = ["" for index in  range(5)] 

#initialse with -1
myList = [-1 for index in range(5)]

#print myList
myList = ["minhas" , "ahmed" , "ali" , "esha" ,"ayan"]
print(myList)

#print myList through loop
myList = ["minhas" , "ahmed" , "ali" , "esha" ,"ayan"]
for index in range(5) :
    print(myList[index])

#input names in list and display in upper case

#declare myList : ARRAY [0:4] OF STRING
myList = ["" for index in  range(5)] 
for index in range(5) :
    name = input("enter name ")
    myList[index] = name.upper()
print(myList)


#linear search with for loop
myList = ["minhas" , "ali" , "amna" , "ali" , "kamran"]
found = False
name = input("enter name to search")
for index in range(5) :
    if name.lower() == myList[index]:
        found = True
        break
if found == False :
    print("not found")
else :
    print(name , "found at position " , index)        


#linear search with while loop
myList = ["minhas" , "ali" , "amna" , "asim" , "kamran"]
found = False
index = 0
name = input("enter name to search ")
while found == False and index < 5 :
    if name.lower() == myList[index] :
        found = True
    else :
        index = index + 1
if found == False :
    print("not found")
else :
    print(name , "found at" , index)   


#linear search function  
myList = ["minhas" , "ali" , "amna" , "kamran" , "asim"] 

def LinearSearch(name) :
    global myList   #using global myList
    index = 0
    while index < 5 :
        if name == myList[index] :
            return index
        else :
            index = index + 1
    return -1

# calling function in main program  
name = input("enter name to search")
x = LinearSearch(name)
if x == -1 :
    print("name not found")
else:
    print(name , "found at" , x)         



#bubble sort through procedure
myList = [45 , 15 , 5 , 35 , 25 , 95 , 55 , 85 , 65 , 75]

def bubblesort() :
    global myList
    for x in range(len(myList) - 1) :
        for y in range(len(myList) - 1) :
            if myList[y] > myList[y+1] :
                temp = myList[y]
                myList[y] = myList[y+1]
                myList[y+1] = temp

#call in main program
print(myList) #before
bubblesort()
print(myList) #after

