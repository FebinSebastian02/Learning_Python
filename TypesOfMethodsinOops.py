#There are 3 types of methods in OOPs:- 1) Instance methods 2) Class methods 3) Static methods
#In variables class and static variables were same, but in methods, they are different

#1) Instance methods are used to work with instance variables. While working with instance varibales, we use self keyword.
#There are 2 types of Instance method as well:- a) Accessor methods b) Mutator methods
#a) Accessor methods (getters):- they just fetch the value or they just get the value
#b) Mutator methods (setters):- they change the value or they set the value

#2) Class methods are used to work with class variables. While working with class variables, we use cls keyword.

#3) Static methods are used when we don't want to work with Instance/Class variables.
#eg:-

class Student:
    school = "ABC"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):  #This is an Instance method as it works with the object. Because, for different objects the method will
                    #will behave differently
        return (self.m1 + self.m2 + self.m3)/3

    def get_m1(self):   #Accessor method/accessor/getter
        return self.m1
    def set_m1(self, newValue): #Mutator method/mutator/setter
        self.m1 = newValue

    @classmethod #This is a decorator used to mention getSchoolName as a class method
    def getSchoolName(cls):  #Class method. We need to use cls keyword for class methods
        return cls.school

    @staticmethod #This is decorator is used to mention info is a static method
    def info(): #For a static method, we don't want to pass cls/self in brackets.
        print("The school has 25 classrooms")

student1 = Student(10, 20, 30)
student2 = Student(40, 50, 60)

print("Avergage marks of student 1:- {}".format(student1.avg()))
print("Avergage marks of student 2:- {}".format(student2.avg()))

print(student1.get_m1())
student2.set_m1(50)
print(student2.m1)

print(Student.getSchoolName())  #As getSchoolName is a class method, we use class name to call the method

print(Student.info())   #As info is a static method, we use class name to call the method


