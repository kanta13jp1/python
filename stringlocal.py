# -*- coding: utf-8 -*-
hi = "hello there"
name = "ana"
greet = hi + name

#print(greet)
#greeting = hi + " " + name
#print(greeting)
#silly = hi + (" " + name) * 3
#print(silly)

x = 1
print(x)
x_str = str(x)
print("my fav number is", x, ".", "x=", x)
print("my fav number is", x_str + "." + "x=" + x_str)
print("my fav number is" + x_str + "." + "x=" + x_str)

s = "6.00 is 6.0001 and 6.0002"

new_str = ""

new_str = s[-1]
new_str += s[0]
new_str += s[4::30]
new_str += s[13:10:-1]

print(new_str)

s1 = "mit u rock"
s2 = "i rule mit"
if len(s1) == len(s2):
    for char1 in s1:
        for char2 in s2:
            if char1 == char2:
                print("common letter")
                break
                