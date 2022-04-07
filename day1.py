#Int data Type

var = 5
print(var)
print(type(var))

#Float data type

var2 = 0.1234
print(var2)
print(type(var2))

#Complex numbers data type

x = 2j
print(x)
print(type(x))

#String Data Type

str_one = "Hello World"
print(str_one)
print(type(str_one))

#list Data type

list1 = ["car","bike"]
print(list1)
print(type(list1))

#Tuple Data Type

tup = ("car","bike","bus")
print(tup)
print(type(tup))

#Dictionary Data type

dict_one = {"Name": "Steve", "Location": "NewYork"}
print(dict_one)
print(type(dict_one))

#Set Data type

set_one = set({"Hello","world","Hello"})
print(set_one)
print(type(set_one))

#Frozen Set

f_one = frozenset({"Hello","World","Hello"})
print(f_one)
print(type(f_one))

#Boolean Data Type

b = True
print(b)
print(type(b))

#Byte Data Type

byte_one = b"World"
print(type(byte_one))
print(byte_one)

#String
str1 = "Welcome to complete Python Course"
str2 = 'Welcome to the complete Python Course'
str3 = """This is a
       multiline 
       String"""
print(str1)
print(str2)
print(str3)

# Indexing : String starts with 0th Index

s= "Captain America"
print(s[4])

#Slicing : slice(start, stop, step), it returns a sliced object containing elements in the given range

s= "Captain America"
print(s[1:5:2])

#Reverse

print(s[::-1])

#capitalize() method : Returns a copy of the string with its first 
#character capitalized and the rest lowercased

a = "complete python course" 
print(a.capitalize())

#centre(width[, fillchar])   : Returns the string centered in a 
#string of length width

a = "Python" 
b = a.center(10, "*")
print(b)

# casefold() method : Returns a casefolded copy of the string. 
#Casefolded strings may be used for caseless matching

a = "PYTHON"
print(a.casefold())

# count(sub[, start[, end]]) : Returns the number of non-overlapping 
#occurrences of substring (sub) in the range [start, end]

a = "Welcome to complete Python Course"
print(a.count("c"))
print(a.count("o"))
print(a.count("Python"))