# ------------------------------------------------------------------------------
# documentary.py - description shrub functions.
# ------------------------------------------------------------------------------
import random
from random import choice
from string import ascii_letters


# ------------------------------------------------------------------------------
# Filling shrub objects with values from file.
def in_from_file(documentary_arr, command):
    str_arr = command.split(' ')
    documentary_arr.append("documentary")
    documentary_arr.append(str_arr[1])
    documentary_arr.append(int(str_arr[2]))
    documentary_arr.append(int(str_arr[3]))
    documentary_arr.append(comparison_param(documentary_arr))


# ------------------------------------------------------------------------------
# Filling shrub objects to random values.
def in_rnd(documentary_arr):
    documentary_arr.append("documentary")
    documentary_arr.append(''.join(choice(ascii_letters) for i in range(12)))
    documentary_arr.append(random.randint(1950, 2021))
    documentary_arr.append(random.randint(1, 240))
    documentary_arr.append(comparison_param(documentary_arr))


# ------------------------------------------------------------------------------
# Comparison parameter for shaker sort.
def comparison_param(movie_arr):
    return int(movie_arr[2]) / 12.0;
