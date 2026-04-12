class Employee :

    # PRIVATE HourlyPay : REAl
    # PRIVATE EmployeeNumber : STRING
    # PRIVATE JobTitle : STRING
    # PRIVATE PayYear2022 : ARRAY [0:51] OF REAL

    def __init__(self , HourPay , EmployNum , JobTitle):
        self.__EmployeeNumber = EmployNum
        self.__JobTitle = JobTitle
        self.__HourlyPay = HourPay
        self.__PayYear2022 = [0.0 for index in range(52)]

    def GetEmployeeNumber(self) :
        return self.__EmployeeNumber

    def SetPay(self , WeekNo , HrWork) :
        TotalPAy = float(self.__HourlyPay) * HrWork
        self.__PayYear2022[WeekNo - 1] = TotalPAy

    def GetTotalPay(self) :
        Total = 0
        for index in range(52) :
            Total = Total + self.__PayYear2022[index]  
        return Total

class Manager(Employee) :

    # PRIAVTE BonusValue : REAL      

    def __init__(self, HourPay, EmployNum, JobTitle , Bonus):
        super().__init__(HourPay, EmployNum, JobTitle)
        self.__BonusValue = Bonus

    def SetPay(self, WeekNo, HrWork) :
        TotalHr = float(HrWork) * float((1 + (self.__BonusValue / 100)))
        super(). SetPay(WeekNo , TotalHr)

# DECLARE EmployeeArray : ARRAY[0:7] OF Employee


EmployeeArray = []
myfile = open("Employees.txt" , "r")
for index in range(8) :
    Pay = myfile.readline().strip()
    EmpNum = myfile.readline().strip()
    Temp = myfile.readline().strip()
    
    try :
        float(Temp)
        Job = myfile.readline()
        EmployeeArray.append (Manager(Pay , EmpNum , Job , float(Temp)))
    except :
        EmployeeArray.append  (Employee(Pay, EmpNum ,  Temp) )   
myfile.close()       

def EnterHours () :
    myfile = open("HoursWeek1.txt" , "r")
    for x in range(8) :
        IdFile = myfile.readline().strip()
        HrFile = myfile.readline().strip()
        for y in range(8) :
            IdArr = EmployeeArray[y].GetEmployeeNumber()
            if IdFile == IdArr :
                EmployeeArray[y].SetPay(1 , float(HrFile))
                break    

EnterHours()
for index in range(8) :
    print(EmployeeArray[index].GetEmployeeNumber() , " " , EmployeeArray[index].GetTotalPay())






