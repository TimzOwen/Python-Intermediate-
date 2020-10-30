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

