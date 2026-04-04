# Input 5 numbers and print:

res = 0
for index in range(5) :
    X = int(input("Enter Number :  "))
    res = res + X
print(res)  


# Even or odd

X = int(input("Enter Number :  "))
if (X % 2) == 0 :
    print ("Even")
else :
    print("odd")    


#calculator

X = int(input("Enter Number :  "))
Y = int(input("Enter Number :  "))
Z = input("Enter operator :  ")

if Z == "+" :
    print(X+Y)
elif Z == "-" :
    print(X-Y)
elif Z == "*" :
    print(X*Y) 
elif Z == "/" :
    print(X/Y)
else :
    print("invalid operator")  


# grade calculator  

X = int(input("enter your marks :  "))
if X >= 90 and X < 101 :
    print("A")
elif X >= 70 and X < 90 :
    print("B")   
elif X >= 60 and X < 70 :
    print("C")
elif X >= 55 and X < 60 :
    print("D")    
elif X < 55 :
    print("F") 
else :
    print("invalid marks")  


#print odd no from 1 to 10

for index in range(1 , 11 , 2):
    print (index)  


#print even no from 1 to 10

for index in range(2 , 11 , 2):
    print(index)


# Print numbers from 1 to 50 But skip multiples of 5

start = 1
while start < 51 :
    if start % 5 != 0:
        print (start)
    start = start + 1    

# Keep asking until correct password = "cs9618"

password = "cs9618"
flag = False
X = input("enter password ")

while X != password :
    print("wrong guess")
    X = input("enter password ")

print("correct guess")


# print each letter

myData = "Ahmed_Raza"
for index in myData :
    print(index)

#how many times letter repeat in particular string

myData = "alpha college"
count = 0
Search = input("Enter letter to search  ")
for index in myData :
    if index == Search :
        count = count + 1
print("the letter repeated" , count , "times")    


#print index of position where letter occur first time 

myData = "alpha college"
Search = input("Enter letter to search  ")
flag = False
count = 0
for index in myData :
    if index == Search :
        flag = True
        break
    else :
        count = count + 1

if flag == False :
    print("letter not found")
else :
    print("letter found at " , count , " position")    
        

