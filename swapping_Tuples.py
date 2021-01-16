#Created by Margarita Busygina
#jan 16 2021
#Learn Python Challenge-day 2
#This file contains tuples practice for swiping and small simple math program with user input
import math

tup1 = (1, 2)
tup2 = (3, 4)
(a, b) = tup1
(c, d) = tup2
print(tup1, tup2)
print(tup2, tup1)
tup3 = (a, d)
print(tup3)

# ask user to enter x and y points and find the distance between them
x = int(input("enter x point "))
y = int(input("enter y point "))
tup0 = (x, y)

result = (math.sqrt(math.pow(x, 2) + math.pow(y, 2)))
print("The distance between x and y is "+str(result))
