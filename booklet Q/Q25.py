class Card() :

    # PRIAVTE Number : INTEGER
    # PRIVATE Colour : STRING

    def __init__(self , No , Color):
        self.__Number = No
        self.__Colour = Color

    def GetNumber(self) :
        return self.__Number

    def GetColour(self) :
        return self.__Colour

Red1 = Card(1 ,"red")
Red2 = Card(2 ,"red")
Red3 = Card(3 ,"red")
Red4 = Card(4 ,"red")
Red5 = Card(5 ,"red")
Blue1 = Card(1 , "blue")
Blue2 = Card(2 , "blue")
Blue3 = Card(3 , "blue")
Blue4 = Card(4 , "blue")
Blue5 = Card(5 , "blue")
Yellow1 = Card(1 , "yellow")
Yellow2 = Card(2 , "yellow")
Yellow3 = Card(3 , "yellow")
Yellow4 = Card(4 , "yellow")
Yellow5 = Card(5 , "yellow")
        
# for index in range(15) :
#     print(CardList[index].GetNumber() , CardList[index].GetColour())     
# 

class Hand() :

     # PRIVATE Cards : ARRAY [0:9]  OF Card
     # PRIVATE FirstCard : INTEGER
     # PRIVATE NumberCards : INTEGER

     def __init__(self , obj)  :
        self.__Cards = obj
        self.__FirstCard = 0
        self.__NumberCards = 5

     def GetCard(self , index) :
         return self.__Cards[index]
     
ArrNum = [1 , 2 , 3 , 4 ,5]
ArrColour = ["red" , "blue ", "yellow"]
CardList = []
count = 0
for x in range(3) :
    for y in range(5) :
        MyCard = Card(ArrNum[y] , ArrColour[x])
        CardList.append(MyCard)
        
CardList1 = [CardList[0] , CardList[1] , CardList[2] , CardList[3] , CardList[10]]
CardList2 = [CardList[11] , CardList[12] , CardList[13] , CardList[14] , CardList[5]]

Player1 = Hand(CardList1)
Player2 = Hand(CardList2)

def CalculateValue(hand) :
    Score = 0
    for index in range(5) :
        No = hand.GetCard(index).GetNumber()
        col = hand.GetCard(index).GetColour()
        if col == "red" :
            Score = Score + 5
        elif col == "blue" :
            Score = Score + 10
        elif col == "yellow":
            Score = Score + 15

        Score = Score + No            
    return Score    
    
X  = CalculateValue(Player1)
Y = CalculateValue(Player2)
if X > Y :
    print("Player1 win")
elif X < Y : 
    print("Player2 wins")
else :
    ("Game Draw")
            