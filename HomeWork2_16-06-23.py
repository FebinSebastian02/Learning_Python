#Write a code to find the maximum value in an array without using an inbuilt function

from numpy import *

arr1 = array([1, 5, 3, 10])
maxNo = arr1[0]

for i in range(len(arr1)):
    if arr1[i] > maxNo:
        maxNo = arr1[i]
print(maxNo, "is the highest number")