# Before creating an object, we need to create a class. Because, class is a design for the object.
# eg:- we need to create a design before we manufacture a phone.

# Suppose, as a person, I want to work with a computer. So, we need to create a computer object. But, before that we need to
# a class for that.

# Syntax:- class className:
#              suite(Where we write statements)
# eg:- class Computer:
#         We can put two things inside this class:- a) Attributes (Variables) b) Behaviours(Methods)
#         Suppose, I am defining a method inside the class.

class Computer:
    def config(self):   #As every computer has a configuration, we created a function called config().
#Here, self in brackets were written automatically when we just entered empty brackets. self is the object we are passing.
        print("i7, 16GB, 1TB SSD ")

#Now, we are creating com1 as an object of class Computer. So we need to mention that
com1 = Computer()
#Syntax:- object1 = ClassName()
print(type(com1))   #Here, we get module name as 'main' as this is an independent module and the class name to which this
#object belongs as 'Computer'.
a = 5
print(type(a))  #Similarly, when we printed type of variable a, we got that this variable belongs to class int which
#is an inbuilt class. This means that, variable a is also an object of class int. That's why we tell,in python everything is
#objects.
#Therefore, there are inbuilt and user defined classes.

#If I need to use the method written inside class Computer, I need to use the following syntax:-
#Syntax:- ClassName.methodName(object)
Computer.config(com1) #We need to mention the object name here. Because, one class can have multiple objects. So, this
#method - config() here will change it's behaviour based on the objects because, different objects have different behaviours
# depended on what they know
# If there are many person objects such person1, person2 etc. in a class Person and there is a function called 'walk()'.
# If I am calling 'walk()', then which object is supposed to walk. So, we need to mention the object name. eg:- object
# person1 needs to walk, so we must mention person1 while calling walk().

com2 = Computer()
Computer.config(com2)

#Another way to call function() is objectName.functionName(). This is the most common way to call functions.
#eg:- a.bit_length()
com1.config()
com2.config()
#Here, we are not passing object names in brackets and still it works. Because, behind the scenes, when the function is called,
#object is passed as a parameter. Here, com1 is passed as parameter while config() is called.
