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



