
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
