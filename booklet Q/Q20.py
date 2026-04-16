class HiddenBox :

    # PRIVATE BoxName : STRING
    # PRIVATE Creator : STRING
    # PRIVATE DateHidden :STRING
    # PRIVATE GameLocation : STRING
    # PRIVATE LastFinds : ARRAY [0 : 9] [0 : 1] OF STRING
    # PRIVATE Active : STRING

    def __init__(self , name , creator , datehid , location) :
        self.__BoxName = name
        self.__Creator = creator
        self.__DateHidden = datehid
        self.__GameLocation = location


    def GetBoxName(self) :
        return self.__BoxName

    def GetGameLocation(self) :
        return self.__GameLocation


TheBoxes = [HiddenBox("" , "" , "" , "") for index in range(10000)]
NumberItems = 0
    
def NewBox() :
    global TheBoxes , NumberItems
    Name = input("input name : ")
    creator = input("enter creator : ")
    date = input("enter date hiddeen : ")
    location = input("enter game location : ")
    TheBoxes[NumberItems] = (HiddenBox(Name , creator , date , location))
    NumberItems = NumberItems + 1

NewBox()

class PuzzleBox(HiddenBox) :
    # PRIVATE PuzzleText : STRING   
    # PRIVATE PuzzleText : STRING   

    def __init__(self, name, creator, datehid, location , PuzText , Sol):
        super().__init__(name, creator, datehid, location)
        self.__PuzzleText = PuzText
        self.__Solution = Sol