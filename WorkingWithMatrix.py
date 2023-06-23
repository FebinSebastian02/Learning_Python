#Creating 2D array

from numpy import *

arr1 = array([[1, 2, 3], [4, 5, 6]])
print(arr1)

#Some attributes and functions
print(arr1.dtype)   #To find type of values in an array
print(arr1.ndim)    #To find the number of dimensions of the array
print(arr1.shape)   #To find the number of rows and columns in an array
print(arr1.size)    #To find the number of elements in an array
print(arr1.flatten())   #To convert multidimensional array to a single dimensional array

arr2 = array([7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])
print(arr2)
print(arr2.reshape(3, 4))   #To convert a single dimensional array to a multidimensional array(2D)
print(arr2.reshape(2, 2, 3))    #To convert to 1 big array with 2 2D array which have 2 1D array each

#Converting array into Matrix
arr3 = array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m = matrix(arr3)
print(m)
print(m.diagonal()) #To print diagonal elements

#Converting string to Matrix
m = matrix('1 2; 3 4; 5 6; 7 8')  #Semicolon is used to add new row
print(m)
print(m.min())  #To get min element in Matrix
print(m.max())  #To get max element in Matrix

#Matrix addition
m1 = matrix('1 2 ; 1 2')
m2 = matrix('1 2 ; 1 2')
m3 = m1 + m2
print(m1)
print(m2)
print(m3)

#Matrix multiplication
m1 = matrix('1 2; 1 2')
m2 = matrix('1 2; 1 2')
m3 = m1 * m2
print(m3)