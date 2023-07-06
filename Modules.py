#Suppose, we have a complex project with all the code written in 1 file, it is difficult to manage.
#In this case, if we change any portion of the program, it may affect other portions of code as well.
#In order to prevent this, a concept called modules can be used.

#Modules can be used to divide complex projects into smaller parts. So that, if we change any code in a single module,
#it won't affect the code in other modules normally. Also, the already created modules can be reused later for complex projects.

#Consider modules as files.
#Suppose, we need to add 2 numbers and I create a module to input values from the user and print result.
#Also, I create other module to define add function
#Here, I am taking this file to take values from user and print the result. I am creating sum module to define add function.
#import Sum #One way to import module.
from Sum import *   #Other way to import all things in a module.
num1 = int(input("Enter a number"))
num2 = int(input("Enter a number"))

#result = Sum.add(num1, num2)   #Either this way can be used or,
result = add(num1, num2)    #this way can be used
print(result)

#We can create as much modules as we require in Python. In addition, python have in-built modules as well.

