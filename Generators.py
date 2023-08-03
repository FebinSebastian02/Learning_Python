#Generators give us Iterators
#To create own Iterators, we need to define 2 methods:-  a) iter() b) __next__()
#If we need to avoid this process, we can use Generators.

#Use of Generators
#Suppose, we are fetching records from a Database with 1000 records. But if we only need to work with one record at a time,
#we can use Generators. So that, it fetch records one at a time.

#yield keyword makes our function a Generator
#return keyword terminates the function whereas, yield does not

class Top10:
    def printTop10(self):
        value = 1
        while value <= 10:
            yield value
            value += 1

obj = Top10()
values = obj.printTop10()
print(values.__next__())
print(values.__next__())
print(values.__next__())
print(values.__next__())
print(values.__next__())
print(next(values))
for i in values:
    print(i)
    