# add record, write record in file , validation checks with input

def AddRecords() :
    myFile = open("Alpha25.txt" , "a")    # w(write) - overwrite so only one data , a(append) - wite all data no overwrite  , r(read)
    studentID = input("enter student ID : ").upper()

    while len(studentID) != 6 :
        studentID = input("invaild , agian enter student ID : ").upper()

    name = input("Enter name : ").upper()

    while name == "" :
        name = input("please Enter name : ").upper()

    age = int(input("Enter age :"))

    while age < 15 or age > 20 :
        age = int(input("invalid please again enter age :"))

    gender = input("Enter gender : ").upper()

    while gender != "M" and gender != "F" :
        gender = input("invaild please re-enter gender : ").upper()

    info = studentID + " " + name + " " +  str(age) + " " + gender + "\n"
    myFile.write(info)
    myFile.close()



#display records

def displayrecords() :
    myFile = open("Alpha25.txt" , "r")
    info = myFile.readline().strip() #.strip  remove special characters
    while info != "" :
        studentID , name , age , gender = info.split() #split data from spaces
        print(studentID , name )
        info = myFile.readline().strip()

    myFile.close()



#call add records
AddRecords()

#call display records
displayrecords()