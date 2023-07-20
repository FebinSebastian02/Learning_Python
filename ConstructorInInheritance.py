#When a class(Class B) inherits another class(Class A) and an object of sub class is created, it will first try to find
#the init method of sub class and if init is not present in sub class, it call the init method of super class.
#Here, A have init method, wheras B doesn't have init method. Therefore, when object of B is created,it calls the init of A.

class A:
    def __init__(self):
        print("In A init")
    def feature1(self):
        print("In feat1-A")
    def feature2(self):
        print("In feat2")

class B(A): #Class B inheriting Class A
    def feature3(self):
        print("In feat 3")
    def feature4(self):
        print("In feat 4")
b1 = B()

#When a sub class(Class D) inherits a super class(Class C) and an object of sub class is created,it will try to find the
#init method of sub class. It init method is present in sub class,then it will print only the init method of sub class.
#Here, if we need to call the init of parent class as well, then we need to use super method inside init of sub class.

class C:
    def __init__(self):
        print("In C init")
    def feature1(self):
        print("In feat1-C")

class D(C): #Class D inheriting Class C
    def __init__(self):
        super().__init__()  #With super(), all features of class C can be accessed
        print("In D init")
    def feature6(self):
        print("In feat 6")
d1 = D()

#Suppose class E inherits both A and C. If we create an object of E, it prints the init of E.
#If super() is used, it can only access the init of A because A is passed as the left argument while inheriting. that is,
#class E(A, C) -> Here, comes the concept of Method Resolution Order(MRO), i.e, whenever we have a multiple inheritance,
#it considers the class from left to right.
#If it was class E(C,A), then init of C can only be accessed with super()
#The same concept applies to methods as well. If there are 2 same method names in A and C. If the method is called with the
#object of E, then the method of class A will be called. Because, A is passed as the left argument.

class E(A, C):  #Here,A is left and C is right.
    def __init__(self):
        super().__init__()  #super() can only access the init of A here as A is passed as left argument while inheriting
        print("In E init")
e1 = E()
e1.feature1()

