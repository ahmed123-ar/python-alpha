class Balloon () :

    # PRIVATE Health : INTEGER
    # PRIVATE Colour : STRING
    # PRIVATE DefenceItem : STRING

    def __init__(self , item , color ) :
        self.__Health = 100
        self.__DefenceItem = item
        self.__Colour = color

    def GetDefenceItem(self) :
        return self.__DefenceItem

    def ChangeHealth(self , num) :
        self.__Health = self.__Health + num

    def CheckHealth(self) :
        if self.__Health <=  0 :
            return True
        else :
            return False

Defence = input("Enter defence item :  ")
Col = input("Enter colour :  ")
Balloon1 = Balloon(Defence , Col)


# def defend(obj) :
def Defend(obj) :
    strength = int(input("Enter strength of oponent :  "))
    obj.ChangeHealth(strength)
    print(obj.GetDefenceItem())
    X = obj.CheckHealth()
    if X == True :
        print("no health remainong")
    else :
        print("Health is remaining")
    return obj

Defend(Balloon1)    


        