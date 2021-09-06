'''
An example of data representation using linked lists.
'''

empty = 'empty'

def is_link(s):
    '''s is a linked list if it is empty or a (first, rest) pair.'''
    return s == empty or (len(s) == 2 and is_link(s[1]))


def link(first, rest):
    '''Construct a linked list from its first element and the rest.'''
    assert is_link(rest), 'rest must be a linked list'
    return [first, rest]


def first(s):
    '''Return the first element of a linked list s.'''
    assert is_link(s), 'first only applies to linked lists.'
    assert s != empty, 'empty linked list has no first element'
    return s[0]


def rest(s):
    '''Return the rest of the elements of a linked list s.'''
    assert is_link(s), 'rest only applies to linked lists.'
    assert s != empty, 'empty linked list has no rest'
    return s[1]


def len_link(s):
    '''Return the length of a linked list.'''
    length = 0
    while s != empty:
        s, length = rest(s), length + 1
    return length


def getitem_link(s, i):
    '''Return the element at index i of linked list s.'''
    if i == 0:
        return first(s)
    return getitem_link(rest(s), i - 1)        


def extend_link(s, t):
    '''Return a linked list with the elements of s followed by elements of t.'''
    assert is_link(s) and is_link(t)
    if s == empty:
        return t
    return link(first(s), extend_link(rest(s), t))
    

def apply_to_all_link(f, s):
    '''Apply function f to each element of s.'''
    assert is_link(s)
    if s == empty:
        return s
    return link(f(first(s)), apply_to_all_link(f, rest(s)))


def keep_if_link(f, s):
    '''Return a linked list of elements of s for which f(e) is true.'''
    assert is_link(s)
    if s == empty:
        return s
    else:
        kept = keep_if_link(f, rest(s))
        if f(first(s)):
            return link(first(s), kept)
        else:
            return kept


def join_link(s, separator):
    '''Return a string of all elements in s separated by separator.'''
    assert is_link(s), 'must be a linked list'
    if s == empty:
        return s
    elif rest(s) == empty:
        return str(first(s))
    return f'{str(first(s))}{separator} {join_link(rest(s), separator)}'


def partitions(n, m):
    '''
        Return a linked list of partitions of n using parts of up to m.
        Each partition is represented as a linked list.
    '''
    if n == 0:
        return link(empty, empty) # A list containing the empty partition
    elif n < 0 or m == 0:
        return empty
    else:
        using_m = partitions(n-m, m)
        with_m = apply_to_all_link(lambda s: link(m, s), using_m)
        without_m = partitions(n, m-1)
        return extend_link(with_m, without_m)


def print_partitions(n, m):
    lists = partitions(n, m)
    strings = apply_to_all_link(lambda s: join_link(s, ' + '), lists)
    print(join_link(strings, '\n'))

    
'''
Implementation of a mutable linked list.
'''


def mutable_link():
    '''Return a function implementaion of a mutable linked list.'''
    contents = empty
    def dispatch(message, value=None):
        nonlocal contents
        if message == 'len':
            return len_link(contents)
        elif message == 'getitem':
            return getitem_link(contents, value)
        elif message == 'push_first':
            contents = link(value, contents)
        elif message == 'pop_first':
            f = first(contents)
            contents = rest(contents)
            return f
        elif message == 'str':
            return join_link(contents, ', ')
    return dispatch


def to_mutable_link(source):
    '''Return a functional list with the same contents as source.'''
    s = mutable_link()
    for e in reversed(source):
        s('push_first', e)
    return s


