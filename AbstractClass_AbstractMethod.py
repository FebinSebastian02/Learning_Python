#Abstract Methods are the methods that have a declaration,but not have a definiton. i.e, they don't have statements to execute.
#A class which have at least 1 Abstract Method is called Abstract Class. We can't create objects of Abstract Class.
#Python by default does not support Abstract classes directly. But we can use "ABC" module to achieve Abstraction.
#ABC -> Abstract Base Classes
#To make a class Abstract, we need to import ABC and abstractmethod from abc module.
#eg:-
from abc import ABC,abstractmethod
class Computer(ABC):    #Class Computer inherits ABC(Abstract Base Classes)
    #eg of Abstract Method
    @abstractmethod #Metioning process() as an abstractmethod with the help of abstractmethod decorator
    def process(self):  #Declaration
        pass
# com1 = Computer() #Error is obtained as we can't create object of an Abstract Class.
# com1.process()

class Laptop(Computer):
    #pass
    def process(self):
        print("Laptop running")
l1 = Laptop()   #Error is obtained because an object of a class that inherits an Abstract class can't be created.
#This error can be only removed if there is a method defined in Laptop class which makes Laptop no longer an Abstract Class.
#That is, if there is an Abstract Method defined in Abstract Class which was inherited by a child class, then the child class
#should define that abstract method in the parent Abstract Class inorder to prevent error
# l1.process()

#Use of Abstract Class and methods
#There's a class called Vehicle and it have some important methods. There are other 2 types of vehicles:- Car and Truck that
#have the same features of Vehicle and some other features. Suppose in Car, we change gears only automatically and in truck we
#change gears only manually. But, if we use inheritance to call changeGear() in car, it will print "Change gears manually"
#which we not desire.
#To avoid this issue, we can make changeGear() an Abstract Method, i.e by just giving declaration and defining that method
#as we desire in class Car and Truck. So when we make changeGear an Abstract Method, class Vehicle will become an Abstract Class.

class Vehicle(ABC): #Class vehicle inheriting ABC(Abstract Base Classes)
    def start(self):
        print("Start engine")
    def stop(self):
        print("Stop engine")
    @abstractmethod
    def changeGear(self):
        print("Change gears manually")

class Car(Vehicle):
   def sunRoof(self):
       print("Open Sun roof")
   def changeGear(self):
       print("Change gears automatically")
class Truck(Vehicle):
    def loadWeight(self):
        print("Load the weight")
    def changeGear(self):
        print("Change gears manually")

c1 = Car()
c1.sunRoof()
c1.changeGear()
print("///////////////////")
t1 = Truck()
t1.loadWeight()
t1.changeGear()