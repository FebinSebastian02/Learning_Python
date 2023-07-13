class Computer:
    pass
com1 = Computer()   #Here, com1 is the new object created or we can saying com1 is referring to an object.
com2 = Computer()   #The Computer() is our constructor
#In our system, we have a special memory called Heap memory and inside this memory, we get all objects. The objects will
#take some space in Heap memory and these spaces have addresses.

#To print the address of objects
print(id(com1))
print(id(com2))
#Every time, we create an object, the object is allocated to new address

#Size of the object is depended upon the number and size of the variables it have
#Constructor is responsible for allocating the size to the object and whenever a constructor is called, __init__() is called
#automatically.

#Assigning variables in objects and changing the values of these variables

print("///////////////////////////////////////////////////")
class Person:
    def __init__(self): #Normally used to initialize variables
        self.name = "Febin"
        self.age = 24


    def details(self):
        print(self.name, self.age)

com1 = Person()
com2 = Person()
#To change the details of com2 explicitly
com2.name = "Sebastian"
com2.age = 60

com1.details()
com2.details()

#self is very important as it's used to refer to the objects passed

print("///////////////////////////////////////////////////")
#Comparing 2 objects
class Person:
    def __init__(self):
        self.name = "Febin"
        self.age = 24

    #Method defined to compare objects
    def compare(self, person2):
        if person1.name == person2.name:
            return True
        else:
            return False

person1 = Person()
person2 = Person()
person2.name = "Sebastian"

if person1.compare(person2):#compare() is a user-defined function
#Here, person1 is also passed behind the scene along with person 2 and person1 is accepted in self in compare().
    print("They are same")
else:
    print("Not same")