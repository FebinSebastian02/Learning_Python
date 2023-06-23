num = int(input("Enter a number"))

for i in range(2, num):
    if num % i == 0:
        print(num, "is not a Prime number")
        break
else:
    print(num, "is a Prime number")
