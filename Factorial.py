#Find factorial of a number given by user

num = int(input("Enter a number"))

def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact = i * fact
    return fact

factorial = factorial(num)
print("The factorial of {} is {}".format(num, factorial))

#Breakpoints help to see the detailed tracing. Therefore, we need to add breakpoints where we need to see detailed
#tracing.