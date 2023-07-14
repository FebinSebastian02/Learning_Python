#In oops, we have 2 types of variables:-
#a) Instance Variable b) Class(Static) Variable

#a) Instance Variables are variables which is different for different objects and are defined inside __init__()
#b) Class variables are variables which is common for different objects and are defined outside __init__() within the class.
#eg:-
class Car:
    wheels = 4
    def __init__(self):
        self.name = "Mustang GT"
        self.speed = "250 kmph"

car1 = Car()
car2 = Car()

car2.name = "Supra"
car2.speed = "200 kmph"
print(car1.name + ", " + car1.speed + ", " + str(Car.wheels))
print(car2.name + ", " + car2.speed + "," + str(Car.wheels))

#Here, name and speed are Instance variables.If we change value of either one of the variable for an object,
# it does not affect other object.
# Wheels is a class variable. If we change value of this variable, it will affect both objects.

#In memory, there are different namespace.
#namespace is an area where we create and store object/variable
#There are 2 types of namespace as well:-
#a) Class namespace:- where all class variables are created and stored
#b) Object/Instance namespace:- where all Instance variables are created and stored




