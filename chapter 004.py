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
