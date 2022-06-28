'''
Method Overriding
implemented in java using abstract class
re-implementing a method is called method overriding

Abstract Classes in Python
An abstract class is a blueprint for other classes
Class containing one or more abstract method is Abstract Class
Abstract method has declaration but no implementation

Abstract classes and interface:
Abstract classes can contain concrete(normal) methods
Interface can only have interfaces

to implement abstract in python,
className(ABC) and module is abc
'''
from abc import ABC, abstractmethod


class poly(ABC):
    @abstractmethod
    def noofsides(self):
        pass
class Tri(poly):
    def noofsides(self):
        print("i have 3 sides")
s=Tri()
s.noofsides()

print(s.noofsides())
