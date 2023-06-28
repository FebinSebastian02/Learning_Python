#Pass a list of random numbers to a function and return the number of odd numbers and even numbers in that list from
#the function

list = []   #Creating an empty list to take values from user
size = int(input("Enter the size of list"))

for i in range(size):
    value = int(input("Enter a value"))
    list.append(value)
print(list)
def count(list):
    even, odd = 0, 0
    for i in list:
        if i % 2 == 0:
            even += 1   #even = even + 1
        else:
            odd += 1
    return even, odd

evenNos, oddNos = count(list)
print("No of even numbers are: {} \nNo of odd numbers are: {}".format(evenNos,oddNos))