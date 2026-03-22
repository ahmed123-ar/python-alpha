print("hello world")

#  input

x = input("enter a number")

# operators

print(3+6)
print(3-6)
print(3*6)
print(3/6)
# mod- give remainder
print(7%3)
# div 
print(7//3)

# #input to integer

x=int(input("enter a number"))

# if else

age = 18
if age >17 :
    print("vote allowed")
else :
    print("not allowed")  

#  if elif for multiple conditions

marks = 79
if marks < 0 and marks > 100:
    print("invalid")
elif marks <=100 and marks > 80:
    print("A") 
elif marks <=80 and marks > 60:
    print("B")   
elif marks <=60 and marks > 50:
    print("C") 
else :
    print("fail")             


# calculator

a = int(input("enter num1"))
b = int(input("enter num2"))
ope = input("enter operator")
if ope == "+" :
    print(a + b)
elif ope == "-" :
    print(a-b)    
elif ope == "*" :
    print(a*b)    
elif ope == "/" :
    print(a/b) 
else :
    print("invalid operator")  

#string concatination

a = "Ahmed"
b = "raza"
c = a + b
print(c) 

# #for space use commas with space

x = "Minhas"
y = "Rupsi"
z = x + " " + y
print(z) 

#for loop
# range (initial count - by default zero , final count - runs till final count minus 1  , step - by default 1)

#print name 10 times

for index in range(1 , 11 , 1 ) :
    print(str(index) + "ahmed") # cannot concate string with int use type cast or f strings

#print odd numbers from 1 to 10

for index in range(1,11,2):
    print(index)

# print each letter

myData = "alpha college"
for index in myData :
    print(index)

#how many times letter repeat in particular string

myData = "alpha college"
search = input("enter letter")
count = 0
for index in myData : 
    if search == index  : 
        count = count + 1

if count == 0 : 
    print(search + " " + "not present in string")
else : 
    print(search + " " + "is repeated" + " " + str(count) + " " + "times")   

#how many times letter repeat in particular string

myData = "ALPHA COLLEGE"
search = input("enter letter to search")
count = 0
for index in myData :
    if index == search.upper() :
        count = count + 1

if count == 0:
    print("not found")
else :
    print(f"{search} appeared {count} times") 


#print index of position where letter occur

myData = "alpha college"
search = input("enter letter to search ")
count = -1
letter_rep = 0
for index in myData : 
    count = count + 1
    if search == index:
        print(f"{search} found at {count}")
        letter_rep = letter_rep + 1
if letter_rep == 0 :
    print("letter not found")        



