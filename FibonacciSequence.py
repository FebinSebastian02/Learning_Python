
size = int(input("Enter the number of fibonacci numbers required"))

def fib(size):
    list = [0, 1]

    for i in range(2, size):
        values = list[i - 2] + list[i - 1]
        list.append(values)
    if size == 0 or size < 0:
        print("Enter a valid number of fibonacci numbers required")
    elif size == 1:
        print([list[0]])
    else:
        print(list)
fib(size)