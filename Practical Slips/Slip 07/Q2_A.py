# Write Python class to perform addition of two complex numbers using binary + operator overloading.

class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __str__(self):
        return str(self.real) + " + " + str(self.imaginary) + "i"


c1 = Complex(2, 3)
c2 = Complex(3, 4)
print(c1 + c2)