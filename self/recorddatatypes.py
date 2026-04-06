# scenario ID, name, age , gender , marks for record data type. make a varible of that record data type

class student :
    def __init__ (self , ID , Name , Age , Gender , Marks) :
        self.studentID = ID
        self.Name = Name
        self.Age = Age
        self.Gender = Gender
        self.Marks = Marks

# DECLARE student1 , student2 :student

student1 = student("MR1001" , "Ahmed" , 19 , "M" , 90)
student2 = student("MR1002" ,  "Ali" , 16   , "M"  , 87)
print(student1.studentID , student1.Name , student1.Age , student1.Gender , student1.Marks)








# scenario ID, name, age , gender , marks for record data type. make array of that record type

class student :
    def __init__(self) :
        self.ID = ""
        self.name = ""
        self.age = 0
        self.gender = ""
        self.mark = 0

# DECLARE List : ARRAY [0:4] OF student

List = [student() for index in range(5)]

List[0].ID = "MR1001"
List[0].name = "Ahmed"
List[0].age =19
List[0].gender = "M"
List[0].mark = 76
List[1].ID = "MR1002"
List[1].name = "Aisha"
List[1].age =21
List[1].gender = "F"
List[1].mark = 89
List[2].ID = "MR1003"
List[2].name = "Ayan"
List[2].age =17
List[2].gender = "M"
List[2].mark = 45
List[3].ID = "MR1004"
List[3].name = "Amna"
List[3].age =18
List[3].gender = "F"
List[3].mark = 66
List[4].ID = "MR1005"
List[4].name = "Hamza"
List[4].age =18
List[4].gender = "M"
List[4].mark = 91

def linearSearch(id) :
    global List
    flag = False
    for index in range(5) :
        if id == List[index].ID :
            print(List[index].ID , List[index].name , List[index].mark)
            flag = True
            break
    if flag == False :
        print("Marks not available")


def BubbleSort() :
    global List
    for x in range(len(List) - 1) :
        for y in range(len(List) - 1) :
            if List[y].mark < List[y+1].mark :
                temp = List[y+1].mark
                List[y+1].mark = List[y].mark
                List[y].mark = temp

                temp = List[y+1].ID
                List[y+1].ID = List[y].ID
                List[y].ID = temp

                temp = List[y+1].name
                List[y+1].name = List[y].name
                List[y].name = temp

                temp = List[y+1].age
                List[y+1].age = List[y].age
                List[y].age = temp

                temp = List[y+1].gender
                List[y+1].gender = List[y].gender
                List[y].gender = temp

    for index in range(5) :
        print(List[index].ID , List[index].name , List[index].age , List[index].gender , List[index].mark)


def BinarySearch(Id) :
    global List
    top = 0
    bottom = len(List) - 1
    while top <= bottom:
        middle = int((top+bottom)/2)
        if Id == List[middle].ID :
            return middle
        elif Id > List[middle].ID :
            top = middle + 1
        else :
            bottom = middle - 1
    return -1

def InsertionSort() :
    global List
    Max = len(List) 
    for index in range ( 1 , Max ) :
        ItemToBeInsertedM = List[index].mark
        ItemToBeInsertedI = List[index].ID
        ItemToBeInsertedN = List[index].name
        ItemToBeInsertedA = List[index].age
        ItemToBeInsertedG = List[index].gender
        CurrentItem = index - 1
        while List[CurrentItem].mark < ItemToBeInsertedM and CurrentItem >= 0 :
            List[CurrentItem + 1].mark = List[CurrentItem].mark
            List[CurrentItem + 1].ID = List[CurrentItem].ID
            List[CurrentItem + 1].name = List[CurrentItem].name
            List[CurrentItem + 1].age = List[CurrentItem].age
            List[CurrentItem + 1].gender = List[CurrentItem].gender
            CurrentItem = CurrentItem - 1
        List[CurrentItem + 1].mark = ItemToBeInsertedM
        List[CurrentItem + 1].ID = ItemToBeInsertedI
        List[CurrentItem + 1].name = ItemToBeInsertedN
        List[CurrentItem + 1].age = ItemToBeInsertedA
        List[CurrentItem + 1].gender = ItemToBeInsertedG 

    for index in range(5) :
       print(List[index].ID , List[index].name , List[index].age , List[index].gender , List[index].mark)

        