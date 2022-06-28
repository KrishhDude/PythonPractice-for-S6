try:
    print("hello")
except:
    print("Something went wrong")
else:
    print("Nothing wrong")
#hello
#Nothing wrong
try:
    print(x)
except:
    print('Something wrong')
finally:
    print("try except finish")
#Something wrong
#try except finish
#finally block executes regardless of error raised or not

#raise an exception
#raise an error and stop run if x<0
x=-1
if x<0:
    raise Exception("Sorry, below zero")

#    raise Exception("Sorry, below zero")
#Exception: Sorry, below zero


#define what kind of error to raise
#raise a TypeError if x not int
x='hi'
if not type(x) is int:
    raise TypeError("Only integers allowed")

#IndexError
a=[1,2,3]
try:
    print(a[3])
except IndexError:
    print("index error raised")