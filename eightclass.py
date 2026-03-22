# OOP

class students :
    
    # PRIVATE StudentID : STRING
    # PRIVATE NAME : STRING
    # PRIVATE AGE : INTEGER

    def __init__(self):
        self.__StudentId = ""
        self.__Name = ""
        self.__Age = 0

    def SetId(self , i) :
        self.__StudentId = i 

    def SetName(self , n):
        self.__Name = n

    def SetAge(self , a):
        self.__Age = a

    def GetId(self):
        return self.__StudentId

    def GetName(self):
        return self.__Name

    def GetAge(self) :
        return self.__Age 

    def Display(self) :
        print ("Student ID : " , self.__StudentId)
        print("Name        : " , self.__Name)
        print("Age         : " , self.__Age)  

class subjects(students):
    
    # PRIVATE Sub1 : INTEGER
    # PRIVATE Sub2 : INTEGER
    # PRIVATE Sub3 : INTEGER

    def __init__(self):
        super().__init__()
        self.__Sub1 =  0
        self.__Sub2 =  0
        self.__Sub3 =  0

    def  setSub(self , s1 , s2 ,  s3):
        self.__Sub1 = s1  
        self.__Sub2 = s2
        self.__Sub3 = s3  

    def GetSub1(self):
        return self.__Sub1 

    def GetSub2(self):
        return self.__Sub2

    def GetSub3(self):
        return self.__Sub3     
    
    def Display(self):
        super().Display()
        print("Subject one is : ",  self.__Sub1)
        print("Subject two is : ",  self.__Sub2)
        print("Subject three is : ",  self.__Sub3)

# variable of that class

Student = students()  
Student.SetId("MR1001")
Student.SetName("Ahmed")
Student.SetAge(19)
Student.Display()    

# array of that class only using students

myList = [students() for index in range(3)]

for index in range(3) :
    id = input("Enter Student ID : ")
    name = input("Enter name : ")
    age = int(input("Enter age :"))
    myList[index].SetId(id)
    myList[index].SetName(name)
    myList[index].SetAge(age)

for index in range(3) :
    print(myList[index].GetId() , myList[index].GetName() , myList[index].GetAge() )    


# array of subjects so both classess used students and subjects    

myList = [subjects() for index in range(3)]

for index in range(3) :

    id = input("Enter Student ID : ")
    name = input("Enter name : ")
    age = int(input("Enter age :"))
    s1 = int(input("Enter subject 1 : "))
    s2 = int(input("Enter subject 2 : "))
    s3 = int(input("Enter subject 3 : "))

    myList[index].SetId(id)
    myList[index].SetName(name)
    myList[index].SetAge(age)
    myList[index].setSub(s1 , s2 , s3)

for index in range(3) :
    print(myList[index].GetId() , myList[index].GetName() , myList[index].GetAge() , myList[index].GetSub1() , myList[index].GetSub2() , myList[index].GetSub3() )    