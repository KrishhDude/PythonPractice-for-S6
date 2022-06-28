def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner
@smart_div
def div(a,b):
    c=print(a/b)
    return c
#div=smart_div(div)
div(2,4)

#output:
#with decorator: 2.0
#without: 0.5