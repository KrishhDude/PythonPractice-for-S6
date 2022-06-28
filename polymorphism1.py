'''
same function name but different signatures being used for different data types.
len()- 
being used for a string: print(len("geeks"))
being used for a list  : print(len([1,2,3]))

'''
#example of user-defined polymorphism
def add(x,y,z=0):
    return x+y+z
print(add(2,3))
print(add(2,3,4))