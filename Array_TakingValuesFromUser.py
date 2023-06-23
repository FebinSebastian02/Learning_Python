#Creating an array and taking values from user
from array import *

array1 = array('i', [])
size = int(input("Enter the size of array:- "))

for i in range(size):
    value1 = int(input("Enter the value:- "))
    array1.append(value1)

print(array1)

#Searching the position of a value in an array manually

value2 = int(input("Enter the value to be searched:- "))
position = 0

for value in array1:
    if value == value2:
        print(position)
        break
    position += 1

#Searching the position of a value in an array using function

print(array1.index(value2))