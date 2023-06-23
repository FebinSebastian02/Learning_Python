#Write a code to reverse an array without using inbuilt function

from array import *

array1 = array('i',[1, 2, 3, 4, 5])
print(array1)
size = len(array1)

for i in range(size//2):
    array1[i], array1[size-1] = array1[size - 1], array1[i]
    size -= 1

print(array1)