# DECALRE Jobs : ARRAY [0:99] [0:1] OF INTEGER
# DECALRE NumberOfJobs : INTEGER

def initialise() :
    global Jobs ,  NumberOfJobs
    NumberOfJobs = 0
    Jobs = [[-1 , -1] for index in range(100)]
    NumberOfJobs = 0


def AddJob (jobNo , priority)  :
    global Jobs ,  NumberOfJobs
    try :
        Jobs[NumberOfJobs][0] = jobNo
        Jobs[NumberOfJobs][1] = priority
        NumberOfJobs = NumberOfJobs + 1
        print("added")
    except :
        print("not added") 

def InsertionSort() :
    global Jobs ,  NumberOfJobs
    for index in range(1 , NumberOfJobs) :
        item0 = Jobs[index][0]
        item1 = Jobs[index][1]
        current = index -1
        while current >= 0 and item1 < Jobs[current][1] :
            Jobs[current + 1][1] =Jobs[current][1]
            Jobs[current + 1][0] =Jobs[current][0]
            current = current - 1
        Jobs[current + 1][1] = item1
        Jobs[current + 1][0] = item0     


def PrintArray() :
    global Jobs ,  NumberOfJobs
    for index in range(NumberOfJobs) :
        print(Jobs[index][0] , " " , " priority" , " " , Jobs[index][1])


initialise()    

AddJob(12,10)
AddJob(526,9)
AddJob(33,8)
AddJob(12,9)
AddJob(78,1)
InsertionSort()
PrintArray()



