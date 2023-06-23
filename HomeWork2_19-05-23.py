num1 = int(input("Enter first number - "))
num2 = int(input("Enter second number - "))
num3 = int(input("Enter third number - "))

if num1 >= num2 and num1 >= num3:
    print(str(num1) + " is greatest")
elif num2 >= num1 and num2 >= num3:
    print(str(num2) + " is greatest")
elif num3 >= num1 and num3 >= num2:
    print(str(num3) + " is greatest")

