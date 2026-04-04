# file name (Alpha1) . add Id , name , age gender , make add and display function

def add_data(id , name , age , gender) :
    myfile = open("Alpha1.txt" , "a")
    info = id + " " + name + " " + str(age) + " " + gender  + "\n"
    myfile.write(info)
    myfile.close()

add_data("MR1001" , "Ahmed" , 19 , "M")
add_data("MR1002" , "Ali" , 18 , "M")
add_data("MR1003" , "Aisha" , 19 , "F")
add_data("MR1004" , "Bob" , 19 , "M")
add_data("MR1005" , "Tony" , 17 , "M")
add_data("MR1006" , "Ayan" , 20 , "M")

def read_data() :
    myfile = open("Alpha1.txt" , "r")
    info = myfile.readline().strip()
    while info != "" :
        Id , name , age , Gender = info.split()
        print(Id , name )
        info = myfile.readline().strip()

    myfile.close()

read_data()




# create file Alpha2 . add Id , name ,  age  , gender ,marks . and output id , name and marks . apply validation checks

def add_data():
    myfile = open("Alpha2.txt" , "a")

    Id = input("Enter your Id : ").upper()
    while len(Id) != 6 :
        print("Invalid ID ! Enter Again ")
        Id = input("Enter your Id : ").upper()


    Name = input("Enter name :  ").upper()
    while len(Name) <= 2 :
        print("Invalid Name ! Enter Again ")
        Name = input("Enter your name :  ").upper()

    Age = int(input("Enter age :  "))  
    while Age < 15 and Age > 20 :
        print("Invalid Age ! Enter Again ")
        Age = int(input("Enter age :  ")) 

    Gender = input("Enter Gender :  ").upper()    
    while Gender != "M" and Gender != "F" :
        print("Invalid Gender ! Enter Again ")
        Gender = input("Enter Gender :  ").upper()

    Marks = int(input ("Enter Marks :  ") )   
    while Marks < 0 and Marks > 100 :
        print("Invalid Marks ! Enter Again ")
        Marks = int(input ("Enter Marks :  "))

    info = Id + " " + Name + " " + str(Age) + " " + Gender + " " + str(Marks ) + "\n"
    myfile.write(info)
    myfile.close()


add_data()   
add_data() 
add_data() 
add_data() 
add_data() 
add_data() 


def display() :
    myfile = open("Alpha2.txt" , "r")
    info = myfile.readline().strip()
    while info != "" :
        Id , name , age , gender , marks = info.split()
        print(Id , name , marks)
        info=myfile.readline().strip()
    myfile.close()  

display()      






