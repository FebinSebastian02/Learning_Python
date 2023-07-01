#Recursion means function calling itself. That is,a function is called from a same function.
import sys

#Max recursion limit in Python by default is 1000. This recursion limit is set to avoid computer hanging.
print(sys.getrecursionlimit())

#To set a new recursion limit
sys.setrecursionlimit(5000)
print(sys.getrecursionlimit())

count = 1
def greet():
    global count
    print("Hello", count)
    count += 1
    greet()

greet()



