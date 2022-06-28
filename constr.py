class computer():
    pass
    def __init__(self):
        self.name="arshad"
        self.age="21"
    def update(self):
        self.age="20"

c1=computer()
print(id(c1))
print(c1.name, c1.age)

c2=computer()
print(c2.name)
c2.name="Krishnaprasad"
print(c2.name)

c1.update()
print(c1.age)
print(c2.age)
