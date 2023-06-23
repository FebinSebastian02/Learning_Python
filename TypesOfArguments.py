#There are 2 types of arguments mainly:- 1) Formal Arguments and 2) Actual Arguments
def add(a, b):  #Here, a and b are called the Formal arguments as they are the arguments present during function definition.
    c = a + b
    print(c)
add(5, 10)  #Here, 5 and 10 are called the Actual arguments as they are the arguments present during function calling and are
            #passing something actually

#Actual arguments are divided into 4:- a) Position b) Keyword c)Default d)Variable length
#a) Position
def person(name, age):  #Here, Febin is assigned to name and 24 is assigned to age correctly because of their positions.
    print(name)         #The arguments here are depended on their positions and positions should be in proper sequence.
    print(age)
person('Febin', 24)

#b) Keyword
def person(name, age):
    print(name)
    print(age)
person(age = 24, name = 'Febin')

#Suppose we don't know the positions of arguments as the functions are defined in some other place in the code.
#In this case, we pass values by assigning the values to their respective variable names(keywords) inorder to avoid error.

#c) Default
#Suppose we don't pass the value for age here during function call. In this case, a default value should be assigned to the
#age variable in order to prevent error. This is called default arguments
def person(name, age = 18):
    print(name)
    print(age)
person('Febin')

#Suppose, we pass the value for age during function call eventhough we defined a default value for age variable. In this
#case, the passed value will overwrite the default value.
def person(name, age = 18):
    print(name)
    print(age)
person('Febin', 17)

#d) Variable length
# Suppose we need to pass multiple values to a function. In this case, it's difficult to assign variables for each values.
#Here, we use variable length arguments so that we can pass multiple values.
def sum(a, *b): #Here, *b refers to the tuple which accepts other values 20,30 and 40
    print(a)
    print(b)
    c = a
    for i in b:     #We need to iterate through the values of tuple b inorder to find the sum
        c = c + i
    print(c)

sum(10, 20, 30, 40)

#Another case where we are not assigning one fixed variable also
def sum(*a):    #Here, *a refers to the tuple which accepts multiple values
    print(a)
    sum = 0
    for i in a:
        sum = sum + i
    print(sum)
sum(10, 20, 30, 40)