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

# Concatenating and repeat lists : use + operator to concate two 
#lists and use * operator to repeat lists

list_one = ["sunday","monday","tuesday","wednesday","thursday"]
print(list_one + [0,1,2,3,4])

#repeat operation 
print(['a','b']*2)

# Delete/Remove List Elements : delete one or more items or entire list using the keyword del

del list_one[2]
print(list_one)

#remove method : remove the given item or pop() method to remove an item at the given index location

list_one = ["sunday","monday","tuesday","wednesday","thursday"]
list_one.remove("tuesday")
print(list_one)

#pop method

list_one = ["sunday","monday","tuesday","wednesday","thursday"]
list_one.pop(2)
print("Pop result:", list_one)

# index() method : Returns the index of the first matched item

list_one = ["sunday","monday","tuesday","wednesday","thursday"]
print(list_one.index("tuesday"))

# sort() method: Sort items in a list in ascending order

list_one = ["sunday","monday","tuesday","wednesday","thursday"]
list_one.sort()
print(list_one)

# reverse() : Reverse the order of items in the list

list_one = ["sunday","monday","tuesday","wednesday","thursday"]
list_one.reverse()
print(list_one)

# copy(): Returns a shallow copy of the list

list_one = ["sunday","monday","tuesday","wednesday","thursday"]
list_two = list_one.copy()
print(list_two)

#Membership : check if an item exists in a list or not, using the keyword in

list_one = ["sunday","monday","tuesday","wednesday","thursday"]
print('tuesday' in list_one)

# insert() method : insert item at a desired location

list_one = ["sunday","monday","tuesday","wednesday","thursday"]
list_one.insert(2,'friday')
print(list_one)

sqr = [2**x for x in range(20)]
print(sqr)


