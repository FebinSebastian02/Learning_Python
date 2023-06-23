#Ways to create array in Numpy
#a) Using array function

from Numpy import *

arr1 = array([1, 2, 3])
print(arr1)
print(arr1.dtype)

arr2 = array([4, 5, 6], float)  #To convert int values in an array to float
print(arr2)

#b) Using linspace function

arr3 = linspace(0, 16, 4)
print(arr3)

#c) Using arange()

arr4 = arange(0, 16, 2)
print(arr4)

#d) Using logspace()

arr5 = logspace(1, 40, 5)
print(arr5)
print('%.2f' % arr5[4]) #To print first value in array normally with just 2 decimal points

#e) Using zeros()

arr6 = zeros(5)
print(arr6)
arr8 = zeros(5, int)
print(arr8)

#f) Using ones()

arr7 = ones(5)
print(arr7)
arr9 = ones(5, int)
print(arr9)