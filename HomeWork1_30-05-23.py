#Create an array with 5 values and delete the value at index 2 without using inbuilt function
from array import *

array1 = array('i', [])
array2 = array('i', [])
size = int(input("Enter the size of array:- "))

for i in range(size):
    value = int(input("Enter the value:- "))
    array1.append(value)

print(array1)

del array1[2]
print(array1)