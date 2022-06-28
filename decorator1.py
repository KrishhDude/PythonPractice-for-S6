def guard_zero(operate):
    def inner(x,y):
        if y==0:
            print("cannod div by 0")
            return
        return operate(x,y)
    return inner
@guard_zero