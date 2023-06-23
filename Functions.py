# Function definition
def greet():
    print('Hello')
    print('Good morning')

# Function calling done twice
greet()
greet()


# Addition of 2 numbers
def add(a, b):  #Here, a & b are called Arguments/Parameters. a & b stores the values passed during function calling.
    sum = a + b
    print(sum)

add(5, 5)

#Function return
def mul(c, d):  #Here,mul function is used to do the multiplication of 2 values
    product = c * d
    return product  #return is the keyword used to return a value

result = mul(5, 5)  #Here, the value(product) returned from the function is stored in a new variable called result
print(result)
#Code walkthrough
#Here, mul function is called and 2 values are passed. The flow goes to mul() definition and multiplies 2 values passed
#and stores inside a variable called product. This variable is then returned to the place where function was called and
#is stored inside a new variable called result. This result variable is then printed. The mul function was only responsible
#for just multiplying 2 numbers only

#Returning 2 values
def add_sub(a, b):
    sum = a + b
    sub = a - b
    return sum, sub

result1, result2 = add_sub(5, 5)    #Here,the 2 returned values are stored in 2 variables result1 and result2
print(result1)
print(result2)
