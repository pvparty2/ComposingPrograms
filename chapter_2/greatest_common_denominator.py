'''
    The greatest common denominator between 2 numbers is 
    the largest positive integer that can divide both numbers, separately, 
    with zero remainder.'''
def gcd_1(a, b):
    '''Euclidian Method.'''
    remainder = 1
    while remainder > 0:
        remainder = a % b
        a = b
        b = remainder

    return a


def gcd_2(a, b):
    while b:
        a, b = b, a % b
    return a
