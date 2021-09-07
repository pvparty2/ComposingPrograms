class Link:
    '''A linked list with a first element and the rest.'''
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]

    def __len__(self):
        return 1 + len(self.rest)

    def __repr__(self):
        '''Return a string that would evaluate to s.'''
        if self.rest is Link.empty:
            rest = ''
        else:
            rest = f', {self.rest.__repr__()}'
        return f'Link({self.first}{rest})'


def extend_link(s, t):
    if s is Link.empty:
        return t
    else:
        return Link(s.first, extend_link(s.rest, t))

Link.__add__ = extend_link


def map_link(f, s):
    if s is Link.empty:
        return s
    return Link(f(s.first), map_link(f, s.rest))


def filter_link(f, s):
    if s is Link.empty:
        return s
    else:
        filtered = filter_link(f, s.rest)
        if f(s.first):
            return Link(s.first, filtered)
        else:
            return filtered


def join_link(s, separator=','):
    if s is Link.empty:
        return ''
    if s.rest is Link.empty:
        return s.first
    return f'{s.first}, {join_link(s.rest)}'


#### Partitions ####
def partitions(n, m):
    '''
        Return a linked list  of partitions of n using parts of up to m.
        Each partition is represented as a linked list.'''
    if n == 0:
        return Link(Link.empty) # A list containing the empty partition.
    elif n < 0 or m == 0:
        return Link.empty
    else:
        using_m = partitions(n-m, m)
        with_m = map_link(lambda s: Link(m, s), using_m)
        without_m = partitions(n, m-1)
        return with_m + without_m


def print_partitions(n, m):
    lists = partitions(n, m)
    strings = map_link(lambda s: join_link(s, ' + '), lists)
    print(join_link(strings, '\n'))



#### Tree ####
class Tree:
    def __init__(self, label, branches=()): # label is an internal value at the root of each subtree
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = branches

    def __repr__(self):
        if self.branches:
            return f'Tree({self.label}, {repr(self.branches)})'
        else:
            return f'Tree({repr(self.label)})'
    
    def is_leaf(self):
        return not self.branches


def fib_tree(n):
    if n == 1:
        return Tree(0)
    elif n == 2:
        return Tree(1)
    else:
        left = fib_tree(n-2)
        right = fib_tree(n-1)
        return Tree(left.label + right.label, (left, right))


def sum_labels(t):
    '''Sum the labels of a Tree instance, which may be None.'''
    return t.label + sum([sum_labels(b) for b in t.branches])


##### Sets #####
def empty(s):
    return s is Link.empty


def set_contains(s, v):
    '''Return True if and only if set s contains v.'''
    if empty(s):
        return False
    elif s.first == v:
        return True
    else:
        return set_contains(s.rest, v)


def adjoin_set(s, v):
    '''Return a set containig all elements of s and element v.'''
    if set_contains(s, v):
        return s
    else:
        return Link(v, s)


