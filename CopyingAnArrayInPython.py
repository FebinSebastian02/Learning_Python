#Assignment
#Add 5 to each and every element of an Array and make a new array with the updated values

from array import *

arr1 = array('i', [1, 2, 3])
print(arr1)

for i in range(0, 3):
    arr1[i] += 5

print(arr1)

from numpy import *
#Adding 2 arrays together in numpy

arr2 = array([4, 5, 6])
arr3 = array([7, 8, 9])
arr4 = arr2 + arr3
print(arr4)

#Adding 5 to each values in an array

arr5 = array([5, 10, 15])
arr5 = arr5 + 5
print(arr5)

#Trigonometric Functions
arr6 = array([1, 2, 4])
print(sin(arr6))    #To print sin values of elements in array
print(cos(arr6))    #To print cos values of elements in array
print(tan(arr6))    #To print tan values of elements in array
print(log(arr6))    #To print log values of elements in array
print(sqrt(arr6))   #To print sqrt values of elements in array
print(sum(arr6))    #To print sum of elements in array
print(min(arr6))    #To print min value in array
print(max(arr6))    #To print max value in array
print(sort(arr6))   #To print the sorted elements in array

#To concatenate 2 arrays
arr7 = array([10, 100, 1000])
arr8 = array([1000, 100, 10])
arr9 = concatenate([arr7, arr8])
print(arr9)

#Arrays pointing to same address after copying
arr1 = array([1, 2, 3])
arr2 = arr1
print(arr1)
print(arr2)
print(id(arr1))    #To check address
print(id(arr2))

#Arrays pointing to different addresses after copying
arr2 = arr1.view()
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))

#Shallow copy
arr1 = array([5, 6, 7])
arr2 = arr1.view()
arr1[0] = 6
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))

#Deep copy
arr1 = array([1, 2, 3])
arr2 = arr1.copy()
arr1[0] = 2

print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))
