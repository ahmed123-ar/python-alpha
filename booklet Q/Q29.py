class Character() :
    # DECLARE Name : STRING
    # DECLARE XPosition : INTEGER
    # DECLARE YPosition : INTEGER

    def __init__(self , Name, XPos , YPos ) :
        self.__Name = Name
        self.__XPosition = XPos 
        self.__YPosition = YPos

    def GetXPosition(self) :
        return self.__XPosition
    
    def GetYPosition(self) :
        return self.__YPosition
    
    def SetXPosition(self , val) :
        self.__XPosition = self.__XPosition + val
        if self.__XPosition > 10000 :
            self.__XPosition = 10000

        if self.__XPosition < 0 :
            self.__XPosition = 0

    def SetYPosition(self , val) :
        self.__YPosition = self.__YPosition + val
        if self.__YPosition > 10000 :
            self.__YPosition = 10000

        if self.__YPosition < 0 :
            self.__YPosition = 0   

    def Move(self , move) :
        if move == "up" :
            self.__YPosition = self.__YPosition + 10

        if move == "down" :
            self.__YPosition = self.__YPosition - 10

        if move == "left" :
            self.__XPosition = self.__XPosition - 10         
        
        if move == "right" :
            self.__XPosition = self.__XPosition + 10


Jack = Character("Jack" , 50 , 50)

class BikeCharacter(Character) :

    def __init__(self, Name, XPos, YPos):
        super().__init__(Name, XPos, YPos)

    def Move(self, move): 
        if move == "up" :
            super().SetYPosition(+20)

        if move == "down" :
            super().SetYPosition(-20)
            

        if move == "left" :
            super().SetXPosition(-20)
                    
        
        if move == "right" :
            super().SetXPosition(+20)
               

Karla = BikeCharacter("Karla" , 100 , 50)

Char = input("enter character to move :  ")
dir = input("Enter direction to move :  ")

if Char == "jack" :
    Jack.Move(dir)
    print("Jack's new position is X =  " , Jack.GetXPosition() , "Y = " , Jack.GetYPosition())
elif Char == "karla" :
    Karla.Move(dir)
    print("Karla's new position is X =  " , Karla.GetXPosition() , "Y = " , Karla.GetYPosition())   