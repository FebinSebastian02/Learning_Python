#Check a given number is prime or not

num = int(input("Enter a number"))

if num < 2:
    print("Entered number is not a prime number")

i = 2
while i < num:
    if num % i != 0:
        pass
    else:
        print(num, "is not a prime number")
        break
    i += 1
if i == num:
    print(num, "is a prime number")