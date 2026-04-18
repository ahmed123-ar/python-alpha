class BoardObject :

    # PRIVATE Code : STRING
    # PRIVATE Value : INTEGER

    def __init__(self ,code , value):
        self.__Code = code
        self.__Value = value

    def GetCode(self) :
        return self.__Code

    def GetValue(self) :
        return self.__Value
    

class Board :

    # PRIVATE TheBoard : ARRAY [0:9] [0:9] OF BoardObject 

    def __init__(self):
        self.__TheBoard = [[None for index in range(10)] for index in range(10)]
        for x in range(10) :
            for y in range(10) :
                self.__TheBoard[x][y] = BoardObject("-" , 0)
    
    def GetObject (self , row , col) :
        return self.__TheBoard[row][col]
    
    def SetObject(self , obj , row , col) :
        self.__TheBoard[row][col] = obj
    
    def DisplayBoard(self) :
        for x in range(10) :
            string = ""
            for y in range(10) :
                string = string + "" + self.__TheBoard[x][y].GetCode()
            print(string)    



Object1 = BoardObject("A" , 2)  
Object2 = BoardObject("B" , 3)  
Object3 = BoardObject("C" , 5)  
Object4 = BoardObject("D" , 2)  
Object5 = BoardObject("E" , 7) 
GameBoard = Board()
GameBoard.SetObject(Object1 , 0 , 0)     
GameBoard.SetObject(Object2 , 9 , 9) 
GameBoard.SetObject(Object3 , 4 , 5) 
GameBoard.SetObject(Object4 , 2 , 2) 
GameBoard.SetObject(Object5 , 8 , 7) 
GameBoard.DisplayBoard()

row = int(input("Enter row position : "))
while row < 0 or row > 9 :
    print("Enter valid row :  ")
    row = int(input("Enter row position : "))
print("Correct entered")    

col = int(input("Enter column position : "))
while col < 0 or col > 9 :
    print("Enter valid column :  ")
    col = int(input("Enter column position : "))
print("Correct entered") 

res = GameBoard.GetObject(row , col).GetCode()
if res == "-" :
    print("Miss")
else :
    print(res , GameBoard.GetObject(row , col).GetValue())    
  
        
