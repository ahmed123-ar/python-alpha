# studebt subject 

class student :
     # PRIVATE ID : STRING
     # PRIVATE Name : STRING
     #PRIVATE Age : INTEGER
     #PRIVATE Gender : STRING

    def __init__(self):
        self.__ID = ""
        self.__Name = ""
        self.__Age = 0
        self.__Gender = ""

    def SetId(self , Id) :
        self.__ID = Id 

    def SetName(self , Name) :
        self.__Name = Name

    def SetAge(self , Age) :
        self.__Age = Age

    def SetGender(self , Gend) :
        self.__Gender = Gend

    def GetName(self) :
        return self.__Name  

    def GetAge(self) :
        return self.__Age  

    def GetId(self) :
        return self.__ID  

    def GetGend(self) :
        return self.__Gender

    def Display(self) :
        print("ID : " , self.__ID , "Name : " , self.__Name , "Age : " , self.__Age , "Gender : " , self.__Gender)   

class Subject(student) :

    # PRIVATE Sub1 = INTEGER
    # PRIVATE Sub2 = INTEGER
    # PRIVATE Sub3 = INTEGER    

    def __init__(self):
        super().__init__()
        self.__Sub1 = 0
        self.__Sub2 = 0
        self.__Sub3 = 0

    def setSub(self , s1 , s2 , s3) :
        self.__Sub1 = s1
        self.__Sub2 = s2
        self.__Sub3 = s3



    def getsub1(self) :
        return self.__Sub1 

    def getsub2(self) :
        return self.__Sub2 

    def getsub3(self) :
        return self.__Sub2    

    def Display(self):
        super().Display()  
        print("subject 1 : " , self.__Sub1 , "Subject 2 : " , self.__Sub2 , "Subject 3 : " , self.__Sub3)  

Student1 = student()
Student1.SetId("MR1001")
Student1.SetName("Ahmed")
Student1.SetAge(18)
Student1.SetGender("M")


# make array of student

# myList = [student() for index in range(3)]

# for index in range(3) :
#     Id = input("enter student id  ")
#     name = input("entrt student name  ")
#     age = int(input("enter student age  "))
#     gender = input("enter gender  ")
#     myList[index].SetId(Id)
#     myList[index].SetName(name)
#     myList[index].SetAge(age)
#     myList[index].SetGender(gender)

# for index in range(3) :
#     myList[index].Display()

#make array of subject

myList =  [Subject() for index in range(2)]

for index in range(2) :
    Id = input("enter student id  ")
    name = input("entrt student name  ")
    age = int(input("enter student age  "))
    gender = input("enter gender  ")
    s1 = input("enter subject code one  ")
    s2 = input("enter subject code two  ")
    s3 = input("enter subject code three  ")
    myList[index].SetId(Id)
    myList[index].SetName(name)
    myList[index].SetAge(age)
    myList[index].SetGender(gender)
    myList[index].setSub(s1,s2,s3)

for index in range(2) :
    print(myList[index].Display())    









