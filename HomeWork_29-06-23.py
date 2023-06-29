#Take the last number from user till which the fibonnaci numbers should be printed.
lastNo = int(input("Enter the last number required till which the fibonacci numbers should be printed"))

def fib(lastNo):
    list = [0, 1]
    for i in range(2, lastNo + 1):  #Here, lastNo + 1 is given to get proper results when value of lastNo is <= 4
        values = list[i - 2] + list[i - 1]
        list.append(values)
    if lastNo <= 0:
        print("Enter a valid number of fibonacci numbers to be printed")
    elif lastNo == 1:
        print([list[0]])
    else:
        list1 = []
        for j in list:
            if j < lastNo:
                list1.append(j)
        print(list1)
fib(lastNo)

