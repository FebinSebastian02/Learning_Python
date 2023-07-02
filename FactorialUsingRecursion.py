num = int(input("Enter a number to find the factorial"))

def fact(num):
    if num == 0:    #A condition is written to break the recursion
        return 1
    return num * fact(num - 1)
#5 *fact(4) num =5
#5 * 4 * fact(3)    num = 4
#5 * 4 * 3 * fact(2)    num = 3
#5 * 4 * 3 * 2 * fact(1)    num = 2
#5 * 4 * 3 * 2 * 1 * fact(0) num = 1
#5 * 4 * 3 * 2 * 1 * 1 [num = 0. When num = 0, we return 1]. Total is 120.

result = fact(num)
print("The factorial of {} is {}".format(num, result))