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
    

# Generic Functions
from math import gcd
class Rational(Number):
    def __init__(self, numer, denom):
        g = gcd(numer, denom)
        self.numer = numer // g
        self.denom = denom // g
    def __repr__(self):
        return f'Rational ({self.numer}, {self.denom})'
    def add(self, other):
        nx, dx = self.numer, self.denom
        ny, dy = other.numer, other.denom
        return Rational(nx * dy + ny * dx, dx * dy)
    def mul(self, other):
        numer = self.numer * other.numer
        denom = self.denom * other.denom
        return Rational(numer, denom)

# Type Dispatching
def is_real(c):
    '''Return whether c is a real number with no imaginary part.'''
    if isinstance(c, ComplexRI):
        return c.imag == 0
    elif isinstance(c, ComplexMA):
        return c.angle % pi == 0 


def add_complex_and_rational(c, r):
    return ComplexRI(c.real + r.numer/r.denom, c.imag)


def mul_complex_and_rational(c, r):
    r_magnitude, r_angle = r.numer/r.denom, 0
    if r_magnitude < 0:
        r_magnitude, r_angle = -r_magnitude, pi
    return ComplexMA(c.magnitude * r_magnitude, c.angle + r_angle)


def add_rational_and_complex(r, c):
    return add_complex_and_rational(c, r)


def mul_rational_and_complex(r, c):
    return mul_complex_and_rational


class Number:
    def __add__(self, other):
        if self.type_tag == other.type_tag:
            return self.add(other)
        elif (self.type_tag, other.type_tag) in self.adders:
            return self.cross_apply(other, self.adders)
    def __mul__(self, other):
        if self.type_tag == other.type_tag:
            return self.mul(other)
        elif (self.type_tag, other.type_tag) in self.multipliers:
            return self.cross_apply(other, self.multipliers)
    def cross_apply(self, other, cross_fns):
        cross_fn = cross_fns[(self.type_tag, other.type_tag)]
        return cross_fn(self, other)
    adders = {('com', 'rat'): add_complex_and_rational,
              ('rat', 'com'): add_rational_and_complex}
    multipliers = {('com', 'rat'): mul_complex_and_rational,
                   ('rat', 'com'): mul_rational_and_complex}


