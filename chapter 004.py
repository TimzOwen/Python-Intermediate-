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



# Class Decorators
# Helps in keeping track of decorators after they have been executed

class CountCalls:
    def __init__(self, func):
        self.func = func
        self.number_of_times_called = 0
    def __call__(self, *args, **kwargs):
        self.number_of_times_called += 1
        print(f'Executed {self.number_of_times_called} times')
        return self.func(*args, **kwargs)

@CountCalls
def morning_greeting():
    print('Good Morning Google')
morning_greeting()
morning_greeting()
morning_greeting()




   


# UP NEXT ON GENERATORS


# Used to create iterators
# functions that return iterable items/elements one at a time
# uses yield instead of generators

def myCountGenerators():
    yield 10
    yield 20
    yield 30
    yield 40
my_g = myCountGenerators()
print(my_g) # <generator object myCountGenerators at 0x000001F3C66FBAC0>
#loop through to check the items
# for x in my_g:
#     print(x)

# get the items one by one
value_n = next(my_g)
print(value_n)

# calculate sum of yield
print(sum(my_g))

#print sorted gen
def myIntGenerators():
    yield 70
    yield 20
    yield 15
    yield 40
my_s_g = myIntGenerators()
print(sorted(my_s_g)) # sorts the elements


# count down while loops
def countingDown(startingNo):
    print('starting at {}', startingNo)
    while startingNo > 0:
        yield startingNo
        startingNo-=1
countDown = countingDown(5)
print(next(countDown))
print(next(countDown))
print(next(countDown))
print(next(countDown))
print(next(countDown))
# print(next(countDown))  # printing this throws a stop iteration ERROR

# working with large data
import sys

def appendingN(num):
    my_list = []
    start_n = 0
    while start_n<num:
        my_list.append(num)
        num +=1
    return my_list
print(appendingN(15))
print(sum(appendingN(10)))


# using generators instead of List to save on space
def appendWithGenerators(n):
    num = 0
    while num<n:
        yield num
        num +=1
print(sum(firstn(10)))
print(sum(appendingWithGenerators(10))

#check size
print(sys.getsizeof(appendingN((10)))
print(sys.getsizeof(appendWithGenerators(10)))



# GENERATORS SAMPLE 2
# using fobonacii series

def fibonacci(max_limit):
    # 0,1
    a,b = 0,1
    while a < max_limit:
        yield a
        a,b = b, a + b
fib  = fibonacci(30)
for i in fibonacci:
    print(i)



# Generator Expression:
# even numbers with for loop 
# simlified loopig of the commands in the for loop and saves on the spaces 
# almost similar to the list comprehension
myGenerator = (i for i in range(20) if i % 2 ==0)
for x in myGenerator:
    print(x)
   
# you can convert it to a list using the list
print(list(myGenerator))   
   
# list comprehension

myListComprehension = [x for x in range(10) if i % 3 == 0]
for i in myListComprehension:
    print(i)


# calculate the siz of a the list for the comparison





# THREADING VS MULTUPROCESSING
# running your code and making it fast

import sys

myListComprehension = [x for x in range(10) if i % 3 == 0]
for i in myListComprehension:
    print(sys.getsizeof(myListComprehension))

myGenerator = (i for i in range(20) if i % 2 ==0)
for x in myGenerator:
    print(sys.getsizeof(myCountGenerators))



# using generators instead of List to save on space
def appendingN(num):
    my_list = []
    start_n = 0
    while start_n<num:
        my_list.append(num)
        num +=1
    return my_list

def appendingWithGenerators(n):
    num = 0
    while num < n:
        yield num
        num += 1
print(sum(appendingWithGenerators(5)))
print(sum(appendingN(5)))





Threading vs Multithreading
allows you to run your code in paralel and speed up your code


Process
This are instances in Programs for code interpreters(Java & Python Interpreters)
The Process can be stopped/ Killed (They are interruptible)
Processes are indpendent and can run without depending on other processes to stop
No memory sharing
Works well with CPU
Takes advantage of multiple CPU and cores
Trys to eliminate GIL Limitation



starting a process is slower
needs more memory
Heavyweight slowing the machine
has a more complicated (Inter-Process Comunicaiton IPC)





THREADS
This are entity within a process that can be scheduled (Leightweight process)
Process can sound multuple threads

share the same memory in same process
Leightweight
More faster in starting a thread than processes
Great for I/o Bounds

Limted by GIL
No Effect for CPU Bound tasks
Not Interruptible
careful with Race Conditions




GIL
Global interperter lock
A lock that allows strictly one thread to execute at a time
needed in C python because of memory is not thread safe
Avoid:

    Use Multprocessing
    Use different, fresh-threaded python implementation (Jthon, IronPython)
    use python as a wrapper for third party library (C/C++)--> numpy/scipy



# MULTIPROCESSING

#STEP 1
# IMPORT
from multiprocessing import Process
import os
import time
#step 5
def square_numbers():
    for i in range(200):
        i * i
        time.sleep(0.1) # TO give room for readable data

#create a list
processes  = []
#define number fo processes(use cpu)
num_process = os.cpu_count()
#create the processes
for i in range(num_process):
    p = Process(target=square_numbers)# Step 4, create a function to be used as target for the args
    processes.append(p)

# Step 5, start the process
for p in processes:
    p.start()

# step 6, join the processes (blocks other processes until they are done)
for p in processes:
    p.join()

print("Processes Ended")





# MultiThreading

from threading import Thread
import os
import time

def squared_number():
    for i in range(100):
        i * i
        time.sleep(0.1)
threads = []
num_threads = 20
#create threads
for i in range (num_threads):
    t = Thread(target=squared_numbers)
    threads.append(t)
#start threads
for t in threads:
    t.start()
# join them
for t in threads:
    t.join()
print(" All the Threads done running")






# THREADING

from threading import Thread
import time
# set db value
db_value  = 0

def increase():
    global db_value

    local_copy = db_value
    time.sleep(0.1)
    #processing
    local_copy += 1

    db_value = local_copy

if __name__ == "__main__":
    print("Starting db Value is : ",db_value)

    #create a thread
    threadOne = Thread(target=increase)
    threadTwo = Thread(target=increase)

    threadOne.start()
    threadTwo.start()

    threadOne.join()
    threadTwo.join()

    print('End value', db_value)
    print('End main')



# soln
from threading import Thread, Lock
import time
# set db value
db_value  = 0

def increase(lock):
    global db_value

    lock.acquire()
    local_copy = db_value
    time.sleep(0.1)
    #processing
    local_copy += 1
    db_value = local_copy
    lock.release()
if __name__ == "__main__":
    lock = Lock()
    print("Starting db Value is : ",db_value)

    #create a thread
    threadOne = Thread(target=increase, args=(lock,))
    threadTwo = Thread(target=increase, args=(lock,))

    threadOne.start()
    threadTwo.start()

    threadOne.join()
    threadTwo.join()

    print('End value', db_value)
    print('End main')

    # you can use log as context managers to avoid forgetting to release
    with lock:
        local_copy = db_value
        time.sleep(0.1)
        local_copy += 1
        db_value = local_copy



# Using QUEUES in Python threads in threads

from threading import Thread, Lock
from queue import Queue
import time

if __name__ == "__main__":
    # create a queue
    q = Queue()
    # Add some elements
    q.put(1)
    q.put(2)
    q.put(3)
    #Fetch the elements
    first_element = q.get()
    print(first_element)
    #check if a queue is empty
    print(q.empty()) # Returns False
    #make sure to end by calling task done
    q.task_done()
    q.join() # blocks all the queue until all the processing is done
    print("End")


# Example of application code

from queue import Queue
from threading import Thread, Lock, current_thread
import time

def worker(que):
    while True:
        value=que.get()

        # Start Processing
        print(f'in {current_thread().name} got {value}')
        que.task_done()
if __name__ == "__main__":
    que = Queue()

    num_threads = 10
    for i in  range(num_threads):
        thread = Thread(target=worker, args=(que,))
        thread.daemon = True
        thread.start()
    for i in range(1,21):
        que.put(i)
    que.join()
    print("End Process, Finished")

    
    
    
 
