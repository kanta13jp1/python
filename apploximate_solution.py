# -*- coding: utf-8 -*-
cube = 27
#cube = 8120601
#cube = 10000
epsilon = 0.01
increment = 0.01
num_guesses = 0
low = 0
high = cube
guess = (high + low)/2.0
while abs(guess**3 - cube) >= epsilon:# and guess <= cube:
    if guess**3 < cube :
        low = guess
    else:
        high = guess
    guess = (high + low) / 2.0        
    num_guesses += 1
print('num_guesses =', num_guesses)
print(guess, 'is close to the cube root of', cube)
#if abs(guess**3 - cube) >= epsilon:
#    print('Failed on cube root of', cube, 'with these parameters')
#else:
#    print(guess, 'is close to the cube root of', cube)
