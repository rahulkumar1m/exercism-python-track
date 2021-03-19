import math

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        return (self.real == other.real) and (self.imaginary == other.imaginary)

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        return ComplexNumber(self.real * other.real - self.imaginary * other.imaginary, self.imaginary * other.real + self.real * other.imaginary)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __truediv__(self, other):
        real_part = (self.real * other.real + self.imaginary * other.imaginary)/(other.real**2 + other.imaginary**2)
        imaginary_part = (self.imaginary * other.real - self.real * other.imaginary)/(other.real**2 + other.imaginary**2)
        return ComplexNumber(real_part, imaginary_part)

    def __abs__(self):
        return math.sqrt(self.real**2 + self.imaginary**2)

    def conjugate(self):
        return ComplexNumber(self.real, -1 * self.imaginary)

    def exp(self):
        e_a = math.exp(self.real)
        return ComplexNumber(e_a*math.cos(self.imaginary), e_a*math.sin(self.imaginary))