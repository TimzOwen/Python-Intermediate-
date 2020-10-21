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

