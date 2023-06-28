#Take 10 names from user and display no. of usernames that have more than 5 letters

list = []
size = int(input("Enter size of the list"))

for i in range(size):
    names = input("Enter a name")
    list.append(names)
print(list)

def count(list):
    count = 0
    for i in list:
        if len(i) > 5:
            count += 1
    return count
count = count(list)
print("Number of user names with more than 5 letters are: {}".format(count))