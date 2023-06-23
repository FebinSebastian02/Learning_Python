#Passing and updating values
def febin(x):
    print(id(x))
    x = 9   #The value of a is changed from 10 to 9
    print(x)
    print((id(x)))

a = 10
print(id(a))
febin(a)    #The value of a which is 10, is passed to variable x
print(a)    #Here, the value of a is not changed and 10 is printed
print(id(a))#The address of a is different to that of x

#The address of both a and x are same before we change the value. Once we change the value,the address of x changes.


#Is Python call by value or call by reference
#eg:1
def increment(a):
    a = a + 1
    print(a)
num = 10
increment(num)
print(num)

#According to the output of example 1, python shows property of call by value because, the value of num is unchanged even
#if we changed the value of num inside the increment().

#eg:2
def list1(a):
    a[0] = 2
    print(a)
    print(id(a))
myList = [1, 2, 3, 4]
list1(myList)
print(myList)
print(id(myList))

#According to the output of example 2, python shows the property of call by reference because, the value of myList is changed
#as we changed the value of myList inside the list1()

#The id of both myList and l are same which means that both of them are referring to the same object.This kind of parameter
#passing technique is called call by object.
#Here, we are passing the complete object as parameters to the function


#eg:3
def clearList(l):
    print(id(l))
    l = []
    print(id(l))
clearList(myList)
print(myList)
print(id(myList))

#Here, the id of both myList and l are same before l is assigned to empty list. That means, both myList and l were referring
#to same object before l was assigned to empty list.
#Once l was assigned to an empty list, the id of l gets changed as it is now referring to a newly created object which is
#the empty list.