#Other than looping and printing values in a collection by their index, we have one more method known as Iterator.
#iter() converts a collection to an iterator.
#Iterator gives values in a collection one by one. next() and __next__() gives the values one by one

nums = [1, 2, 3, 4, 5]

it = iter(nums)
# print(it)   #prints the object of iterator
# print(it.__next__())    #prints the first value of list
# print(it.__next__())    #prints the second value of list
# print(it.__next__())
# print(next(it))
# print(next(it)) #another method to print next value

#Creating own Iterator
#An Iterator needs to 2 methods, i) __iter__() -> give object of Iterator. Makes the object iterable
                              # ii) __next__() -> give next value/ next object
#A class to print top 10 numbers

class Top10:
    def __init__(self):
        self.value = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.value <= 10:
            value = self.value
            self.value += 1
            return value
        else:
            raise StopIteration #raise keyword is used to raise an exception. StopIteration is the exception here

values = Top10()
print(values.__next__())
print(values.__next__())
# print(values.__next__())
# print(values.__next__())
# print(values.__next__())
# print(values.__next__())
# print(values.__next__())
# print(values.__next__())
# print(values.__next__())
# print(values.__next__())

for i in values:    #for loop internally uses __next__(). Therefore, we get the next values one by one from object values.
    print(i)
#Here,as we have already got the first and second values using __next__(), we will only get the remaining values when we
#use for loop.