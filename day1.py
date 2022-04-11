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

# rindex(sub[, start[, end]]) : Just like rfind() but raises 
#ValueError when the substring sub is not found

a = "Hi World"
print(a.rindex("d"))
print(a.rindex("W"))

a = "abcabc"
print(a.index("a"))
print(a.rindex("a"))

def max_no(x,y):
    return x if x>y else y
f_no= 12
s_no =25
print(f'Max of {f_no} and {s_no} is {max(f_no,s_no)}')

from decimal import Decimal
width = 4
round_point = 2
value = Decimal('12.39065')
print(f'result:{value:{width}.{round_point}}')

#Arithmatic Operators
x=20
y=4

#Addition
print("Addition:",x+y)

#Subtraction
print("Subtraction:",x-y)

#Multiply
print("Multiply: ",x*y)

#Division
print("Division:",x/y)

#Modulus
print("Modulus:",x%y)

#Floor Division
print("Floor Division:",x//y)

#Exponent
print("Exponent:",x**y)

#Comparison Operator  : Result is either True or False
x=5
y=3

#Greater than
print("Greater than:",x>y)

#Less than
print("Greater than:",x<y)

#Greater than equal to 
print("Greater than equal to:",x>=y)

#less than equal to
print("Less than:",x<=y)

#Not equal to 
print("Not equal to:",x!=y)

#Equal to
print("Equal to:",x==y)

#Logical Operators : and, or, not [Result is either True or False]

x= True
y= False

#And
print("And result:",(x and y))

#Or
print("Or result:",(x or y))

#Not
print("Not result:",(not y))