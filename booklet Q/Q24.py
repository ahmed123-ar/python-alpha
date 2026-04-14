class Card :

    # PRIAVTE Number  : INTEGER
    # PRIAVTE Colour : STRING

    def __init__(self , num , color) :
        self.__Number = num
        self.__Colour = color

    def GetNumber(self) :
        return self.__Number

    def GetColour(self) :
        return self.__Colour

#DECLARE CardData : ARRAY [0:29] OF Card

CardData = [Card(0 , "" ) for index in range(30)]
myfile = open("CardValues.txt" , "r")
for index in range(30) :
    NumF = myfile.readline().strip()
    ColF = myfile.readline().strip()
    CardData[index] = Card(int(NumF) , ColF)
myfile.close()

def ChooseCard (Arr) :

    for x in range(4) :
        found = False
        while found == False :
            index = int(input("Enter Number Between 1 and 30 : "))
            while index < 1 or index > 30 :
                print("Not a valid number : ")
                index = int(input("Enter Number Between 1 and 30"))
            print("Valid Number") 

            if CardData[index-1] in Arr :
               print("this card is already selected") 
            else :
               Arr[x] = CardData[index-1]
               found = True                   


Player1 = [Card(0 , "") for index in range (4)]
ChooseCard(Player1)
for index in range(4) :
    print(Player1[index].GetNumber()  , Player1[index].GetColour())



