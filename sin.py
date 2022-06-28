from math import factorial
def sinefn(x):
    sine = 0
    for i in range(10):
        sign = -1**i
        sine = sine + ((x**(2.0*i+1))/factorial(2*i+1))*sign
    return sine
def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    return 1

print(sinefn(46))