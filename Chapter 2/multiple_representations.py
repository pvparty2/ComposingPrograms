def make_adder(n):
    def adder(k):
        return n + k
    return adder


class Adder(object):
    def __init__(self, n):
        self.n = n
    def __call__(self, k):
        return self.n + k


# Multiple Representation
class Number:
    def __add__(self, other):
        return self.add(other)
    def __mul__(self, other):
        return self.mul(other)


class Complex(Number):
    def add(self, other):
        return ComplexRI(self.real + other.real, self.imag + other.imag)
    def mul(self, other):
        magnitude = self.magnitude * other.magnitude
        return ComplexMA(magnitude, self.angle + other.angle)


from math import atan2
class ComplexRI(Complex):
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    @property   # allows functions to be called without call expression syntax
    def magnitude(self):
        return (self.real ** 2 + self.imag ** 2) ** 0.5
    @property
    def angle(self):
        return atan2(self.imag, self.real)
    def __repr__(self):
        return f'ComplexRI({self.real}, {self.imag})'


from math import sin, cos, pi
class ComplexMA(Complex):
    def __init__(self, magnitude, angle):
        self.magnitude = magnitude
        self.angle = angle
    @property
    def real(self):
        return self.magnitude * cos(self.angle)
    @property
    def imag(self):
        return self.magnitude * sin(self.angle)
    def __repr__(self):
        return f'ComplexMA({self.magnitude}, {self.angle/pi} * pi)'
    