#Sorting an array in ascending order
from array import *

ar1 = array('I', [1, 3, 2, 4])

for i in range(len(ar1)):
    for j in range(i+1, len(ar1)):
        if ar1[i] > ar1[j]:
            ar1[i], ar1[j] = ar1[j], ar1[i]

print(ar1)
