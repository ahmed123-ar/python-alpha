class Vehicle() :

    # PRIAVTE ID : STRING
    # PRIVATE MaxSpeed : INTEGER
    # PRIVATE CurrentSpeed : INTEGER
    # PRIVATE IncreaseAmount : INTEGER
    # PRIVATE HorizontalPosition : INTEGER

    def __init__(self, id , maxspeed , increaseAmount):
        self.__ID  = id
        self.__MaxSpeed = maxspeed
        self.__IncreaseAmount = increaseAmount
        self.__CurrentSpeed = 0
        self.__HorizontalPosition = 0

    def GetCurrentSpeed(self) :
        return self.__CurrentSpeed

    def IncreaseAmount(self) :
        return self.__IncreaseAmount
    
    def GetHorizontalPosition(self) :
        return self.__HorizontalPosition
    
    def GetMaxSpeed(self) :
        return self.__MaxSpeed
    
    def SetCurrentSpeed(self , speed) :
        self.__CurrentSpeed = speed

    def SetHorizontalPosition(self , Pos) :
        self.__HorizontalPosition= Pos

    def IncreaseSpeed(self) :
        if self.__CurrentSpeed + self.__IncreaseAmount <= self.__MaxSpeed :
            self.__CurrentSpeed = self.__CurrentSpeed + self.__IncreaseAmount
        else :
            self.__CurrentSpeed = self.__MaxSpeed

        self.__HorizontalPosition = self.__HorizontalPosition + self.__CurrentSpeed    

class Helicopter(Vehicle) :

    # PRIVATE VerticalPosition : INTEGER
    # PRIVATE VerticalChange : INTEGER
    # PRIVATE MaxHeight : INTEGER

    def __init__(self, id, maxspeed, increaseAmount , VertCahnge , MAxHeight):
        super().__init__(id, maxspeed, increaseAmount)
        self.__VerticalPosition = 0
        self.__VerticalChange = VertCahnge
        self.__MaxHeight = MAxHeight

    def GetVerticalPosition(self) :
        return self.__VerticalPosition    

    def IncreaseSpeed(self) :
        if self.__VerticalChange + self.__VerticalPosition  <= self.__MaxHeight :
            self.__VerticalPosition = self.__VerticalPosition + self.__VerticalChange
            
        else :
            self.__VerticalPosition = self.__MaxHeight

        super().IncreaseSpeed()

        # if self.__CurrentSpeed + self.__IncreaseAmount <= self.__MaxSpeed :
        #     self.__CurrentSpeed = self.__CurrentSpeed + self.__IncreaseAmount
        # else :
        #     self.__CurrentSpeed = self.__MaxSpeed

        # self.__HorizontalPosition = self.__HorizontalPosition + self.__CurrentSpeed

def PrintDetails (obj) :
    if isinstance(obj,Helicopter) :
        speed = obj.GetCurrentSpeed()
        HPos = obj.GetHorizontalPosition()
        VPos = obj.GetVerticalPosition()
        print("Speed of vehicle is " , speed , "The horizontal position is " , HPos , "The Vertical Position is" , VPos)
    else :
        speed = obj.GetCurrentSpeed()
        HPos = obj.GetHorizontalPosition()
        print("Speed of vehicle is " , speed , "The horizontal position is " , HPos )

           


Car1 = Vehicle("Lion" , 100 , 20)
Heli1 = Helicopter("Lion" , 350 , 40 , 3 , 100)
Car1.IncreaseSpeed()
Car1.IncreaseSpeed()
Heli1.IncreaseSpeed()
Heli1.IncreaseSpeed()

PrintDetails(Car1)
PrintDetails(Heli1)



    
        
