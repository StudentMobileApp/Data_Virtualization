# as descibed at: 
# https://docs.microsoft.com/en-us/visualstudio/python/working-with-c-cpp-python-in-visual-studio?view=vs-2017

from itertools import islice
from random import random
from time import perf_counter

COUNT = 500000  # Change this value depending on the speed of your computer
DATA = list(islice(iter(lambda: (random() - 0.5) * 3.0, None), COUNT))

e = 2.7182818284590452353602874713527


def sinh(x):
    return (1 - (e ** (-2 * x))) / (2 * (e ** -x))


def cosh(x):
    return (1 + (e ** (-2 * x))) / (2 * (e ** -x))


def tanh(x):
    tanh_x = sinh(x) / cosh(x)
    return tanh_x


def test(fn, name):

    start = perf_counter()
    result = fn(DATA)
    duration = perf_counter() - start
    print('{} took {:.3f} seconds\n\n'.format(name, duration))

    for d in result:
        assert -1 <= d <= 1, " incorrect values"


if __name__ == "__main__":
    print('Running benchmarks with COUNT = {}'.format(COUNT))

    test(lambda d: [tanh(x) for x in d], '[tanh(x) for x in d] (Python implementation)')
    
    # I can't get the IDE to find the C++ module
    # Is it because solution was started in Python?
    from superfastcode import fast_tanh
    test(lambda d: [fast_tanh(x) for x in d], '[fast_tanh(x) for x in d] (CPython C++ extension)')