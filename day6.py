#Decorators

def test_decorator(func):
    def function_wrapper(x):
        print("Before calling" + func.__name__)
        res = func(x)
        print(res)
        print("After calling" + func.__name__)
    return function_wrapper@test_decorator
def sqr(n):
    return n**2
