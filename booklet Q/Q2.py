# DECLARE Animals : ARRAY [0:9] OF STRING

Animals = ["horse" , "lion" , "rabbit" , "mouse" , "bird" , "deer" , "whale" , "elephant" , "kangaroo" , "tiger"]

def SortDescending () :
    global Animals
    ArrayLength = len(Animals)
    for x in range(ArrayLength - 1) :
        for y in range(ArrayLength - 1) :
            if Animals[y+1][0] > Animals[y][0] :
                temp = Animals[y]
                Animals[y] = Animals[y+1]
                Animals[y+1] = temp


SortDescending()
for index in range(10) :
    print(Animals[index])