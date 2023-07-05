#Extra features can be added to the existing functions using Decorators.
#Suppose, we need to divide 2 numbers using a function in which the numerator should be always greater than the deominator.

def div(a, b):
    print(a / b)
div(2, 4)
#Here, numerator is less than denominator and we need to keep the numerator greater. Therefore, we should swap numbers.
def div(a, b):
    a, b = b, a #Code for swapping
    print(a / b)
div(2, 4)

#Suppose, this code for swapping is not present in this function or we are not able to modify the div function to
#add this code for swapping. In such situations, to add extra features to an existing function,we use Decorators.
#Here, we don't habe permission to write code for swapping inside existing div function
def div(a, b):
    print(a / b)

#decorator for existing div function is defined
def smartDiv(div):#Here, existing div function is passed as a parameter to smartDiv().
    #To write the logic, we are creating a new function inside a function
    def innerFunc(a, b):
        if a < b:
            a, b = b, a
        return div(a, b)    #Here, old div function is called by passing the swapped variables a & b.
    return innerFunc    #Function that has the logic is returned

div = smartDiv(div)    #old div function is passed to smart div(). Here, we can give name of div1 as div also
print(div.__name__)
div(2, 4)   #Here, we can give name of div1 as div also

#Flow
#1) smartDiv(div) is called and it doesn't goes inside innerFunc(a,b) as innerFunc(a,b) not called. Then, it returns
# inner function and assign it to div1
#2) div1() is called which is assigned to the innerFunc(a,b). Now, values are passed inside innerFun(a,b).
#3) condition is checked and values are swapped if condition is true. Then, old div function is called and new swapped
#variables are passed to the old div function
#4) result of a/b is printed

#In short, we are establishing an indirect connection to old div().