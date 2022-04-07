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

# endswith(suffix[, start[, end]]) : Returns True if the string ends 
#with the specified suffix, otherwise it returns False

a = "Watermelon"
print(a.endswith("s"))
print(a.endswith("melon"))

# find(sub[, start[, end]]) : Returns the lowest index in the string 
# where substring sub is found within the slice s[start:end]

a = "Exercise"
print(a.find("r"))
print(a.find("e"))

# index(sub[, start[, end]]) : Similar to find function, except that 
# it raises a ValueError when the substring is not found

a = "Continent"
print(a.index("i"))
print(a.index("C"))
print(a.index("nent"))

# isalnum() : Returns True if all characters in the string are 
#alphanumeric, else returns False

c = "456"
d = "$*%!!**"
print(c.isalnum())
print(d.isalnum())

# isalpha() : Returns True if all characters in the string are 
#alphabetic, else returns False

c = "456"
d = "Python"
print(c.isalpha())
print(d.isalpha())

# isdecimal() : Returns True if all characters in the string are 
#decimal characters, else returns False

c = u"\u00B10"
x = "10"
print(c.isdecimal())
print(x.isdecimal())

# isdigit() : Returns True if all characters in the string are 
#digits, else returns False

c = "4567"
d = "1.65"
print(c.isdigit())
print(d.isdigit())

# join(iterable) : Returns a string which is the concatenation of 
#the strings in iterable. 
# A TypeError will be raised if there are any non-string values in 
#iterable

a = ","
print(a.join("CD"))

# partition(sep) : Splits the string at the first occurrence of sep, 
#and returns a 3-tuple containing the part before the separator, the 
#separator itself, and the part after the separator

a = "Complete.Python-course"
print(a.partition("-"))
print(a.partition("."))

# split(sep=None, maxsplit=-1) : Returns a list of the words in the 
#string,using sep as the delimiter strip.If maxsplit is given,at 
#most maxsplit splits are done.If maxsplit is not specified or -1, 
#then there is no limit on the number of splits.

a = "Welcome,,Friends,,,,,,,,,,,,"
print(a.split(",",0))
print(a.split(",",1))
print(a.split(",",2))
print(a.split(",",3))
print(a.split(","))

# strip([chars]) : Returns a copy of the string with leading and 
#trailing characters removed. The chars argument is a string 
#specifying the set of characters to be removed

a = "***Python***"
print(a.strip("*"))

# swapcase() : Returns a copy of the string with uppercase 
#characters converted to lowercase and vice versa

a = "Hi Homies"
print(a.swapcase())

# zfill(width) : Returns a copy of the string left filled with ASCII 
#0 digits to make a string of length width

a = "-124"
print(a.zfill(6))

# lstrip([chars]) : Return a copy of the string with leading 
#characters removed.The chars argument is a string specifying the 
#set of characters to be removed.

a = "*****Python-----"
print(a.lstrip("*"))