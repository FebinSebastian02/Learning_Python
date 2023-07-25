#If there's a class with 2 same method names and the methods have different types of arguments/different number of arguments,
#it's called Method Overloading.
#eg:- def avg(a,b)  -> 2 arguments
#     def avg(a,b,c)    -> 3 arguments
#In Python, we don't have this concept

#If there are methods with same names and same number of arguments,it's called Method Overriding.
#However,one class can't have methods with same name and same number of arguments. Method Overriding can only be achieved with
#the concept of Inheritance
#eg: - def avg(a,b)
#      def avg(a,b)

#Method Overloading -> Can't be done directly in Python. We are doing it by a trick.
#Suppose, we are not passing 3 arguments to sum(), in this case, we get an error. To avoid this error, we can keep accepting
#arguments by default as None. So, in case, incorrect number of arguments are passed, it will not throw an error. Because,
#the accepting argument will take the value as None if no argument was passed to it. If arguments are passed, None value
#will be replaced with the value of argument passed.
class Student:
    def sum(self, a = None, b = None, c = None):
        sum = 0
        if a != None and b != None and c != None:
            sum = a + b + c
        elif a != None and b != None:
            sum = a + b
        else:
            sum = a
        return sum

s1 = Student()
sum = s1.sum(5)
print(sum)

#Method Overriding
class A:
    def show(self):
        print("In A show")

class B(A): #B inherits A
    pass
b = B()
b.show()
#Here,the same method name in class A is called because class B have no methods

class C:
    def show(self):
        print("In C show")

class D(C):
    def show(self):
        print("In D show")

d = D()
d.show()
#Here, method in class D is called eventhough class C have same method name. The method in D overrides method in C