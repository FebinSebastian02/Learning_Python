#There is a class called Student and it have some variables and methods. Suppose,every student has a laptop
#and we need to create a class for it as the laptop has several configurations.
#Here,we can actually pass laptop parameters inside Student constructor as well. But, as there are several number of
#configurations,it's better to create a class for Laptop inside Student class because laptop belongs to only students

class Student:  #Outer class
    def __init__(self, name, age):
        self.name = name
        self.age = age
        #self.lap = self.Laptop()    #Object is created inside outer class

    def display(self):
        print(self.name, self.age)
        #self.lap.display()
    #Inside class Student
    class Laptop:   #Inner class
        def __init__(self, ram, processor):
            self.ram =ram
            self.processor = processor

        def display(self):
            print(self.ram, self.processor)

s1 = Student('Febin', 24) #Object creation outside of outer class
s1.display()

s2 = Student("Sebastian", 60)
s2.display()

#print(s1.lap.ram) #As lap object is inside the student class,we need to mention like this to access laptop variables
l1 = Student.Laptop("8gb","i5")
l2 = Student.Laptop("16gb","i5")
l1.display()
l2.display()
#Object of inner class can be created inside Outer class or,
#it can be created outside the Outer class provided we use Outer class name to call it. -> Better way