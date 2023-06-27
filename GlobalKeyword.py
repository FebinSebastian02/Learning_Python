#Global Keyword in Python
print("Example 1")
a = 10  #Global variable with scope inside and outside of something function
b = 20
def something():
    a = 15  #Local variable with scope only inside of function
    print(a)
    print(id(a))
    print(b)    #Global variable b can be accessed inside and outside something function

something()
print(a)
print(id(a))

#Here, a outside is a global variable. But, when we assign a new value to a inside something function, then that a is
#changed to a local variable.
#Suppose, we don't want to change a to a local variable and use it as a global variable itself,in that case we should
#use global keyword
print("Example 2")
a = 30
def something():
    global a    #Here, we declared a inside this function as a global variable.
    a = 40      #We changed the value of global variable here.
    print(a)
something()
print(a)    #We got the changed value of global variable here

#Suppose, I assigned a new value to variable a inside the function, then that a is also a global variable because
# we declared a as a global variable at the beginning of function itself and if we change it's value,the value of a
# outside the function also gets changed.
print("Example 3")

a = 40  #global variable
def something():
    global a
    a = 50  #global variable
    print(a)
    a = 60  #global variable
    print(a)
something()
print(a)

#Suppose, I don't want to create a as another global variable inside the function. Instead, I want a to be a local variable,
# In this case, we use globals(). globals() helps to use a variable as both global and local inside same function.
print("Example 4")
a = 50
print(id(a))
b = 60
c = 70
def something():
    a = 40  #Local variable
    print(a)
    #Now, we need to change the value of a global variable also.
    x = globals()['a']   #Gives access to all the global variables declared inside and outside the function.
    #Here, we are accessing global variable a from all the global variables declared.
    y = globals()['b']
    print(x)
    print(y)
    print(id(x))    #x is pointing to same global variable a.
    #Now, we need to change the value of global variable a. For this, we don't change the value of x as it will create a
    #new memory. Instead we do:-
    globals()['a'] = 80

something()
print(a)