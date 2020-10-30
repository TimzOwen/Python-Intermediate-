
# UP NEXT ON STRINGS
# Strings are text representation, they are unodered and immutable rep of texts
#creating a string you can use double r single quotes

# create string
my_string = "CodersTrust Academy"
my_string2 = 'codersTrust'
print(my_string)
print(my_string2)

#escape charters
my_string3 = "we're coderstrust"
my_string4 = 'we\'re codersTrust'
print(my_string3)
print(my_string4)

#multiline string uses triple quotes
my_string5 = """we are 
coders trust 
and we run code worldwide"""
#use backslash to remain on the same line 
my_string6 = """we are \
coders trust  \
and we run code worldwide"""
print(my_string5)
print(my_string6)

#accessing char in a string
my_string7 = "CodersTrust Academy"
print(my_string7[0]) #c
print(my_string7[-1]) # Y

#cannot asign new values because string are immutable
# print(my_string7[0] = 'T') # throws an error. make sure to uncomment and comment  to allow other programs to run

 #slicing
print(my_string7[1:6])
print(my_string7[::2]) #takes every second char
print(my_string7[::-1]) #reverse the string

#contatinating strings (+)
user_name = "Timz"
role = "software developer"
print("Hello " + user_name + " " + " welcome our " + role)


#Iterating over a string
for s in my_string7:
    print(s)

#check if a string is present in a sentence
if "code" in my_string7:
    print("yes")
else:
    print("No")

#removing white spaces
my_string7 = "   Welcome to Software Development    "
print(my_string7)
print(my_string7.strip())

#covert to upper and lower case
print(my_string7.upper())
print(my_string7.lower())
#check if it starts with specific char or words
print(my_string7.startswith("welcome"))

#ends with
my_string7 = "welcome to CTA"
print(my_string7.endswith('A'))

#locating index of a char
print(my_string7.find('o'))

#string count
print(my_string7.count('o'))


#list and string 
my_string = "Hello Code ninja"
print(my_string.split()) #conversts to a list
#rejoin a string

new_string_now = ' '.join(my_string)
print(new_string_now)
my_string8 = ['a'] * 6
print(my_string8)

new_string = ''
for x in my_string8:
    new_string += x
print(my_string8)



#checking time and speed of string joining
from timeit import default_timer as timer

my_list = ['b']*1000000

#wrong approach
start = timer()
my_string = ''
for i in my_list:
    my_string += i
stop = timer()
print(stop-start) #0.57553...

#right approach
start = timer()
my_string = ''.join(my_list)
stop = timer()
print(stop-start) #0.0192...

#formating a string
#using , modulous ,.formart() and f-String

#formating with %
my_name = "Timz Owen"
age = 25
floating_age = 25.456123
intro = ("Our instructor's name is %s" %my_name)
intro_age = (" he is aged %d " %age)
print(intro)
print(intro_age)
print(" He has a floating age of %.2f" %floating_age)

#formating with {}
my_user_id = 25.3698521
position = "Engineer"
my_string = "The user Id for Timz is {:.2f} and he is an {}".format(my_user_id,position)
print(my_string)

#formating with f-string
my_user_id = 25.3698521
position = "Engineer"
my_string = f"The user Id for Timz is {my_user_id} and he is an {position}"
print(my_string)

# UP NEXT

# COLLECTIONS
# containers used to store collection of data example, list, dict, set, tuple

# creating containers
from collections import Counter
char_abc = "aaabbbccc"
my_counter = Counter(char_abc)
print(my_counter)
print(my_counter.values())
print(my_counter.keys())
# most common element
print(my_counter.most_common(1))

# accessing index of an element
print(my_counter.keys(1[0[0]])) # indexing to get the element
print(my_counter.elements())

# Named Tuples
from collections import namedtuple

#creating a namedTuple
Point = namedtuple('Point','x,y')
pt = Point(2,6)
print(pt)
print(pt.x,pt.y) #access elements

# odered Dictionary
# a dictionary with oder of items created
from collections import OrderedDict
odered_dict = OrderedDict()
odered_dict['a']=2
odered_dict['b']=4
odered_dict['d']=8
odered_dict['e']=10
odered_dict['c']=6
print(odered_dict)

#default dictionary
#sets a key if no key has been set yet
from collections import defaultdict
dic = defaultdict(int) #float can also be used d=0.0
dic['a']=2
dic['b']=4
dic['c']=6
print(dic)
print(dic['d']) # assigns a default value of non been assigned
print(dic['b'])

# deque
# this is a double ended queue where elements can be added and removed from both sides
# deque
# this is a double ended queue where elements can be added and removed from both sides
from collections import deque
#creating a deque
deq = deque()
deq.append(10)
deq.append(20)
deq.append(30)
deq.appendleft(60) #adds element to the left
print(deq)

deq.pop() #removes last element
print(deq)

deq.popleft() # removes left most elements
print(deq)

#clear removes all the elements
deq.clear()
print(deq)

# add multiple items same time using a list
deq.extend([70,80,910])
print(deq)
deq.extendleft([12,14,16])
print(deq)
print(deq.rotate(12)) #rotates to the right
print(deq.rotate(-2)) # rotates to the left



# ITERTOOLS
# used to iterate over data structures in for-loop

# 1.0 the Product
from itertools import product
list_1 = [2,4,6,]
list_2 = [8,10,12]
prod = product(list_1, list_2)
print(list(prod)) # combines all the elements in both list
# [(2, 8), (2, 10), (2, 12), (4, 8), (4, 10), (4, 12), (6, 8), (6, 10), (6, 12)]
# can also define the number of repetition
prod=product(list_1, list_2, repeat=2) # repeat prints repeated values
print(list(prod))


# 2.0 permutation
# returns all possible oderings of input elements
from itertools import permutations
numbers = [2,4,6,8]
perm = permutations(numbers)
print(list(perm))

# 3.0 combination
from itertools import combinations
combi = [1,2,3,4,5]
posible_combination = combinations(combi,2)
print(list(posible_combination))


# ITERTOOLS
# used to iterate over data structures in for-loop


# 4.0
# Accumulated Function, returns sum of the elements
from itertools import accumulate
num = [2,4,6,8]
acc = accumulate(num)
print(num)
print(list(acc))

# multiply
from itertools import accumulate
import operator
num1 = [2,4,6,8]
acc = accumulate(num1, func=operator.mul)
print(num1)
print(list(acc))

# return Max
from itertools import accumulate
import operator
num1 = [2,4,10,6,8]
acc = accumulate(num1, func=max)
print(num1)
print(list(acc))


import itertools count, cycle, repeat
# ITERTOOLS
# used to iterate over data structures in for-loop

# 5.0
# GroupBy
# returns keys and values

from itertools import groupby
#define a method to be used
def test_g_s(y):
    return y<6

list_g = [2,4,6,8]

g_elements  = groupby(list_g,key=test_g_s)
#iterate through the elements
for key,value in g_elements:
    print(key,list(value))


# using lambda
def test_g_s(y):
    return y<6

list_g = [2,4,6,8]

g_elements  = groupby(list_g,key=lambda x: x<6)
#iterate through the elements
for key,value in g_elements:
    print(key,list(value))




# using lambda

from itertools import groupby
#define a method to be used
def test_g_s(y):
    return y<6

list_g = [2,4,6,8]

g_elements  = groupby(list_g,key=test_g_s)
#iterate through the elements
for key,value in g_elements:
    print(key,list(value))


# example
persons = [{'name':'Tim', 'age':25},{'name':'Timz', 'age':35},{'name':'Timo', 'age':25},
          {'name':'Timothy', 'age':28}]

g_elements  = groupby(persons, key=lambda x:x['age'])
#iterate through the elements
for key,value in g_elements:
    print(key, list(value))
    
    
# 6.0 infinite iterators


#count
# counts by adding 1 at each step interger
for i in count(15):
    print(i)
    if i ==100:
        break
    
#cycle , loops infinately through a list
num_list = [2,4,6]
for x in cycle(num_list):
    print(x)
    

# repeat, prints  over repeating times in a value
num_list = [2,4,6]
for x in repeat(2,10):
    print(x)
    
# LAMBDA
# the shortened function
multiplication = lambda i: i*12
print(multiplication(12))

# same as
def mult(x):
    return x * 12
print(mult(12))

# more than one arguement
addition = lambda x,y,z: x+y+z
print(addition(2,4,6))

#sorting with lambda
# random_2D = [(2,4),(-2,8),(12,11)(9,-8)]
# sorted_random = sorted(random_2D)
# print(list(sorted_random))
# print(random_2D)

#sort with lambda key
# random_2D = [(2,4),(-2,8),(12,11)(9,-8)]
# sorted_random = sorted(random_2D, key=lambda :x[1])
# print(list(sorted_random))
# print(random_2D)

# map Function
# used for transformation (fun-argu, sequence )
list_a = [2,4,6,8]
list_b_multiplied = map(lambda z: z*2, list_a)
print(list(list_b_multiplied))

#or use list comprehension
double_num = [x*2 for x in list_a]
print(double_num)

# Filter Function
# cal even numbers using the filter function
list_even = [1,2,3,4,5,6,7,8,9,10]
filter_even = filter(lambda x: x%2==0,list_even)
print(list(filter_even))

# using list comprehension to calculate even
list_even_2 = [i for i in list_even if i%2==0]
print(list(list_even_2))

#Reduce Function
# calculates sum of a given condition
from functools import reduce
list_a = [2,4,6]
product_sum = reduce(lambda x,y: x*y, list_a)
print(product_sum)

 
    

