class TreasureChest() :

    # PRIVATE question : STRING
    # PRIVATE answer : INTEGER
    # PRIVATE points : INTEGER

    def __init__(self , quest , ans , point):
        self.__question = quest
        self.__answer = ans
        self.__points = point

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
            return int(self.__points//2) 
        elif attempts ==3 or attempts == 4  :
            return int(self.__points//4)
        else :
            return 0



# DECLARE ArrayTreasure : [0:4] OF TreasureChest
ArrayTreasure = [TreasureChest("" , 0 , 0) for index in range(5)]
def readData() :
    try :
        myfile = open("TreasureChestData.txt")
        for index in range(5) :
            Ques =  myfile.readline().strip()
            Ans = int(myfile.readline().strip())
            Points = int(myfile.readline().strip())
            ArrayTreasure[index] = (TreasureChest(Ques , Ans , Points))
        myfile.close()    

    except :
        print("An error occurred")



readData()  
QNo = int(input("Enter question no :  "))
print(ArrayTreasure[QNo-1].getQuestion())
Ans = int(input("enter answer"))
attempts = 1
Res = ArrayTreasure[QNo-1].checkAnswer(Ans)
while Res == False :
    print("wrong answer")
    print(ArrayTreasure[QNo-1].getQuestion())
    Ans = int(input("enter answer"))
    attempts = attempts + 1
    Res = ArrayTreasure[QNo-1].checkAnswer(Ans)
print("correct answer")
print(ArrayTreasure[QNo-1].getPoints(attempts))



