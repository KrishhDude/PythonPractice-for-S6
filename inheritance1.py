'''
~to inherit a class, put the parent class name in the paranthesis of child class
here, Derived(Base)

~to keep a variable or instance private, put double underscores befoe the
instance/var name
here, __d
Error while accessing a private instance:
"AttributeError: 'Derived' object has no attribute 'd'"

'''
class Base():
    def __init__(self):
        print("base")
        self.c = 100    #public var
        self.__d = 20   #private instance(cant inherit)
class Derived(Base):
    def __init__(self):
        super().__init__()
        print("derived")
        print(self.c)
        #print(self.d)  will return error
s=Derived()
print(s)