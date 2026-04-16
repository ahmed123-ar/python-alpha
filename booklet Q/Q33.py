def IterativeCalculateNumber(Num) :
    ToFind = Num
    Total = 0
    while Num != 0 :
        if ToFind % Num == 0 :
            Total = Total + Num
        Num = Num - 1
    return Total

print(IterativeCalculateNumber(10))     

def RecursiveValue(Num , ToFind) :
    if Num == 0:
        return 0
    else :
        if ToFind % Num == 0:
            return Num + RecursiveValue(Num - 1 , ToFind)
        else :
            return RecursiveValue(Num - 1 , ToFind)
        
print(RecursiveValue(50,50))     