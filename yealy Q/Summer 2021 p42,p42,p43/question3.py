class TreasureChest :

    # PRIVATE question : STRING
    # PRIVATE answer : INTEGER
    # PRIVATE points : INTEGER

    def __init__(self , question , answer , points):
        self.__question = question
        self.__answer = answer
        self.__points = points

    def getQuestion(self) :
        return self.__question

    def checkAnswer(self , ans) :
        if self.__answer == ans :
            return True
        else :
            return False

    def getPoints(self , attempts) :
        if attempts == 1 :
            return self.__points
        elif attempts == 2 :
            return self.__points//2   
        elif attempts == 3 or attempts == 4 :
            return self.__points//4
        else :
            return 0
                

# DECLARE arrayTreasure : [0:4] OF TreasureChest
arrayTreasure = []
def readData() :
    global arrayTreasure
    try :
        myfile = open("TreasureChestData.txt" , "r")
        for index in range(5) :
            question = myfile.readline().strip()
            answer = int(myfile.readline().strip())
            points = int(myfile.readline().strip())
            arrayTreasure.append(TreasureChest(question , answer , points))

    except FileNotFoundError :
        print("The file is not found")  

readData()
QNo = int(input("Enter question number between 1 and 5 :  "))
print(arrayTreasure[QNo - 1].getQuestion())
Ans = int(input("Enter answer :  "))
attempt = 1
Res = arrayTreasure[QNo - 1].checkAnswer(Ans)
while Res == False :
    print("Wrong answer . Enter Again")
    Ans = int(input("Enter answer :  "))
    attempt = attempt + 1
    Res = arrayTreasure[QNo - 1].checkAnswer(Ans)
print("Correct answer entered")
Points = arrayTreasure[QNo - 1].getPoints(attempt)
print("You have got" , Points , "points") 





    