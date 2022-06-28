class com:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram
    def config(self):
        print("config is", self.cpu, self.ram)

com1 = com("i5",16)
com2 = com("i3", 8)
com1.config()
com2.config()

#print class of the given object
print(type(com1))
