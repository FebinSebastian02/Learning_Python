print("print() inside SpecialVariable2 "+__name__)

#we are defining some functions in this module also.
#Here, add and sub functions are called inside main(). When we run this module as an independent(standalone) module,
#we get the output as Result is, Result is
def add():
    print("Result is " + __name__)
def sub():
    print("Result is "+ __name__)

def main():
    add()
    sub()

if __name__ == "__main__":
    main()