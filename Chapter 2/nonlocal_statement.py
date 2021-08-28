'''
An example of how nonlocal statement works in Python.
The _nonlocal_ statement in the nested _withdraw_ function tells Python 
    that _balance_ is not local to the frame that the function was called.

Remove the _nonlocal_ statement and Python will raise an UnboundLocalError:
    "local variable 'balance' reference before assignment".

This means that Python performs actions before running the function because, otherwise,
    how would Python know that _balance_ is assigned somewhere else in the function?

Contrary to Python, many other programming languages treat _nonlocal_ as the default behavior.
'''

def make_withdraw(balance):
    '''Return a withdraw function that draws down balance with each call.'''
    def withdraw(amount):
        assert amount > 0, 'Can only withdraw an amount > 0'
        nonlocal balance
        if amount > balance:
            return 'Insufficient funds'
        else:
            balance = balance - amount
            return balance
    return withdraw