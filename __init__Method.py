#__init__ -> Special method
#If there is a term special, then that method or variable will be having __. eg:- __name__ ->Special variable
class Computer:
    # This method is normally is used to initialize the variables.
    # This method acts as a constructor. That is, normally functions need to be manually called in order to be executed. But,
    # constructors, get called automatically.
    def __init__(self, ram, ssd, graphics): #Here, object is accepted in self.
#We need to assign the other 3 arguments to the objects if we want those argument to the part of objects. Here, as the object
#is accepted in self, the object is self.
        self.rams = ram #The accepting names can be different
        self.ssds = ssd
        self.graphics = graphics
#Now, the values passed as arguments are assigned to the objects and each object have it's own variables.
#That is, com1 have different ram, ssd and graphics than that of com2.
        print("Inside __init__" + ram, ssd, graphics ) #Here, ram,ssd and graphics are local variables
#Init gets executed twice even though we didn't call __init__. It executed twice because, during every object creation,
#__init__ method is called. As we have 2 objects, it was called twice.
#Now, if I want to pass some arguments to the __init__ method, i should pass it in the constructor.

    def config(self):
        print("The configuration is:- {},{},{}".format(self.rams, self.ssds, self.graphics))
#Here, as ram, ssd and graphics are now a part of Objects,we need to refer to the objects for printing those.
#Object creations
com1 = Computer("16 GB RAM", "1TB SSD", "8 GB RTX 3070 Ti") #Here, 3 arguments + object is also passed to __init__method.
#The passing of object is done behind the scenes.
com2 = Computer("8 GB RAM", "500 GB SSD", "4 GB RTX 3070 Ti")

#Here, we saw, one object has it's own method and it's own variables and they are working together.

Computer.config(com1)
com2.config()