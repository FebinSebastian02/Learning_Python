#Write a code to add 2 arrays using for loop

from numpy import *

arr1 = array([1, 2, 3])
arr2 = array([4, 5, 6])
arr3 = zeros(3, int)

for i in range(0, 3):
    arr3[i] = arr1[i] + arr2[i]

print(arr3)

