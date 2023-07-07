
from SpecialVariable2 import *
#__name__ is a special variable.
#The first module that gets executed in a program is called main.

#Suppose we have 2 modules SpecialVariablePart1 and Part2, if we print __name__ in both modules, we will get __main__ as
#output in both modules as they are independent
print(__name__)

#Suppose, we import SpecialVariablePart2 module in Part 1, then the print statement in SpecialVariablePart2 gives
#the name of that module. The print statement in SpecialVariablePart1 gives main as module name because program starts
#execution from SpecialVariablePart1
print("print() inside SpecialVariable1 "+__name__)

#Suppose, I have some functions in this module as well as SpecialVariablePart2 module.
#fun1 and fun2 are 2 functions inside this module. I am calling these functions from a main function because in projects
#we use main function as our starting point of execution.
#When we run this module as an independent(standalone) module, we get the result as __main__, print() inside SpecialVariable1
#__main__, inside fun1, inside fun2.
def fun1():
    print("inside fun1")
    add()
def fun2():
    print("inside fun2")

def main():
    fun1()
    fun2()
main()

#When we include the import statement, from SpecialVariable2 import *,
#we get output as,
# print() inside SpecialVariable2 SpecialVariable2
# Result is SpecialVariable2 -> Here, SpecialVariable2 is the module name of module 2
# Result is SpecialVariable2
# __main__
# print() inside SpecialVariable1 __main__
# inside fun1
# Result is SpecialVariable2 -> Result of calling add() from module2
# inside fun2

#But, if I don't want to print those unnecessary statements from module2, i need to give a condition in module 2 which
#prints those unnecessary print statements only if module 2 is executed as a standalone file
