# In a + b, a and b are operands. + is the operator
#eg:-
a = 5
b = 6
print(a + b)
#Here, a and b are objects and 5 and 6 of type int. int is a class as well.
#int have a method called __add__. So whenever we write a + b, this __add__ method in int class is called.
print(int.__add__(a, b))

#Similarly for strings,
c = "feb"
d = "in"
print(c + d)
#Here, c and d are objects of type string. String is a class as well.
#String have a method called __add__ which concatenates 2 strings. This method is called when we add 2 strings
print(str.__add__(c, d))

#Operator overloading
#From the above examples, we understood that integer class and string class have add methods.
#But if I create a new class and add 2 objects together, then it will throw error because we don't have add method defined
#in our new class.
#Therefore, we need to overload the plus operator in our new class by defining __add__method in order to add 2 objects.
#eg:-
class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
    def __add__(self, other):   #s1 = self, s2 = other
        m1 = self.m1 + other.m1 #-> s1.m1 + s2.m1
        m2 = self.m2 + other.m2 #-> s1.m2 + s2.m2
        s3 = Student(m1, m2)    #init of s3 is called. s3.m1 = m1 we passed and s3.m2 = m2 we passed
        return s3
    def __gt__(self, other):    #s1 = self, s2 = other
        mS1 = self.m1 + self.m2 #mS1 denotes mark of student1
        mS2 = other.m1 + other.m2   #mS2 denotes mark of student2
        #Here,ms1 and ms2 are of type int.
        if mS1 > mS2:
            return True
        else:
            return False
    def __str__(self):
        return f"{self.m1},{self.m2}"
s1 = Student(10, 20)
s2 = Student(30, 40)
s3 = s1 + s2    #Behind the scenes, once __add__ method is defined, __add__ method is called as follow:
                #Student.__add__(s1, s2)
print(s3.m1)
print(s3.m2)

#This same thing above can be done with multiplication, subtraction etc. as well

#Suppose, we need to compare 2 objects based on their marks, we need to define the method.
if s1 > s2: #Here, we need to overload > operator. Once __gt__ method is defined, it's called as follow:
            #Student.__gt__(s1, s2)
    print("s1 wins")
else:
    print("s2 wins")

#Similarly, let's try to print an object
a = 10  #a is an object of type int
print(a)
#Here, we get value of a. Behind the scenes,__str__() is called. i.e, a.__str__()
print(a.__str__())
print(s1)   #s1 is an object of type Student
#Here, we get module and address of s1. Behind the scenes,__str__() is called. i.e, s1.__str__()
print(s1.__str__())
#Therefore, we need to override this, inorder to get a value for s1. Suppose, i need to get marks of s1, when s1 is
#printed, then we need to define __str__ in our Student class
