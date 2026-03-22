# Q 23 

class balloon :

    # PRIVATE Health : INTEGER
    # PRIVATE Colour : STRING
    # PRIVATE DefenceItem : STRING

    def __init__(self , Col , DefItem):
        self.__Health = 100
        self.__Colour = Col
        self.__DefenceItem = DefItem

    def GetDefenceItem(self) :
        return self.__DefenceItem

    def ChangeHealth(self , num) :
        self.__Health = self.__Health + num

    def CheckHealth(self):
        if self.__Health <= 0 :
            return True
        else :
            return False        

defence = input("input defence item : ")
colr = input("input colour : ")
Balloon1 = balloon(colr , defence)

def Defend(obj) :
    strength = int(input("input the strength of oponent :  "))
    obj.ChangeHealth(strength * -1)
    obj.GetDefenceItem()
    check = obj.CheckHealth()
    if check == True :
        print("No health remaining")
    else :
        print("health is remaining")    
    
    return obj

Defend(Balloon1)
