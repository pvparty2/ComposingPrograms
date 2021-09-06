'''Minimum perimeter of a rectangle given the rectangles Area.'''
def divisors(n):
    return [1] + [x for x in range(2, n) if n % x == 0]


def width(area, height):
    assert area % height == 0
    return area // height


def perimeter(width, height):
    return 2 * width + 2 * height


def minimum_perimeter(area):
    heights = divisors(area)
    widths = [width(area, h) for h in heights]
    h_w_pairs = zip(heights, widths)
    perimeters = [2 * h + 2 * w  for h, w in h_w_pairs]
    return min(perimeters)


