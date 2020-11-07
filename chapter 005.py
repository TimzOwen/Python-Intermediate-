
# MULTIPROCESSING

from multiprocessing import Process
import os

def squared_number():
    for i in range(1000):
        i * i
if __name__ == "__main__":
    processes = []
    num_process = os.cpu_count()
for i in range (num_process):
    process = Process(target=squared_number)
    process.append(process)
for process in processes:
    process.start()
for process in processes:
    process.join()

# MultiProcessing share data for one value
from multiprocessing import Process, Value, Array
import os
def squared_Number():
    for i in range(1000):
        i * i
if __name__ == "__main__":
    shared_number = Value('i',1)
    print("Number at starting point is ", shared_number.value) # 1
    

# MultiProcessing shared value with more than  one process
from multiprocessing import Process, Value, Array
import time

#define after creating the target
def add_50(number):
    for i in range(50):
        time.sleep(0.01)
        number.value += 1
if __name__ == "__main__":
    shared_number = Value('i',1)
    print("Number at starting point is ", shared_number.value) # 1
    #create process that will modify the number, args are tuples, rem the ","
    process1 = Process(target=add_50,args=(shared_number,))
    process2 = Process(target=add_50, args=(shared_number,))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print("Number at the End is ", shared_number.value) 
    # not same output running 2nd time because of 2 multiprocess running together
    
    
    
# MultiProcessing shared value with more than  one process, using Lock to correct the error(Multiprocess same access)
from multiprocessing import Process, Value, Array, Lock
import time

#define after creating the target
# make sure to acquire and release
def add_50(number, lock):
    for i in range(50):
        time.sleep(0.01)
        lock.acquire() # Means no other process is running until completion
        number.value += 1
        lock.release() # the second process can now run
if __name__ == "__main__":
    #create a Lock Object
    lock = Lock()
    shared_number = Value('i',1)
    print("Number at starting point is ", shared_number.value) # 1
    #create process that will modify the number, args are tuples, rem the ","
    process1 = Process(target=add_50,args=(shared_number,lock))
    process2 = Process(target=add_50, args=(shared_number,lock))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print("Number at the End is ", shared_number.value)
    # not same output running 2nd time because of 2 multiprocess running together
    # to stop this, use Lock to prevent same access
    

# MultiProcessing shared value with more than  one process, using Lock to correct the error(Multiprocess same access)
# use Lock as context managers to automatically start and stop
from multiprocessing import Process, Value, Array, Lock
import time

#define after creating the target
# make sure to acquire and release
# use lock for Context managers
def add_50(number, lock):
    for i in range(50):
        time.sleep(0.01)
        with lock:
            number.value += 1
if __name__ == "__main__":
    #create a Lock Object
    lock = Lock()
    shared_number = Value('i',1)
    print("Number at starting point is ", shared_number.value) # 1
    #create process that will modify the number, args are tuples, rem the ","
    process1 = Process(target=add_50,args=(shared_number,lock))
    process2 = Process(target=add_50, args=(shared_number,lock))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print("Number at the End is ", shared_number.value)
    # not same output running 2nd time because of 2 multiprocess running together
    # to stop this, use Lock to prevent same access
    



# MultiProcessing shared Value With Arrays
# use Lock as context managers to automatically start and stop
from multiprocessing import Process, Value, Array, Lock
import time

# define the numbers to be iterated
def add_50(numbers, lock): 
    for i in range(50):
        time.sleep(0.01)
        # increament each value from range of the numbers array
        for i in range(len(numbers)):
            #access each element and add 1
            with lock:
                numbers[i] += 1
if __name__ == "__main__":
    #create a Lock Object
    lock = Lock()
    shared_array = Array('d',[0.0,50.0 ,100.0])
    #Access the index with either slicing or indexing
    print("Array at starting point is ", shared_array[:]) # 1
    #create process that will modify the number, args are tuples, rem the ","
    process1 = Process(target=add_50,args=(shared_array,lock))
    process2 = Process(target=add_50, args=(shared_array,lock))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print("Array at End point is ", shared_array[:])





# MultiProcessing shared Value With QUEUES for process data exchange (FIFO Algorithim)
# use Lock as context managers to automatically start and stop
from multiprocessing import Process, Value, Array, Lock
from multiprocessing import Queue
import time

#create the aquare function and put it in the queue
def square(numbers, queue):
    for i in numbers:
        queue.put(i*i)
def make_negative(numbers, queue):
    for i in numbers:
        queue.put(-1 * i)
if __name__ == "__main__":
    #create queue
    #define the numbers Range
    numbers = range(1,6)
    q = Queue()
    p1 = Process(target=square, args=(numbers,q))
    p2 = Process(target=make_negative, args=(numbers,q))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    # print out the elements
    while not q.empty():
        print(q.get())





# Process Pool, to manage multiple process and small data management
# Pooling Methods: apply,map, join close.........
from multiprocessing import Pool

#create the aquare function and put it in the queue
def square(number):
    return number * number
if __name__ == "__main__":
    #create pool
    pool = Pool()
    numbers = range(10)

    #using Maps
    results = pool.map(square, numbers)
    pool.close()
    pool.join()
    
    print(results)


# UP NEXT
# DEEP DIVE INTO FUNCTION ARGUMENTS

# difference between arguments and parameters
# parameters are variables defined in functions
# arguements are variables in function

def createFunction(name): # this the parameter
    print(name)
print(createFunction("Nothings")) # this the argument


# Positional and Keyword Argument
def positional(a,b,c):
    print(a,b,c)
print(positional(10,20,30))
# key word argument
def key_word(a,b,c):
    print(a,b,c)
print(key_word(a=10,b=40,c=65)) # order is
# mix
print(key_word(20, b= 50,c=100))
# cannot modify elements
print(key_word(10,a=50,12) # error 
# default arguments *(always placed at the end)
def default_arg(a,b,c,d=10):
    print(a,b,c,d)
print(default_arg(2,4,6))

# default arguments *(always placed at the end)
def default_arg(a,b,c,d=10):
    print(a,b,c,d)
print(default_arg(2,4,6))

# Variable length Arguments
# * one asterik means any number of arguments can go inside
# ** Nay number of keyword arguments
def fool(a,b,*args,**kwargs):
    # since its a tuple we can iterate
    for arg in args:
        print(arg)
    # since **kwargs is a dictionary we can print keys
    for key in kwargs:
        print(key, kwargs[key])
print(fool(2,4,6,8,10,Eleven=11,Twelve=12))



# Unpacking arguments
# unpacking from a list into a function args
def unpackList(a,b,c):
    print(a,b,c)
my_list = [0,1,2]
print(unpackList(*my_list))



# unpacking into a dictionary
# number of parameters must match the list of elements
def unpackDict(a,b,c):
    print(a,b,c)
my_dict = {'a':1, 'b':2, 'c':3}
print(unpackDict(**my_dict))


# Local vs Global variables


def local_global():
    i = Number
    print("The number in the function is : ", i)
Number = 5
print(local_global())

# Local vs Global variables
def local_global():
    i = Number
    i=30 # modify this throws an error becase the value is of the global and not local variable
    print("The number in the function is : ", i)
Number = 5


# To modify use global in the function
def local_global():
    global Number
    i = Number
    Number = 20
    print("The number in the function is : ", i)
Number = 5
print(local_global())
print(local_global())
print(local_global())





# ASTERISK OPERATORS IN PYTHON

# multiplication
mult = 5 * 2
# power operation
power = 2 ** 4
# repeated elements in a list
sixtens = [6] * 10
tupleRepeatition = (1,5) * 10
stringMultiple = "CD" * 10

print(mult)
print(power)
print(tupleRepeatition)
print(stringMultiple)
print(sixtens)


# args and kwargs
def argsKwargs(a,b, *args, **kwargs):
    print(a,b)
    #args is a tuple and is there iterable
    for arg in args:
        print(arg)
    #kwargs is dictionary and therefore iterable
    for key in kwargs:
        print(key, kwargs[key])
print(argsKwargs(2,4,6,8,10,12,ten=10,twenty=20))



# elements after * in a function are all keys, otherwise throws an exception

# wrong approach
def asterisk(a,b,*,c):
    print(a,b,c)
print(asterisk(1,2,3))
#TypeError: asterisk() takes 2 positional arguments but 3 were given



#right approach
def goodAsterisk(a,b,c):
    print(a,b,c)
print(goodAsterisk(10,20,c=30))


# Asterisk unpacking
# Rem number of args must match the number os the parameters
def unpackList(a,b,c):
    print(a,b,c)
my_list = [10,20,30]

# unpacking with asterisk for dictionaries
# rem the keys must match the variable parameter names
def unpackDictionary(a,b,c):
    print(a,b,c)
my_dict = {'a':10, 'b':20,'c':30}
print(unpackDictionary(**my_dict))

#unpacking elements into a list 
#unpacking a tuple will pack it into a list, so be careful
numbers = [10,20,30,40,50,60]
*start, last = numbers
print(start)
print(last)

#unpack first and follwing into a list
numbers = [10,20,30,40,50,60]
start, *last = numbers
print(start)
print(last)

#unpack midle numbers alone
numbers = [10,20,30,40,50,60]
start, *middle, last = numbers
print(start)
print(middle)
print(last)

# merging list and sets with tuple using asterisk
my_list = [2,4,6]
my_tuple = (8,10,12)
my_set = {14,16,18}
new_list_now = [*my_list,*my_tuple,*my_set]
print(new_list_now)


# merging dictionaries with asterisk
my_dict1 = {'a':10,'b':20,'c':30}
my_dict2 = {'d':40,'e':50,'f':60}
new_merge = {**my_dict1, **my_dict2}
print(new_merge)

# CONTEXT MANAGERS
# allow automatic allocation and release of resources

# dealing with files
with open('myFile.txt','w') as file:
    file.write('remane the file....') # this allows automatic close and file open

# sample two
from threading import Lock
lock = Lock()
lock.acquire()
#.....code to do 
lock.release()

with lock:
    #code and release automatically
