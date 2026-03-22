# scenario student id and its marks - record data type
class students:
    def __init__(self):
        self.studentID = ""
        self.Marks = 0

# make array of that record data type

myList = [students() for index in range(5)]

#input in array of that record data type OR initialize it one by one

myList[0].studentID = "MR1001"
myList[0].Marks = 54
myList[1].studentID = "MR1002"
myList[1].Marks = 34
myList[2].studentID = "MR1003"
myList[2].Marks = 67
myList[3].studentID = "MR1004"
myList[3].Marks = 89
myList[4].studentID = "MR1005"
myList[4].Marks = 99


for index in range(5):
    myList[index].studentID = input("Enter student ID : ").upper()
    myList[index].Marks = input("Enter Student Marks : ")

#display array of that record data type     

def display():
    global myList
    for index in range(5):
        print(myList[index].studentID , myList[index].Marks)

#call display function
# display()

#linearsearch take steudent id as parameter return marks/-1

def LinearSearch(ID):
    global myList
    for index in range(5):
        if (myList[index].studentID == ID) :
            return myList[index].Marks
    return -1

id = input("Enter Student ID : ").upper()
x = LinearSearch(id) 
if x == -1   :
    print("student id not found")
else : 
    print("marks" , x)


# bubble sort highest to lowest on marks method 1 

def BubbleSort() :
    global myList
    for x in range(len(myList) - 1) :
        for y in range(len(myList) - 1):
            if (myList[y].Marks < myList[y+1].Marks):
                temp1 = myList[y].Marks
                myList[y].Marks = myList[y+1].Marks
                myList[y+1].Marks=temp1

                temp1 = myList[y].studentID
                myList[y].studentID = myList[y+1].studentID
                myList[y+1].studentID=temp1

# bubble sort highest to lowest on marks method 2

def BubbleSort() :
    global myList
    temp = students()
    for x in range(len(myList) - 1) :
        for y in range(len(myList) - 1):
            if (myList[y].Marks < myList[y+1].Marks):
                temp = myList[y]
                myList[y]= myList[y+1]
                myList[y+1]=temp



BubbleSort()
display()


