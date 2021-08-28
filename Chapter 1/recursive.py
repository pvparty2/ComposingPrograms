def sum_digits(n) -> int:
    '''Add all individual numbers in a number.'''
    if n < 10:
        return n
    else:
        all_but_last = n // 10
        last = n % 10
        return sum_digits(all_but_last) + (last)


print(sum_digits(4562))


def factorial(n) -> int:
    if n == 1:
        return n
    else:
        all_but_last = n - 1
        last = n
        return factorial(all_but_last) * last


print(factorial(4))


# Mutual Recursion
def is_even(n):
    if n == 0:
        return True
    else:
        return is_odd(n-1)


def is_odd(n):
    if n == 0:
        return False
    else:
        return is_even(n-1)


print(is_even(5))


def cascade(n):
    print(n)
    if n >= 10:
        cascade(n//10)
        print(n)


cascade(2013)


def alice(n):
    if n == 0:
        print('Bob wins!')
    else:
        bob(n-1)

def bob(n):
    if n == 0:
        print('Alice wins!')
    elif (n%2) == 0:
        alice(n-2)
    else:
        alice(n-1)


alice(20)


def count_partitions(n, m):
    '''Count the ways to partition n using parts up to m.
        For example, the number of partitions of 6 using parts up to 4 is 9.
    '''
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        return count_partitions(n-m, m) + count_partitions(n, m-1)


print(count_partitions(6, 6))

