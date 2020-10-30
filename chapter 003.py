# HANDLING ERRORS

# EXCEPTIONS:


#syntax and exception
# syntax----> occurs when IDE detects incorrect code format
# Exception,causes errors even if the code's syntax is correct

#syntax error
a=5 print(5) 
print(hello)))

# exceptions

#type error 
print("juma Allan" + 10)
#import error
import nonexisting_module
#name error
a=20
b=h
#FilenotFoundError
file_f = open('nonfile.txt')
#Value Error
value_list=[10,20,3,40]
value_list.remove(15)
#index error
print(value_list[6])
#key error
my_dict = {'Code':'likeNinja'}
print(my_dict['year'])


#Raising exceptions

#check computer's ram
toshiba = 8
if toshiba<16:
    raise Exception('You need additional Ram')
    

  #Raising exceptions

#check computer's ram
toshiba = 8
if toshiba<16:
    raise Exception('You need additional Ram')
     
# using Assert statement
assert(toshiba>=16), 'More Ram needed to run android studio'

# Try catch Exception block

#division by 0 error
try:
    div = 5/0
except:
    print("No division by Zero allowed !")
    
# catch by exception 
#division by 0 error
try:
    div = 5/0
except Exception as e:
    print(e)    # division by zero
    

# catch specific errors
try:
    div = 5/0
    addString = 10 + '10'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
    
    
# Finally and close Else
try:
    a = 10/0
    b = a + 15
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print("all is OK")
finally:
    print("always running......if correct/not")
    
    

# define error classes

class NetWorkTooLow(Exception):
    pass

def checking_networkTraffic(i):
    if i <500:
        raise NetWorkTooLow('Low bandwidth in Data Link layer')
    
print(checking_networkTraffic(2000))

#using try cath

try:
    checking_networkTraffic(250)
except Exception as e:
    print(e)

# Try catch Exception block with defined func inside
# takes in exception as the base class

class TrafficTooHigh(Exception):
    pass

class TrafficToLow(Exception):
    def __init__(self, warnings,exact_value):
        self.warnings = warnings
        self.exact_value = exact_value

def check_traffic(x):
    if x > 500:
        raise TrafficTooHigh('Don\'t drive just board a cab')
    if x<499:
        raise TrafficTooHigh('You can drive safely',x)

try:
    check_traffic(10)
except TrafficTooHigh as e:
    print(e)
except TrafficToLow as e:
    print(e)
    
    
    
# LOGGING
# log levels in python
# Debug, info, warning,error, critical

import logging

logging.error('error messsage')
logging.debug('Debugging message')
logging.warning('warning message')
logging.critical("critical message")
logging.info('info message')


# LOGGING
# log levels in python
# Debug, info, warning,error, critical

import logging

# basic configuration
# check on documentation--->logging.basicConfig on python.org

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%m/%d/%y %H:%M:%S')

logging.error('error messsage')
logging.debug('Debugging message')
logging.warning('warning message')
logging.critical("critical message")
logging.info('info message')

# Desired Output
10/30/20 11:04:24 - root - ERROR - error messsage
10/30/20 11:04:24 - root - DEBUG - Debugging message
10/30/20 11:04:24 - root - WARNING - warning message
10/30/20 11:04:24 - root - CRITICAL - critical message
10/30/20 11:04:24 - root - INFO - info message





# Logging not from the Root
# basic configuration
#check on documentation--->logging.basicConfig on python.org

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%m/%d/%y %H:%M:%S')

#creating your own logger module
# create a different file and name it logger module where you will import to the mail file.
# avoid using the root

import loggerModule






 

