#One of the concepts in Oop is Inheritance.
#Suppose, we have 2 classes. Let the first class have 2 methods. Also, the second class have 2 other methods.
#Now, if we need to access the methods in second class, we need to create objects for second class. If we need to access
#the methods in first class as well in the second class, then we need to mention that class 2 is the child of class 1.

#Here, the Inheritance comes into picture. That is, whatever belongs to the parent class(super class), belongs to the
#child class(sub class) as well. Sub class can access the features of Super class. But, Super class can't access the features
#of Sub class.

#Types of Inheritance:-
#a) Single level Inheritance - 1 sub class inheriting 1 super class
#eg:- B inheriting A
#b) Multilevel Inheritance - 1 sub class inheriting 1 super class and it's superior super class.
#eg:- C inheriting B
#c) Multiple Inheritance:- 1 child class inheriting more than 1 parent classes
#eg:- E inheriting A and D
class A:
    def func1(self):
        print("Inside func1")
    def func2(self):
        print("Inside func2")

class B(A): #Class B inherits class A
    def func3(self):
        print("Inside func3")
    def func4(self):
        print("Inside func4")

class C(B): #Class C inherits class B
    def func5(self):
        print("Inside func5")

class D:
    def func6(self):
        print("Inside func6")

class E(A, D):  #Class E inherits A and D
    def func7(self):
        print("Inside func7")

obj1 = A()
obj1.func1()
obj1.func2()

obj2 = B()
obj2.func3()
obj2.func4()

#After Inheritance, functions from class A can be accessed with class B object
obj2.func1()
obj2.func2()

#Object of class C can access all functions of class A and B as class C inherits class B which inherits class A.
obj3 = C()
obj3.func1()
obj3.func2()
obj3.func3()
obj3.func4()
obj3.func5()

#Object of class E can access functions of class A and D as class E inherits both A and D
obj4 = E()
obj4.func7()
obj4.func1()
obj4.func2()
obj4.func6()
