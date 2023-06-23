num = int(input("Enter a number"))
check = num % 2

if check == 0:
    print("The number entered is even")
    if (num == 0):
        print("Zero is neither a positive nor a negative integer")
    else:
        print("The number entered is not zero")
else:
    print("The number is odd")
