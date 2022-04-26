#Create a List

list_one = ["sunday","monday","tuesday","wednesday","thursday"]
print(list_one)
print(type(list_one))

#List Length

print(len(list_one))

# List with different data types

list_two = ['abc',67,True,3.14,"female"]
print(list_two)

#type() with List
print(type(list_two))

#list() constructor to make a List

list_cons = list(("hello","World","Beautiful","Day"))
print(list_cons)

# nested list

list_nest= ["hello",[8,4,6],['World']]
print(list_nest)

#slice lists in Python : Use the slicing operator :(colon)

list_one = ["sunday","monday","tuesday","wednesday","thursday"]
print(list_one[1:4])

#Add/Change List Elements : use the assignment operator = to change 
#an item

list_one = ["sunday","monday","tuesday","wednesday","thursday"]
list_one[3] = 'friday'
print(list_one)

# Appending and Extending lists in Python : Use the append() or 
#extend() method

list_one = ["sunday","monday","tuesday","wednesday","thursday"]
list_one.append('friday')
print(list_one)

#extend

list_one.extend(['saturday'])
print(list_one)