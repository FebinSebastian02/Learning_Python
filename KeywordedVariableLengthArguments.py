#Suppose we are passing multiple values during function call using variable length arguments
#In this case, we don't know what are the values we are sending
#eg.
def person(name, *data):    #Here, *data refers to the tuple created
    print(name)
    print(data)

person('Febin', 24, 'Thrissur', 944)

#Here, we know Febin is the name. But we don't know, what other values are. In this case, we give keywords to other values
#To accept keyworded variable length arguments,we should use **
def person(name, **data):   #**data is used to accept keyworded variable length arguments
    print(name)
    print(data)
person('Febin', age = 24, city = 'Thrissur', mob = 944)

#To print key and value pair
def person(name, **data):
    for i, j in data.items():
        print(i,j)
person('Febin', age = 24, city = 'Thrissur', mob = 944)