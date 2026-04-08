# DECLARE Stack : ARRAY [0:3] OF STRING

Stack = ["" for index in range(4)]
Tos = -1

def push(animal) :
    global Stack , Tos
    if Tos == len(Stack)- 1 :
        print("Stack is full")
    else :
        Tos = Tos + 1
        Stack[Tos] = animal 
        print("Animal added")

def pop() :
    global Stack , Tos
    if Tos == -1  :
        print("No items to remove ")
    else :
        Stack[Tos] = "" 
        Tos = Tos - 1
        print("Animal removed")


def display () :
    global Stack , Tos
    for index in range(4) :
        print(Stack[index])  
    print("Tos is" , Tos)

push("elephant")
push("Ant") 
push("goat")
push("cow")
push("camel")
display()
pop()
push("camel")
display()


