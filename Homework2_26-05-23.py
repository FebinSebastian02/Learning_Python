#Print factorial of a number.
#The factorial of a number is the product of all the integers from 1 to that number.
#eg: 5! = 1*2*3*4*5 => 120

num = int(input("Enter a number"))
factorial = 1

for i in range(1, num+1):
    factorial = factorial * i
print("Factorial of ", num, "is", factorial)

# i = 1
# while i <= num:
#     factorial = factorial * i
#     i += 1
# print("Factorial of ", num, "is", factorial)
