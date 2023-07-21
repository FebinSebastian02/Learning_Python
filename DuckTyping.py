#If there's a bird that behaves like a duck (bird swimms,quacks,looks etc.like a duck), then the bird is probably a duck.

#eg:-
class Pycharm:
    def execute(self):
        print("Compiling")
        print("Running")
class Laptop:
    def code(self, ide): #This method executes the code. We need an ide to write the code. So an ide is passed. Here,
                         #we don't know the type of ide.
        ide.execute()   #This execute() does not belongs to this class as well.

#ide = Pycharm()

#Suppose, iff we create a new class and create the object 'ide' of the new class, then also the execute() will work.
#Irrespective o the ide, what is important is that the execute method should be present in new class as well to avoid error,

class MyEditor:
    def execute(self):
        print("Spellcheck")
        print("Autoformatting")
        print("Compiling")
        print("Running")

ide = MyEditor()

l1 = Laptop()
l1.code(ide)

#Here, we have an object ide and it have an execute method. The class to which ide belongs doesn't matter.
#The only thing that matters is whether the execution method is present in that class or not to which the object belongs
#or not