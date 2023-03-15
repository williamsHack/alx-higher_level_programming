#!/usr/bin/python3
# williamsHack <williamyawdickson1998@gmail.com>
def square_matrix_map(matrix=[]):
    return (list(map(lambda x: list(map(lambda y: y ** 2, x[:])), matrix)))
