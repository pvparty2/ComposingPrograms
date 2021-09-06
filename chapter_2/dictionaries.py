from typing import NoReturn


def dictionary():
    '''Return a functional implementation of a dictionary.'''
    records = [] # list of (key, value) pairs
    def getitem(key):
        matches = [r for r in records if r[0] == key]
        if len(matches) == 1:
            key, value = matches[0]
            return value
    def setitem(key, value):
        nonlocal records
        non_matches = [r for r in records if r[0] != key]
        records = non_matches + [[key, value]]
    def dispatch(message, key=None, value=None):
        if message == 'getitem':
            return getitem(key)
        elif message == 'setitem':
            setitem(key, value)
    return dispatch
        

def account(initial_balance) -> dict:
    def deposit(amount):
        dispatch['balance'] += amount
        return dispatch['balance']
    
    def withdraw(amount):
        if amount > dispatch['balance']:
            return 'Insufficient Funds'
        dispatch['balance'] -= amount
        return dispatch['balance']

    dispatch = {'deposit': deposit,
                'withdraw': withdraw,
                'balance': initial_balance}
    return dispatch


def withdraw(account, amount):
    return account['withdraw'](amount)
def deposit(account, amount):
    return account['deposit'](amount)
def check_balance(account):
    return account['balance']


# Ideal Gas Law: P * V = n * K * T
# Celsius vs Fahrenheit: 9 * C = 5 * (F - 32)
# Constraint Programming
def connector(name=None):
    '''A connector between constraints.'''
    informant = None
    constraints = []
    def set_value(source, value):
        nonlocal informant
        val = connector['val']
        if val is None:
            informant, connector['val'] = source, value
            if name is not None:
                print(f'{name} = {value}')
            inform_all_except(source, 'new_val', constraints)
        elif val != value:
            print(f'Contradiction detected: {val} vs {value}')
    
    def forget_value(source):
        nonlocal informant
        if informant == source:
            informant, connector['val'] = None, None
            if name is not None:
                print(f'{name} is forgotten')
            inform_all_except(source, 'forget', constraints)

    connector = {'val': None,
                 'set_val': set_value,
                 'forget': forget_value,
                 'has_val': lambda: connector['val'] is not None,
                 'connect': lambda source: constraints.append(source), }
    return connector


def inform_all_except(source, message, constraints):
    '''Inform all constraints of the message, except source.'''
    for c in constraints:
        if c != source:
            c[message]()


def converter(c, f):
    '''pass'''
    pass  # I choose to use object oriented programming, instead.
          # Maybe I will come back to this topic in the future.