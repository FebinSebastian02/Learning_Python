#Functions without function names are called Anonymous functions or Lambda functions
#Suppose we have a function that is only executed once and it have only one expression, in this case we use lambda functions.
def sqrt(num):
    return num * num
result = sqrt(5)
print(result)
#The same function above can be rewritten as Lambda function as there is only one expression.

f = lambda num: num * num #Lambda expression used to create anonymous functions. Here f represents function.
result = f(5)
print(result)

#We can use multiple arguments for Lambda functions. But we can only write one expression in lambda functions.
s = lambda a, b: a + b
result = s(5, 5)
print(result)
#We are defining a function using lambda and no function name is used.
#Functions can be passed in Python because functions are also objects in Python.
