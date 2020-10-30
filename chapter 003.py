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


# use the config file on the files in the code to import

import logging
import logging.config
# file configuration

logging.config.fileConfig('logging.conf')

logger = logging.getLogger('simpleExample')
logger.debug('debug message')



# Dealing with structraces in python
import logging 
#lisr out of range

try:
    list_range = [1,2,3,4,5]
    b = list_range[6]
except IndexError as e:
    logging.error(e)    # out of range


# get the exact error and value causing error
try:
    list_range = [1,2,3,4,5]
    b = list_range[6]
except IndexError as e:
    logging.error(e, exc_info=True)    # out of range
    
    
# Not sure of the exact type of error
import logging
import traceback
#lisr out of range

try:
    list_range = [1,2,3,4,5]
    b = list_range[6]
except IndexError as e:
    logging.error("Error is %s", traceback.format_exc())



# Rotating file handlers
# allows you to keep track of most recent errors where files are large

import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# roll over to next files once we are at 3kb per file and keep recording log errors
handler = RotatingFileHandler('app.log', maxBytes=3000, backupCount=6)
logger.addHandler(handler)

for _ in range(15000):
    logger.info('Error code on line 123 of 12') # creates files in the folder ith debug info each with 3kb memory space
    
# TimeRotating log File
# keeps record if the app is being logged after some time

import logging
import time
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# roll over to next files once we are at 3kb per file and keep recording log errors
handler = TimedRotatingFileHandler('timed_app.log', when='s',interval=10, backupCount=6)
logger.addHandler(handler)

for _ in range(15000):
    logger.info('Error code on line 123 of 12')
    time.sleep(5)
    
    
  JSON IN PYTHON

# JavaScript object Notation
# encoding dic to JSON

import json

laptop_status = {"brand":"Toshiba", "operation":2, "company":"Samsung","hasGPU":False,"Tasks":["Code","Gaming"]}

laptop_json = json.dumps(laptop_status, indent=4)
print(laptop_json)
      
{
    "brand": "Toshiba",
    "operation": 2,
    "company": "Samsung",
    "hasGPU": false,
    "Tasks": [
        "Code",
        "Gaming"
    ]
}

# print sorted keys
laptop_json = json.dumps(laptop_status, indent=4, sort_keys=True)
print(laptop_json)

{
    "Tasks": [
        "Code",
        "Gaming"
    ],
    "brand": "Toshiba",
    "company": "Samsung",
    "hasGPU": false,
    "operation": 2
}



# export to File 
# encoding dic to JSON

import json

laptop_status = {"brand":"Toshiba", "operation":2, "company":"Samsung","hasGPU":False,"Tasks":["Code","Gaming"]}


#create and dump to a new file
with open('laptops.json','w') as file:
    json.dump(laptop_status, fil,indent=4)
# creates a file with the json data inside it



# encoding dic to JSON

import json

#Decerealization back to dictionary from json

laptop_status = {"brand":"Toshiba", "operation":2, "company":"Samsung","hasGPU":False,"Tasks":["Code","Gaming"]}

laptopJSON = json.dumps(laptop_status, indent=4)

laptop = json.loads(laptopJSON)
print(laptop)


# decoding from a json file to a dict file
#Decerealization back to dictionary from json

laptop_status = {"brand":"Toshiba", "operation":2, "company":"Samsung","hasGPU":False,"Tasks":["Code","Gaming"]}

laptopJSON = json.dumps(laptop_status, indent=4)

# decode into a file from json file
with open('laptops.json', 'r') as file:
    lapi = json.load(file)
    print(lapi)




