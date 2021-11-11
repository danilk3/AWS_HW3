# ------------------------------------------------------------------------------
# fiction.py - description fiction functions.
# ------------------------------------------------------------------------------
import random
from random import choice
from string import ascii_letters


# ------------------------------------------------------------------------------
# Filling tree objects with values from file.
def in_from_file(fiction_arr, command):
    str_arr = command.split(' ')
    fiction_arr.append("fiction")
    fiction_arr.append(str_arr[1])
    fiction_arr.append(int(str_arr[2]))
    fiction_arr.append(str_arr[3])
    fiction_arr.append(comparison_param(fiction_arr))


# ------------------------------------------------------------------------------
# Filling tree objects to random values.
def in_rnd(fiction_arr):
    fiction_arr.append("fiction")
    fiction_arr.append(''.join(choice(ascii_letters) for i in range(12)))
    fiction_arr.append(random.randint(1950, 2021))
    fiction_arr.append(''.join(choice(ascii_letters) for i in range(12)))
    fiction_arr.append(comparison_param(fiction_arr))


# ------------------------------------------------------------------------------
# Comparison parameter for shaker sort.
def comparison_param(movie_arr):
    return int(movie_arr[2]) / 12.0;
