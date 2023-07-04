#filter, map and reduce functions are used to do some operations on the big chunks of data.
#filter() -> Used for filtering a sequence.
#syntax -> filter(function,iterable) -> iterable means sequence like list.
#eg:- We need to create a new list with only even numbers from a random list of both odd and even numbers

nums = [1, 2, 3, 4, 5]  #List of random numbers

def checkEven(nums):
    return nums % 2 == 0 #This function will return the values that satisfies the condition.Here, 2 & 4 are returned.

evenNums = list(filter(checkEven,nums)) #Variable evenNums is converted into list using list().
#Here the filter function takes the list and filter the even numbers for us and give us the output.
#We need to give a function to filter where we will write logic. Here, we are passing function as an argument and therefore
#we need to write function name without brackets.

print(evenNums)

#Above written example can also be done using lambda expression.
numList = [5, 10, 15, 20, 25, 30]

evenList = list(filter(lambda numList: numList % 2 == 0, numList))
#Here, lambda expression is used with numList as the passed argument and numList % 2 ==0 as the return statement.
print(evenList)

#map()
#Whenever we need to change every value, map can be used.
#eg:- Now we need to double the values in the even numbers list which we obtained using filter() earlier. Here, we use map()
#Syntax -> map(function,iterable)

doubleNums = list(map(lambda evenList: evenList * 2, evenList))
print(doubleNums)

#reduce()
#When we need to reduce the number of values, we use reduce().
#reduce needs to be imported from functools module
#Syntax -> reduce(function, iterable)

#eg:- Here, we need to add all the values in doubleNums list and display the total sum.
from functools import reduce
def sumList(a, b):  #Here, the first two values of doubleNums list is taken and added. After that, the obtained sum and
    #the third value is taken and added together.
    print(a,b)
    return a + b
sum = reduce(sumList, doubleNums)
print(sum)

#Using lambda expression

sum1 = reduce(lambda a, b: a + b, doubleNums)
print(sum1)