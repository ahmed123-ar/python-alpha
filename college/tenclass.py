# winter 2023 p41 q3

class Character :
    
    # PRIVATE Name : STRING
    # PRIVATE XPosition : INTEGER
    # PRIVATE YPosition :INTEGER

    def __init__(self , name , XPos , YPos) :
        self.__Name = name
        self.__XPosition = XPos
        self.__YPosition = YPos

    def GetXPosition(self) :
        return self.__XPosition

    def GetYPosition(self) :
        return self.__YPosition

    def SetXPosition(self , valueX) :
        self.__XPosition = self.__XPosition + valueX

        if self.__XPosition > 10000 :
            self.__XPosition = 10000
        elif self.__XPosition < 0 :
            self.__XPosition = 0 

    def SetYPosition(self , valueY) :
        self.__YPosition = self.__YPosition + valueY

        if self.__YPosition > 10000 :
            self.__YPosition = 10000
        elif self.__YPosition < 0 :
            self.__YPosition = 0  

    def move(self , move) :
        if move == "up":
            self.SetYPosition(+10)
        elif move == "down" :
            self.SetYPosition(-10)
        elif move == "left" :
            self.SetXPosition(-10)
        elif move == "right" :
            self.SetXPosition(+10) 

Jack = Character("Jack" , 50 , 50) 

class BikeCharacter(Character) :

    def __init__(self, name, XPos, YPos):
        super().__init__(name, XPos, YPos)

    def move(self, move):
        if move == "up":
            super().SetYPosition(+20)
        elif move == "down" :
            super().SetYPosition(-20)
        elif move == "left" :
            super().SetXPosition(-20)
        elif move == "right" :
            super().SetXPosition(+20)
           
Karla = BikeCharacter("Karla" ,100 , 50)

character = input("which Character would you like to move : ")
direction = input("input the direction : ")
if character == "Jack" :
    Jack.move(direction)
    print(character , "new position is X = " , Jack.GetXPosition() , " Y = ", Jack.GetYPosition())
elif character == "Karla" :   
    Karla.move(direction)
    print(character , "new position is X = " , Karla.GetXPosition() , " Y = ", Karla.GetYPosition())


                






