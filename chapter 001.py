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
