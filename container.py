# ------------------------------------------------------------------------------
# container.py - Container handling functions.
# ------------------------------------------------------------------------------

import random
from extender import *


# ------------------------------------------------------------------------------
# Input data from file.
def in_from_file(cont, movies_data):
    for movie in movies_data:
        type_of_movie = movie[0]
        if type_of_movie == '1':
            fiction_arr = []
            fiction.in_from_file(fiction_arr, movie)
            cont.append(fiction_arr)
        if type_of_movie == '2':
            cartoon_arr = []
            cartoon.in_from_file(cartoon_arr, movie)
            cont.append(cartoon_arr)
        if type_of_movie == '3':
            documentary_arr = []
            documentary.in_from_file(documentary_arr, movie)
            cont.append(documentary_arr)


# ------------------------------------------------------------------------------
# Random filling container.
def in_rnd(cont, size):
    for _ in range(size):
        type_of_movie = random.randint(1, 3)
        if type_of_movie == 1:
            fiction_arr = []
            fiction.in_rnd(fiction_arr)
            cont.append(fiction_arr)
        if type_of_movie == 2:
            cartoon_arr = []
            cartoon.in_rnd(cartoon_arr)
            cont.append(cartoon_arr)
        if type_of_movie == 3:
            documentary_arr = []
            documentary.in_rnd(documentary_arr)
            cont.append(documentary_arr)


# ------------------------------------------------------------------------------
# Output in file.
def out(cont, out_stream):
    out_stream.write(f"Container contains {len(cont)} elements:\n")
    count = 0
    for movie in cont:
        count += 1
        out_stream.write(f"{count}: It is a {movie[0]}, ")

        if movie[0] == "fiction":
            out_stream.write(f'name = {movie[1]}, release date = {movie[2]}, director = {movie[3]}')
        elif movie[0] == 'cartoon':
            out_stream.write(f'name = {movie[1]}, release date = {movie[2]}, way to create = {movie[3]}')
        elif movie[0] == 'documentary':
            out_stream.write(f'name = {movie[1]}, release date = {movie[2]}, minutes = {movie[3]}')

        out_stream.write(f" comparison parameter = {movie[len(movie) - 1]}\n")


# ------------------------------------------------------------------------------
# Heap sorting.
def shaker_sort(cont):
    left = 0
    right = len(cont) - 1
    while left <= right:
        for i in range(right, left, -1):
            if cont[i - 1][4] > cont[i][4]:
                # swap
                cont[i - 1], cont[i] = cont[i], cont[i - 1]
        left += 1
        for i in range(left, right + 1):
            if cont[i - 1][4] > cont[i][4]:
                # swap
                cont[i - 1], cont[i] = cont[i], cont[i - 1]
        right -= 1