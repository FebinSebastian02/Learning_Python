from array import *

values = array('i', [1, 2, 3, 4, 5])
print(values)   #To print values of array

print(values.buffer_info()) #To print address and size of an array

print(values.typecode)  #To print type code of the data type in array

values.append(6)    #To add an element to the end of array
print(values)

values.remove(6)    #To remove a value from an array
print(values)

values.reverse()    #To reverse the values in an  array
print(values)

print(values[0])    #To print 1 value in an array

for i in values:    #To print all values in array 1 by 1
    print(i)

for i in range(len(values)):    #To print all values in array 1 by 1
    print(values[i])

newArray = array(values.typecode, (i for i in values))  #To define a new array with same values of the old array
print(newArray)

i = 0   #To print values of  an array using while loop
while i < len(newArray):
    print(newArray[i])
    i += 1