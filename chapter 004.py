# DECORATORS

# DECORATORS IN PYTHON

# DECORATORS IN PYTHON
# modifying classes and functions in python

def before_after_dec(func):
    def wrapper():
        print('before this')
        func()
        print('after function')
    return wrapper
    
def user_name():
    print("Timz Owen")

user_name = before_after_dec(user_name)

user_name()

# before this
# Timz Owen
# after function

#same as  (using '@')
def before_after_dec(func):
    def wrapper():
        print('before this')
        func()
        print('after function')
    return wrapper
@before_after_dec
def user_name():
    print("Timz Owen")
user_name()


# functions with arguments
# Functions with Arguments

def before_after_dec(func):
    def wrapper(*args, **kwargs):
        print('before this')
        results = func(*args, **kwargs)
        print('after function')
        return results
    return wrapper
# arguments
@before_after_dec
def additionBy20(y):
    return y + 10

print(additionBy20(12))


# Function Identity


def before_after_dec(func):
    def wrapper(*args, **kwargs):
        print('before this')
        results = func(*args, **kwargs)
        print('after function')
        return results
    return wrapper
#arguement
@before_after_dec
def additionBy20(y):
    return y + 10

print(help(additionBy20))
print(additionBy20.__name__)
#output
# Help on function wrapper in module __main__:

# wrapper(*args, **kwargs)

# None
# wrapper     # which is not correct and so,

#soln
import functools


def before_after_dec(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('before this')
        results = func(*args, **kwargs)
        print('after function')
        return results
    return wrapper
#arguement
@before_after_dec
def additionBy20(y):
    return y + 10

print(help(additionBy20))
print(additionBy20.__name__) # correct output now

#output 
# Help on function additionBy20 in module __main__:

# additionBy20(y)

# None
# additionBy20



# Recap 2

import functools

def orders(num_orders):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_orders):
                final_result=func(*args, **kwargs)
            return final_result
        return wrapper
    return decorator_repeat
@orders(num_orders=2)
def command(team):
    print(f'Team G, Ready to Attack!11, Clear team {team}')
command('H')


