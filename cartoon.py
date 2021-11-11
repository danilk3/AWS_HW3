# ------------------------------------------------------------------------------
# cartoon.py - description flower functions.
# ------------------------------------------------------------------------------
import random
from random import choice
from string import ascii_letters


# ------------------------------------------------------------------------------
# Filling flower objects with values from file.
def in_from_file(cartoon_arr, command):
    str_arr = command.split(' ')
    cartoon_arr.append("cartoon")
    cartoon_arr.append(str_arr[1])
    cartoon_arr.append(int(str_arr[2]))
    way_to_create = int(str_arr[3]) % 3
    if way_to_create == 0:
        cartoon_arr.append("DRAWED")
    elif way_to_create == 1:
        cartoon_arr.append("PUPPET")
    elif way_to_create == 2:
        cartoon_arr.append("PLASTIC")
    cartoon_arr.append(comparison_param(cartoon_arr))


# ------------------------------------------------------------------------------
# Filling flower objects to random values.
def in_rnd(cartoon_arr):
    cartoon_arr.append("cartoon")
    cartoon_arr.append(''.join(choice(ascii_letters) for i in range(12)))
    cartoon_arr.append(random.randint(1950, 2021))
    type_of_movie = random.randint(0, 3) % 3
    if type_of_movie == 0:
        cartoon_arr.append("DRAWED")
    elif type_of_movie == 1:
        cartoon_arr.append("PUPPET")
    elif type_of_movie == 2:
        cartoon_arr.append("PLASTIC")
    cartoon_arr.append(comparison_param(cartoon_arr))


# ------------------------------------------------------------------------------
# Comparison parameter for shaker sort.
def comparison_param(movie_arr):
    return int(movie_arr[2]) / 12.0;