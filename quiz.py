# Python Pop Quiz
from re import X
import numpy as np

language = "Python"
class Snake:
    language += " boa"

print(Snake.language)

# 🔴 Note for primitive types like String __add__ and __iadd__ (inplace add) are same.
# 🔴 Stringのようなプリミティブ型では __add__ と __iadd__ (inplace add) は同じであることに注意。
# language += " boa" is same as language = language + " boa"
# 言語 += " ボア" は、言語 = 言語 + " ボア" と同じです。
# both operation lead to creation of new language object as Strings are immutable
# 文字列は不変なので、両方の操作で新しい言語オブジェクトが作成されます。
# -------------------------------------------------------------------------------------

# 👇 Global var language
# 👇 グローバル変数言語
language = "Python"
print(f'Id of  global var language outside class: {id(language)}')

class Snake:

    print(f'Id of  global var language inside class: {id(language)}')

                                           # 👇 this language is a global var
    # 👇 can also be written as language = language + " boa"
    language += " boa"
    # 👆 is a new class variable language

    print(f'Id of  new class variable language is: {id(language)}')

print(f'Class variable language becomes: {Snake.language}')

print(f'Global var language is still: {language}')

# -------------------------------------------------------------------------------------
# 🔵 Let's quickly see another example to make our understanding concrere 👊 👊 
# この理解を具体化するために、別の例を見てみましょう。
language =["Python"]

class Snake:
    # list allow __iadd__ (inplace add)
    # 👇 here we modify the global var and same becomes class var
    language += [" boa"]

print(Snake.language)
print(language)
print(id(language), id(Snake.language))


def my_function():
    Ellipsis

print(my_function())

def foo(x = ...):
    return x

print(foo())

A = np.random.rand(2, 2, 2)

print(A)

print(A[:, :, 0])

print(A[..., 0])

print(A[Ellipsis, 0])

# quiz

def test():
    x = 7, 8, 9

    return sorted(x) == x

print(test())

x = 7, 8, 9

print(x)
print(type(x))

print(sorted(x))
print(type(sorted(x)))

x = [7, 8, 9]
print(sorted(x) == x)

x = 7, 9, 8
print(x)
print(sorted(x))

x = [7, 9, 8]
print(sorted(x) == x)
