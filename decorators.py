# decorator pattern
from time import time


def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('*********')
        func(*args, **kwargs)
        print('*********')
    return wrap_func


@my_decorator
def hello(greeting, emoji):
    print(greeting, emoji)


@my_decorator
def bye():
    print('see ya later')


hello('hiiiii', ':)')
bye()

hello2 = my_decorator(hello)
hello2('heyyyy', ':(')


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'Took {t2 - t1} s')
        return result
    return wrapper


@performance
def long_time():
    for i in range(1000000):
        i*5


long_time()
