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
