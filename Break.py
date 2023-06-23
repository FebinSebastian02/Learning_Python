#Candy Vending machine

maxStock = 5  #Max. no of candies in vending machine

noOfCandies = int(input("Enter number of candies required?"))

i = 1
while i <= noOfCandies:
    if i > maxStock:
        print("Out of stock. Visit again after some time")
        break
    print("Candy")
    i += 1  #=>i+1

