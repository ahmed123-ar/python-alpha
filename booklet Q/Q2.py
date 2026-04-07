# DECLARE Animals : ARRAY [0 : 9 ] OF STRING
Animals = ["horse" , "lion" , "rabbit" , "mouse" , "bird" , "deer" , "whale" , "elephant" , "kangaroo" , "tiger"]

def SortDescending() :
    global Animals
    for x in range(len(Animals) - 1) :
        for y in range(len(Animals) - 1) :
            if Animals[y][0] < Animals[y+1][0] :
                temp =  Animals[y]
                Animals[y] = Animals[y + 1]
                Animals[y+1] = temp

    for index in range(len(Animals)) :
        print(Animals[index])

SortDescending()    