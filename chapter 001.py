# Lists
#are mutable ,ordered and allows duplicate elements
myNewList = ["Hp",2.5,"Kenya made"]
print(myNewList)

#create empty list
emptyList = []
print(emptyList)

#duplicate elements
duplicateList = ["owen","timz","owen"]
print(duplicateList)

#iterate through elements i a list
for i in duplicateList:
    print(i)

#Accessing elements and out of range incase of larger index
print(duplicateList[-2])
print(myNewList[0])

#check if element in an list (always case sensitive)
if "Hp" in myNewList:
    print("yes")
else:
    print("No")
    
#check number of elements in a list
print(len(myNewList))


#append items on a list
myNewList.append("Toshiba")
print(myNewList)

#insert at specific index
myNewList.insert(1,"Lenovo")
print(myNewList)

#remove items using (pop)
item_removed = myNewList.pop()
print(item_removed)
print(myNewList)

#Remove a particular item
myNewList.remove("Hp")
print(myNewList)

#remove all elements (clear)
myNewList.clear()
print(myNewList)

#Reverse list
myNewList = ["Hp", "Macbook","Lenovo","samsung"]
myNewList.reverse()
print(myNewList)

#Sort List method
myNewList.sort()
print(myNewList)

#new list with same items
same_list = [5] * 5
print(same_list)

#List contatination
list_1 = ["Hp", "Toshiba","Mac","carbon","Intel"]
list_2 = [2.5, 3.5,10.6,12.5,15.5]
new_list = list_1 + list_2 
print(new_list)

#list slicing, if no start specified it starts from begining, same for the end
list_one = [1,2,3,4,5,6,7,8,9,10,11,12,13]
list_slice = list_one[2:]
print(list_slice)
#step index
print(list_slice[::3])

#copying a list
#appending an item to the copy also modifies the copy and original list
# to avoid modifiying the original list use (.copy method)
original_list = ["owen",23,"Kabarak university"]
copy_owen = original_list
copy_owen.append("Chebara")
print(copy_owen)
print(original_list)

#List comprehension
original_elements = [2,4,6,8,10]
square_elements = [i*i for i in original_elements]
print(original_elements)
print(square_elements)


#UPNEXT_TUPPLES


# UP NEXT TUPLES
#odered an immutable data type collection
# cannot be changed after its creation

#creating a tuple, parenthesis are optional
#even with one element, you have to place a comma otherwise it is taken as a string
myTuple = ("Timz","CodersTrust",2020)
print(myTuple)

string_nT = ("Apple")
print(type(string_nT)) #gives a string

string_t = ("Apple",)
print(type(string_t)) #gives a tuple

#creating a tuple from a list
list_tuple = tuple(["Timz","Lenovo",2.5])
print(type(list_tuple))
print(list_tuple)

#accessing members of a tuple
# Negative -1 starts from the back
item = list_tuple[0]
print(item) #Timz

#change elements
#they are immutable and you get an error message
# list_tuple[0] = "James"
# # object does not support assignment

#iterate through a tuple
for x in list_tuple:
    print(x)
    
#check if an element is present in a file
if "timz" in list_tuple:
    print("yes")
else:
    print("No")
    
#more methods with tuple
#len
my_tuple = ("M","a","c","b","o","o","k")
print(len(my_tuple))
#count elements
print(my_tuple.count("o"))
#find first index
print(my_tuple.index("o"))
#convert to list
my_list_tuple = list(myTuple)
print(type(my_list_tuple))
print(my_list_tuple)
#convert back to tuple
new_tuple = tuple(my_list_tuple)
print(type(new_tuple))
print(new_tuple)

#slicing tuples

#slicing tuples
#if no start ,starts from 0 and end
num_tuple = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)
slice_tuple = num_tuple[1:5]
print(slice_tuple)
#interval specific
new_slice = num_tuple[::-1]
print(new_slice)
#reverse a tuple
print(new_slice)

#unpacking a tuple
coders_Trust = ("Bangladesh",2017,"Mads")
company, year,ceo = coders_Trust
print(company)
print(year)
print(ceo)

#unpacking in intervals
num_unpack = (0,1,2,3,4,5,6,7,8,9,10)
num1, *num, num2 = num_unpack
print(num1) #first number
print(num2) #last number
print(num) #other  numbers now converted into a list

#comparison between list and tuples on system files
import sys
list_size = [0,1,2,3,4,5,6,7,8,9,10]
tuple_size = (0,1,2,3,4,5,6,7,8,9,10)
print(sys.getsizeof(list_size),bytes) #bigger
print(sys.getsizeof(tuple_size), bytes)  #smaller

#time taken to create list and tuple comparison
import timeit
print(timeit.timeit(stmt="[0,1,2,3,4,5,6,7,8,9,10]",number=1000000)) #longer time to create
print(timeit.timeit(stmt="(0,1,2,3,4,5,6,7,8,9,10)",number=1000000)) #shorter time to create

#Dictionaries
#Dictionaries
#Key-paired Values ,are mutable and are unordered

#create a dictionary
dict_ = {"city":"Bangladesh", "year":2017,"CEO":"Mads"}
print(dict_)

#using the dictionary function
my_new_dict = dict(city="India",started=2018, CEO="Mads")
print(dict_)

#accesing values
ceo_name = my_new_dict["CEO"]
print(ceo_name)

#add values to our dictionary
my_new_dict["seniority"] = "senior Engineer"
print(my_new_dict)

#delete elements of a dictionary
del my_new_dict["city"]
print(my_new_dict)
my_new_dict.pop("started")
print(my_new_dict)
my_new_dict.popitem() #removes last element
print(my_new_dict)\

#check is element exists ib a dictionary
dict_ = {"city":"Bangladesh", "year":2017,"CEO":"Mads"}
if "city" in dict_:
    print(dict_["city"])
else:
    print("no such Key")

#check with try catch block
try:
    print(dict_["year"])
except:
    print("ERROR !!! No Key")

#loop through a dictionary using for loop
for key in dict_:
    print(key)
for key in dict_.keys():
    print(key)

for values in dict_.values():
    print(values)

for key,values in dict_.items():
    print(key,values)

#copying dict also a change in the copy modifies the parent copy
copy_dict = dict_
print(copy_dict)



my_dict = dict(Name="Timz owen",position="Software Engineer",Experience=5,company="Coderstrust")
print(my_dict)

copy_dict = my_dict
print(copy_dict)

copy_dict["Experience"] = 8

print(copy_dict)
print(my_dict)

#copy with the coy function
dist_copy = my_dict.copy()
print(dist_copy)


#copy with dict
copy_copy_dict  = dict(dist_copy)
print(copy_copy_dict)
copy_copy_dict["Name"] = "Timz"
print(copy_copy_dict)
print(dist_copy)

#merging  or more dictionaries
dict_1 = {"Name":"Timothy","Age":24,"Country":"Europe"}
dict_2 = dict(Name="Owen",Role="Instructor",Number=254740354167)
print(dict_1)
print(dict_2)
dict_1.update(dict_2)
print(dict_1) #{'Name': 'Owen', 'Age': 24, 'Country': 'Europe', 'Role': 'Instructor', 'Number': 254740354167}

#accessing integer values in dictionary
int_dict = {2:4,5:25,9:81}
print(int_dict)
# print(int_dict[0]) #brings a key error, instead use the key number            #### UNCOMMENT TO RUN AND COMMENT OUT AGAIN
print(int_dict[2])

#using tuples as key values in dictionaries
my_tuple_dict = (12,18)
ditc_tuple = {my_tuple_dict: 30}
print(ditc_tuple)
