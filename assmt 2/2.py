class Complex ():
    def numSplit(self):
        self.real = int(input("Enter the real part"))
        self.imag = int(input("Enter the imaginary part: "))            

    def display(self):
        print(self.real,"+",self.imag,"i", sep="")

    def add(self, one, two):
        self.real = one.real + two.real
        self.imag = one.imag + two.imag

one = Complex()
two = Complex()
disp = Complex()

print("Enter first complex number")
one.numSplit()
print("Enter second complex number")
two.numSplit()

print("Sum = ", end="")
disp.add(one,two)
disp.display()