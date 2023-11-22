import cProfile
import pstats
import functools
from functools import wraps
import cProfile
import pstats
import functools


def profile_deco(func):
    profiler = cProfile.Profile()
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        profiler.enable()
        result = func(*args, **kwargs)
        profiler.disable()
        global stats
        stats = pstats.Stats(profiler)
        stats.strip_dirs()
        stats.sort_stats('cumulative')
        return result

    def print_stat():
        stats.print_stats()

    wrapper.print_stat = print_stat
    return wrapper

@profile_deco
def add(a, b):
    return a + b

@profile_deco
def sub(a, b):
    return a - b

add(1, 2)
add(4, 5)
sub(4, 5)

add.print_stat()

for x in range(1000):
    add(x, 2)
    for y in range(1000):
        sub(x, y)


add.print_stat()
sub.print_stat()