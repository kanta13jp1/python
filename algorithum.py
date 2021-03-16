# -*- coding: utf-8 -*-
s = "abcdefgh"
print(s)

print(s[3:6])
print(s[3:6:2])
print(s[::])
print(s[::-1])
print(s[4:1:-2])

#s[0] = 'y'
s = 'y' + s[1:len(s)]
print(s)

for var in range(4):
    print(var)
    
for var in range(4,6):
    print(var)
    
for index in range(len(s)):
    if s[index] == 'y' or s[index] == 'u':
        print("There is an y or u")

for char in s:
    if char == 'i' or char == 'f':
        print("There is an i or f")
        
an_letters = "aefhilmnorsxAEFHILMNORSX"
word = input("I will cheer for you! Enter a word: ")
times = int(input("Enthusiasm level (1-10): "))

i = 0
#while i < len(word):
#    char = word[i]
for char in word:
    if char in an_letters:
        print("Give me an " + char + "! " + char)
    else:
        print("Give me a  " + char + "! " + char)
#    i += 1
print("What does that spell?")
for i in range(times):
    print(word, "!!!")
