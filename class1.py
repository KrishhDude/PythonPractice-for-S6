#class className:
class hey:
    def hello(self):
        print("hello from class")

#objectName = className()
h = hey()
h.hello()

#className.methodName(objectName)
hey.hello(h)

#__init__ method

class comp:
    def __init__(self):
        print("heyy")

c = comp()
print(c)